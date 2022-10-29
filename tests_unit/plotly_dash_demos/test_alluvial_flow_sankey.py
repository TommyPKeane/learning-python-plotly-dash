import json
import urllib

import pandas

from plotly_dash_demos.alluvial_flow_sankey import sankey_diagram_from_dataframes

def test_sankey_diagram_from_dataframes():
    url = "https://raw.githubusercontent.com/plotly/plotly.js/master/test/image/mocks/sankey_energy.json"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    nodes_df = pandas.DataFrame(
        {
            "label": data["data"][0]["node"]["label"],
            "color": data["data"][0]["node"]["color"],
        },
    )
    links_df = pandas.DataFrame(
        {
            "source": data["data"][0]["link"]["source"],
            "target": data["data"][0]["link"]["target"],
            "value": data["data"][0]["link"]["value"],
            "color": data["data"][0]["link"]["color"],
        },
    )
    fig_obj = sankey_diagram_from_dataframes(
        nodes_df=nodes_df,
        links_df=links_df,
    )
    fig_obj.show()
    return None
