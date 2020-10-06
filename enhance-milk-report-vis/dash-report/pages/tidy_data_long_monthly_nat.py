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
# cast Year column to string
if 'Year' in tidy_df.columns:
    tidy_df = tidy_df.astype({'Year': 'str'})

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
                                    html.H5("Tidy Data - Long Format"),
                                    html.P(
                                        "Long format makes it very easy to automatically generate correlation analyses (scatter plots showing change of one variable as a function of another)",
                                        style={"color": "#ffffff"},
                                        className="row",
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
                                        pd.to_numeric(tidy_df.Year) >= 2019
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