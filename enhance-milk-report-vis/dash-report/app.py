# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from pages import (
    page1,
    page2
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
    if pathname == "/dash-report/page2":
        return page2.create_layout(app)
    elif pathname == "/dash-report/full-view":
        return (
            page1.create_layout(app),
            page2.create_layout(app)
        )
    else:
        return page1.create_layout(app)


if __name__ == "__main__":
    app.run_server(debug=True)