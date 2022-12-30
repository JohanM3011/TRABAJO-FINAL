# -*- coding: utf-8 -*-
"""fun corr C.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DiocIYPEaviPLZA4gOBxSxvyyN9A4c4z
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

"""# PRECIPITACIÓN"""

Pisco_anom_mensual = xr.open_dataset("/content/drive/MyDrive/PROYECTO FINAL/PP anom mensual/Pisco_anom_mensual.nc")
Pisco_anom_mensual

"""# INDICE C"""

indiceC = pd.read_csv("/content/drive/MyDrive/PROYECTO FINAL/INDICE C y E (1981-2010)/df_indice_C_(1981-2010).csv")
indiceC

df_C_1= indiceC.set_index("Fecha")
df_C_1

#Correlacion
def cor_point_grid(y,x):
  res = np.corrcoef(y,x)[0,1]
  return res

cor_point_grid_example1 = xr.apply_ufunc(cor_point_grid,
                                        Pisco_anom_mensual,
                                        np.array(df_C_1).ravel(),
                                        input_core_dims=[["time"], ["Fecha"]],
                                        vectorize=True)


cor_point_grid_example1

cor_point_grid_example1.Prec.plot() 
plt.title("Corr PP - INDICE C (1981-2010)") 
plt.xlabel("Longitud")
plt.ylabel("Latitud")