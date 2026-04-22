import mesa
import numpy as np
import pandas as pd

class FarmerAgent(mesa.Agent):
    def __init__(self, model, farm_size, initial_savings, initial_debt):
        super().__init__(model)
        self.farm_size = farm_size
        self.savings = initial_savings
        self.debt = initial_debt
        self.base_yield = 400  # CALIBRATION: Dropped from 550 to reflect non-intensified yields
        self.is_impoverished = True if self.savings < 300 else False

    def step(self):
        # 1. DYNAMIC COST OF LIVING
        # In reality, costs rise when the economy is good (Price Transmission)
        dynamic_cost = self.model.monthly_cost_of_living + (self.model.market_price * 5)

        # 2. AGGRESSIVE REINVESTMENT (The Wealth Brake)
        # Households don't hoard cash; they spend on social obligations/upkeep
        # We increase the 'tax' on high savings to 8% to keep it near $1,500
        reinvestment_spend = max(0, (self.savings - 400) * 0.08) if self.savings > 400 else 0

        self.savings -= (dynamic_cost + reinvestment_spend)

        # 3. INTERVENTIONS
        current_yield_potential = self.base_yield
        if self.model.intervention == "Intensification":
            current_yield_potential += 250 
            if (self.model.months_passed % 12) == 0: self.savings -= 80 # Higher input costs

        elif self.model.intervention == "Diversification":
            self.savings += 18 # Lower livestock margins
            if self.model.months_passed <= 24: self.savings -= 15

        # 4. ANNUAL HARVEST
        if (self.model.months_passed % 12) == 11:
            actual_yield = self.farm_size * current_yield_potential * self.model.yield_multiplier
            revenue = actual_yield * self.model.market_price
            self.savings += revenue

            # Productivity Scarring remains (the real "trap")
            if self.is_impoverished:
                self.base_yield *= 0.96 

        # 5. DEBT & STATUS
        if self.debt > 0 and self.savings > 100:
            repayment = min(self.savings * 0.15, self.debt)
            self.savings -= repayment
            self.debt -= repayment

        self.is_impoverished = True if self.savings < 300 else False
        if self.savings < 0: self.savings = 0

class LivelihoodModel(mesa.Model):
    def __init__(self, N=1000, intervention="Control"):
        super().__init__()
        self.num_agents = N
        self.intervention = intervention
        self.months_passed = 0
        self.market_price = 1.35 # Lower starting price
        self.monthly_cost_of_living = 65 # Higher base cost
        self.yield_multiplier = 1.0

        self.datacollector = mesa.DataCollector(
            model_reporters={
                "Poverty_Rate": lambda m: len([a for a in m.agents if a.is_impoverished]) / m.num_agents,
                "Avg_Savings": lambda m: np.mean([a.savings for a in m.agents])
            }
        )

        for i in range(self.num_agents):
            f_size = np.random.gamma(2, 2.0/2) # Slightly smaller farms
            s_val = np.random.lognormal(6.0, 0.4) 
            d_val = np.random.choice([0, 500, 1000], p=[0.70, 0.20, 0.10])
            FarmerAgent(self, f_size, s_val, d_val)

    def step(self):
        self.months_passed += 1
        if self.months_passed % 12 == 0: self.monthly_cost_of_living *= 1.06 # Higher inflation

        self.market_price += np.random.normal(0, 0.06)
        self.market_price = np.clip(self.market_price, 1.10, 2.20) # Realistic price band

        # Severe Drought
        self.yield_multiplier = 0.45 if 30 <= self.months_passed <= 40 else 1.0

        self.datacollector.collect(self)
        self.agents.shuffle_do("step")
