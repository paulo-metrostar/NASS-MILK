import dash_html_components as html
import dash_core_components as dcc
import pandas as pd


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
                    
                    #html.A(
                    #    html.Button("Download full tidy data from this report (xlsx, csv, json, zip)", 
                                    # apologies for using the id for another element, didn't feel like defining the css for a new element right now
                    #                id="learn-more-button",
                    #            ),
                    #    href="https://github.com/paulo-metrostar/NASS-MILK/tree/master/enhance-milk-report-vis/dash-report/dummy-data",
                    #),
                    html.A(
                        "Download full tidy data from this report (xlsx, csv, json, zip)",
                        id="learn-more-button",
                        href = "https://github.com/paulo-metrostar/NASS-MILK/tree/master/enhance-milk-report-vis/dash-report/dummy-data",
                        style={"color": "#007364", "padding-top": "15px", "font-weight": "bold"}
                        
                    ),
                ],
                className="row",
            ),
            html.P(
                [
                    html.Strong("ISSN: [####-####] "),
                    html.Span("Released [MM-DD-YYYY] by the Martinez Agricultural Statistics Service (MASS), Agricultural Statistics Board, Paulo G. Martinez Department of Agriculture (PGMDA).")
                ], style={"padding-left": "25px"},
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
                "Overview",
                href="/dash-report/overview",
                className="tab first",
            ),
            dcc.Link(
                "Dictionary & Footnotes",
                href="/dash-report/data_dictionary",
                className="tab",
            ),
            dcc.Link(
                "Tables - Wide",
                href="/dash-report/tables",
                className="tab",
            ),
            dcc.Link(
                "Tidy Data - Long (Mo. Nat. 19-20)",
                href="/dash-report/tidy_data_long_monthly_nat",
                className="tab",
            ),
        ],
        className="row all-tabs",
    )
    return menu


def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    # init the html table with the first row being the column headers
    table = [html.Tr([html.Td(col, style={"font-weight": "bold"}) for col in df.columns])]
    # iterate through each df row
    for index, row in df.iterrows():
        # init an empty html row
        html_row = []
        for i in range(len(row)):
            
            # handle nulls (recall we are casting for HTML copy-pastability into excel which will handle blank strings to null conversion well)
            if pd.isna(row[i]):
                html_row.append(html.Td(''))
            
            # handle string values
            elif type(row[i]) == str:
                html_row.append(html.Td(row[i]))
                
            # handle ints
            elif str(row[i])[-2:] == ".0" or type(row[i]) == int:
                html_row.append(html.Td(f"{int(row[i]):,}"))
            
            # handle floats
            else:
                html_row.append(html.Td(row[i]))
                
        table.append(html.Tr(html_row))
        
    return table