# 1. **BUSINESS PROBLEM**

## 1. 1. **Context**
* Urban areas face daily risks, and government agencies need data-driven insights to allocate resources and reduce them.

## 1. 2. **Defining**
* How to Mitigate Road Accidents in Buenos Aires?

# 2. **DATA PIPELINE**

## 2. 1. **ETL**

### 2. 1. 1. **Data Collection**

'1. Importing Libraries'

import pandas as pd
import numpy as np

'2. Importing Dataset' # (Uploading) from Desktop to Colab.

from google.colab import files
uploaded = files.upload()

'3. Loading Dataset'

' 3. 1. Load Dataset "homicides" '

homicides = pd.read_excel('homicides.xlsx')

'3. 1. 1. Show DataFrame "homicides" Summary' # to know what to Transform.

homicides.info()

' 3. 2. Load Dataset "injuries" '

injuries = pd.read_excel('injuries.xlsx')

'3. 2. 1. Show DataFrame "injuries" Summary' # to know what to Transform.

injuries.info()

### 2. 1. 2. **Data Wrangling**

'5. Cleaning Data'

' 5. 1. Insert Identifying Column "TIPO_ACCIDENTE", to DataFrame "homicides" '  # to label and distinguish datasets.

# In dataframe `homicidios`, add at position `0`, a new column `TIPO_ACCIDENTE`, label it `Homicidios` to identify the dataset.
homicides.insert(0, 'TIPO_ACCIDENTE', 'Homicidios')

# Display
homicides.head()

' 5. 2. Style Column Names, of Dataframe "homicides" '

# Rename "TIPO_ACCIDENTE" → "Tipo Accidente"
homicides.rename(columns={"TIPO_ACCIDENTE": "Tipo Accidente"}, inplace=True)

# Rename "Nº VICTIMAS" → "Nº Víctimas"
homicides.rename(columns={"Nº VICTIMAS": "Nº Víctimas"}, inplace=True)

# Capitalize all UPPERCASE column names
homicides.columns = [
    col.replace("_", " ").title() if col.isupper() else col
    for col in homicides.columns
]

# Display
homicides.head()

' 5. 3. Insert Identifying Column "TIPO_ACCIDENTE", to DataFrame "injuries" '  # to label and distinguish datasets.

# In DataFrame `lesiones`, add at position `0`, a new column `TIPO_ACCIDENTE`, label it `Lesiones` to identify the dataset.
injuries.insert(0, 'TIPO_ACCIDENTE', 'Lesiones')
# Display
injuries.head()


