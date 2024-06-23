import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('C:\\Users\\KUBER\\OneDrive\\Documents\\ITR\\Py ITR\\Assignments\\Assignment-7\\clean_country_wise_data.csv')

countries = dataset['Country/Region']

selected_country_1 = st.selectbox('Select First Country/Region', countries)
selected_country_2 = st.selectbox('Select Second Country/Region', countries)

case_types = ['Confirmed', 'Deaths', 'Recovered', 'Active', 'New cases', 'New deaths', 'New recovered']
selected_case_type = st.selectbox('Select Case Type', case_types)

st.set_option('deprecation.showPyplotGlobalUse', False)

def filter_data(data, country, case_type):
    return data[data['Country/Region'] == country][[case_type]]

def plot_data(data1, data2, case_type, country1, country2):
    plt.figure(figsize=(10, 6))
    plt.scatter(data1.index, data1[case_type], label=country1)
    plt.scatter(data2.index, data2[case_type], label=country2)
    plt.xlabel('Index')
    plt.ylabel('Number of Cases')
    plt.title(f'Total {case_type} Cases in {country1} and {country2}')
    plt.grid(True)
    plt.legend()
    st.pyplot()

def update_plots(data, country1, country2, case_type):
    filtered_data1 = filter_data(data, country1, case_type)
    filtered_data2 = filter_data(data, country2, case_type)
    plot_data(filtered_data1, filtered_data2, case_type, country1, country2)

update_plots(dataset, selected_country_1, selected_country_2, selected_case_type)
