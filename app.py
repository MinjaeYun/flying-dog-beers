import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

fig = go.Figure() # or any Plotly Express function e.g. px.bar(...)
fig.add_trace(go.Candlestick(x=df['Date'],
                open=df['AAPL.Open'], high=df['AAPL.High'],
                low=df['AAPL.Low'], close=df['AAPL.Close'], name='Total'))
fig.add_trace(go.Scatter(x=df['Date'], y=df['AAPL.Close'],
                         line_color='rgb(0,200,200)',
                         name='Closing'))

########### Define your variables
tabtitle='minjae'
myheading='test'
githublink='https://github.com/MinjaeYun/flying-dog-beers'
sourceurl='https://mytrialforwhat.herokuapp.com/'

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='test',
        figure=fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A('Data Source', href=sourceurl),
    ]
)

if __name__ == '__main__':
    app.run_server()
