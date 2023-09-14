from datetime import date
from functools import cache
from typing import cast

import geopandas as gpd
import importlib_resources
import pandas as pd


@cache
def all() -> pd.DataFrame:
    source = (
        importlib_resources.files(__package__)
        .joinpath("resources")
        .joinpath("outbreaks.csv")
    )

    with importlib_resources.as_file(source) as csv:
        return pd.read_csv(csv, parse_dates=["start_date", "end_date"]).assign(
            start_year=lambda df: df.start_date.dt.year,
            start_month=lambda df: df.start_date.dt.month,
            duration_months=lambda df: 12 * (df.end_date.dt.year - df.start_year)
            + df.end_date.dt.month
            - df.start_month,
        )


def within_admin2() -> pd.DataFrame:
    return all().query("spatial_scale == 'admin2'")


@cache
def _africa_shapes() -> gpd.GeoDataFrame:
    source = (
        importlib_resources.files(__package__)
        .joinpath("resources")
        .joinpath("AfricaShapefiles")
        .joinpath("total_shp_0427.shp")
    )

    with importlib_resources.as_file(source) as shp:
        return cast(
            gpd.GeoDataFrame,
            cast(gpd.GeoDataFrame, gpd.read_file(shp)).rename(
                columns={"lctn_pr": "location_period_id"}
            ),
        )


def regions(outbreaks: pd.DataFrame | None = None) -> gpd.GeoDataFrame:
    return cast(
        gpd.GeoDataFrame,
        _africa_shapes()
        .merge(
            (outbreaks or within_admin2())["location_period_id"].drop_duplicates(),
            how="inner",
            on="location_period_id",
            copy=False,
            sort=True,
        )
        .drop_duplicates("geometry", keep=False)
        .astype({"location_period_id": int}, copy=False)
        .reset_index(drop=True),
    )


def start_month_range(outbreaks: pd.DataFrame | None = None) -> pd.DatetimeIndex:
    dates = (outbreaks or within_admin2())["start_date"].map(
        lambda d: date(d.year, d.month, 1)
    )

    return pd.date_range(dates.min(), dates.max(), freq=pd.offsets.MonthBegin())
