import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header, make_dash_table

import pandas as pd
import pathlib

# Load Data
# ---------------------------
# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../../dummy-data/").resolve()



# read in the quarterly data in tidy wide format
quarterly_long_df = pd.read_excel(
    io = DATA_PATH.joinpath("milk-prod-data-mart-reqs-1.5.xlsx"),
    sheet_name = "QtrNatWdYrsPrsntLst"
)
# rearrange the columns in the order they currently exist in the milk report
quarterly_long_df = quarterly_long_df[[
    'Quarter', '2019 Milk Cows', '2020 Milk Cows', '2019 Milk Per Cow', '2020 Milk Per Cow', '2019 Milk Production (lbs)', '2020 Milk Production (lbs)', '2020 Milk Production (lbs) Percent Change from 2019'
]]

# get qtly aggregates
agg_qtly_df = pd.read_excel(
    io = DATA_PATH.joinpath("milk-prod-data-mart-reqs-1.5.xlsx"),
    sheet_name = "AggrQNWYPL"
)[
    # rearrange the columns in the order they currently exist in the milk report
    [
    'Estimate', '2019 Milk Cows', '2020 Milk Cows', '2019 Milk Per Cow', '2020 Milk Per Cow', '2019 Milk Production (lbs)', '2020 Milk Production (lbs)', '2020 Milk Production (lbs) Percent Change from 2019'
]]


# read in the monthly nat data in tidy wide format
monthly_nat_wide_df = pd.read_excel(
    io = DATA_PATH.joinpath("milk-prod-data-mart-reqs-1.5.xlsx"),
    #sheet_name = "month-wide-region24-2019-2020",
    sheet_name = "MoNtnlWdYrsPrsntLst",
)
# rearrange the columns in the order they currently exist in the milk report
monthly_nat_wide_df = monthly_nat_wide_df[[
    'Month', '2019 Milk Cows', '2020 Milk Cows', '2019 Milk Per Cow', '2020 Milk Per Cow', '2019 Milk Production (lbs)', '2020 Milk Production (lbs)', '2020 Milk Production (lbs) Percent Change from 2019'
]]
# get monthly aggregates
agg_monthly_nat_wide_df = pd.read_excel(
    io = DATA_PATH.joinpath("milk-prod-data-mart-reqs-1.5.xlsx"),
    sheet_name = "AggrNWYPL"
)[
    # rearrange the columns in the order they currently exist in the milk report
    [
    'Estimate', '2019 Milk Cows', '2020 Milk Cows', '2019 Milk Per Cow', '2020 Milk Per Cow', '2019 Milk Production (lbs)', '2020 Milk Production (lbs)', '2020 Milk Production (lbs) Percent Change from 2019'
]]

# read in the monthly 24state data in tidy wide format
monthly_24st_wide_df = pd.read_excel(
    io = DATA_PATH.joinpath("milk-prod-data-mart-reqs-1.5.xlsx"),
    #sheet_name = "month-wide-region24-2019-2020",
    sheet_name = "Mo24stWdYrsPrsntLst",
)
# rearrange the columns in the order they currently exist in the milk report
monthly_24st_wide_df = monthly_24st_wide_df[[
    'Month', '2019 Milk Cows', '2020 Milk Cows', '2019 Milk Per Cow', '2020 Milk Per Cow', '2019 Milk Production (lbs)', '2020 Milk Production (lbs)', '2020 Milk Production (lbs) Percent Change from 2019'
]]
# get monthly aggregates
agg_monthly_24st_wide_df = pd.read_excel(
    io = DATA_PATH.joinpath("milk-prod-data-mart-reqs-1.5.xlsx"),
    sheet_name = "AggrM24sWYPL"
)[
    # rearrange the columns in the order they currently exist in the milk report
    [
    'Estimate', '2019 Milk Cows', '2020 Milk Cows', '2019 Milk Per Cow', '2020 Milk Per Cow', '2019 Milk Production (lbs)', '2020 Milk Production (lbs)', '2020 Milk Production (lbs) Percent Change from 2019'
]]



# Define HTML layout
# ---------------------------
def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 2
            html.Div(
                [
                    html.P("Values in tables may not add due to rounding. Blank cells indicate estimation period has not yet begun"),
                    # Row 3
                    html.Div(
                        [
                            html.H6(
                                        "Milk Cows and Production by Quarter - United States: 2019-2020",
                                        className="subtitle padded",
                                    ),
                            html.A(
                                "Analyze online ⚡️",
                                id="learn-more-button",
                                # saving page to pdf breaks the link by replacing "#" with "%23"
                                #href = "https://docs.google.com/spreadsheets/d/1ZcBD8Dk6EcTx1TuHo6_LdB0wcZkvPkXoptBmE7zWyXM/edit#gid=311186345",
                                href = "https://bit.ly/31d1Qnu",
                                style={
                                    "color": "#00c1a8", 
                                   #"padding-top": "15px", 
                                   "font-weight": "bold"
                                      }

                            ),
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
                    # Row 4
                    html.Div(
                        [
                            html.H6(
                                        "Milk Cows and Production by Month - [24 Selected] States: 2019-2020",
                                        className="subtitle padded",
                                    ),
                            html.A(
                                "Analyze online ⚡️",
                                id="learn-more-button",
                                # saving page to pdf breaks the link by replacing "#" with "%23"
                                href = "https://bit.ly/3j6K3ob",
                                #href = "https://docs.google.com/spreadsheets/d/1ZcBD8Dk6EcTx1TuHo6_LdB0wcZkvPkXoptBmE7zWyXM/edit#gid=1904881237",
                                style={
                                    "color": "#00c1a8", 
                                   #"padding-top": "15px", 
                                   "font-weight": "bold"
                                      }

                            ),
                            html.Table(
                                make_dash_table(
                                    monthly_24st_wide_df
                                ),
                            ),
                            # add aggregate
                            html.Table(
                                make_dash_table(
                                    agg_monthly_24st_wide_df
                                ),
                            ),
                        ],
                        style = {"overflow-x":"auto"},
                    ),
                    # Row 5
                    html.Div(
                        [
                            html.H6(
                                        "Estimated Milk Cows and Production by Month - United States: 2019-2020",
                                        className="subtitle padded",
                                    ),
                            html.A(
                                "Analyze online ⚡️",
                                id="learn-more-button",
                                # saving page to pdf breaks the link by replacing "#" with "%23"
                                href = "https://bit.ly/2H6q2RQ",
                                #href = "https://docs.google.com/spreadsheets/d/1ZcBD8Dk6EcTx1TuHo6_LdB0wcZkvPkXoptBmE7zWyXM/edit#gid=2641315",
                                style={
                                    "color": "#00c1a8", 
                                   #"padding-top": "15px", 
                                   "font-weight": "bold"
                                      }

                            ),
                            html.Table(
                                make_dash_table(
                                    monthly_nat_wide_df
                                ),
                            ),
                            # add aggregate
                            html.Table(
                                make_dash_table(
                                    agg_monthly_nat_wide_df
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