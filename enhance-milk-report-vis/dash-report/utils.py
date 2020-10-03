import dash_html_components as html
import dash_core_components as dcc


def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])


def get_header(app):
    header = html.Div(
        [
            html.Div(
                [
                    html.Img(
                        src=app.get_asset_url("USDA-NASS-logos.png"),
                        className="logo",
                    ),
                    html.A(
                        html.Button("Download the full tidy data set for all years", 
                                    # apologies for using the id for another element, didn't feel like defining the css for a new element right now
                                    id="learn-more-button"),
                        href="https://github.com/paulo-metrostar/NASS-MILK/blob/master/enhance-milk-report-vis/data-mart-tech-specs/tidy-data.csv",
                    ),
                    
                ],
                className="row",
            ),
            html.P(
                        "ISSN: [####-####] Released [MM-DD-YYYY] by the Martinez Agricultural Statistics Service (MASS), Agricultural Statistics Board, Paulo G. Martinez Department of Agriculture (PGMDA).",
                        style={"padding-left": "25px"},
                    ),
            html.Div(
                [
                    html.Div(
                        [html.H5("Milk Production")],
                        className="seven columns main-title",
                    ),
                    html.Div(
                        [
                            dcc.Link(
                                "Full View",
                                href="/dash-report/full-view",
                                className="full-view-link",
                            )
                        ],
                        className="five columns",
                    ),
                ],
                className="twelve columns",
                style={"padding-left": "0"},
            ),
        ],
        className="row",
    )
    return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "Page 1",
                href="/dash-report/page1",
                className="tab first",
            ),
            dcc.Link(
                "Page 2",
                href="/dash-report/page2",
                className="tab",
            ),
            dcc.Link(
                "Tidy Data Long Monthly National 2019 & 2020",
                href="/dash-report/tidy_data_long_monthly_nat",
                className="tab",
            )
        ],
        className="row all-tabs",
    )
    return menu


def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    # init the html table with the first row being the column headers
    table = [html.Tr([html.Td(col) for col in df.columns])]
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table