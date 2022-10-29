"""Example Demo of a `dash` Web-app for Geographical Data Visualizations

References:
- https://plotly.com/python/px-arguments/
"""
import logging
import warnings
import webbrowser

import pandas
import plotly.express
from dash import Dash, dcc, html


dash_app = None

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    dash_app = Dash(__name__)

module_logs = logging.getLogger(__name__)

us_cities = pandas.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")

fig = plotly.express.scatter_mapbox(
    us_cities,
    lat="lat",
    lon="lon",
    hover_name="City",
    hover_data=["State", "Population"],
    color_discrete_sequence=["fuchsia"],
    zoom=3,
    height=300,
)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

dash_app.layout = html.Div(
    children=[
        html.H1(children="👋 Hello Dash"),
        html.Div(children="⚡️ Top 1,000 US Cities by Census Population"),
        dcc.Graph(id="us-cities-data", figure=fig),
    ],
)


def test_run(
    run_host,
    run_port,
):
    """Run the main runtime app as a pytest Test

    ⚠️ Note that this method alias has to start with `test_` so that it will be
    captured by `pytest` as runnable.
    """
    app_url = (
        f"{run_host}:{run_port}"
        if run_host.startswith("unix://")
        else f"http://{run_host}:{run_port}"
    )
    try:
        module_logs.info(f"🌐  Opening App URL: {app_url}")
        webbrowser.open(app_url, new=2)
        module_logs.info("⚡️  Starting Dash Server")
        module_logs.info("👋  End Demo by pressing `CTRL+C`")
        dash_app.run_server(
            host=run_host,
            port=run_port,
            debug=True,
        )
    except KeyboardInterrupt:
        pass  # Quit Quietly (Successfully)
    return None
