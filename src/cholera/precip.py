from datetime import date
from typing import Final

import geopandas as gpd
import pandas as pd
import xarray as xr

from cholera import compress_kwargs
from cholera import xarray_ as xr_


OPENDAP_URL: Final = (
    "https://coastwatch.pfeg.noaa.gov/erddap/griddap/chirps20GlobalMonthlyP05"
)


def dataset(
    *,
    longitude: slice | None = None,
    latitude: slice | None = None,
    time: date | slice | None = None,
) -> xr.Dataset:
    """Fetch precipitation (millimeters) within a spatial and temporal range."""

    with xr_.open_dataset(OPENDAP_URL, chunks="auto") as dataset:
        return dataset.sel(
            compress_kwargs(
                longitude=longitude,
                latitude=latitude,
                time=slice(time, time) if isinstance(time, date) else time,
            )
        )


def zonal_means(regions: gpd.GeoDataFrame, time: date | slice) -> pd.DataFrame:
    """Compute monthly precipiations zonal means (millimeters) within a spatial
    and temporal range.
    """
    return xr_.zonal_means(
        regions,
        dataset,
        lon_name="longitude",
        lat_name="latitude",
        time=time,
    )
