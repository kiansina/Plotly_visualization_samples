#######
# Objective: Using the iris dataset, develop a Distplot
# that compares the petal lengths of each class.
# File: '../data/iris.csv'
# Fields: 'sepal_length','sepal_width','petal_length','petal_width','class'
# Classes: 'Iris-setosa','Iris-versicolor','Iris-virginica'
######

# Perform imports here:
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import plotly.offline as pyo



# create a DataFrame from the .csv file:
df=pd.read_csv(r"C:\Users\sina.kian\Desktop\New folder\plotly\iris.csv")


# Define the traces
hist_data=[]
group_labels=[]
for i in df['class'].unique():
    x=df[df['class']==i]['petal_length']
    hist_data.append(x)
    group_labels.append(i)
# HINT:
# This grabs the petal_length column for a particular flower
#df[df['class']=='Iris-some-flower-class']['petal_length']



# Define a data variable



# Create a fig from data and layout, and plot the fig
fig = ff.create_distplot(hist_data, group_labels)
pyo.plot(fig, filename='flower_length_comparison.html')
