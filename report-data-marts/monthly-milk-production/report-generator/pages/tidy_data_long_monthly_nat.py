import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header, make_dash_table

import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../../dummy-data/").resolve()

# get data
tidy_df = pd.read_excel(
    io = DATA_PATH.joinpath("milk-prod-data-mart-reqs-1.5.xlsx"),
    sheet_name = "MoNtnlLngYrsPrsntLst",
)
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
                            html.A(
                                "Analyze online ⚡️",
                                id="learn-more-button",
                                #href = "https://docs.google.com/spreadsheets/d/1ZcBD8Dk6EcTx1TuHo6_LdB0wcZkvPkXoptBmE7zWyXM/edit#gid=389230414",
                                href = "https://docs.google.com/spreadsheets/d/1ZcBD8Dk6EcTx1TuHo6_LdB0wcZkvPkXoptBmE7zWyXM/edit?usp=sharing",
                                style={
                                    "color": "#00c1a8", 
                                   #"padding-top": "15px", 
                                   "font-weight": "bold"
                                      }

                            ),
                            html.Table(
                                make_dash_table(
                                    # select the columns in an order conducive to automated analysis 
                                    tidy_df
                                ),
                            ),
                            
                        ],
                        style = {"overflow-x":"auto"},
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )