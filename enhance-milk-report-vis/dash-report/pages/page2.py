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
# read in the quarterly data in tidy long format
quarterly_long_df = pd.read_excel(
    io = "dummy-data/milk-prod-data-mart-reqs-1.4.xlsx",
    sheet_name = "quarter-wide-nat-2019-2020"
)
# rearrange the columns in the order they currently exist in the milk report
quarterly_long_df = quarterly_long_df[[
    'Quarter', '2019 Milk Cows', '2020 Milk Cows', '2019 Milk Per Cow', '2020 Milk Per Cow', '2019 Milk Production (lbs)', '2020 Milk Production (lbs)', '2020 Milk Production (lbs) Percent Change from 2019'
]]

# get qtly aggregates
agg_qtly_df = pd.DataFrame()
agg_qtly_df['Annual'] = ['Aggregate']
for col in quarterly_long_df.columns:
    if col not in ('Quarter', '2020 Milk Production (lbs) Percent Change from 2019', 'Month'):
        agg_qtly_df['Sum ' + col] = [quarterly_long_df[col].sum()]

agg_qtly_df['Avg 2020 Milk Production (lbs) Percent Change from 2019'] = round(quarterly_long_df['2020 Milk Production (lbs) Percent Change from 2019'].mean(), 2)

# read in the quarterly data in tidy long format
monthly_long_df = pd.read_excel(
    io = "dummy-data/milk-prod-data-mart-reqs-1.4.xlsx",
    sheet_name = "month-wide-region24-2019-2020"
)
# rearrange the columns in the order they currently exist in the milk report
monthly_long_df = monthly_long_df[[
    'Month', '2019 Milk Cows', '2020 Milk Cows', '2019 Milk Per Cow', '2020 Milk Per Cow', '2019 Milk Production (lbs)', '2020 Milk Production (lbs)', '2020 Milk Production (lbs) Percent Change from 2019'
]]

# get monthly aggregates
agg_monthly_df = pd.DataFrame()
agg_monthly_df['Annual'] = ['Aggregate']
for col in monthly_long_df.columns:
    if col not in ('Quarter', '2020 Milk Production (lbs) Percent Change from 2019'):
        agg_monthly_df['Sum ' + col] = [monthly_long_df[col].sum()]

agg_monthly_df['Avg 2020 Milk Production (lbs) Percent Change from 2019'] = round(monthly_long_df['2020 Milk Production (lbs) Percent Change from 2019'].mean(), 2)

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
                                    html.H5("Tidy Data - Wide Format"),
                                    html.Br([]),
                                    html.P(
                                        "Wide format makes it very easy to automatically generate time-series analyses (line plots that show the change of a metric over time)",
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
                                        "Quarterly National Tidy Data - Wide Format",
                                        className="subtitle padded",
                                    ),
                            html.P("May not add due to rounding. Blank data cells indicate estimation period has not yet begun"),
                            html.Table(
                                make_dash_table(
                                    quarterly_long_df
                                ),
                            ),
                            # add aggregate
                            html.Table(
                                make_dash_table(
                                    agg_qtly_df
                                ),
                            ),
                        ],
                        style = {"overflow-x":"auto"},
                    ),
                    # Row 5
                    html.Div(
                        [
                            html.H6(
                                        "Monthly National Tidy Data - Wide Format",
                                        className="subtitle padded",
                                    ),
                            html.P("May not add due to rounding. Blank data cells indicate estimation period has not yet begun"),
                            html.Table(
                                make_dash_table(
                                    monthly_long_df
                                ),
                            ),
                            # add aggregate
                            html.Table(
                                make_dash_table(
                                    agg_monthly_df
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