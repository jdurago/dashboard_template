import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.figure_factory as ff

import numpy as np
from utils import gini


app = dash.Dash('')

data1 =np.random.power(50,500)
data2 = np.random.uniform(0,1,10000)

print 'Gini of Data1: ', gini(data1)
print 'Gini of Data2: ', gini(data2)

trace1 = go.Histogram(
                    x=data1,
                    histnorm='probability density',
                    name='power distribution',
                    cumulative=dict(enabled=True)

                )

trace2 = go.Histogram(
                    x=data2,
                    histnorm='probability density',
                    name='unform',
                    cumulative=dict(enabled=True)

                )

data = [trace1, trace2]

app.layout = html.Div(children=[
    dcc.Graph(
        id='my-graph',
        figure=go.Figure(
            data=data,
            layout=go.Layout(
                title='Lorenz Curve of ETH',
                showlegend=True,
                legend=go.Legend(
                    x=0,
                    y=1.0
                ),
                margin=go.Margin(l=40, r=0, t=40, b=30)
            )
        ),

    )
])

app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

if __name__ == '__main__':
    app.run_server(host='0.0.0.0')