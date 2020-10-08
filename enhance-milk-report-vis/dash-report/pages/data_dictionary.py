import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header, make_dash_table

import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../dummy-data/").resolve()

# get data
data_dict_df = pd.read_excel(
    io = DATA_PATH.joinpath("milk-prod-data-mart-reqs-1.5.xlsx"),
    sheet_name = "data-dictionary"
)

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
                                    html.H5("Data-Dictionary & Footnotes"),
                                    html.P(
                                        "A data-dictionary describes the attributes (aka variables) that appear in a table.",
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
                                        "Data Dictionary",
                                        className="subtitle padded",
                                    ),
                            html.Table(
                                make_dash_table(
                                    # select the columns in an order conducive to automated analysis 
                                    data_dict_df
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