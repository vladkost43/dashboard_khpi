import dash
from dash import dcc
from dash import html
import plotly.express as px

# Create sample data for KPIs and operational metrics
kpi_data = {
    'Sales': [500000, 20000, 100000, 200000, 300000],
    'Profit': [100000, 50000, 20000, 45000, 45000],
    'Customers': [1000, 800, 900, 1000, 1300],
    'Orders': [500, 932, 900, 200, 932],
}

operational_data = {
    'Monday': 120,
    'Tuesday': 150,
    'Wednesday': 100,
    'Thursday': 180,
    'Friday': 200
}

# Create the Dash application
app = dash.Dash(__name__)

# Create the layout for the KPI dashboard
kpi_layout = html.Div([
    html.H1('KPI Dashboard'),
    html.Div([
        html.Div([
            html.H3('Sales'),
            *[html.P(data) for data in kpi_data['Sales']],
        ], className='kpi-card'),
        html.Div([
            html.H3('Profit'),
            *[html.P(data) for data in kpi_data['Profit']],
        ], className='kpi-card'),
        html.Div([
            html.H3('Customers'),
            *[html.P(data) for data in kpi_data['Customers']],
        ], className='kpi-card'),
        html.Div([
            html.H3('Orders'),
            *[html.P(data) for data in kpi_data['Orders']],
        ], className='kpi-card')
    ], className='kpi-container')
])

# Create the layout for the operational dashboard
operational_layout = html.Div([
    html.H1('Operational Dashboard'),
    dcc.Graph(
        figure=px.bar(
            x=list(operational_data.keys()),
            y=list(operational_data.values()),
            labels={'x': 'Day', 'y': 'Value'},
            title='Daily Operational Metrics'
        )
    )
])

# Define the app's layout using tabs for different dashboard views
app.layout = html.Div([
    dcc.Tabs(id='dashboard-tabs', value='kpi-tab', children=[
        dcc.Tab(label='KPI Dashboard', value='kpi-tab'),
        dcc.Tab(label='Operational Dashboard', value='operational-tab')
    ]),
    html.Div(id='dashboard-content')
])

# Define callback to switch between dashboard views
@app.callback(
    dash.dependencies.Output('dashboard-content', 'children'),
    [dash.dependencies.Input('dashboard-tabs', 'value')]
)
def switch_dashboard_tab(tab):
    if tab == 'kpi-tab':
        return kpi_layout
    elif tab == 'operational-tab':
        return operational_layout
    else:
        return html.Div('Invalid tab selected.')


# Run the Dash application
if __name__ == '__main__':
    app.run_server(debug=True)
