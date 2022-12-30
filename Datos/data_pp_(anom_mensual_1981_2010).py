# -*- coding: utf-8 -*-
"""data PP (Anom_mensual 1981-2010).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vH2MDrVwOKBWt6AyEZzGm6fhh9IjHENw
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

# PISCOt v1.2 (Prec: PRECIPITACION)
PP = xr.open_dataset("/content/drive/MyDrive/TPM_II/datos/PISCO_precipitation/PISCOp.nc")
PP

PP = PP.rename({"X":"longitude", "Y":"latitude", "T":"time"})
PP

PP_2 = PP.sel(time=slice("1981-01-01T12:00:00.000000000","2010-12-31T12:00:00.000000000"))
PP_2

PP_3 = PP_2.resample(time='M').sum()
PP_3

PISCO_clim = PP_3.groupby('time.month').mean()
PISCO_clim

Pisco_anom_mensual = PP_3.groupby("time.month") - PISCO_clim
Pisco_anom_mensual

Pisco_anom_mensual = Pisco_anom_mensual.to_netcdf("Pisco_anom_mensual.nc")

from google.colab import files
files.download("Pisco_anom_mensual.nc")