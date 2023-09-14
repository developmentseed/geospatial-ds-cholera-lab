from datetime import date

import geopandas as gpd
import pandas as pd
import xarray as xr

from cholera import compress_kwargs
from cholera import xarray_ as xr_


def opendap_url(d: date) -> str:
    """
    Fetch the URL for the Land Surface Temperature (LST) data for a specific month from
    the [Centre for Environmental Data Analysis Archive](https://archive.ceda.ac.uk/)
    (CEDA Archive) via OPeNDAP.
    """
    year, month = d.year, d.month

    return (
        "https://dap.ceda.ac.uk/thredds/dodsC/neodc/esacci/"
        "land_surface_temperature/data/MULTISENSOR_IRCDR/L3S/0.01/v2.00/"
        f"monthly/{year}/{month:02d}/ESACCI-LST-L3S-LST-IRCDR_-0.01deg_1"
        f"MONTHLY_DAY-{year}{month:02d}01000000-fv2.00.nc"
    )


def dataset(
    *,
    longitude: slice | None = None,
    latitude: slice | None = None,
    time: date | slice | None,
) -> xr.Dataset:
    """Fetch monthly land surface temperatures within a spatial and temporal range."""

    indexers = compress_kwargs(lon=longitude, lat=latitude)
    timestamps = pd.date_range(
        start=time.start if isinstance(time, slice) else time,
        end=time.stop if isinstance(time, slice) else time,
        freq=pd.offsets.MonthBegin(),
    )

    return xr_.open_mfdataset(
        tuple(opendap_url(ts.date()) for ts in timestamps),
        chunks="auto",
        parallel=True,
        preprocess=lambda ds: ds.sel(indexers)[["lst"]],
    )


def zonal_means(regions: gpd.GeoDataFrame, time: date | slice) -> pd.DataFrame:
    """Compute monthly land surface temperature zonal means (Celsius) within a
    temporal and spatial range.
    """
    return xr_.zonal_means(
        regions, dataset, lon_name="lon", lat_name="lat", time=time
    ).assign(
        lst=lambda df: df["lst"] - 273.15  # Convert LST from Kelvin to Celsius
    )
