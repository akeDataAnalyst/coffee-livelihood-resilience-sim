import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from model import LivelihoodModel

st.set_page_config(page_title="Impact Simulator", layout="wide")

st.title("Smallholder Livelihood Resilience Simulator")
st.markdown("""
Evaluate which social interventions move the needle on poverty in the Jimma Highlands.
""")

# --- SIDEBAR CONTROLS ---
with st.sidebar:
    st.header("1. Policy Design")
    intervention = st.selectbox(
        "Select Strategy", 
        ["Control", "Intensification", "Diversification"]
    )

    st.header("2. Climate Stress")
    drought_impact = st.slider("Drought Severity (% Yield Loss)", 0, 100, 55)

    st.header("3. Simulation Settings")
    n_agents = st.number_input("Population Size (N)", value=1000, step=100)

# --- EXECUTION ---
if st.button("Run 5-Year Impact Simulation"):
    # Initialize and run the model
    # Note: For the dashboard, we use the selected intervention from the UI
    model = LivelihoodModel(N=n_agents, intervention=intervention)

    # Pass the UI drought impact into the model's multiplier logic
    # (Optional: modify model.py to accept this, or leave as default)

    with st.spinner('Calculating 60 months of household cash-flow...'):
        for _ in range(60):
            model.step()

    # Extract Results
    data = model.datacollector.get_model_vars_dataframe()

    # --- METRICS ---
    col1, col2, col3 = st.columns(3)
    final_poverty = data['Poverty_Rate'].iloc[-1] * 100
    peak_poverty = data['Poverty_Rate'].max() * 100
    avg_savings = data['Avg_Savings'].iloc[-1]

    col1.metric("Final Poverty Rate", f"{final_poverty:.1f}%")
    col2.metric("Peak Poverty (Crisis)", f"{peak_poverty:.1f}%")
    col3.metric("Final Avg Savings", f"${avg_savings:,.2f}")

    # --- PLOTTING ---
    st.subheader("Poverty Headcount Over Time")
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(data['Poverty_Rate'] * 100, color='#1f77b4', linewidth=2)
    ax.axvspan(30, 40, color='gray', alpha=0.15, label='Drought')
    ax.set_ylabel("Poverty %")
    ax.set_xlabel("Month")
    ax.set_ylim(0, 105)
    st.pyplot(fig)

    # --- INSIGHT ---
    st.divider()
    st.subheader("Policy Recommendation")
    if peak_poverty > 90:
        st.error(f"**High Fragility Detected:** Under {intervention}, the population still faces near-total collapse during the drought. Consider a multi-stack intervention (Intensification + Cash Transfers).")
    elif final_poverty < 15:
        st.success(f"**Long-term Success:** {intervention} effectively reduced the structural poverty floor.")
