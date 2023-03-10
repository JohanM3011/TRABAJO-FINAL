# -*- coding: utf-8 -*-
"""packages.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1krnJm6KhCNOx1OgLe_gPhHzg0t5Z8hhj
"""

# Commented out IPython magic to ensure Python compatibility.
# %%capture
# !pip install netcdf4

import xarray as xr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Commented out IPython magic to ensure Python compatibility.
# %%capture
# !pip install geopandas
# !pip install rioxarray

import rioxarray
from geopandas import read_file as gpd_read_file