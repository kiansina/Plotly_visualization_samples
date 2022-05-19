#######
# Objective: Make a DataFrame using the Abalone dataset (../data/abalone.csv).
# Take two independent random samples of different sizes from the 'rings' field.
# HINT: np.random.choice(df['rings'],10,replace=False) takes 10 random values
# Use box plots to show that the samples do derive from the same population.
######

# Perform imports here:
import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go




# create a DataFrame from the .csv file:
df=pd.read_csv(r"C:\Users\sina.kian\Desktop\New folder\plotly\abalone.csv")

# take two random samples of different sizes:
A=np.random.choice(df['rings'],10,replace=False)
B= np.random.choice(df['rings'],10,replace=False)


# create a data variable with two Box plots:
data = [
    go.Box(
        y=A,
        name='sample 1'
    ),
    go.Box(
        y=B,
        name='sample 2'
    )
]
layout = go.Layout(
    title = 'Comparison of two samples'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='ex_box.html')










# add a layout




# create a fig from data & layout, and plot the fig
