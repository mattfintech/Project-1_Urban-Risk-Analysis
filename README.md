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

#In dataframe `homicidios`, add at position `0`, a new column `TIPO_ACCIDENTE`, label it `Homicidios` to identify the dataset.

homicides.insert(0, 'TIPO_ACCIDENTE', 'Homicidios')

#Display

homicides.head()

' 5. 2. Style Column Names, of Dataframe "homicides" '

#Rename "TIPO_ACCIDENTE" → "Tipo Accidente"

homicides.rename(columns={"TIPO_ACCIDENTE": "Tipo Accidente"}, inplace=True)

#Rename "Nº VICTIMAS" → "Nº Víctimas"

homicides.rename(columns={"Nº VICTIMAS": "Nº Víctimas"}, inplace=True)

#Capitalize all UPPERCASE column names

homicides.columns = [
    col.replace("_", " ").title() if col.isupper() else col
    for col in homicides.columns
]

#Display

homicides.head()

' 5. 3. Insert Identifying Column "TIPO_ACCIDENTE", to DataFrame "injuries" '  # to label and distinguish datasets.

#In DataFrame `lesiones`, add at position `0`, a new column `TIPO_ACCIDENTE`, label it `Lesiones` to identify the dataset.

injuries.insert(0, 'TIPO_ACCIDENTE', 'Lesiones')

#Display

injuries.head()

' 5. 3. Insert Identifying Column "TIPO_ACCIDENTE", to DataFrame "injuries" '  # to label and distinguish datasets.

#In DataFrame `lesiones`, add at position `0`, a new column `TIPO_ACCIDENTE`, label it `Lesiones` to identify the dataset.

injuries.insert(0, 'TIPO_ACCIDENTE', 'Lesiones')

#Display

injuries.head()

' 5. 4. Style Column Names, of Dataframe "homicides" '

#Rename "TIPO_ACCIDENTE" → "Tipo Accidente"

injuries.rename(columns={"TIPO_ACCIDENTE": "Tipo Accidente"}, inplace=True)

#Capitalize all UPPERCASE column names

injuries.columns = [
    col.replace("_", " ").title() if col.isupper() else col
    for col in injuries.columns
]

#Display

injuries.head()

'5. 5. Standardize Values into DateTime' # for accurate time-based analysis.

#In dataframe `lesiones`, column `Fecha`; convert string values; into datetime format, store the converted values back.

injuries['Fecha'] = pd.to_datetime(injuries['Fecha'])

#In dataframe `homicidios`, column `Fecha`; convert string values; into datetime format, store the converted values back.

homicides['Fecha'] = pd.to_datetime(homicides['Fecha'])

'5. 6. Concatenate multiple DataFrames' # to combine multiple DataFrames into one DataFrame.

#In DataFrame `accidentes_viales`; combine DataFrame `lesiones` and DataFrame `homicidios`, ignoring index numbers to avoid duplicates.

accidents = pd.concat([injuries, homicides], ignore_index=True)

'5. 7. Sort Values' # to order rows based on column values.

#In DataFrame `X`; sort values by column `Fecha` (oldest → newest).

accidents = accidents.sort_values(by='Fecha')

#Display

accidents

'5. 6. Review Dataframe Columns' # to decide which are relevant for analysis (after merging/cleaning).

#In Dataframe `columnas`; review Dataframe `accidentes_viales` columns.

columns = accidents.columns

#Display

columns

' 5. 7. Check Nulls Dataframe "accidents" ' # to spot incomplete or irrelevant columns to fix or drop.

#Count Nulls (Missing Values)

null_counts = accidents.isnull().sum()

#Nulls Percentage

null_percentage = (null_counts / len(accidents)) * 100

#Combine into one DataFrame for clarity

missing_data = pd.DataFrame({
    'Null Count': null_counts,
    'Null Percentage': null_percentage.round(2)  # round to 2 decimals
})

#Display

missing_data

'5. 8. Drop Useless Columns' # to remove incomplete or irrelevant columns that do not contribute to the analysis.

#In variable `cols_drop`; store in a list the columns to drop.

cols_drop = ['ID','OTRA DIRECCION','CALLE','ALTURA','CRUCE']

#In DataFrame `accidents`; drop columns from variable `cols_drop` forcing execution.

accidents = accidents.drop(columns = cols_drop, errors='ignore')

#Display

accidents

'5. 9. Show DataFrame "accidents" Summary' # to know what to Transform.

accidents.info()

# 3. **DATA VISUALIZATION**

## 3. 1. **EDA**

'1. Identifying the Responsible' # for the Business Problem.

#In variable `responsibles`; DataFrame `accidents`, column `ACUSADO`, filter rows different from value `SD`.

responsibles = accidents[accidents['Acusado'] != 'SD']

#In variable `responsibles`, column `ACUSADO`; calculate percentage distribution of each value.

responsibles['Acusado'].value_counts(normalize=True) * 100

