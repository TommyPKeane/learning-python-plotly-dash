import json
import urllib

import pandas

from plotly_dash_demos.alluvial_flow_sankey import (
    describe_sankey_diagram_from_dataframes,
    sankey_diagram_from_dataframes,
)


def test_sankey_diagram_from_dataframes(plotly_example_sankey_energy_json):
    nodes_df = pandas.DataFrame(
        {
            "label": plotly_example_sankey_energy_json["data"][0]["node"]["label"],
            "color": plotly_example_sankey_energy_json["data"][0]["node"]["color"],
        },
    )
    links_df = pandas.DataFrame(
        {
            "source": plotly_example_sankey_energy_json["data"][0]["link"]["source"],
            "target": plotly_example_sankey_energy_json["data"][0]["link"]["target"],
            "value": plotly_example_sankey_energy_json["data"][0]["link"]["value"],
            "color": plotly_example_sankey_energy_json["data"][0]["link"]["color"],
        },
    )
    fig_obj = sankey_diagram_from_dataframes(
        nodes_df=nodes_df,
        links_df=links_df,
    )
    fig_obj.write_html("_plots/test_sankey_diagram_from_dataframes.html")
    return None


def test_describe_sankey_diagram_from_dataframes(plotly_example_sankey_energy_json):
    nodes_df = pandas.DataFrame(
        {
            "label": plotly_example_sankey_energy_json["data"][0]["node"]["label"],
            "color": plotly_example_sankey_energy_json["data"][0]["node"]["color"],
        },
    )
    links_df = pandas.DataFrame(
        {
            "source": plotly_example_sankey_energy_json["data"][0]["link"]["source"],
            "target": plotly_example_sankey_energy_json["data"][0]["link"]["target"],
            "value": plotly_example_sankey_energy_json["data"][0]["link"]["value"],
            "color": plotly_example_sankey_energy_json["data"][0]["link"]["color"],
        },
    )
    info = describe_sankey_diagram_from_dataframes(
        nodes_df=nodes_df,
        links_df=links_df,
    )
    with open("_plots/test_describe_sankey_diagram_from_dataframes.json", "w+") as file_obj:
        json.dump(info, file_obj, indent=2)
    return None
