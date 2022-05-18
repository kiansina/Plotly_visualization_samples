#######
# A bubble chart is simply a scatter plot
# with the added feature that the size of the
# marker can be set by the data.
######
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv(r"C:\Users\sina.kian\Desktop\New folder\plotly\mpg.csv")

data = [go.Scatter(          # start with a normal scatter plot
    x=df['horsepower'],
    y=df['mpg'],
    text=df['name'],
    mode='markers',
    marker=dict(size=1.5*df['cylinders'],
    color=df['cylinders'],
    showscale=True) # set the marker size
)]

layout = go.Layout(
    title='Vehicle mpg vs. horsepower',
    xaxis = dict(title = 'horsepower'), # x-axis label
    yaxis = dict(title = 'mpg'),        # y-axis label
    hovermode='closest'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubble1.html')

#########################################################################
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv(r"C:\Users\sina.kian\Desktop\New folder\plotly\mpg.csv")

data = [go.Scatter(          # start with a normal scatter plot
    x=df['horsepower'],
    y=df['mpg'],
    text=df['name'],
    mode='markers',
    marker=dict(size=df['weight']/100,
    color=df['cylinders'],
    showscale=True) # set the marker size
)]

layout = go.Layout(
    title='Vehicle mpg vs. horsepower',
    xaxis = dict(title = 'horsepower'), # x-axis label
    yaxis = dict(title = 'mpg'),        # y-axis label
    hovermode='closest'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubble3.html')


#########################################################################
#######
# A bubble chart is simply a scatter plot
# with the added feature that the size of the
# marker can be set by the data.
######
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv(r"C:\Users\sina.kian\Desktop\New folder\plotly\mpg.csv")

# Add columns to the DataFrame to convert model year to a string and
# then combine it with name so that hover text shows both:
df['text1']=pd.Series(df['model_year'],dtype=str)
df['text2']="'"+df['text1']+" "+df['name']

data = [go.Scatter(
            x=df['horsepower'],
            y=df['mpg'],
            text=df['text2'],  # use the new column for the hover text
            mode='markers',
            marker=dict(size=1.5*df['cylinders'])
    )]
layout = go.Layout(
    title='Vehicle mpg vs. horsepower',
    hovermode='closest'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubble2.html')
