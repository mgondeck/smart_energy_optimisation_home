**Energy Optimization**  
Marie Gondeck

----

This repository contains a project inspired by my family. It focuses on optimizing strategies for a typical home having solar cells, a battery, an electric car and a heatpump. The main goal is to develop and simulate a control algorithm to maximize the use of the solar energy usage, optimally charge the car while reducing energy costs.

**Project Overview**

The project includes the following key components:

- **Data**: Original historical data containing: Timestamp, Grid Load, Grid Feed, Generation (Solar Energy), Storage Charge, Storage Discharge, Consumption, State of Charge. 
- **Control Algorithms**: Implementing rule-based control strategies to manage energy flows within the household, with a focus on:
  - **Autarky Optimization**: Maximizing self-consumption of solar energy and minimizing dependency on the grid.
  - **Cost Optimization**: Minimizing energy costs by considering varying electricity prices and feed-in tariffs.
  - **Car Charging Optimization**: Ensuring the electric car is optimally charged using the most cost-effective and sustainable energy sources.
- **Optimization Algorithm**: Using linear programming to optimize all three criteria based on weighted priorities.
- **Visualization**: Plotting results to compare the performance of different optimization strategies.

