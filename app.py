# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.patches as mpatches
from plotly.subplots import make_subplots
#from wordcloud import WordCloud
import seaborn as sns  
sns.set(color_codes = True)
sns.set(style="whitegrid")
import plotly.figure_factory as ff
from plotly.colors import n_colors
import dash
from dash import html
from dash import dcc
import plotly.graph_objects as go

app = dash.Dash()   #initialising dash app

csv = pd.read_csv('https://raw.githubusercontent.com/M3IT/COVID-19_Data/master/Data/COVID_AU_state_cumulative.csv')
csv.date = pd.to_datetime(csv.date)
date_wise_df = csv.groupby(['date', 'state'])['positives'].sum().reset_index()

def stock_prices():
    # Function for creating line chart showing Google stock prices over time 
    #date_wise_df = csv.groupby(['date', 'state'])['positives'].sum().reset_index()
    fig = px.bar(date_wise_df, x= 'date', y = 'positives', color = 'state')
                    
                
    fig.update_layout(title = 'Prices over time',
                      xaxis_title = 'Dates',
                      yaxis_title = 'Prices'
                      )
    return fig  

 
 
 
 
app.layout = html.Div(id = 'parent', children = [
    html.H1(id = 'H1', children = 'Styling using html components', style = {'textAlign':'center',\
                                            'marginTop':40,'marginBottom':40}),

        
        dcc.Graph(id = 'line_plot', figure = stock_prices())    
    ]
                     )


if __name__ == '__main__': 
    app.run_server()