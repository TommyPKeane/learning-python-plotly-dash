import pathlib

import pytest
import plotly.express

from plotly_dash_demos.gantt_chart import (
    create_jobseeking_dataframe_from_csv,
    GanttJobSeeking,
)


@pytest.fixture()
def jobseeking_csv():
    return "/Path/To/JobSearch.csv"  # ⚠️ CHANGE THIS


@pytest.fixture()
def output_path():
    return pathlib.Path("/Path/To/Output/Directory/")  # ⚠️ CHANGE THIS


@pytest.fixture()
def output_file_basename():
    return "basename"  # ⚠️ CHANGE THIS


def test_jobseeking_2023(jobseeking_csv, output_path, output_file_basename):
    chart_obj = GanttJobSeeking(
        jobsearch_df=create_jobseeking_dataframe_from_csv(jobseeking_csv),
    )
    chart_obj.write_html(output_path / f"{output_file_basename}-Gantt.html")
    # chart_obj.show()

    status_sr = chart_obj.jobsearch_df["ApplicationStatus"].value_counts(normalize=False)
    status_df = status_sr.to_frame()

    fig_obj = plotly.express.pie(
        status_df,
        names=status_df.index,
        values="ApplicationStatus",
        custom_data=("ApplicationStatus",),
    ).update_traces(textinfo="value").update_layout(title="Job Search")  # ⚠️ CHANGE THIS
    fig_obj.write_html(output_path / f"{output_file_basename}-Pie.html")
    # fig_obj.show()

    role_sr = chart_obj.jobsearch_df["CommonRole"].value_counts(normalize=False)
    role_df = role_sr.to_frame()

    fig_obj = plotly.express.pie(
        role_df,
        names=role_df.index,
        values="CommonRole",
        custom_data=("CommonRole",),
    ).update_traces(textinfo="value").update_layout(title="Job Search")  # ⚠️ CHANGE THIS
    fig_obj.write_html(output_path / f"{output_file_basename}-Pie-Roles.html")
    # fig_obj.show()

    return None
