import streamlit as st
import pycountry
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Muat data
data = pd.read_csv('world_population.csv')

# Buat aplikasi Streamlit
st.title('World Population Data Visualization')

# Tampilkan dataset
st.subheader('Data')
st.write(data)

# Top 10 
st.title('Bar Plot dan Pie Chart Populasi 2022')
data['2022 Population'] = pd.to_numeric(data['2022 Population'], errors='coerce')

# Create a select menu for choosing between "Countries" and "Continents"
option = st.selectbox("Select an option:", ("Countries", "Continents"))

# Filter the data based on the selected option
if option == "Countries":
    data_sorted = data.sort_values(by='2022 Population', ascending=False)
    title = 'Top Countries by Population'
    x_label = 'Country/Territory'
    y_label = '2022 Population'
else:
    continent_data = data.groupby('Continent')[['2022 Population']].sum().reset_index()
    data_sorted = continent_data.sort_values(by='2022 Population', ascending=False)
    title = 'Top Continents by Population'
    x_label = 'Continent'
    y_label = '2022 Population'

# Create a slider for selecting the number of countries to display
min_countries = 1
max_countries = len(data_sorted)
num_countries = st.slider("Select the number of countries to display:", min_countries, max_countries, min_countries)

# Select the top countries based on the slider value
top_countries = data_sorted.head(num_countries)

# Create the bar chart using Plotly Express
bar_chart = px.bar(top_countries, x=x_label, y=y_label, color=x_label, text=y_label, title=title)

# Create the pie chart using Plotly Express
pie_chart = px.pie(top_countries, values=y_label, names=x_label, title=f'{title} - Pie Chart')

# Render the charts using Streamlit
st.plotly_chart(bar_chart)

st.write("\n")  # Add some spacing between the charts

st.plotly_chart(pie_chart)


# Treemap
df22 = data[['Continent', 'Country/Territory', '2022 Population']].copy()
df22['Year'] = 2022
df22['Population'] = df22['2022 Population']
df22.drop('2022 Population', axis=1, inplace=True)

df20 = data[['Continent', 'Country/Territory', '2020 Population']].copy()
df20['Year'] = 2020
df20['Population'] = df20['2020 Population']
df20.drop('2020 Population', axis=1, inplace=True)

df15 = data[['Continent', 'Country/Territory', '2015 Population']].copy()
df15['Year'] = 2015
df15['Population'] = df15['2015 Population']
df15.drop('2015 Population', axis=1, inplace=True)

df10 = data[['Continent', 'Country/Territory', '2010 Population']].copy()
df10['Year'] = 2010
df10['Population'] = df10['2010 Population']
df10.drop('2010 Population', axis=1, inplace=True)

df00 = data[['Continent', 'Country/Territory', '2000 Population']].copy()
df00['Year'] = 2000
df00['Population'] = df00['2000 Population']
df00.drop('2000 Population', axis=1, inplace=True)

df90 = data[['Continent', 'Country/Territory', '1990 Population']].copy()
df90['Year'] = 1990
df90['Population'] = df90['1990 Population']
df90.drop('1990 Population', axis=1, inplace=True)

df80 = data[['Continent', 'Country/Territory', '1980 Population']].copy()
df80['Year'] = 1980
df80['Population'] = df80['1980 Population']
df80.drop('1980 Population', axis=1, inplace=True)

df70 = data[['Continent', 'Country/Territory', '1970 Population']].copy()
df70['Year'] = 1970
df70['Population'] = df70['1970 Population']
df70.drop('1970 Population', axis=1, inplace=True)

df_combined = pd.concat([df22, df20, df15, df10, df00, df90, df80, df70])

df_population = df_combined.groupby(['Year', 'Continent', 'Country/Territory']).sum(numeric_only=True)['Population']
df_population = df_population.reset_index()

st.title('Population Treemap')
fig = px.treemap(df_population, path=['Year', 'Continent', 'Country/Territory'], values='Population', color='Population', color_continuous_scale='Viridis_r')
st.plotly_chart(fig)

cols = ['Area (km²)', 'Density (per km²)', 'Growth Rate']
xols = ['1970 Population', '2022 Population', 'Area (km²)']

for i in xols:
    df_cc = data.groupby(['Continent', 'Country/Territory']).sum(numeric_only=True)[i]
    df_cc = df_cc.reset_index()
    fig = px.treemap(df_cc, path=['Continent', 'Country/Territory'], values=i, color=i, color_continuous_scale='Viridis_r', title=f'{i} Treemap')
    st.plotly_chart(fig)

# Choropleth
st.title('Population Choropleth')
countries = {country.name: country.alpha_3 for country in pycountry.countries}

# Function to calculate the average of a list
def Average(lst):
    return sum(lst) / len(lst)

# Filter the data for the selected year
year_options = [1970, 1980, 1990, 2000, 2010, 2015, 2020, 2022]
selected_year = st.selectbox("Select a year", year_options, index=len(year_options)-1)
df_selected_year = data.loc[:, ["CCA3", "Country/Territory", str(selected_year) + " Population"]]
df_selected_year["CCA3"] = [countries.get(country, 'Unknown code') for country in df_selected_year["Country/Territory"]]

# Calculate the minimum and maximum population values for the selected year
min_population = df_selected_year[str(selected_year) + " Population"].min()
max_population = df_selected_year[str(selected_year) + " Population"].max()

# Create the choropleth map using Plotly Express
fig = px.choropleth(df_selected_year, locations="CCA3",
                    hover_name="Country/Territory",
                    hover_data=df_selected_year.columns,
                    color=str(selected_year) + " Population",
                    color_continuous_scale="Viridis",
                    range_color=(min_population, max_population),
                    projection="natural earth")

fig.update_layout(margin={"r": 5, "t": 0, "l": 5, "b": 0})

# Render the choropleth map using Streamlit
st.plotly_chart(fig)

for i in cols:
    if i == 'Density (per km²)':
        fig = px.choropleth(data,locations = 'CCA3', color = i,hover_name="Country/Territory",title = f'{i} Choropleth',color_continuous_scale='Viridis_r')
        st.plotly_chart(fig)
    else:
        fig = px.choropleth(data,locations = 'CCA3', color = i,hover_name="Country/Territory",title = f'{i} Choropleth',color_continuous_scale='Viridis_r')
        st.plotly_chart(fig)

