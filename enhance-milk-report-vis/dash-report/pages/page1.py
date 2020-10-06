import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header, make_dash_table

import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../../data-mart-tech-specs").resolve()

# get data
tidy_df = pd.read_csv(DATA_PATH.joinpath("tidy-data.csv"))

# init the figure
col = 'Milk Production Lbs'
fig = go.FigureWidget()
# add some traces
for yr in tidy_df.Year.unique():
    if yr in {2020, 2019}:
        fig.add_trace(
            go.Scatter(
                x = tidy_df[tidy_df.Year == yr].sort_values(by = ['Month'])['Period'],
                y = tidy_df[tidy_df.Year == yr].sort_values(by = ['Month'])[col],
                mode = 'lines+markers',
                name = str(yr),
            )
        )
    # add the rest of the traces toggled off
    else:
        fig.add_trace(
            go.Scatter(
                x = tidy_df[tidy_df.Year == yr].sort_values(by = ['Month'])['Period'],
                y = tidy_df[tidy_df.Year == yr].sort_values(by = ['Month'])[col],
                mode = 'lines+markers',
                name = str(yr),
                visible='legendonly'
            )
        )
# Add title
fig.update_layout(
    title = 'Monthly ' + col + ' - National',
    #yaxis_title = col,
)

# init the figure
col = 'Milk Cows'
fig2 = go.FigureWidget()
# add some traces
for yr in tidy_df.Year.unique():
    if yr in {2020, 2019}:
        fig2.add_trace(
            go.Scatter(
                x = tidy_df[tidy_df.Year == yr].sort_values(by = ['Month'])['Period'],
                y = tidy_df[tidy_df.Year == yr].sort_values(by = ['Month'])[col],
                mode = 'lines+markers',
                name = str(yr),
            )
        )
    # add the rest of the traces toggled off
    else:
        fig2.add_trace(
            go.Scatter(
                x = tidy_df[tidy_df.Year == yr].sort_values(by = ['Month'])['Period'],
                y = tidy_df[tidy_df.Year == yr].sort_values(by = ['Month'])[col],
                mode = 'lines+markers',
                name = str(yr),
                visible='legendonly'
            )
        )
# Add title
fig2.update_layout(
    title = 'Monthly ' + col + ' - National',
    #yaxis_title = col,
)


def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        "[Month] Milk Production [up/down] [#.#] Percent.",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                    html.Br([]),
                                    html.P(
                                        [
                                            html.Strong("Milk production "),
                                            html.Span("in the United States during [MONTH] totaled [##.# order of magnitude] pounds, [up/down] [#.#] percent from [MONTH] [LAST YEAR].",
                                        style={"color": "#ffffff"},
                                        className="row",)
                                        ]
                                    ),
                                    html.P(
                                        [
                                            html.Strong("Production per cow "),
                                            html.Span("in the United States averaged [#,###] pounds for [MONTH], [##] pounds [above/below] [MONTH LAST YEAR].",
                                            style={"color": "#ffffff"},
                                            className="row",
                                            ),
                                        ]
                                    ),
                                    html.P(
                                        [
                                            html.Strong("The number of milk cows "),
                                            html.Span("on farms in the United States was [#,## order of magnitude] head, [##,###] head more than [MONTH LAST YEAR], but [unchanged from/above/below] [LAST MONTH]",
                                            style={"color": "#ffffff"},
                                            className="row",
                                            ),
                                        ]
                                    ),
                                ],
                                className="product",
                            )
                        ],
                        className="row",
                    ),
                    # Row 4
                    html.Div(
                        [
                            dcc.Graph(
                                id = 'month-national-milk-prod',
                                figure = fig
                            ),
                        ],
                    ),
                    # Row 5
                    html.Div(
                        [
                            dcc.Graph(
                                id = 'month-national-milk-prod',
                                figure = fig2
                            ),
                        ],
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )