# Import Libraries
import dash
from dash import dcc 
from dash import html
from dash import Dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px


# Load the dataset
df = pd.read_csv('price_prediction.csv')

# Create the Dash app
# app = dash.Dash()
app = dash.Dash(__name__)
server = app.server

#Set up the app layout
app.layout = html.Div([

        html.Div([
            html.H1(children= "House Pricing Prediction Dashboard",
            style={"text-align": "center", "color":"brown"},
            id="heading")
        ]),

        html.Div([
            html.Label(['X-axis categories to compare:'],style={'font-weight': 'bold',"color":"brown"}),
            dcc.RadioItems(
                id='xaxis_raditem',
                options=[
                         {'label': 'Total Basement Surface Area', 'value': 'Total Basement Surface Area'},
                         {'label': 'Above Ground Living Area', 'value': 'Above Ground Living Area'},
                         {'label': 'Number of Bedrooms', 'value': 'Bedrooms'},
                ],
                value='Bedrooms',
                style={"width": "50%", "color":"brown"}
            ),
        ]),

        html.Div([
            html.Br(),
            html.Label(['Y-axis values to compare:'], style={'font-weight': 'bold',"color":"brown"}),
            dcc.RadioItems(
                id='yaxis_raditem',
                options=[
                         {'label': 'Sale Price', 'value': 'SalePrice'},
                ],
                value='SalePrice',
                style={"width": "50%", "color":"brown"}
            ),
        ]),

    html.Div([
        html.Br(),
        html.Br(),
        dcc.Graph(id='the_graph')
    ]),

])

@app.callback(
    Output(component_id='the_graph', component_property='figure'),
    [Input(component_id='xaxis_raditem', component_property='value'),
     Input(component_id='yaxis_raditem', component_property='value')]
)

def update_graph(x_axis, y_axis):

    dff = df

    barchart=px.bar(
            data_frame=dff,
            x=x_axis,
            y=y_axis,
            title="Price variations with respect to "+x_axis,
            color_discrete_sequence=["#3d8361"],
            opacity=1,
            #facet_col='SaleCondition',
            #color='SaleCondition',
            #barmode='group',
            )

    barchart.update_layout(xaxis={'categoryorder':'total ascending'},
                           title={'xanchor':'center', 'yanchor': 'top', 'y':0.9,'x':0.5,},plot_bgcolor='#f4f9f9')

    return (barchart)


""" app.layout = html.Div(
    children=[
        html.H1(children="House Pricing Prediction Dashboard", style={'text-align': 'center'}),
        html.P(
            children="Display of predicted Sales Prices of houses", style={'text-align': 'center'}
        ),
        dcc.Dropdown(id='Neighborhood',
                 options= [{'label': i, 'value':i}
                          for i in df['Neighborhood'].unique()],
                value='Blmngtn'),
        dcc.Graph(
            figure={
                "data": [ 
                    {
                        "x": df["LotArea"],
                        "y": df["SalePrice"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Prices based on Lot Area"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [ 
                    {
                        "x": df["BedroomAbvGr"],
                        "y": df["SalePrice"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Price variations with respect to Number of Bedrooms"},
            },
        ),
    ]
) """

""" # Set up the app layout
app.layout = html.Div(children = [
    html.H1(children = 'Housing Prices Prediction Dashboard', style={'text-align': 'center'}),
    dcc.Dropdown(id='Neighborhood',
                 options= [{'label': i, 'value':i}
                          for i in df['Neighborhood'].unique()],
                value='Blmngtn'),
    dcc.Graph(id='price-graph')
])

# Set up the callback function
@app.callback(
    Output(component_id='price-graph',component_property='figure'),
    Input(component_id='Neighborhood', component_property='value')
)

def update_graph(selected_geography):
    filtered_df = df[df['Neighborhood'] == selected_geography]
    line_fig = px.line(filtered_df,
                        x='SaleCondition', y='SalePrice',
                        #color = 'HouseStyle',
                        title=f'House Prices in {selected_geography}')
    return line_fig
 """

# Run local server
if __name__ == '__main__':
    app.run_server(debug=True)
