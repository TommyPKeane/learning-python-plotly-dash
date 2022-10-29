"""Demos of Sankey Diagrams (also called Alluvial or Flow Diagrams)

References:
- https://en.wikipedia.org/wiki/Alluvial_diagram
- https://en.wikipedia.org/wiki/Sankey_diagram
- https://plotly.com/python/sankey-diagram/
"""
# import pandas
import plotly.graph_objects


def sankey_diagram_from_dataframes(
    nodes_df,
    links_df,
):
    """
    """
    figure_obj = None
    figure_obj = plotly.graph_objects.Figure(
        data=[
            plotly.graph_objects.Sankey(
                valueformat=".0f",
                valuesuffix="TWh",
                node={
                    "pad": 15,
                    "thickness": 15,
                    "line": {
                        "color": "black",
                        "width": 0.5,
                    },
                    "label": nodes_df["label"].values.tolist() if "label" in nodes_df else None,
                    "color": nodes_df["color"].values.tolist() if "color" in nodes_df else None,
                },
                link={
                    "source": links_df["source"].values.tolist(),
                    "target": links_df["target"].values.tolist(),
                    "value": links_df["value"].values.tolist(),
                    "label": links_df["label"].values.tolist() if "label" in links_df else None,
                    "color": links_df["color"].values.tolist() if "color" in links_df else None,
                },
            ),
        ],
    )
    return figure_obj

