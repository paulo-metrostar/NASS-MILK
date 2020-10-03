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

def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
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
                            html.H6(
                                        "Monthly National Tidy Data - Long Format",
                                        className="subtitle padded",
                                    ),
                            html.Table(
                                make_dash_table(
                                    # select the columns in an order conducive to automated analysis 
                                    tidy_df[[
                                        'Milk Cows', 'Milk Production Lbs', 'Milk Per Cow', 'Period', 'Year', 'Month'
                                    ]][
                                        # filter to only the 2019 2020 data
                                        tidy_df.Year >= 2019
                                    ]
                                ),
                            )
                        ],
                        style = {"overflow-x":"auto"},
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )