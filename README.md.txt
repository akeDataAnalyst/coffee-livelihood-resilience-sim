# Smallholder Livelihood Resilience Simulator

## Title
Measuring ROI on Social Interventions: An Agent-Based Modeling Approach for the Jimma Highlands

## Description
This project is a high-fidelity Agent-Based Model (ABM) designed to evaluate the economic resilience of 1,000 coffee-farming households in Ethiopia. By simulating 60 months (5 years) of household cash-flow, the system quantifies how market volatility, inflation, and climate shocks (drought) impact the poverty headcount. The project moves beyond static data analysis to provide a dynamic Intervention Tournament between different sustainability strategies.

## The Problem: "The Resilience Gap"
Most sustainability interventions in the coffee sector are implemented without predictive modeling. Organizations often face a choice:
1. **Intensification:** Boosting yields through fertilizer/inputs.
2. **Diversification:** Creating secondary income streams (livestock).

As established in our Baseline Stress-Test, without intervention, a severe drought (Year 3) can lead to a 100% Systemic Collapse, where every household falls below the poverty line simultaneously due to a lack of liquidity, even if the long-term averages look profitable.

## The Solution: Agent-Based Simulation
Using the Mesa framework, we built a "Virtual Village" with:
- **Synthetic Population:** Farmers assigned realistic land sizes (Gamma distribution) and initial wealth (Lognormal distribution).
- **Economic Physics:** Monthly consumption floors, progressive spending, and coffee price transmission logic.
- **Productivity Scarring:** A "Poverty Trap" mechanic where being impoverished during harvest causes permanent damage to future tree productivity.

### Key Features:
- **Baseline Stress-Test:** Identifies the "Sawtooth" poverty trap.
- **Intervention Tournament:** Comparative analysis of Strategy A vs. Strategy B.
- **Statistical Rigor:** Independent T-tests to prove significance (Final results yielded p < 0.001).
- **Policy Dashboard:** A Streamlit interface for Impact Directors to test different "dosages" of interventions.

## Results & Recommendation
Our simulation revealed a critical insight:
- **Intensification** is statistically superior for long-term wealth accumulation (p < 0.0000000000), yet it offers 0% Resilience against extreme drought.
- **Diversification** (at the current simulated dosage) provides a small monthly cushion but is insufficient to prevent the 100% poverty spike during total crop failure.

**Final Recommendation:** To achieve true Livelihood Resilience, Pursue a Hybrid Model. Neither strategy alone prevents collapse; a "Safety Net" or "Climate Insurance" mechanism is required to bridge the 100% peak poverty period identified in the simulation.

## Tech Stack
- **Language:** Python 3.9+
- **Simulation Engine:** [Mesa](https://mesa.readthedocs.io/) (Agent-Based Modeling)
- **Data Science:** Pandas, NumPy, SciPy (T-testing)
- **Visualization:** Matplotlib, Seaborn
- **Deployment:** Streamlit (Policy Dashboard)

---
*Developed by Aklilu Abera | Senior Impact Analytics Portfolio Project.*