from pathlib import Path
import pandas as pd
import streamlit as st

BASE = Path(__file__).parent
what_if = pd.read_csv(BASE / "data" / "what_if_scenarios.csv")
final = pd.read_csv(BASE / "data" / "final_recommendation.csv").iloc[0]

st.set_page_config(page_title="Smoke Pit Simulation Explorer", layout="wide")

st.title("Smoke Pit Operations & Inventory Simulation")
st.caption(
    "Interactive portfolio view of precomputed Simio experiment results. "
    "This app does not run the Simio engine; it explores exported scenario outputs."
)

tab1, tab2, tab3 = st.tabs(["Final Recommendation", "What-if Explorer", "Model Story"])

with tab1:
    st.subheader("Recommended operating policy")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Customer-service workers", int(final["Customer Service Workers"]))
    c2.metric("Food-prep workers", int(final["Food Preparation Workers"]))
    c3.metric("Expected daily profit", f'${final["Expected Daily Profit ($)"]:,.2f}')
    c4.metric("Avg. order-to-delivery", f'{final["Avg Order-to-Delivery (min)"]:.2f} min')

    st.write(
        f'**Profit 95% confidence interval:** '
        f'${final["Profit 95% CI Low ($)"]:,.2f} – ${final["Profit 95% CI High ($)"]:,.2f}'
    )
    st.info(
        "The selected configuration balances profit, service time, staffing, "
        "inventory availability, replenishment, and operational feasibility."
    )

with tab2:
    st.subheader("Compare precomputed what-if scenarios")
    scenario = st.selectbox("Choose a scenario", what_if["Scenario"].tolist())
    row = what_if.loc[what_if["Scenario"] == scenario].iloc[0]

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Daily profit", f'${row["Avg Daily Profit ($)"]:,.2f}')
    c2.metric("Order-to-delivery", f'{row["Avg Order-to-Delivery (min)"]:.2f} min')
    c3.metric("Time in system", f'{row["Avg Time in System (min)"]:.2f} min')
    c4.metric("Food-prep workers", int(row["Food Preparation Workers"]))

    metric = st.selectbox(
        "Compare scenarios by metric",
        [
            "Avg Daily Profit ($)",
            "Avg Order-to-Delivery (min)",
            "Avg Time in System (min)",
            "Balked Customers",
            "Reneged Customers",
            "Switched Orders",
        ],
    )
    chart_df = what_if.set_index("Scenario")[[metric]]
    st.bar_chart(chart_df)

    st.dataframe(
        what_if[
            [
                "Scenario",
                "Customer Service Workers",
                "Food Preparation Workers",
                "Avg Daily Profit ($)",
                "Avg Order-to-Delivery (min)",
                "Avg Time in System (min)",
            ]
        ],
        use_container_width=True,
        hide_index=True,
    )

    baseline = what_if.loc[what_if["Scenario"] == "Lower food-prep capacity"].iloc[0]
    recommended = what_if.loc[what_if["Scenario"] == "Recommended flexible policy"].iloc[0]
    cycle_improvement = (
        (baseline["Avg Order-to-Delivery (min)"] - recommended["Avg Order-to-Delivery (min)"])
        / baseline["Avg Order-to-Delivery (min)"]
        * 100
    )
    st.success(
        f"Compared with the lower food-prep-capacity scenario, the recommended flexible "
        f"policy improves modeled order-to-delivery cycle-time performance by "
        f"{cycle_improvement:.1f}%."
    )

with tab3:
    st.subheader("Modeling approach")
    st.markdown(
        """
        **Problem:** Balance staffing, inventory, replenishment, and service performance under constrained resources.

        **Simulation:** A multi-stage discrete-event model representing ordering and downstream preparation activities,
        with finite inventory, queues, replenishment logic, and shared resources.

        **Analysis:** Scenario testing, sensitivity analysis, input-distribution fitting, validation, and operational
        policy comparison.

        **Decision focus:** Identify bottlenecks and recommend an operating configuration that balances service
        performance, stockout risk, staffing cost, and profitability.
        """
    )
