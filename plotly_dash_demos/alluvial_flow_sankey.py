"""Demos of Sankey Diagrams (also called Alluvial or Flow Diagrams)

References:
- https://en.wikipedia.org/wiki/Alluvial_diagram
- https://en.wikipedia.org/wiki/Sankey_diagram
- https://plotly.com/python/sankey-diagram/
- https://community.plotly.com/t/sankey-diagram-with-percentages/28884/3
"""
import numpy
import pandas
import plotly.graph_objects


class SankeyDiagramInfo(dict):
    """Python dict Container for Sankey Diagram data information.

    Note that this class is filled-in by the utility method:
    `describe_sankey_diagram_from_dataframes()`

    Keys:
        sources (list[int]): All Link "source" Indices
        targets (list[int]): All Link "target" Indices
        all_values (list[float]): All Link "value" Values, which are (by design)
            equal for both the "source" and the "target" of the Link
        node_labels (list[str]): Labels (strings) for all the Nodes
        node_colors (list[str]): `rgb()` or `rgba()` Strings for coloring each
            Node.
        source_values (dict[str, float]): Sum Total of Out-flow Values for each
            Node by aligning all the "source" values for every Link.
        target_values (dict[str, float]): Sum Total of In-flow Values for each
            Node by aligning all the "target" values for every Link.
        node_balance (dict[str, float]): Difference between the sum-total of the
            in-flow values vs. the sum-total out-flow values for each Node.
        deficit_nodes (dict[str, float]): Nodes where the sum of the output flow
            of values is more than the input flow of values.
        surplus_nodes (dict[str, float]): Nodes where the sum of the output flow
            of values is less than the input flow of values.
        balanaced_nodes (dict[str, float]): Nodes where the in-flow and out-flow
            of values are equivalent in sum-total. Depending on the context, all
            Nodes may be balanced, but this is not a necessity of the
            visualization.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__post_init__()
        return None

    def __post_init__(self):
        self["sources"] = None
        self["targets"] = None
        self["all_values"] = None
        self["node_labels"] = None
        self["node_colors"] = None
        self["source_values"] = None
        self["target_values"] = None
        self["node_balance"] = None
        self["deficit_nodes"] = None
        self["surplus_nodes"] = None
        self["balanaced_nodes"] = None
        return None


def describe_sankey_diagram_from_dataframes(
    nodes_df: pandas.DataFrame,
    links_df: pandas.DataFrame,
) -> SankeyDiagramInfo:
    """Summary

    Args:
        nodes_df (pandas.DataFrame): Description
        links_df (pandas.DataFrame): Description
    """
    sankey_info = SankeyDiagramInfo()

    sankey_info["sources"] = links_df["source"].values.tolist()
    sankey_info["targets"] = links_df["target"].values.tolist()
    sankey_info["all_values"] = links_df["value"].values.tolist()
    sankey_info["node_labels"] = nodes_df["label"].values.tolist()
    sankey_info["node_colors"] = nodes_df["color"].values.tolist()

    sankey_info["source_values"] = {
        sankey_info["node_labels"][source]: sum(links_df["value"][links_df["source"] == source].values)
        for source in sankey_info["sources"]
    }
    sankey_info["target_values"] = {
        sankey_info["node_labels"][target]: sum(links_df["value"][links_df["target"] == target].values)
        for target in sankey_info["targets"]
    }
    sankey_info["node_balance"] = {
        node: sankey_info["target_values"].get(node, 0) - sankey_info["source_values"].get(node, 0)
        for node in sankey_info["node_labels"]
    }
    sankey_info["deficit_nodes"] = {
        node: value
        for node, value in sankey_info["node_balance"].items()
        if value < 0
    }
    sankey_info["surplus_nodes"] = {
        node: value
        for node, value in sankey_info["node_balance"].items()
        if value > 0
    }
    sankey_info["balanaced_nodes"] = {
        node: value
        for node, value in sankey_info["node_balance"].items()
        if value == 0
    }
    return sankey_info


def sankey_diagram_from_dataframes(
    nodes_df: pandas.DataFrame,
    links_df: pandas.DataFrame,
) -> plotly.graph_objects.Figure:
    """Create a Sankey Diagram Figure Object from two DataFrames for the Nodes
    and Links

    A Sankey Diagram is comprised of Links that essentially are defined as a
    3-tuple of the "source", "target", and "value" elements. The "source" is the
    index of the Node where a flow linkage should begin, and the "target" is the
    index of the Node where that flow linkage should end. The "value" defines
    the amount (in the common data Domain) of the node at the source and at the
    target that the flow linkage should represent.

    These values are direct domain values, not proportions (unless the domain is
    proportional or fractional). This means that it's the duty of the caller of
    this method to make sure that the values are consistent and meaningful.

    Since the Nodes do not have a "value" field, their overall size is set by
    the proportional size of all the nodes in the diagram, relative the maximum
    Node's size. The size of the maximum node is determined automatically by
    finding the Node which has the largest sum total of all Link values for that
    Node. Note that the sum of all "source" values and the sum of all "target"
    values are generally unrelated, such that the size of a Node is defined by
    whichever sum ("source" or "target") is largest.

    To further break-down the design of this diagram, we have the utility method
    called `describe_sankey_diagram_from_dataframes()`.

    Arguments:
        nodes_df (pandas.DataFrame): Nodes of the Sankey Diagram (the vertical
            rectangular bars that connect the flow Links). Expected Columns:
            - "label"
            - "color"
        links_df (pandas.DataFrame): Links of the Sankey Diagram (the horizontal
            flow bars between Nodes). Expected Columns:
            - "source"
            - "target"
            - "value"
            - "label"
            - "color"

    Returns:
        plotly.graph_objects.Figure: plotly.graph_objects.Sankey Figure instance
    """
    sankey_info = describe_sankey_diagram_from_dataframes(
        nodes_df=nodes_df,
        links_df=links_df,
    )

    nodes_customdata: numpy.ndarray = numpy.stack(
        (
            [sankey_info["node_balance"][label] for label in nodes_df["label"].values.tolist()],
            [sankey_info["target_values"].get(label, 0) for label in nodes_df["label"].values.tolist()],
            [sankey_info["source_values"].get(label, 0) for label in nodes_df["label"].values.tolist()],
        ),
        axis=-1,
    )

    links_customdata: numpy.ndarray = numpy.array([])

    figure_obj = None
    figure_obj = plotly.graph_objects.Figure(
        data=[
            plotly.graph_objects.Sankey(
                valueformat=".0f",
                valuesuffix=" [TWh]",
                node={
                    "pad": 15,
                    "thickness": 15,
                    "line": {
                        "color": "black",
                        "width": 0.5,
                    },
                    "label": nodes_df["label"].values.tolist() if "label" in nodes_df else None,
                    "color": nodes_df["color"].values.tolist() if "color" in nodes_df else None,
                    "customdata": nodes_customdata,
                    "hovertemplate": (
                        "<b>%{label}</b><br>"
                        "Balance: %{customdata[0]:+,.3} [TWh]<br>"
                        "(+) In: %{customdata[1]:,} [TWh]<br>"
                        "(-) Out: %{customdata[2]:,} [TWh]<br>"
                        "<extra>%{value}</extra>"
                    ),
                },
                link={
                    "customdata": links_customdata,
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
