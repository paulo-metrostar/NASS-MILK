import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header, make_dash_table

import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
#DATA_PATH = PATH.joinpath("../data").resolve()


#df_fund_facts = pd.read_csv(DATA_PATH.joinpath("df_fund_facts.csv"))
#df_price_perf = pd.read_csv(DATA_PATH.joinpath("df_price_perf.csv"))


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
                                    html.H5("Page 2 Summary"),
                                    html.Br([]),
                                    html.P(
                                        "Page 2 Page 2 Page 2 etc",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                ],
                                className="product",
                            )
                        ],
                        className="row",
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )