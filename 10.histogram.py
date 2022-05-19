#######
# This histogram looks back at the mpg dataset
######
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv(r"C:\Users\sina.kian\Desktop\New folder\plotly\mpg.csv")

data = [go.Histogram(
    x=df['mpg']
)]

layout = go.Layout(
    title="Miles per Gallon Frequencies of<br>\
    1970's Era Vehicles"
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='basic_histogram.html')


###############################################################
#######
# This histogram has wider bins than the previous hist1.py
######
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv(r"C:\Users\sina.kian\Desktop\New folder\plotly\mpg.csv")

data = [go.Histogram(
    x=df['mpg'],
    xbins=dict(start=8,end=50,size=6),
)]

layout = go.Layout(
    title="Miles per Gallon Frequencies of<br>\
    1970's Era Vehicles"
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='wide_histogram.html')
#############################################################
#######
# This histogram has narrower bins than the previous hist1.py
######
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv(r"C:\Users\sina.kian\Desktop\New folder\plotly\mpg.csv")

data = [go.Histogram(
    x=df['mpg'],
    xbins=dict(start=8,end=50,size=1),
)]

layout = go.Layout(
    title="Miles per Gallon Frequencies of<br>\
    1970's Era Vehicles"
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='narrow_histogram.html')
###########################################################
#######
# This histogram compares heights by gender
######
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv(r"C:\Users\sina.kian\Desktop\New folder\plotly\arrhythmia.csv")

data = [go.Histogram(
    x=df[df['Sex']==0]['Height'],
    opacity=0.75,
    name='Male'
),
go.Histogram(
    x=df[df['Sex']==1]['Height'],
    opacity=0.75,
    name='Female'
)]

layout = go.Layout(
    barmode='overlay',
    title="Height comparison by gender"
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='basic_histogram2.html')
############################################################
#######
# This histogram displays the number of Reddit button presses
# over the two months of their social experiment.
######
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../data/thebutton_presses.csv')

data = [go.Histogram(
    x=df['press time'],
    nbinsx=60
)]

layout = go.Layout(
    title="Number of presses per timeslot"
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='button_presses2.html')

##########################################################
#######
# This bar chart mimics a histogram as the x-axis
# is a continuous time series, and the y-axis sums
# a frequency that is already part of the dataset
######
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv(r"C:\Users\sina.kian\Desktop\New folder\plotly\FremontBridgeBicycles.csv")

# Convert the "Date" text column to a Datetime series:
df['Date'] = pd.to_datetime(df['Date'])

# Add a column to hold the hour:
df['Hour']=df['Date'].dt.time

# Let pandas perform the aggregation
df2 = df.groupby('Hour').sum()

trace1 = go.Bar(
    x=df2.index,
    y=df2['Fremont Bridge West Sidewalk'],
    name="Southbound",
    width=1  # eliminates space between adjacent bars
)
trace2 = go.Bar(
    x=df2.index,
    y=df2['Fremont Bridge East Sidewalk'],
    name="Northbound",
    width=1
)
data = [trace1, trace2]

layout = go.Layout(
    title='Fremont Bridge Bicycle Traffic by Hour',
    barmode='stack'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='fremont_bridge.html')
