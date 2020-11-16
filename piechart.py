import plotly.plotly as py
from plotly.graph_objs import *

fig = {
    'data': [{'labels': ['Residential', 'Non-Residential', 'Utility'],
              'values': [19, 26, 55],
              'type': 'pie'}],
    'layout': {'title': 'Forcasted 2014 U.S. PV Installations by Market Segment'}
}

url = py.plot(fig, validate=False, filename='Pie Chart Example')
