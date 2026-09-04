# Smallholder Livelihood Resilience Simulator

[![Live Demo](https://img.shields.io/badge/Streamlit-Live%20Demo-brightgreen)](https://coffee-livelihood-resilience-sim-viupaahzz2wpmyuedbqfeb.streamlit.app/)

## Description

An agent-based simulation model for exploring how smallholder farming households may respond to climate and economic shocks. The model allows different intervention strategies to be tested over time using simulated household data.

## Problem

Smallholder households can face volatile incomes, rising costs, and climate-related shocks, while intervention planning often relies on static analysis. This can make it difficult to:

* Understand how shocks may affect households over time
* Compare potential intervention strategies
* Identify conditions that may increase vulnerability to poverty

## Solution

I built a simulation environment to model household-level dynamics:

* Simulated 1,000 heterogeneous households over five years
* Modeled income, consumption, inflation, and climate shocks
* Incorporated poverty traps and productivity-loss mechanisms
* Compared intervention strategies using statistical tests

## Recommendation

Based on the simulated results:

* Consider combining productivity support with income diversification strategies
* Explore safety-net mechanisms such as climate insurance and cash support
* Consider targeting interventions during periods of elevated shock exposure rather than relying only on average conditions

## Tech Stack

* **Python:** Pandas, NumPy, SciPy
* **Agent-Based Modeling:** Mesa
* **Statistical Analysis:** T-tests
* **Visualization:** Matplotlib, Seaborn
* **Deployment:** Streamlit
