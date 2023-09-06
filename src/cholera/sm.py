from datetime import date
from typing import Final

import geopandas as gpd
import pandas as pd
import xarray as xr

from cholera import compress_kwargs
from cholera import xarray_ as xr_


OPENDAP_URL: Final = (
    "https://icdc.cen.uni-hamburg.de/thredds/dodsC/ascat_soilmoisture_asc"
)


def dataset(
    *,
    longitude: slice | None = None,
    latitude: slice | None = None,
    time: date | slice | None = None,
) -> xr.Dataset:
    """Fetch soil moisture (percentage) within a spatial and temporal range."""

    time_slice = (
        # When given a single date, create time slice from the start of the
        # month to the end of the month to make sure it spans the entire month.
        (start := date(time.year, time.month, 1), start + pd.offsets.MonthEnd())
        if isinstance(time, date)
        else time
    )
    indexers = compress_kwargs(lon=longitude, lat=latitude, time=time_slice)

    with xr_.open_dataset(OPENDAP_URL, chunks="auto") as dataset:
        return dataset.sel(indexers).rename_vars(sm_ext="sm")[["sm"]]


def zonal_means(regions: gpd.GeoDataFrame, time: date | slice) -> pd.DataFrame:
    """Compute monthly soil moisture zonal means (percentage) within a spatial
    and temporal range.
    """
    return xr_.zonal_means(
        regions,
        dataset,
        lon_name="lon",
        lat_name="lat",
        time=time,
    )
