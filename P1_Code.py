# 1. **PROBLEM**

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

# Rename "TIPO_ACCIDENTE" → "Tipo Accidente"
injuries.rename(columns={"TIPO_ACCIDENTE": "Tipo Accidente"}, inplace=True)

# Rename "Nº VICTIMAS" → "Nº Victimas"
injuries.rename(columns={"Nº VICTIMAS": "Nº Victimas"}, inplace=True)

# Capitalize all UPPERCASE column names
injuries.columns = [
    col.replace("_", " ").title() if col.isupper() else col
    for col in injuries.columns
]

# Show all columns
pd.set_option('display.max_columns', None)

# Display
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

' 5. 6. Review Dataframe "accidents" Columns ' # to decide which are relevant for analysis (after merging/cleaning).

# In Dataframe `columnas`; review Dataframe `accidentes_viales` columns.
columns = accidents.columns

# Display
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

' 5. 8. Drop Useless Columns in Dataframe "accidents" ' # to remove incomplete or irrelevant columns that do not contribute to the analysis.

# In variable `cols_drop`; store in a list the columns to drop.
cols_drop = ['Id','Otra Direccion','Calle','Altura','Cruce']

# In DataFrame `accidents`; drop columns from variable `cols_drop` forcing execution.
accidents = accidents.drop(columns = cols_drop, errors='ignore')

# Display
accidents

'5. 9. Show DataFrame "accidents" Summary' # to know what to Transform.

accidents.info()

# 3. **DATA VISUALIZATION**

## 3. 1. **EDA**

' 1. Identifying the Perpetrators from Dataframe "accidents" ' # for identifying the Problem's Perpetrator.

# Filter records with identified responsibles, exclude Value "SD".
responsibles = accidents[accidents["Acusado"] != 'SD']

# Calculate percentage distribution of responsibles
responsibles["Acusado"].value_counts(normalize=True) * 100

'2. Identifying the Victims' # of the Business Problem.

# Filter records with identified responsibles, exclude Value "SD".
victims = accidents[accidents['Victima'] != 'SD']

# Calculate percentage distribution of responsibles
victims['Victima'].value_counts(normalize=True) * 100

'3. Importing Libraries'

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns

' 4. Histogram of DataFrame "homicides", Column "Fecha" ' # to visualize distribution of Continuous (Numeric) values.

# 1. Histogram structure
n, bins, patches = plt.hist(homicides['Fecha'], bins=20, edgecolor='#00664D')

# 2. Colors set-up
colors = ['#66FFDE', '#66FFDE']

# 3. Apply colors
for i, p in enumerate(patches):
    p.set_facecolor(colors[i % 2])

# 4. Apply fonts
fm.fontManager.addfont("/content/Century Gothic.ttf")
fm.fontManager.addfont("/content/Century Gothic Bold.ttf")
fm.fontManager.addfont("/content/Century Gothic Italic.ttf")
fm.fontManager.addfont("/content/Century Gothic Bold Italic.ttf")

# 5. Set font as global default
plt.rcParams['font.family'] = "Century Gothic"

# 6. Title
plt.title('Deaths Over Time', fontsize=12.5, fontweight='bold', fontname='Century Gothic')

# 7. Y-axis label
plt.ylabel('Number of Deaths', fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.5)

# 8. Remove top + right border lines
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# 9. Display
plt.show()

' 5. Histogram of DataFrame "injuries", Column "Fecha" ' # to visualize distribution of Continuous (Numeric) values.

# 1. Create the Histogram structure
'''
## Syntax Structure
library.function(variable["argument"], parameter1=argument, parameter2="argument", parameter3="argument")
## Syntax Template
plt.hist(dataset["column"], bins=#, facecolor="#color_code1", edgecolor="#color_code2")
## Code Read: plot, histogram, of DataFrame `injuries`, column `FECHA`, using 20 bins, and custom colors.
'''
plt.hist(injuries['Fecha'], bins=20, facecolor='#66FFDE', edgecolor='#00664D')

# 2. Set a Font as the global default
'''
## Syntax Structure
submodule.dictionary['key'] = "value"
## Syntax Template
plt.rcParams['font.family'] = "Font Name"
## Code Read: plot, access (.), dictionary, key 'font.family', assign (=), value "Century Gothic"
'''
plt.rcParams['font.family'] = "Century Gothic"

# 3. Create the Title
'''
## Syntax Structure
submodule.method("argument", parameter1=argument, parameter2="argument", parameter3="argument")
## Syntax Template
plt.title("Text", fontsize=#, fontweight="bold", fontname="Font Name")
## Code Read: plot, access title, text assing, size assign, weight assign, font assign.
'''
plt.title("Injuries Over Time", fontsize=12.5, fontweight='bold', fontname='Century Gothic')

# 4. Create the Y-axis Label
'''
## Syntax Structure
submodule.method("argument", parameter=argument)
## Syntax Template
plt.ylabel("Label", fontsize=#)
## Code Read: plot, access y-axis label, text, size assign.
'''
plt.ylabel('Number of Injuries', fontsize=10)

# 5. Rotate the X-axis Ticks
'''
## Syntax Structure
submodule.method(parameter=argument)
## Syntax Template
plt.xticks(rotation=#)
## Code Read: plot, access x-axis tick, rotation assign.
'''
plt.xticks(rotation=45)

# 6. Create the Grid lines
'''
## Syntax Structure
submodule.method(parameter1="argument", parameter2="argument", parameter3=argument)
## Syntax Template
plt.grid(axis="y", linestyle="--", alpha=#)
## Code Read: plot, access grid, axis assing, linestyle assign, transparency assign.
'''
plt.grid(axis='y', linestyle='--', alpha=0.5)

# 7. Remove top + right Border lines
'''
## Syntax Structure
submodule.method().dictionary["argument"].method(argument)
## Syntax Template
plt.gca().spines["border_remove"].set_visible(False)
## Code Read: plot, access get-current-axes, access spines "top", access set_visible False.
## Code Read: plot, access get-current-axes, access spines "right", access set_visible False.
'''
plt.gca().spines['top'].set_visible(False)
plt.gca().spines["right"].set_visible(False)

# 8. Display the Plot
'''
## Syntax Structure
submodule.method()
## Syntax Template
plt.show()
## Code Read: plot, access show.
'''
plt.show()

' 6. KDE (Kernel Density Estimation) of DataFrame "homicides", Column "Fecha" ' # to visualize smooth distribution of Continuous values.

# 1. Create the KDE structure
sns.kdeplot(homicides["Fecha"], color="#66FFDE", fill=True)  # Fill color
sns.kdeplot(homicides["Fecha"], color="#00664D", fill=False, linewidth=1)  # Edge color

# 2. Set a Font as the global default
plt.rcParams["font.family"] = "Century Gothic"

# 3. Create the Title
plt.title("Deaths Over Time", fontsize=12.5, fontweight="bold", fontname="Century Gothic")

# 4. Create the Y-axis Label
plt.ylabel('Density of Deaths', fontsize=10)  # Density = Concentration ⇒ Deaths are more concentrated around 2017–2019, than around 2015 or 2023.

# 5. Remove the auto-generated X-axis label
plt.gca().set_xlabel("")

# 6. Create the Grid lines
plt.grid(axis="y", linestyle="--", alpha=0.5)

# 7. Remove top + right Border lines
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)

# 8. Display the Plot
plt.show()

' 7. KDE of DataFrame "injuries", Column "Fecha" ' # to visualize smooth distribution of Continuous values.

# 1. Create the KDE structure
sns.kdeplot(homicides["Fecha"], color="#66FFDE", fill=True)  # Fill color
sns.kdeplot(homicides["Fecha"], color="#00664D", fill=False, linewidth=1)  # Edge color

# 2. Set a Font as the global default
plt.rcParams["font.family"] = "Century Gothic"

# 3. Create the Title
plt.title("Injuries Over Time", fontsize=12.5, fontweight="bold", fontname="Century Gothic")

# 4. Create the Y-axis Label
plt.ylabel('Density of Injuries', fontsize=10)  # Density = Concentration ⇒ Deaths are more concentrated around 2017–2019, than around 2015 or 2023.

# 5. Remove the auto-generated X-axis label
plt.gca().set_xlabel("")

# 6. Create the Grid lines
plt.grid(axis="y", linestyle="--", alpha=0.5)

# 7. Remove top + right Border lines
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)

# 8. Display the Plot
plt.show()

' 8. Scatter Plot of DataFrame "homicides", Column "Fecha" ' # to visualize Categorical or Continuous values against Time (datetime).

# 1. Encode Categorical values as Numeric codes to enable visualization.
homicides["Victima_Code"] = pd.factorize(homicides["Victima"])[0]

# 2. Create the Scatter Plot structure.
plt.scatter(homicides["Fecha"], homicides["Victima_Code"], alpha=0.5, color="#66FFDE")

# 3. Set a Font as the global default.
plt.rcParams['font.family'] = "Century Gothic"

# 4. Map (assign) Numeric codes back to Categorical Y-axis labels.
labels = homicides["Victima"].unique()
plt.yticks(range(len(labels)), labels)

# 5. Create the Title.
plt.title("Deaths Over Time", fontsize=12.5, fontweight="bold", fontname="Century Gothic")

# 6. Create the Y-axis Label.
plt.ylabel("Type of Victim", fontsize=10)

# 7. Create the Grid lines.
plt.grid(axis="y", linestyle="--", alpha=0.5)

# 8. Remove top + right Border lines.
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)

# 9. Display the Plot.

# Rename.
homicides["Victima"] = homicides["Victima"].replace({
    "Moto Peaton": "Motorcycle Pedestrian",
    "Object": "Object Fixed",
    "Mobile": "Moving Object",
    "PASAJEROS": "Passenger",
    "BICICLETA": "Bicycle",
    "CARGAS": "Cargo",
    "SD": "Unknown",
    "PEATON": "Pedestrian",
    "AUTO": "Car",
    "MOTO": "Motorcycle"
})

## Display.
plt.show()

' 9. Scatter Plot of DataFrame "injuries", Column "Fecha" ' # to visualize Categorical or Continuous values against Time (datetime).

# 1. Encode Categorical values as Numeric codes to enable visualization.
injuries['Victima_Code'] = pd.factorize(injuries['Victima'])[0]

# 2. Create the Scatter Plot structure.
plt.scatter(injuries["Fecha"], injuries["Victima_Code"], alpha=0.5, color="#66FFDE")

# 3. Set a Font as the global default.
plt.rcParams['font.family'] = "Century Gothic"

# 4. Map (assign) Numeric codes back to Categorical Y-axis labels.
labels = injuries["Victima"].unique()
plt.yticks(range(len(labels)), labels)

# 5. Create the Title.
plt.title("Injuries Over Time", fontsize=12.5, fontweight="bold", fontname="Century Gothic")

# 6. Create the Y-axis Label.
plt.ylabel("Type of Victim", fontsize=10)

# 7. Rotate the X-axis Ticks.
plt.xticks(rotation=45)

# 8. Create the Grid lines.
plt.grid(axis="y", linestyle="--", alpha=0.5)

# 9. Remove top + right Border lines.
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)

# 10. Display the Plot.

## Rename.
injuries["Victima"] = injuries["Victima"].replace({
    "MIXTO": "Mix",
    "TAXI": "Taxi",
    "UTILITARIO": "Utilitarian",
    "MONOPATIN": "Skateboard",
    "CAMION": "Truck",
    "OTRO": "Other",
    "MOVIL": "Moving Object",
    "CAMIONETA": "Pick-Up",
    "TRANSPORTE PUBLICO": "Public Transport",
    "MOTO": "Motorcycle",
    "PEATON": "Pedestrian",
    "SD": "Unknown",
    "AUTO": "Car",
    "CICLISTA": "Bicycle"
})

## Display.
plt.show()

' 10. Heatmap of DataFrame "homicides", Numeric Columns ' # to visualize correlation between Continuous (numeric) variables.

# 1. Create the Heatmap structure.

## Import Library.
from matplotlib.colors import LinearSegmentedColormap

## Define a custom color map for correlation intensity.
cmap_cust = LinearSegmentedColormap.from_list(
    "correlation_scale",
    ["#99FFEB", "#00FFC1", "#009974"]
)

## Generate the heatmap using the correlation matrix.
sns.heatmap(
    homicides.corr(numeric_only=True),
    annot=True,
    cmap=cmap_cust,
    vmin=-1,
    vmax=1,
    center=0
)

# 2. Create the Title.
plt.title("Deaths Correlation Matrix", fontsize=12.5, fontweight="bold", fontname="Century Gothic")

# 3. Display the Plot.

## Rename.
homicides.rename(columns={"Nº Víctimas": "Nº Victims", "Comuna": "Commune", "Victima_Code": "Victim Type"}, inplace=True)

## Display.
plt.show()

' 11. Heatmap of DataFrame "injuries", Numeric Columns ' # to visualize correlation between Continuous (numeric) variables.

# 1. Create the Heatmap structure.

## Define a custom color map for correlation intensity.
cmap_cust = LinearSegmentedColormap.from_list(
    "correlation_scale",
    ["#99FFEB", "#00FFC1", "#009974"]
)

## Generate the heatmap using the correlation matrix.
sns.heatmap(
    injuries.corr(numeric_only=True),
    annot=True,
    cmap=cmap_cust,
    vmin=-1,
    vmax=1,
    center=0
)

# 2. Create the Title
plt.title("Injuries Correlation Matrix", fontsize=12.5, fontweight="bold", fontname="Century Gothic")

# 3. Display the Plot

## Rename.
injuries.rename(columns={"Nº Victimas": "Nº Victims", "Altura": "Commune", "Victima_Code": "Victim Type"}, inplace=True)

## Display.
plt.show()

' 12. Pie Chart of DataFrame "homicides", Column "Acusado" ' # to visualize proportion of Categorical values.

# 1. Filter and count Categorical values.
counts = homicides.loc[
    ~homicides["Acusado"].isin(["SD", "PASAJEROS"]),
    "Acusado"
].value_counts()

# 2. Select top "4" Categories and group the Rest as "Other".
counts_plot = counts.head(4)
rest = counts.iloc[4:].sum()
if rest: counts_plot["Other"] = rest

# 3. Assing a color and rename each Category.

## Color.
color_map = {
    "AUTO": "#009974",
    "CARGAS": "#00CC9A",
    "OBJETO FIJO": "#00FFC1",
    "MOTO": "#33FFD0",
    "Other": "#66FFDE",
}
colors = [color_map.get(cat, "#CCCCCC") for cat in counts_plot.index]

## Rename.
label_map = {
    "AUTO": "Car",
    "CARGAS": "Cargo",
    "OBJETO FIJO": "Fixed Object",
    "MOTO": "Motorcycle",
    "Other": "Other",
}
labels = [label_map.get(cat, cat) for cat in counts_plot.index]

# 4. Create the Pie Chart structure.
fig, ax = plt.subplots(figsize=(7, 7))
wedges, *_ = ax.pie(
    counts_plot,
    autopct="%1.01f%%",
    startangle=90,
    colors=colors,
    wedgeprops=dict(edgecolor="white", linewidth=1),
    pctdistance=0.50
)

# 5. Set Title and enforce circular aspect.
plt.title("Perpetrators", fontsize=12.5, fontweight="bold", fontname="Century Gothic", y=0.95) # move title upward)
ax.set_aspect("equal")

# 6. Add legend mapping slices to categories.
ax.legend(wedges, labels, title="Accused", loc="center left", bbox_to_anchor=(0.95, 0.5), frameon=False)

# 7. Adjust layout spacing.
plt.tight_layout()

# 8. Display.
plt.show()
