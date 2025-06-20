import pandas as pd
from dash import Dash, dcc, html
# import dash_core_components as dcc
from dash import dcc
from dash import Input, Output
from dash import dash_table
from datetime import date
import plotly.graph_objects as go
import datetime as dt
import us
import model
import numpy as np
# from dash import dcc
# from dash_html_template import Template


import data_manager

# Filter options
all_options =  ["Housing Price Index", "S&P 500", "Lumber Prices", "Unemployment Rate", "Housing Supply", "Interest Rate", "Building Permits", "Consumer Price Index", "Rent Prices", "Savings", "Rental Vacancies", "Labor Participation"]
all_states = [state.name for state in us.states.STATES]
state_options = ["Housing Price Index", "S&P 500", "Unemployment Rate","Personal Income","Rental Vacancy"]
table_df = pd.DataFrame(columns=["Data_Set_1", "Data_Set_2", "Correlation_Coefficient"])


"""Import all data here"""
SP500_data = data_manager.get_sp500_data()
interest_data = data_manager.get_interest_rate_data()
house_supply_data = data_manager.get_house_supply_data()
lumber_data = data_manager.get_lumber_price_data()
hpi_data = data_manager.get_house_price_index_data()
unemployment_data = data_manager.get_unemployment_data()
permit_data = data_manager.get_permit_data()
cpi_data = data_manager.get_cpi_data()
rental_data = data_manager.get_rental_data()
savings_data = data_manager.get_savings_data()
rental_vac_data = data_manager.get_rental_vac_data()
labor_part_data = data_manager.get_labor_part_data()

correlation_data = data_manager.get_correlation_to_hpi()


data_manager.get_correlation_to_hpi()


"""State data"""
hpi_data_per_state = data_manager.hpi_data_state()
unemp_data_per_state = data_manager.unemployment_data()
personal_income = data_manager.personal_income_state()
rental_vacancy = data_manager.rental_vacancy_rate()


external_stylesheets = [
    {
        "href": (
            "https://fonts.googleapis.com/css2?"
            "family=Lato:wght@400;700&display=swap"
        ),
        "rel": "stylesheet",
    }
]

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    children=[

        # Header div
        html.Div(
            children=[
                html.P(
                    children="Data & Visual Analytics: Spring 2023 Project",
                    className="header-description"
                ),
                html.H1(children="Correlations of Housing Prices",
                        className='header-title'),
                html.P(
                    children="Joshua Tyndale, Chirag Dhawan, Timothy Lee, Yu-Xi Chen, Manasa Kumbashi, Nikolos Lahanis",
                    className="names"
                ),
            ],
            className="header"
        ),

        # Start of the tabs definition
        dcc.Tabs(id="tabs-example-graph", value='tab-1-example-graph', children=[

            # First tab (federal data)
            dcc.Tab(label='Federal Level Analysis', value='tab-1-example-graph',
                    children=[

                        # Filter check boxes div
                        html.Div(
                            children=[
                                html.Div(
                                    children=[
                                        html.Div(children="", className="menu-title"),
                                        dcc.Checklist(

                                           id="select-checklist",
                                           options=all_options,
                                           value=["Housing Price Index", "S&P 500", "Lumber Prices"]
                                           
                                        )
                                    ]
                                ),
                            ],
                            className="menu",
                        ),

                        # Date Range div
                        html.Div(
                            children=
                            [
                                dcc.DatePickerRange(
                                    id='my-date-picker-range',
                                    min_date_allowed=date(1975, 1, 1),
                                    max_date_allowed=date(2023, 1, 1),
                                    initial_visible_month=date(1975, 1, 1),
                                    start_date=date(1975, 1, 1),
                                    end_date=date(2023, 1, 1)
                                ),
                                html.Div(id='output-container-date-picker-range')
                            ],
                            className="date-range"
                        ),

                        # interactive line plot visualization div
                        html.Div(
                            children=[
                                html.Div(
                                    children=dcc.Graph(
                                        id="price-chart-2",
                                        config={"displayModeBar": False},
                                        # remove the floating toolbar that Plotly shows by default.
                                        className="card",
                                    ),
                                    className="wrapper",
                                )
                            ]
                        ),
                        
                        # Shows the top features in the form of bar chart
                        html.Div(
                            children=[
                                html.Div(
                                    children=dcc.Graph(
                                        id="features",
                                        config={"displayModeBar": False}, # remove the floating toolbar that Plotly shows by default.
                                        className="card",
                                    ),
                                className="wrapper",
                                )
                            ], style= {'display': 'block'}
                        ),


                        # table  div
                        html.Div(
                            children=[
                                html.Div(
                                    children=dash_table.DataTable(
                                        id="data-table",

                                        
                                        ),


                                    className="wrapper",
                                )
                            ], style= {'display': 'block'}
                        )

                    ]  # end of tab 1 children
                    ),  # End of Tab 1 container

            # Tab 2
            dcc.Tab(label='Local Level Analysis', value='tab-2-example-graph',
                    children=[
                    html.Div(
                        [
                        html.Div(
                            [
                            dcc.Dropdown(
                                id='state-dropdown',
                                options=[{'label': state, 'value': state} for state in all_states],
                                value='California',
                                style={'width': '200px', 'height':'50px','marginRight': '10px','padding-left': '100px','fontSize': '20px','text-align': 'center'}
                                    ),
                                ],
                            ),
                        html.Div(
                            [
                            dcc.DatePickerRange(
                                id='my-date-picker-range-state',
                                min_date_allowed=date(1975, 1, 1),
                                max_date_allowed=date(2023, 1, 1),
                                initial_visible_month=date(1975, 1, 1),
                                start_date=date(1975, 1, 1),
                                end_date=date(2023, 1, 1),
                                style={'width': '300px','height':'50px','marginLeft': '10px','fontSize': '20px'}
                                    )
                                ],
                            ),

                        ],style={'display': 'flex', 'justify-content': 'center', 'margin-bottom': '10px', 'margin-top': '30px'} ),


                    html.Div(
                        [
                        dcc.Graph(
                            id="price-chart-local",
                            config={"displayModeBar": False},
                            # remove the floating toolbar that Plotly shows by default.
                            className="card",
                            # style={'display': 'block', 'margin': 'auto', 'marginTop': '50px'}
                                    )
                                ], style={'width': '80%','display': 'block', 'margin': 'auto', 'marginTop': '20px'}
                            ),

                        # Checklist on the right
                        html.Div(
                            [
                            dcc.Checklist(id='select-checklist-local',
                                          options=state_options,
                                          value=["Housing Price Index","S&P 500","Personal Income"],
                                          labelStyle={'display': 'inline-block'}
                                          ),
                                ],
                            className="check-list-state",
                                ),


                        # Shows the top features in the form of bar chart
                        html.Div(
                            children=[
                                html.Div(
                                    children=dcc.Graph(
                                        id="features-local",
                                        config={"displayModeBar": False}, # remove the floating toolbar that Plotly shows by default.
                                        className="card",
                                    ),
                                className="wrapper",
                                )
                            ], style= {'display': 'block'}
                        ),

                        # table  div
                        html.Div(
                            children=[
                                html.Div(
                                    children=dash_table.DataTable(
                                        id="data-table-state",
                                    ),

                                    className="wrapper",
                                )
                            ], style={'display': 'block'}
                        ),

                        ]
                    )

                ]  # End of tabs children
         ),  # End of all tabs definition

    ]  # end of all children
)  # end of app

@app.callback(
    Output("features", "figure"),
    Input("select-checklist", "value"),
    Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date')
)
def update_charts(checked_data_sources, start_date, end_date):
    top_features, top_score = model.predict_top_features(checked_data_sources,SP500_data, interest_data, house_supply_data, lumber_data, hpi_data, unemployment_data, 5)
    #print(top_features)
    data = []
    data.append(go.Bar(
                {
                    "x": top_features, 
                    "y": top_score,
                    # "name": "Feature Score",
                }))
    top_features_figure = {
        "data": data, # Set data equal to line plot data array defined above
        "layout": 
            {"title": { 
                    "text": f" Linear Regression Top Feature : {top_features[0]}",
                    "x": 20
                    },
            "xaxis": {'title': 'Feature'},
            "yaxis": {'title': 'Score'},
            # "xaxis_title": "Feature", 
            # "yaxis_title": "Score", 
             "colorway": ["#7EC8E3"]
            }
        }
    if(len(checked_data_sources) <= 1):
        top_features_figure = {
        "data": data, # Set data equal to line plot data array defined above
        "layout": 
            {"title": { 
                    "text": f" Top Feature : {top_features[0]}",
                    "x": 20
                    },
            "xaxis": {'title': 'Feature'},
            "yaxis": {'title': 'Score'},
             "colorway": ["#7EC8E3"],
             'display': 'none'
            }
        }

    return  top_features_figure


@app.callback(
    Output("price-chart-2", "figure"),
    Input("select-checklist", "value"),
    Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date')
)
def update_charts(checked_data_sources, start_date, end_date):

    forecast = model.predict_future_values(checked_data_sources,SP500_data, interest_data, house_supply_data, lumber_data, hpi_data, unemployment_data)
    dates = []
    for item in list(forecast.index.values):
        ts = pd.to_datetime(str(item)) 
        dates.append(ts.strftime('%Y-%m-%d'))
    # print("The dates are : ")
    # print(dates)
    """This dynamically adds a new line for each data source checked on the gui"""
    line_plots = []
    for i in range(len(checked_data_sources)):
        if(checked_data_sources[i] == "S&P 500"):

            line_plots.append(go.Scatter(
                {
                    "x": SP500_data["Date"],
                    "y": SP500_data["Close*"],
                    "type": "lines",
                    "name": "S&P 500",
                    "line": dict(color="red")
                }))

        if(checked_data_sources[i] == "Interest Rate"):

            line_plots.append(go.Scatter(
                {
                    "x": interest_data["Date"],
                    "y": interest_data["FEDFUNDS"],
                    "type": "lines",
                    "name": "Interest Rate",
                    "line": dict(color="grey")
                }))

        if(checked_data_sources[i] == "Housing Supply"):        
            line_plots.append(go.Scatter(
                {
                    "x": house_supply_data["Date"],
                    "y": house_supply_data["MSACSR"],
                    "type": "lines",
                    "name": "Housing Supply",
                    "line": dict(color="orange")
                }))

        if(checked_data_sources[i] == "Lumber Prices"):

            line_plots.append(go.Scatter(
                {
                    "x": lumber_data["Date"],
                    "y": lumber_data["WPU081"],
                    "type": "lines",
                    "name": "Lumber Prices",
                    "line": dict(color="purple")
                }))

        if(checked_data_sources[i] == "Housing Price Index"):

            line_plots.append(go.Scatter(
                {
                    "x": hpi_data["Date"],
                    "y": hpi_data["USSTHPI_normalized"],
                    "type": "lines",
                    "name": "Housing Price Index",
                    "line": dict(color="blue")
                }))

            line_plots.append(go.Scatter(
                {
                    "x": dates,
                    "y": forecast.values, 
                    "type": "lines",
                    "name": "HPI forecast data",
                    "line": dict(dash='dash', color="green")
                }))
        if(checked_data_sources[i] == "Unemployment Rate"):

            line_plots.append(go.Scatter(
                {
                    "x": unemployment_data["Date"],
                    "y": unemployment_data["Value"],
                    "type": "lines",
                    "name": "Unemployment Rate",
                    "line": dict(color="brown")
                }))
        if(checked_data_sources[i] == "Building Permits"):
            line_plots.append(go.Scatter(
                {
                    "x": permit_data["Date"],
                    "y": permit_data["Total"], 
                    "type": "lines",
                    "name": "Building Permits",
                    "line": dict(color="black")
                }))
        if(checked_data_sources[i] == "Consumer Price Index"):
            line_plots.append(go.Scatter(
                {
                    "x": cpi_data["Date"],
                    "y": cpi_data["CPIAUCSL"], 
                    "type": "lines",
                    "name": "Consumer Price Index",
                    "line": dict(color="black")
                }))
        
        
        ###########################################################
        if(checked_data_sources[i] == "Rent Prices"):
            line_plots.append(go.Scatter(
                {
                    "x": rental_data["Date"],
                    "y": rental_data["CUSR0000SEHA"], 
                    "type": "lines",
                    "name": "Rent Prices",
                    "line": dict(color="magenta")
                }))
        if(checked_data_sources[i] == "Savings"):
            line_plots.append(go.Scatter(
                {
                    "x": savings_data["Date"],
                    "y": savings_data["PSAVERT"], 
                    "type": "lines",
                    "name": "Savings",
                    "line": dict(color="grey")
                }))
        if(checked_data_sources[i] == "Rental Vacancies"):
            line_plots.append(go.Scatter(
                {
                    "x": rental_vac_data["Date"],
                    "y": rental_vac_data["RRVRUSQ156N"], 
                    "type": "lines",
                    "name": "Rental Vacancies",
                    "line": dict(color="green")
                }))
        if(checked_data_sources[i] == "Labor Participation"):
            line_plots.append(go.Scatter(
                {
                    "x": labor_part_data["Date"],
                    "y": labor_part_data["CIVPART"], 
                    "type": "lines",
                    "name": "Labor Participation",
                    "line": dict(color="goldenrod")
                }))
        
        
    """This returns the figure on update"""
    end_date = '2031-01-01'
    price_chart_figure = {
        "data": line_plots, # Set data equal to line plot data array defined above
        "layout": 
            {"title": { 
                    "text": "Normalized Value of Features",
                    "x": 20
                    },
             #"xaxis": {'range': [dates[0] , dates[1]]},
             "xaxis": {'range': [start_date , end_date], 'title': 'Year'},
             #"xaxis": {"fixedrange": True},
             "yaxis": {
                 "fixedrange": True,
                 'showticklabels': False,
                 'title': 'Relative data'},
             "colorway": ["#17b897"]
            }
    }
    return price_chart_figure


@app.callback(
    Output("features-local", "figure"),
    Input("state-dropdown", "value"),
    Input("select-checklist-local", "value"),
    Input('my-date-picker-range-state', 'start_date'),
    Input('my-date-picker-range-state', 'end_date')
)
def update_charts(dropdown_value, selected_data_sources, start_date, end_date):
    top_features, top_score = model.predict_top_features_local(selected_data_sources,SP500_data, hpi_data_per_state[dropdown_value], unemp_data_per_state[dropdown_value],personal_income.loc[personal_income['state'] == dropdown_value],rental_vacancy[dropdown_value], 5)
    #print(top_features)
    data = []
    data.append(go.Bar(
                {
                    "x": top_features, 
                    "y": top_score,
                    # "name": "Feature Score",
                }))
    top_features_figure = {
        "data": data, # Set data equal to line plot data array defined above
        "layout": 
            {"title": { 
                    "text": f" Linear Regression Top Feature : {top_features[0]}",
                    "x": 20
                    },
            "xaxis": {'title': 'Feature'},
            "yaxis": {'title': 'Score'},
            # "xaxis_title": "Feature", 
            # "yaxis_title": "Score", 
             "colorway": ["#7EC8E3"]
            }
        }
    if(len(selected_data_sources) <= 1):
        top_features_figure = {
        "data": data, # Set data equal to line plot data array defined above
        "layout": 
            {"title": { 
                    "text": f" Top Feature : {top_features[0]}",
                    "x": 20
                    },
            "xaxis": {'title': 'Feature'},
            "yaxis": {'title': 'Score'},
             "colorway": ["#7EC8E3"],
             'display': 'none'
            }
        }

    return  top_features_figure


@app.callback(
    Output("price-chart-local", "figure"),
    Input("state-dropdown", "value"),
    Input("select-checklist-local", "value"),
    Input('my-date-picker-range-state', 'start_date'),
    Input('my-date-picker-range-state', 'end_date')
)
def update_charts_state(dropdown_value, selected_data_sources, start_date, end_date):
    # model.predict_top_features(checked_data_sources, SP500_data, interest_data, house_supply_data, lumber_data,
    #                            hpi_data, unemployment_data, 5)
    forecast = model.predict_future_values_local(selected_data_sources,SP500_data, interest_data, house_supply_data, lumber_data, hpi_data_per_state[dropdown_value], unemployment_data)
    dates = []
    for item in list(forecast.index.values):
        ts = pd.to_datetime(str(item)) 
        dates.append(ts.strftime('%Y-%m-%d'))
    """This dynamically adds a new line for each data source checked on the gui"""
    line_plots = []
    #print("state value is ", dropdown_value)
    #print("seleced data sources ", ",".join(selected_data_sources))
    for i in range(len(selected_data_sources)):
        if (selected_data_sources[i] == "S&P 500"):
            line_plots.append(go.Scatter(
                {
                    "x": SP500_data["Date"],
                    "y": SP500_data["Close*"],
                    "type": "lines",
                    "name": "S&P 500",
                    "line": dict(color="#2166ac")
                }))

        if (selected_data_sources[i] == "Housing Price Index"):
            # state_hpi = hpi_data_per_state.loc[hpi_data_per_state['state'] == dropdown_value]
            line_plots.append(go.Scatter(
                {
                    "x": hpi_data_per_state[dropdown_value]["Date"],
                    "y": hpi_data_per_state[dropdown_value]["hpi"],
                    "type": "lines",
                    "name": "Housing Price Index",
                    "line": dict(color="#b2182b")
                }))
            line_plots.append(go.Scatter(
                {
                    "x": dates,
                    "y": forecast.values, 
                    "type": "lines",
                    "name": "HPI forecast data",
                    "line": dict(dash='dash', color="green")
                }))
        if (selected_data_sources[i] == "Unemployment Rate"):
            line_plots.append(go.Scatter(
                {
                    "x": unemp_data_per_state[dropdown_value]["Date"],
                    "y": unemp_data_per_state[dropdown_value]["Value"],
                    "type": "lines",
                    "name": "Unemployment Rate",
                    "line": dict(color="#542788")
                }))
        if (selected_data_sources[i] == "Personal Income"):
            state_inc = personal_income.loc[personal_income['state'] == dropdown_value]
            line_plots.append(go.Scatter(
                {
                    "x": state_inc["Date"],
                    "y": state_inc["value"],
                    "type": "lines",
                    "name": "Personal Income",
                    "line": dict(color="#f4a582")
                }))
        if (selected_data_sources[i] == "Rental Vacancy"):
            # state_inc = rental_vacancy.loc[rental_vacancy['state'] == dropdown_value]
            line_plots.append(go.Scatter(
                {
                    "x": rental_vacancy[dropdown_value]["Date"],
                    "y": rental_vacancy[dropdown_value]["value"],
                    "type": "lines",
                    "name": "Rental Vacancy",
                    "line": dict(color="#999999")
                }))
    """This returns the figure on update"""
    end_date = '2031-01-01'
    price_chart_figure = {
        "data": line_plots,  # Set data equal to line plot data array defined above
        "layout":
            {"title": {
                "text":"Normalized Value of Features",
                "x": 20
            },
                # "xaxis": {'range': [dates[0] , dates[1]]},
                "xaxis": {'range': [start_date, end_date]},
                # "xaxis": {"fixedrange": True},
                "yaxis": {
                    "fixedrange": True,
                    'showticklabels': False},
                "colorway": ["#17b897"]
            }
    }
    return price_chart_figure


@app.callback(
    Output("data-table-state", "data"),
    Output("data-table-state", "columns"),
    Input("state-dropdown", "value"),
    Input("select-checklist-local", "value")
)

def update_table_state(state, checked_data_sources):

    df_to_return = pd.DataFrame(columns=["Data_Set_1", "Data_Set_2", "Correlation_Coefficient"])
    df_to_return = df_to_return[["Data_Set_1", "Data_Set_2", "Correlation_Coefficient"]]

    #
    for i in range(len(checked_data_sources) - 1):
        dataset_a = None
        if checked_data_sources[i] in ["Housing Price Index", "Unemployment Rate", "Personal Income",
                                       "Rental Vacancy"]:
            if checked_data_sources[i] == "Housing Price Index":
                hpi_data_temp = hpi_data_per_state[state]
                hpi_data_temp = hpi_data_temp.set_index('Date')
                hpi_data_temp = hpi_data_temp.resample('MS').ffill()
                hpi_data_temp['Date'] = hpi_data_temp.index
                # hpi_data_temp.reset_index(drop=True, inplace=True)
                dataset_a = hpi_data_temp["hpi"]
            if checked_data_sources[i] == "Unemployment Rate":
                unemp_data_temp = unemp_data_per_state[state]
                unemp_data_temp = unemp_data_temp.set_index('Date')
                unemp_data_temp['Date'] = unemp_data_temp.index
                dataset_a = unemp_data_temp["Value"]
            if checked_data_sources[i] == "Personal Income":
                pers_inc_temp = personal_income.loc[personal_income['state'] == state]
                pers_inc_temp = pers_inc_temp.set_index('Date')
                pers_inc_temp['Date'] = pers_inc_temp.index
                dataset_a = pers_inc_temp["value"]
            if checked_data_sources[i] == "Rental Vacancy":
                rental_data_temp = rental_vacancy[state]
                rental_data_temp = rental_data_temp.set_index('Date')
                rental_data_temp['Date'] = rental_data_temp.index
                dataset_a = rental_data_temp["value"]
        else:
            if checked_data_sources[i] == "S&P 500":
                sp_500_temp = SP500_data
                sp_500_temp = sp_500_temp.set_index('Date')
                sp_500_temp = sp_500_temp.resample('MS').mean()
                sp_500_temp['Date'] = sp_500_temp.index
                dataset_a = sp_500_temp['Close*']

        for j in range(i + 1, len(checked_data_sources)):
                dataset_b = None
                if checked_data_sources[j] in ["Housing Price Index", "Unemployment Rate", "Personal Income",
                                               "Rental Vacancy"]:
                    if checked_data_sources[j] == "Housing Price Index":
                        hpi_data_temp = hpi_data_per_state[state]
                        hpi_data_temp = hpi_data_temp.set_index('Date')
                        hpi_data_temp = hpi_data_temp.resample('MS').ffill()
                        hpi_data_temp['Date'] = hpi_data_temp.index
                        # hpi_data_temp.reset_index(drop=True, inplace=True)
                        dataset_b = hpi_data_temp["hpi"]
                    if checked_data_sources[j] == "Unemployment Rate":
                        unemp_data_temp = unemp_data_per_state[state]
                        unemp_data_temp = unemp_data_temp.set_index('Date')
                        unemp_data_temp['Date'] = unemp_data_temp.index
                        dataset_b = unemp_data_temp["Value"]
                    if checked_data_sources[j] == "Personal Income":
                        pers_inc_temp = personal_income.loc[personal_income['state'] == state]
                        pers_inc_temp = pers_inc_temp.set_index('Date')
                        pers_inc_temp['Date'] = pers_inc_temp.index
                        dataset_b = pers_inc_temp["value"]
                    if checked_data_sources[j] == "Rental Vacancy":
                        rental_data_temp = rental_vacancy[state]
                        rental_data_temp = rental_data_temp.set_index('Date')
                        rental_data_temp['Date'] = rental_data_temp.index
                        dataset_b = rental_data_temp["value"]
                        print("dsb rental", dataset_b.head())
                else:
                    if checked_data_sources[j] == "S&P 500":
                        sp_500_temp = SP500_data
                        sp_500_temp = sp_500_temp.set_index('Date')
                        sp_500_temp = sp_500_temp.resample('MS').mean()
                        sp_500_temp['Date'] = sp_500_temp.index
                        dataset_b = sp_500_temp['Close*']
                        # print("dsb",dataset_b.head())

                resampled_a = dataset_a.resample('MS').mean()
                resampled_b = dataset_b.resample('MS').mean()

                # Reindex both dataframes to a common set of dates
                common_index = resampled_a.index.union(resampled_b.index)
                dataset_a_reindexed = resampled_a.reindex(common_index)
                dataset_b_reindexed = resampled_b.reindex(common_index)

                # Create a new DataFrame with the row data
                coeff = round(dataset_a_reindexed.corr(dataset_b_reindexed), 4)

                df_to_return.loc[len(df_to_return.index)] = [checked_data_sources[i], checked_data_sources[j], coeff]
                print(df_to_return)
    df_to_return = df_to_return.sort_values(by="Correlation_Coefficient", ascending=False)


    print('in update table state')

    columns = [{'name': table_df.columns[i],'id': table_df.columns[i]} for i in range(len(table_df.columns))]
    # print(df_to_return.drop_duplicates().to_dict('records'))
    print('columns')
    print(columns)
    return df_to_return.drop_duplicates().to_dict('records'), columns


@app.callback(
    Output("data-table", "data"),
    Output("data-table", "columns"),
    Input("select-checklist", "value"))

def update_table(checked_data_sources):
    # n = len(checked_data_sources)
    # number_of_iterations = int(n*(n-1) / 2)

    df_to_return = pd.DataFrame(columns=["Data_Set_1", "Data_Set_2", "Correlation_Coefficient"])
    df_to_return = df_to_return[["Data_Set_1", "Data_Set_2", "Correlation_Coefficient"]]

    for i in range(len(checked_data_sources)):
        # This is the syntax to find a row that has the combination of two datasets
        current_row = correlation_data.loc[((correlation_data["Data_Set_2"] == checked_data_sources[i]))]

        """appending the dataframe here is probably cleaner"""
        if not current_row.empty:
            data_set_1 = current_row["Data_Set_1"].to_list()
            data_set_2 = current_row["Data_Set_2"].to_list()
            number = current_row["Correlation_Coefficient"].to_list()

            df_to_return.loc[len(df_to_return.index)] = [data_set_1[0], data_set_2[0], number[0]]

    """Sorting the Correlation_Coefficient in descending order"""
    df_to_return = df_to_return.sort_values(by="Correlation_Coefficient", ascending=False)

    
    if(len(checked_data_sources) > 1):
        columns=[{
            'name': table_df.columns[i],
            'id': table_df.columns[i]} for i in range(len(table_df.columns))]
    elif(len(checked_data_sources) <= 1):
        columns=[]
        
    return df_to_return.drop_duplicates().to_dict('records'), columns
    
@app.callback(
    Output("features", "style"),
    Input("select-checklist", "value"))
def hide_unhide_chart(checked_data_sources):
    if len(checked_data_sources) <= 1:
        return {'display': 'none'}
    elif  len(checked_data_sources) > 1:
        return {'display': 'block'}



if __name__ == "__main__":
    app.run_server(host="0.0.0.0", debug=False, port="8000")

    """
            "data": [go.Scatter(
            {
                "x": SP500_data["Date"],  #, house_supply_data['DATE']
                "y": SP500_data["Close*"],  #, house_supply_data['MSACSR']
                "type": "lines",
                "name": "S&P 500"
            },
        ),
            go.Scatter(
            {
                "x": interest_data["Date"],  #, house_supply_data['DATE']
                "y": interest_data["Effective Federal Funds Rate"],  #, house_supply_data['MSACSR']
                "type": "lines",
                "name": "Interest Rates",
                "fill": "none",  # ['none', 'tozeroy', 'tozerox', 'tonexty', 'tonextx','toself', 'tonext']
                "line": dict(color="red")
            },
                )
            ],
    """

    """
            # visualization div
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="price-chart",
                        config={"displayModeBar": False}, # remove the floating toolbar that Plotly shows by default.
                        figure={
                            "data": [
                                {
                                    "x": data["Date"],
                                    "y": data["Close*"],
                                    "type": "lines"
                                },
                            ],
                            "layout": 
                                {"title": { 
                                        "text": "S&P 500 Closes",
                                        "x": 20,
                                        #"text-align": "center",
                                        "xanchor": "left"
                                        },
                                 "xaxis": {"fixedrange": True},
                                 "yaxis": {"tickprefix": "$","fixedrange": True},
                                 "colorway": ["#17b897"]
                                }
                        },
                        className="card",
                    ),
                className="wrapper",
                )
            ]
        ),
    """