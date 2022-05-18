#######
# Objective: Create a stacked bar chart from
# the file ../data/mocksurvey.csv. Note that questions appear in
# the index (and should be used for the x-axis), while responses
# appear as column labels.  Extra Credit: make a horizontal bar chart!
######

# Perform imports here:
import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go




# create a DataFrame from the .csv file:
df=pd.read_csv(r"C:\Users\sina.kian\Desktop\New folder\plotly\mocksurvey.csv")

# create traces using a list comprehension:
data=[]
colors=['blue','orange','green','red','pink']
c=1
for i in range(len(df.columns)-1):
    trace=go.Bar(
    x=df[df.columns[0]],
    y=df[df.columns[c]],
    name=df.columns[c],
    marker=dict(
    color=colors[c-1])
    )
    data.append(trace)
    if c < 5:
        c+=1





# create a layout, remember to set the barmode here
layout = go.Layout(
    title='Questionnaire',
    barmode='stack')




# create a fig from data & layout, and plot the fig.
fig=go.Figure(data=data,layout=layout)
pyo.plot(fig,filename='exercise_bar.html')
