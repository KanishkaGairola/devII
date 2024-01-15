#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import scipy.stats as sps
import statsmodels as sm
import statsmodels.formula.api as smf

# Define File Path : Replace xxxxx with appropriate File Path


# Import & Read Dataset
df = pd.read_csv('Top Rated Movie Database.csv')

# Display Dataset Information
df.info()


# In[2]:


df.head(10)


# From the tabular representaion, we can infer the following : 
# 
# The most popular movie in 2019 was Ad Astra, with a popularity vote count of 453,361. It was also the highest-rated movie of the year, with a title vote average of 5.9.
# The most popular movie in 2020 was Bad Boys for Life, with a popularity vote count of 315,622. It was the second-highest-rated movie of the year, with a title vote average of 7.1.
# The highest-rated movie of 2020 was Sonic the Hedgehog, with a title vote average of 7.4. However, it was not as popular as some of the other movies on the list, with a popularity vote count of only 192,374.
# The least popular movie on the list was Teen Titans: The Judas Contract, with a popularity vote count of only 167,159. However, it was still relatively well-rated, with a title vote average of 7.2.
# 

# In[4]:


pip install dash


# In[5]:


import pandas as pd
import plotly.express as px
import dash
from dash import html, dcc
from dash.dependencies import Input, Output

# Load the dataset
filename = 'Top Rated Movie Database.csv'  # Replace with the actual file path
df = pd.read_csv(filename)

# Create Dash app
app = dash.Dash(__name__)

# Layout of the dashboard
app.layout = html.Div([
    dcc.Dropdown(
        id='year-dropdown',
        options=[{'label': year, 'value': year} for year in df['year'].unique()],
        value=df['year'].min(),  # Default to the minimum year
        style={'width': '50%'}
    ),
    
    dcc.Graph(id='popularity-bar-chart'),
    dcc.Graph(id='vote-count-bar-chart'),
    dcc.Graph(id='vote-average-line-chart'),
    dcc.Graph(id='scatter-plot'),
    dcc.Graph(id='top-20-popularity-bar-chart'),
    
    html.Div(id='table-container')
])

# Callback to update charts and table based on selected year
@app.callback(
    [Output('popularity-bar-chart', 'figure'),
     Output('vote-count-bar-chart', 'figure'),
     Output('vote-average-line-chart', 'figure'),
     Output('scatter-plot', 'figure'),
     Output('top-20-popularity-bar-chart', 'figure'),
     Output('table-container', 'children')],
    [Input('year-dropdown', 'value')]
)
def update_charts_and_table(selected_year):
    # Filter data based on selected year
    filtered_df = df[df['year'] == selected_year]

    # Bar graph for Popularity
    fig1 = px.bar(filtered_df, x='Titile', y='Popularity', title=f'Popularity for {selected_year}')

    # Bar graph for Vote Count
    fig2 = px.bar(filtered_df, x='Titile', y='Vote Count', title=f'Vote Count for {selected_year}')

    # Line chart for Vote Average
    fig3 = px.line(filtered_df, x='Release Date', y='Vote Average', title=f'Vote Average over Time for {selected_year}')

    # Scatter plot for Popularity vs. Vote Average
    fig4 = px.scatter(filtered_df, x='Popularity', y='Vote Average', title=f'Popularity vs. Vote Average for {selected_year}')

    # Bar graph for Top 20 Popularity
    top_20_popularity_df = filtered_df.nlargest(20, 'Popularity')
    fig5 = px.bar(top_20_popularity_df, x='Titile', y='Popularity', title=f'Top 20 Popularity for {selected_year}')

    # Table for the selected year
    table = html.Table(
        # Header
        [html.Tr([html.Th(col) for col in filtered_df.columns])] +
        # Body
        [html.Tr([html.Td(filtered_df.iloc[i][col]) for col in filtered_df.columns]) for i in range(len(filtered_df))]
    )

    return fig1, fig2, fig3, fig4, fig5, table

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)


# In[ ]:




