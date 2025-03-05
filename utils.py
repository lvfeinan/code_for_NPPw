from pathlib import Path
from io import StringIO
import pickle

import numpy as np
import pandas as pd
import geopandas as gpd
from shapely import box, Polygon
from pyproj import CRS

import xarray as xr
import rioxarray
from xrspatial import zonal_stats, slope
from geocube.api.core import make_geocube

import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.colors as mcolors
from matplotlib.colors import ListedColormap
import seaborn as sns

import cartopy.crs as ccrs
import cartopy.feature as cfeat

plt.rcParams.update({
    "font.family": "Arial",
    'mathtext.fontset': 'custom',
    'mathtext.rm': "Arial",
    "svg.fonttype": "none",
    "font.size": "6",
    "mathtext.default": "regular",
    "pdf.fonttype": 42,
})
path_data = Path("E:/GEODATA/HANPP_data/global")
gdf_world = gpd.read_file(path_data / "vector/globalmap_revise/map.shp").clip(box(-180, -60, 180, 85))

res = 1 / 12
x_template = np.arange(-180 + res / 2, 180, res)
y_template = np.arange(-60 + res / 2 , 85, res)
da_world = xr.open_dataarray(path_data / "world.tif").sel(band=1).drop('band')
