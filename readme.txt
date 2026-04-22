# Smallholder Livelihood Resilience Simulator

## Description
This project is an agent-based simulation model designed to evaluate the resilience of smallholder farming households under climate and economic shocks. It enables dynamic testing of different intervention strategies over time.

## Problem
Smallholder farmers face volatile income streams and climate risks, but most interventions are designed using static analysis. This leads to:
- Poor understanding of system-wide shocks
- Ineffective intervention strategies
- High vulnerability to poverty during extreme events

## Solution
We built a simulation environment to model real-world dynamics:

- Simulated 1,000 heterogeneous households over 5 years
- Modeled income, consumption, inflation, and climate shocks
- Incorporated poverty traps and productivity loss mechanisms
- Compared intervention strategies using statistical testing

## Recommendation
- Implement hybrid intervention strategies combining productivity and diversification
- Introduce safety net mechanisms (e.g., climate insurance, cash support)
- Design interventions specifically for shock periods, not average conditions

## Tech Stack
- Python (Pandas, NumPy, SciPy)
- Agent-Based Modeling: Mesa
- Statistical Analysis (T-tests)
- Visualization: Matplotlib, Seaborn
- Deployment: Streamlit