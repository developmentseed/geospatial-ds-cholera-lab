from datetime import date
from typing import Protocol

import dask.distributed as distributed
import geopandas as gpd
import pandas as pd
import regionmask
import stamina
import xarray as xr


class DataFetcher(Protocol):
    def __call__(
        self,
        *,
        time: date | slice | None,
        longitude: slice | None,
        latitude: slice | None,
    ) -> xr.Dataset:
        ...


def lonlat_indexers(regions: gpd.GeoDataFrame) -> tuple[slice, slice]:
    """Return a pair of min-max slices usable as longitude and latitude indexers,
    respectively, for xarray ``sel`` methods, based on the total bounds of a
    ``GeoDataFrame``.

    Example
    -------
    ```python
    lon, lat = lonlat_indexers(gdf)
    ds.sel(longitude=lon, latitude=lat)
    ```
    """
    minx, miny, maxx, maxy = regions.total_bounds
    return slice(minx, maxx), slice(miny, maxy)


_retry_os_error = stamina.retry(on=OSError, wait_initial=1, timeout=60)

# Make opening datasets a bit more resilient to network errors
open_dataset = _retry_os_error(xr.open_dataset)
open_mfdataset = _retry_os_error(xr.open_mfdataset)


def zonal_means(
    regions: gpd.GeoDataFrame,
    fetch_data: DataFetcher,
    *,
    lon_name: str,
    lat_name: str,
    time: date | slice,
) -> pd.DataFrame:
    lon, lat = lonlat_indexers(regions)

    with distributed.Client():
        values = fetch_data(longitude=lon, latitude=lat, time=time)
        zones = regionmask.mask_geopandas(regions, values[lon_name], values[lat_name])

        return (
            values.assign_coords(zone=zones)
            .groupby("zone")
            .mean(skipna=True, engine="flox", method="cohorts")
            .to_dataframe()
            .dropna()
            .reset_index()
            .astype({"zone": int})
            .set_index(["time", "zone"])
        )
