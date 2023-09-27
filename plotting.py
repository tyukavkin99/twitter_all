import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from datetime import datetime, timedelta

import dash
from dash import Dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objects as go

# Importing the data
new_df = pd.read_csv('category_data.csv', parse_dates=['tweet_time'])
new_df['end_time'] = new_df['tweet_time'] + timedelta(minutes=10)
df = pd.read_csv('all_data.csv', parse_dates={'date':['tweet_time','tweet_time.1','tweet_time.2']})

# Data transformation
df['sum_all'] = df.sum(axis=1)
df.reset_index(inplace=True)

# Selecting the date of data
check = new_df[(new_df['tweet_time'] >= '2014-10-21 00:00:00') & (new_df['tweet_time'] <= '2014-10-21 23:59:59') & (new_df['category'] != 'Unidentified')]
#categories_agg
#sample_df = check.sample(n=1000, random_state=1)

# Choosing the top 30 users by the number of posts
top_list = check.userid.value_counts().head(30)
top_list = top_list.to_frame()
top_list.reset_index(inplace=True)
top_users = top_list['index'].tolist()
check = check[check['userid'].isin(top_users)]



#fig = px.timeline(check, x_start="tweet_time", x_end="end_time", y="userid", color="category")
#fig.show()

# Figure for multiple lines
#fig_lines = go.Figure()
'''fig_lines = px.line(x=df['date'], y=df['Russian_Independent_Media'])
fig_lines.add_scatter(x=df['date'], y=df['UK_Media'],mode='lines', name='UK Media')
fig_lines.add_scatter(x=df['date'], y=df['Russian_Social_Media'],mode='lines', name='Russian Social Media')
fig_lines.add_scatter(x=df['date'], y=df['Russian_Propaganda_Media'],mode='lines', name='Russian Propaganda Media')
fig_lines.add_scatter(x=df['date'], y=df['US_Big_Media'],mode='lines', name='US Big Media')
fig_lines.add_scatter(x=df['date'], y=df['US_Local_Media'],mode='lines', name='US Local Media')
fig_lines.add_scatter(x=df['date'], y=df['US_Social_Media'],mode='lines', name='US Social Media')
fig_lines.add_scatter(x=df['date'], y=df['Unidentified'],mode='lines', name='Unidentified')
fig_lines.add_scatter(x=df['date'], y=df['Video_Hosting_Website'],mode='lines', name='Video Hosting Website')
'''

fig_lines = go.Figure()
fig_lines.add_trace(go.Scatter(x=df['date'], y=df['Russian_Independent_Media'], mode='lines', name='Russian Independent Media'))
fig_lines.add_trace(go.Scatter(x=df['date'], y=df['UK_Media'],mode='lines', name='UK Media'))
fig_lines.add_trace(go.Scatter(x=df['date'], y=df['Russian_Social_Media'],mode='lines', name='Russian Social Media'))
fig_lines.add_trace(go.Scatter(x=df['date'], y=df['Russian_Propaganda_Media'],mode='lines', name='Russian Propaganda Media'))
fig_lines.add_trace(go.Scatter(x=df['date'], y=df['US_Big_Media'],mode='lines', name='US Big Media'))
fig_lines.add_trace(go.Scatter(x=df['date'], y=df['US_Local_Media'],mode='lines', name='US Local Media'))
fig_lines.add_trace(go.Scatter(x=df['date'], y=df['US_Social_Media'],mode='lines', name='US Social Media'))
fig_lines.add_trace(go.Scatter(x=df['date'], y=df['Unidentified'],mode='lines', name='Unidentified'))
fig_lines.add_trace(go.Scatter(x=df['date'], y=df['Video_Hosting_Website'],mode='lines', name='Video Hosting Website'))


#fig_lines.add_trace(go.Scatter(x=new_df['tweet_time'], y=df['Russian_Independent_Media'], name='Russian_Independent_Media',
#                         line=dict(color='firebrick', width=4), mode='lines'))
#fig_lines.add_trace(go.Scatter(x=new_df['tweet_time'], y=df['UK_Media'], name = 'UK_Media',
#                         line=dict(color='royalblue', width=4), mode='lines'))
#fig_lines.add_trace(go.Scatter(x=new_df['tweet_time'].values, y=high_2007, name='High 2007'
#                               line=dict(color='firebrick', width=4, dash='dash') # dash options include 'dash', 'dot', and 'dashdot'
#))
#fig_lines.add_trace(go.Scatter(x=new_df['tweet_time'].values, y=low_2007, name='Low 2007',
#                         line = dict(color='royalblue', width=4, dash='dash')))
#fig_lines.add_trace(go.Scatter(x=new_df['tweet_time'].values, y=high_2000, name='High 2000',
#                         line = dict(color='firebrick', width=4, dash='dot')))
#fig_lines.add_trace(go.Scatter(x=new_df['tweet_time'].values, y=low_2000, name='Low 2000',
#                         line=dict(color='royalblue', width=4, dash='dot')))

# Edit the layout
fig_lines.update_layout(title='Time Series of Categories',
                   xaxis_title='Year, Month, Day',
                   yaxis_title='Number of Tweets'
                   )


# Dash App

app = Dash(__name__)

app.layout = html.Div([
    html.Div(children='Change Detection App'),
    dcc.Graph(figure=px.line(df, x="date", y="sum_all", title='Overall Number of Tweets Over Time',width=800, height=400)),
    dcc.Graph(figure=fig_lines),
    dcc.Graph(figure=px.timeline(check, x_start="tweet_time", x_end="end_time", y="userid", color="category" ))#,width=2000, height=2000))
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)