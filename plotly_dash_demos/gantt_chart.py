import pandas
import plotly.express


def create_jobseeking_dataframe_from_csv(
    csv_filename,
):
    tmp_df = pandas.read_csv(
        csv_filename,
        index_col=False,
    )
    jobsearch_df = pandas.DataFrame().assign(
        **{
            "Company": tmp_df["company"],
            "Role": tmp_df["role"],
            # "URL": tmp_df["job listing url"],
            "ApplicationDate": tmp_df["application date"],
            "ApplicationStatus": tmp_df["status"],
            # "": tmp_df["last-checked date"],
            "FirstContact": tmp_df["first contact date"],
            "NumberOfInterviews": tmp_df["number of interviews"],
            "Outcome": tmp_df["final response"],
            "LastContact": tmp_df["final response date"],
        },
    )
    jobsearch_df["LastContact"].fillna(
        value="2023-02-09",
        inplace=True,
    )
    jobsearch_df["Outcome"].fillna(
        value="Open",
        inplace=True,
    )
    return jobsearch_df


class GanttJobSeeking():
    jobsearch_df = None
    figure_obj = None
    index_col_name = "Application Status"
    show_colorbar = False
    group_tasks = False
    color_mapping = {
        "Applied": "#72A0C1", # (0.45, 0.63, 0.76, 1.00),  # Air superiority blue
        "Contacted by Recruiter": "#72A0C1", # (0.45, 0.63, 0.76, 1.00),  # Air superiority blue
        "In Review": "#7FFFD4", # (0.50, 1.00, 0.83, 1.00),  # Aquamarine
        "Interviewing": "#3B7A57", # (0.23, 0.48, 0.34, 1.00),  # Amazon
        "Rejected": "#B31B1B", # (0.70, 0.11, 0.11, 1.00),  # Carnelian
        "No Contact": "#915C83", # (0.57, 0.36, 0.51, 1.00),  # Antique fuchsia
    }
    x_daterange = (
        # "2022-10-16",
        # "2022-10-23",
        # "2022-10-30",
        # "2022-11-06",
        # "2022-11-13",
        # "2022-11-20",
        # "2022-11-27",
        # "2022-12-04",
        # "2022-12-11",
        # "2022-12-18",
        # "2022-12-25",
        "2023-01-01",
        # "2023-01-08",
        # "2023-01-15",
        # "2023-01-22",
        # "2023-01-29",
        # "2023-02-05",
        # "2023-02-12",
        "2023-02-19",
    )

    def __init__(
        self,
        jobsearch_df: pandas.DataFrame = None,
        color_mapping: dict = None,
        index_col_name: str = None,
        show_colorbar: bool = None,
        group_tasks: bool = None,
    ):
        self.__update_attributes(
            jobsearch_df,
            color_mapping,
            index_col_name,
            show_colorbar,
            group_tasks,
        )
        self.update_figure()
        return None

    def __update_attributes(
        self,
        jobsearch_df: pandas.DataFrame = None,
        color_mapping: dict = None,
        index_col_name: str = None,
        show_colorbar: bool = None,
        group_tasks: bool = None,
    ):
        if jobsearch_df is not None:
            self.jobsearch_df = jobsearch_df
        else:
            pass

        if color_mapping is not None:
            self.color_mapping = color_mapping
        else:
            pass

        if index_col_name is not None:
            self.index_col_name = index_col_name
        else:
            pass

        if show_colorbar is not None:
            self.show_colorbar = show_colorbar
        else:
            pass

        if group_tasks is not None:
            self.group_tasks = group_tasks
        else:
            pass
        return None

    def update_figure(
        self,
        jobsearch_df: pandas.DataFrame = None,
        color_mapping: dict = None,
        index_col_name: str = None,
        show_colorbar: bool = None,
        group_tasks: bool = None,
    ):
        self.__update_attributes(
            jobsearch_df,
            color_mapping,
            index_col_name,
            show_colorbar,
            group_tasks,
        )
        self.figure_obj = plotly.express.timeline(
            self.jobsearch_df[self.jobsearch_df["ApplicationDate"] > self.x_daterange[0]],
            x_start="ApplicationDate",
            x_end="LastContact",
            y="Role",
            hover_name="Company",
            # facet_row="Role",
            # facet_row_spacing=0.010,
            color="ApplicationStatus",
            color_discrete_map=self.color_mapping,
            # index_col=self.index_col_name,
            # show_colorbar=self.show_colorbar,
            # group_tasks=self.group_tasks,
        )
        self.figure_obj.update_xaxes(range=self.x_daterange)
        return None

    def show(self, *args, **kwargs):
        self.figure_obj.show(*args, **kwargs)
        return None

    def write_html(self, *args, **kwargs):
        self.figure_obj.write_html(*args, **kwargs)
        return None