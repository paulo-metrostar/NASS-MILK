# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from pages import (
    overview,
    tables,
    data_dictionary,
    tidy_data_long_monthly_nat
)

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server

# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)

# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/report-generator/tables":
        return tables.create_layout(app)
    elif pathname == "/report-generator/tidy_data_long_monthly_nat":
        return tidy_data_long_monthly_nat.create_layout(app)
    elif pathname == "/report-generator/data_dictionary":
        return data_dictionary.create_layout(app)
    elif pathname == "/report-generator/full-view":
        return (
            overview.create_layout(app),
            data_dictionary.create_layout(app),
            tables.create_layout(app),
            tidy_data_long_monthly_nat.create_layout(app)
        )
    else:
        return overview.create_layout(app)


if __name__ == "__main__":
    app.run_server(debug=True)