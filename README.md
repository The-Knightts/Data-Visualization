# Assignment : Data Visualization of COVID-19 Dataset
# Overview
    This assignment involves creating insightful visualizations of a cleaned COVID-19 dataset and building an interactive dashboard using Streamlit. Building on the previous assignment's data cleaning and basic analysis, you will now focus on data visualization and interactivity.

# Requirements
    Data Visualization with Matplotlib
    Create various plots to visualize the cleaned COVID-19 data, including:
    Total confirmed cases, deaths, and recovered cases over time.
    Top 10 countries/states with the highest number of cases.
    Daily new cases and growth rates.
    Save the plots as images.
# Interactive Dashboard with Streamlit
    Build an interactive dashboard to display your visualizations.
    Allow users to filter data by:
    Date range
    Countries/states
    Case types (confirmed, deaths, recovered)
    Include widgets for user interaction, such as sliders, dropdowns, and date pickers.
# File Handling
    Ensure the cleaned data is loaded from clean_covid_data.csv.
    Save and load visualization configurations if needed.
# User-Defined Exceptions
    Use previously defined exceptions (DataCleaningError) to handle issues during visualization (e.g., missing data columns).
# Tasks

## Data Visualization Module (visualization.py)
    Import necessary libraries:
    pandas, numpy, matplotlib.pyplot
    Load the cleaned dataset (clean_covid_data.csv).
    Implement functions to create the required plots:
    plot_total_cases(df): Plot total confirmed, deaths, and recovered cases over time.
    plot_top_countries(df): Plot top 10 countries/states with the highest number of cases.
    plot_daily_cases(df): Plot daily new cases and growth rates.
    Save the plots as images (e.g., total_cases.png, top_countries.png, daily_cases.png).

## Streamlit Dashboard (dashboard.py)
    Import necessary libraries:
    streamlit, pandas, matplotlib.pyplot
    Load the cleaned dataset (clean_covid_data.csv).
    Create Streamlit widgets for user interaction:
    Date range picker for selecting the date range.
    Dropdown for selecting countries/states.
    Dropdown for selecting case types (confirmed, deaths, recovered).
    Display the plots interactively based on user selections.
    Implement functions to update plots based on user input.

## File Handling Module (file_handling.py)
    Ensure functions to read from and write to CSV files are in place.
    Optionally, implement functions to save and load visualization configurations.

## User-Defined Exceptions (exceptions.py)
    Ensure DataCleaningError and other relevant exceptions are used appropriately during the visualization process.

## Main Analysis Script (analysis.py)
    Ensure integration of data cleaning, visualization, and exception handling.
    Provide a command-line interface to run data cleaning, create visualizations, and start the Streamlit dashboard.

# Submission
    Submit the following files:

    visualization.py
    dashboard.py
    clean_covid_data.csv (after cleaning)
    README.md (documentation)
    Saved plot images (e.g., total_cases.png, top_countries.png, daily_cases.png)