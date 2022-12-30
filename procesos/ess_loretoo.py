# -*- coding: utf-8 -*-
"""ess Loreto.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SJYnGoja0ymelMgs4sN8taT9q32a2yB9
"""

from google.colab import drive
drive.mount('/content/drive/')

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

Pisco_anom_masked_Loreto = xr.open_dataset("/content/drive/MyDrive/PROYECTO FINAL/shp Loreto/Pisco_anom_masked_Loreto.nc")
Pisco_anom_masked_Loreto

Pisco_anom_masked_Loreto.Prec.isel(time=30).plot()

Pisco_anom_masked_Loreto.mean(dim=["latitude", "longitude"]).Prec.plot()

Pisco_anom_masked_Loreto.rolling(time=12, center=True).mean().mean(dim=("latitude","longitude")).Prec.plot()

plt.figure(figsize=(10,6))
plt.subplot(121)
Pisco_anom_masked_Loreto.Prec.isel(time=30).plot()
plt.title("Anom_pp - LORETO (JULIO-1983)") 
plt.xlabel("Longitud")
plt.ylabel("Latitud")

plt.subplot(322)
Pisco_anom_masked_Loreto.mean(dim=["latitude", "longitude"]).Prec.plot()
plt.title("CORTE TEMPORAL - LORETO")   
plt.xlabel("Años")
plt.ylabel(".")

plt.subplot(326)
Pisco_anom_masked_Loreto.rolling(time=12, center=True).mean().mean(dim=("latitude","longitude")).Prec.plot()
plt.xlabel("Años") 
plt.ylabel(".")


plt.show()