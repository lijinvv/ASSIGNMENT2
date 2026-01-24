# World Bank Sustainability & Energy Trends Analysis 🌍

This repository contains a specialized data analysis suite designed to explore global environmental indicators. Using World Bank datasets, the project examines the intersection of energy consumption, renewable resources, and population growth across diverse economies.

## 🚀 Project Overview
The project implements a modular approach to Exploratory Data Analysis (EDA). It automates the process of transposing time-series data, filtering regional metrics, and generating high-resolution comparative visualizations to identify global sustainability trends.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Data Processing:** Pandas, NumPy
- **Visualization:** Matplotlib
- **Dataset Source:** World Bank Open Data

## 📋 Key Features
- **Data Transformation Engine:** A custom transposition function (`trans_file`) that reformats World Bank CSVs into time-series indices for easier longitudinal analysis.
- **Energy Metrics Visualization:**
  - **Line Plots:** Comparative analysis of Renewable Energy vs. Electricity consumption trends.
  - **Bar Plots:** Multi-year snapshots (1990–2014) of Fossil Fuel consumption and Population Growth.
- **Statistical Analysis:** Automated calculation of Mean and Standard Deviation for energy consumption patterns to identify data variance.

## 📊 Analytical Insights
The suite produces several visual outputs (saved as `.png` files):
- `renewable.png`: Tracking the shift toward sustainable energy.
- `electricity.png`: Monitoring global electrification trends.
- `fossil.png`: Cross-country comparison of fossil fuel dependency.
- `population.png`: Regional population growth dynamics.



