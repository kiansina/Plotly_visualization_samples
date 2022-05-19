#######
# This distplot uses plotly's Figure Factory
# module in place of Graph Objects
######
import plotly.offline as pyo
import plotly.figure_factory as ff
import numpy as np

x = np.random.randn(1000)
hist_data = [x]
group_labels = ['distplot']

fig = ff.create_distplot(hist_data, group_labels)
pyo.plot(fig, filename='basic_distplot.html')
#########################################################
#######
# This distplot demonstrates that random samples
# seldom fit a "normal" distribution.
######
import plotly.offline as pyo
import plotly.figure_factory as ff
import numpy as np

x1 = np.random.randn(200)-2
x2 = np.random.randn(200)
x3 = np.random.randn(200)+2
x4 = np.random.randn(200)+4

hist_data = [x1,x2,x3,x4]
group_labels = ['Group1','Group2','Group3','Group4']

fig = ff.create_distplot(hist_data, group_labels,bin_size=[.2,.1,.3,.4])
pyo.plot(fig, filename='multiset_distplot.html')
######################################################
#######
# This distplot looks back at the Mark Twain/
# Quintus Curtius Snodgrass data and tries
# to compare them.
######
import plotly.offline as pyo
import plotly.figure_factory as ff

snodgrass = [.209,.205,.196,.210,.202,.207,.224,.223,.220,.201]
twain = [.225,.262,.217,.240,.230,.229,.235,.217]

hist_data = [snodgrass,twain]
group_labels = ['Snodgrass','Twain']

fig = ff.create_distplot(hist_data, group_labels, bin_size=[.005,.005])
pyo.plot(fig, filename='SnodgrassTwainDistplot.html')
