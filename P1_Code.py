# 1. **BUSINESS PROBLEM**

## 1. 1. **Context**
* Urban areas face daily risks, and government agencies need data-driven insights to allocate resources and reduce them.

## 1. 2. **Defining**
* How can I reduce urban risk?

## 1. 3. **Solving**
* ETL to clean and unify data, EDA to uncover patterns, Visualizations to identify hotspots.

# 2. **DATA PIPELINE**

## 2. 1. **ETL**

'1. Import Required Libraries'

import pandas as pd
import numpy as np

'2. Import Dataset'

# `homicides`
from google.colab import files
uploaded = files.upload()

# injuries
from google.colab import files
uploaded = files.upload()

'3. Load Dataset'

homicidios = pd.read_excel('homicides.xlsx')
lesiones = pd.read_excel('injuries.xlsx')

# Display
homicidios.info()

# Display
lesiones.info()

'4. Clean Data'

# Add a new first column called `TIPO_ACCIDENTE` to the `lesiones` DataFrame, filling every row with "Lesiones"; to tag the dataset so when merged with homicidios, distinguish accident types.
lesiones.insert(0, 'TIPO_ACCIDENTE', 'Lesiones')
lesiones.head()

# Add a new first column called `TIPO_ACCIDENTE` to the `homicidios` DataFrame, filling every row with "Homicidios"; to tag the dataset so when merged with lesiones, distinguish accident types.
homicidios.insert(0, 'TIPO_ACCIDENTE', 'Homicidios')
homicidios.head()

# Standardize (convert) `FECHA` column to datetime format: in both DataFrames (otherwise they’d be strings).
lesiones['FECHA'] = pd.to_datetime(lesiones['FECHA'])
homicidios['FECHA'] = pd.to_datetime(homicidios['FECHA'])

# Concatenate (combine) DataFrames: (`lesiones` + `homicidios`) into one called `accidentes_viales`.
accidentes_viales = pd.concat([lesiones, homicidios], ignore_index=True)   # `ignore_index=True` resets the row numbering so you don’t get duplicate indices.

# Sort by `FECHA` column (oldest → newest).
accidentes_viales = accidentes_viales.sort_values(by='FECHA')

# Display
accidentes_viales

# Review what columns are available after merging/cleaning, to decide which are relevant for analysis.
columnas = accidentes_viales.columns
columnas

'Spot incomplete or irrelevant columns to drop or fix'

# Count Nulls (Missing Values)
accidentes_viales.isnull().sum()

# Percentage of nulls
null_percentage = (null_counts / len(accidentes_viales)) * 100

# Combine into one DataFrame for clarity
missing_data = pd.DataFrame({
    'Null Count': null_counts,
    'Null Percentage': null_percentage.round(2)  # round to 2 decimals
})

# Display
missing_data

# Remove Useless Columns
cols_drop = ['ID','OTRA DIRECCION','CALLE','ALTURA','CRUCE']
accidentes_viales = accidentes_viales.drop(columns=cols_drop, errors='ignore')
accidentes_viales

# Check what type of data each column has (numeric, text, date), to decide what cleaning and converted is needed 
accidentes_viales.info()

## 2. 2. **EDA**

'1. Who causes the most risk?'

acusados = accidentes_viales[accidentes_viales['ACUSADO'] != 'SD']
acusados['ACUSADO'].value_counts(normalize=True) * 100

'2. Who are the most affected?'

victimas = accidentes_viales[accidentes_viales['VICTIMA'] != 'SD']
victimas['VICTIMA'].value_counts(normalize=True) * 100

# 3. **DATA VISUALIZATION**

'1. Import Required Libraries'

import matplotlib.pyplot as plt
import seaborn as sns

'2. Histogram'

# Homicides Over Time
homicidios['FECHA'].hist(bins=20, color='skyblue', edgecolor='black')
plt.title('Homicides Over Time')
plt.xlabel('Date')
plt.ylabel('Number')
plt.show()

# Injuries Over Time
lesiones['FECHA'].hist(bins=20, color='skyblue', edgecolor='black')
plt.title('Injuries Over Time')
plt.xlabel('Date')
plt.ylabel('Number')
plt.show()

'3. KDE (Kernel Density Estimation)'

# Homicides Over Time
sns.kdeplot(homicidios['FECHA'], shade=True, color='skyblue')
plt.title('Homicides Over Time')
plt.xlabel('Date')
plt.ylabel('Density')
plt.show()

# Injuries Over Time
sns.kdeplot(lesiones['FECHA'], shade=True, color='skyblue')
plt.title('Injuries Over Time')
plt.xlabel('Date')
plt.ylabel('Density')
plt.show()

'4 Time Scatter'

# Homicides Over Time
homicidios['Victima_Code'] = pd.factorize(homicidios['VICTIMA'])[0]
plt.scatter(homicidios['FECHA'], homicidios['Victima_Code'], alpha=0.5)
plt.yticks(range(len(homicidios['VICTIMA'].unique())), homicidios['VICTIMA'].unique())
plt.title("Homicides Victims Over Time")
plt.xlabel("Date")
plt.ylabel("Victim Type")
plt.show()

# Injuries Over Time
lesiones['Victima_Code'] = pd.factorize(lesiones['VICTIMA'])[0]

plt.scatter(lesiones['FECHA'], lesiones['Victima_Code'], alpha=0.5)
plt.yticks(
    range(len(lesiones['VICTIMA'].unique())), 
    lesiones['VICTIMA'].unique()
)
plt.title("Injuries Victims Over Time")
plt.xlabel("Date")
plt.ylabel("Victim Type")
plt.show()

'5. Heatmap'

sns.heatmap(homicidios.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

'6. Pie Chart'

# Accused
acusado_counts = homicidios[homicidios['ACUSADO'] != 'SD']['ACUSADO'].value_counts()
plt.pie(acusado_counts, labels=acusado_counts.index, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title('Accused Distribution')
plt.show()

# https://www.argentina.gob.ar/caba/comunas
porcentajes_comuna = homicidios['COMUNA'].value_counts(normalize=True) * 100
porcentajes_comuna = porcentajes_comuna.sort_values(ascending=False)
porcentajes_comuna

# COnsiderar cada fila como un accidente vial y separapr por horas para saber en qué horario suceden más accidentes

import numpy as np

# Convierte la columna 'HORA' a formato de fecha y hora, ignorando los valores 'SD'
siniestros_viales = homicidios[homicidios['HORA'] != 'SD'] # != (desigual): ignorar datos 'SD'
siniestros_viales['HORA'] = pd.to_datetime(homicidios['HORA'], errors='coerce') # errors='coerce' forzar errores

# Redondea las horas al múltiplo de 2 más cercano
# Opción 1
siniestros_viales['HORA_redondeada'] = (siniestros_viales['HORA'] + pd.to_timedelta(1, 'h')).dt.floor('6h')
# Opción 2
# siniestros_viales['HORA_redondeada'] = (siniestros_viales['HORA'] + np.timedelta64(1, 'h')).dt.floor('6h') # pasar a tiempo de una jora dividio cada 6 horas. dt es segmentos de tiempos

# Cuenta el número de accidentes por intervalo de 2 horas
conteo_accidentes = siniestros_viales.groupby('HORA_redondeada').size().reset_index(name='NumAccidentes') # Ordenar por horas y resetar index y que el nuevo indice sea n accidentes.

# Ordena el DataFrame de mayor a menor
conteo_accidentes = conteo_accidentes.sort_values(by='NumAccidentes', ascending=False) # sort_values ordenar, ascending=False mayor a menor

# Extrae solo la hora de la columna 'HORA_redondeada'
conteo_accidentes['HORA_redondeada'] = conteo_accidentes['HORA_redondeada'].dt.time # pasar a datetime pero extraer la fecha

conteo_accidentes

# Accidents by Hour (rounded to 6h)

homicidios = homicidios[homicidios['HORA'] != 'SD']
homicidios['HORA'] = pd.to_datetime(homicidios['HORA'], errors='coerce')
homicidios['HORA_redondeada'] = (homicidios['HORA'] + pd.to_timedelta(1, 'h')).dt.floor('6h')

conteo_horas = homicidios.groupby('HORA_redondeada').size().reset_index(name='NumAccidentes')
conteo_horas = conteo_horas.sort_values(by='NumAccidentes', ascending=False)
conteo_horas['HORA_redondeada'] = conteo_horas['HORA_redondeada'].dt.time
conteo_horas['NumAccidentes'].plot(kind='line', figsize=(8, 4), title='Accidentes por Franja Horaria')

plt.show()

# COnsiderar cada fila como un accidente vial y separapr por Comuna y Hora para saber en qué horario suceden más accidentes

# Filtra las filas que no contienen 'SD' en la columna 'HORA'
siniestros_viales = homicidios[homicidios['HORA'] != 'SD']

# Convierte la columna 'HORA' a tipo datetime
siniestros_viales['HORA'] = pd.to_datetime(homicidios['HORA'], errors='coerce')

# Redondea las horas al múltiplo de 2 más cercano
siniestros_viales['HORA_redondeada'] = (siniestros_viales['HORA'] + pd.to_timedelta(1, 'h')).dt.floor('6h')

# Filtra las filas que no contienen 'SD' en la columna 'HORA_redondeada'
siniestros_viales = siniestros_viales[siniestros_viales['HORA_redondeada'].notna()]

# Cuenta el número de accidentes por intervalo de 2 horas
conteo_accidentes = siniestros_viales.groupby(['COMUNA', 'HORA_redondeada']).size().reset_index(name='NumAccidentes')

# Ordena por 'NumAccidentes' de mayor a menor
conteo_accidentes = conteo_accidentes.sort_values(by='NumAccidentes', ascending=False)

# Muestra el DataFrame resultante
conteo_accidentes

# 4. **HYPOTHESIS**

**EDA**

1. Risk Causers: Cars (≈53%) are the main source of accidents; public transport, pickups, motorcycles, and taxis follow.

2. Most Affected: Motorcyclists (≈42%) are most vulnerable, followed by pedestrians, cyclists, car occupants, and public transport users.

**Visualizations**

1. Histogram: No clear time trend in homicides/injuries.

2. KDE: Suggests a decline toward 2023.

3. Heatmap: No strong correlation between victims, commune, or victim type codes.

# 5. **RESULTS**

**Business Problem**
  - How can I reduce urban risk?

**Business Recommendation**

1. Target the biggest risk causers (Cars, ≈53%).
  * Stricter speed monitoring, awareness campaigns, and traffic law enforcement for private cars.

2. Protect the most affected (Motorcyclists, ≈42%).
  * Enforce helmet use, create safe lanes, and increase rider safety training.

3. Urban infrastructure & zoning
  * High-risk zones need improved lighting, signage, and redesign to reduce accidents.

4. Policy & planning
  * Focus resources on the top 2–3 victim groups (motorcyclists, pedestrians, cyclists).

5. Continuous monitoring (track KPIs).
