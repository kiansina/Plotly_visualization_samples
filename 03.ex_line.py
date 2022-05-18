#######
# Objective: Using the file 2010YumaAZ.csv, develop a Line Chart
# that plots seven days worth of temperature data on one graph.
# You can use a for loop to assign each day to its own trace.
######

# Perform imports here:

import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go


# Create a pandas DataFrame from 2010YumaAZ.csv
df = pd.read_csv(r"C:\Users\sina.kian\Desktop\New folder\plotly\2010YumaAZ.csv")
days = ['TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY','MONDAY']


# Use a for loop (or list comprehension to create traces for the data list)
for i in range(1,8):
    locals()['trace'+str(i)]=[]

data = []
colors=['red','yellow','blue','black','green','brown','cyan']
c=0
for day in days:
    # What should go inside this Scatter call?
    trace = go.Scatter(
    x=df[df['DAY']==day]['LST_TIME'],
    y=df[df['DAY']==day]['T_HR_AVG'],
    mode='lines',
    line=dict(
    color=colors[c]
    ),
    name=day
    )
    data.append(trace)
    c+=1



# Define the layout
layout = go.Layout(
    title = 'Temperature tendency on each day of week',
    xaxis = dict(title = 'Day Time'), # x-axis label
    yaxis = dict(title = 'Temperature'), # y-axis label
    hovermode ='closest' # handles multiple points landing on the same vertical
)




# Create a fig from data and layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='ex_line.html')
