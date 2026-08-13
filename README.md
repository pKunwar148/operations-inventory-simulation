# Smoke Pit Operations & Inventory Simulation

A discrete-event simulation and operations-optimization project built in **Simio** to study how staffing, inventory, replenishment policies, and process capacity affect service performance and profitability.

## Portfolio Highlights

- Modeled a multi-stage service and preparation workflow with queues, finite inventory, replenishment logic, and shared resources.
- Evaluated staffing, inventory, replenishment, and capacity scenarios to identify operational bottlenecks.
- Used time-study data and fitted process-time distributions to support realistic simulation inputs.
- Compared what-if policies across profit, order-to-delivery time, time in system, balking, reneging, and order switching.
- Recommended an operating policy balancing service performance, inventory availability, staffing, and cost.

## Key Result

The final recommended policy used **2 customer-service workers and 4 food-preparation workers**, with an expected average daily profit of **$1,707.66** and an average order-to-delivery time of **6.03 minutes**.

In a separate what-if comparison, the recommended flexible staffing policy improved modeled order-to-delivery cycle-time performance by about **27.6%** versus the lower food-preparation-capacity case.

## Interactive Demo

This repository includes a small **Streamlit scenario explorer** built from exported/precomputed simulation results.

Run locally:

```bash
pip install -r requirements.txt
streamlit run app.py
```

The app lets you:
- inspect the final recommendation,
- compare what-if scenarios,
- explore KPI trade-offs,
- review the modeling and decision logic.

> Note: the Streamlit app explores exported Simio results; it does not execute the Simio simulation engine.

## Repository Structure

```text
.
├── app.py
├── requirements.txt
├── README.md
├── data/
│   ├── final_recommendation.csv
│   └── what_if_scenarios.csv
├── model/
│   └── add-your-simio-model-here
├── demo/
│   └── add-demo-video-or-link-here
├── report/
│   └── add-portfolio-report-here
└── assets/
    └── add-screenshots-gifs-diagrams-here
```

## Suggested Demo Flow

A 60–90 second recording works well:

1. Show the Simio process flow.
2. Point out inventory/replenishment logic.
3. Run or show experiment/scenario outputs.
4. Explain the bottleneck identified.
5. Show the final recommendation and KPI trade-offs.
6. End on the interactive Streamlit dashboard.

## Tools

**Simulation & Optimization:** Simio, discrete-event simulation, scenario analysis, sensitivity analysis  
**Analytics:** Excel, time-study analysis, KPI comparison  
**Operations:** Inventory planning, capacity analysis, replenishment, bottleneck analysis, resource allocation

## Notes

This repository is intended as a portfolio presentation of the project. Before publishing course materials, data, reports, or group work publicly, confirm that you have permission to redistribute them.
