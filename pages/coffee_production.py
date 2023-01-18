import dash
from dash import html, dcc, callback, Input, Output
import pandas as pd


dash.register_page(__name__)

df = pd.read_csv('coffee_analytics_csv/Coffee_production.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +
        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))],
    )


layout = html.Div(children=[
    html.H1(children='Coffee production (1990-2020)'),
    html.H4(children='Select a country: '),
    html.Div([
        dcc.Dropdown(
            df['Country'].unique(),
            'Country',
            id='analytics-input',
        ),
    ]),
    html.Br(),
    html.Div(id='analytics-output2'),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df['Country'], 'y': df['Total_production'], 'type': 'bar',
                 'name': 'Coffee production'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'coffee'},
            ],
        }
    ),
    html.H3(
        children='Coffee production table (1990-2020)',
    ),
    generate_table(df)

])


@callback(
    Output(component_id='analytics-output2', component_property='children'),
    Input(component_id='analytics-input', component_property='value')
)
def update_city_selected(input_value):
    return generate_table(df.loc[df['Country'] == input_value])
