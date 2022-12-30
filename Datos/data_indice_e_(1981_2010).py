# -*- coding: utf-8 -*-
"""data Indice E (1981-2010).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ok40FOsJ5gCf1kC4jC19tV_emWRztobL
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

# INDICES SST (C y E)
indice = pd.read_csv("/content/drive/MyDrive/TPM_II/datos/indice_c_y_e/ecindex_ersstv5_CSV.csv")
indice

Fecha = pd.date_range('1880-1','2022-11',freq='M')

indice['Fecha'] = Fecha
indice

df_indices = indice.set_index("Fecha")
df_indices

df_indices_1 = df_indices.loc["1981":"2010"]
df_indices_1

df_indices_2 = df_indices_1.drop(columns=['year',"month"])
df_indices_2

"""# INDICE E"""

df_indice_E = df_indices_2.drop(columns=["C_index"])
df_indice_E

"""# GUARDAR ARCHIVO ES CSV"""

df_indice_E.to_csv("df_indice_E_(1981-2010).csv")

from google.colab import files
files.download("df_indice_E_(1981-2010).csv")