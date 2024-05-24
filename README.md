# Smart Energy Optimization

This repository contains a project inspired by my family. It focuses on optimizing strategies for a typical home having solar cells, a battery, an electric car and a heatpump. The main goal is to develop and simulate a control algorithm to maximize the use of the solar energy usage, optimally charge the car while reducing energy costs.

## Project Overview

The project includes the following key components:

- **Data Simulation**: Generating simulated data for solar energy production, household energy consumption, battery storage, energy prices, and electric car charging needs.
- **Control Algorithms**: Implementing rule-based control strategies to manage energy flows within a household, with a focus on three scenarios:
  - **Autarky Optimization**: Maximizing self-consumption of solar energy and minimizing dependency on the grid.
  - **Cost Optimization**: Minimizing energy costs by considering varying electricity prices and feed-in tariffs.
  - **Car Charging Optimization**: Ensuring the electric car is optimally charged using the most cost-effective and sustainable energy sources.
- **Optimization Algorithm**: Using linear programming to optimize all three criteria (maximizing solar energy usage, minimizing costs, and optimally charging the car) based on weighted priorities.
- **Visualization**: Plotting the results to compare the performance of different optimization strategies.

