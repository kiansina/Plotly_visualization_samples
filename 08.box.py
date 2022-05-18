#######
# This simple box plot places the box beside
# the original data points on the same graph.
######
import plotly.offline as pyo
import plotly.graph_objs as go

# set up an array of 20 data points, with 20 as the median value
y = [1,14,14,15,16,18,18,19,19,20,20,23,24,26,27,27,28,29,33,54]

data = [
    go.Box(
        y=y,
        boxpoints='all', # display the original data points
        jitter=0.3,      # spread them out so they all appear
        pointpos=-1.8    # offset them to the left of the box
    )
]
pyo.plot(data, filename='box1.html')

#######################################################################

#######
# This simple box plot displays outliers
# above and below the box.
######
import plotly.offline as pyo
import plotly.graph_objs as go

# set up an array of 20 data points, with 20 as the median value
y = [1,14,14,15,16,18,18,19,19,20,20,23,24,26,27,27,28,29,33,54]

data = [
    go.Box(
        y=y,
        boxpoints='outliers' # display only outlying data points
    )
]
pyo.plot(data, filename='box2.html')
####################################################################

#######
# This plot compares sample distributions
# of three-letter-words in the works of
# Quintus Curtius Snodgrass and Mark Twain
######
import plotly.offline as pyo
import plotly.graph_objs as go

snodgrass = [.209,.205,.196,.210,.202,.207,.224,.223,.220,.201]
twain = [.225,.262,.217,.240,.230,.229,.235,.217]

data = [
    go.Box(
        y=snodgrass,
        name='QCS'
    ),
    go.Box(
        y=twain,
        name='MT'
    )
]
layout = go.Layout(
    title = 'Comparison of three-letter-word frequencies<br>\
    between Quintus Curtius Snodgrass and Mark Twain'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='box3.html')
