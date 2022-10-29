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

warnings.filterwarnings("ignore", category=DeprecationWarning)

dash_app = Dash(__name__)

module_logs = logging.getLogger(__name__)

bargraph_df = pandas.DataFrame(
    {
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"],
    },
)

fig = plotly.express.bar(
    bargraph_df,
    x="Fruit",
    y="Amount",
    color="City",
    barmode="group",
)

dash_app.layout = html.Div(
    children=[
        html.H1(children="👋 Hello Dash"),
        html.Div(children="⚡️ Dash: A web application framework for your data."),
        dcc.Graph(id="city-fruits-bar", figure=fig),
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
