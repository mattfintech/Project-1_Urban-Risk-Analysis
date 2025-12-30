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

'2. Identifying the Victims' # of the Business Problem.

#In variable `victims`; DataFrame `accidents`, column `VICTIMA`, filter rows different from value `SD`.

victims = accidents[accidents['Victima'] != 'SD']

#In variable `victims`, column `VICTIMA`; calculate percentage distribution of each value.

victims['Victima'].value_counts(normalize=True) * 100

'3. Importing Libraries'

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns

'4. Histogram of DataFrame "homicides", Column "Fecha" ' # to visualize distribution of Continuous (Numeric) values.

#Histogram structure

##In variable `n`, `bins`, `patches`; plot histogram DataFrame `homicides`, column `FECHA`, bin-quantity=20, bin-edge-color=00664D.

n, bins, patches = plt.hist(homicides['Fecha'], bins=20, edgecolor='#00664D')

#Colors set-up

##In variable `colors`; create a list of [`color_code1`, `color_code2`] to alternate in the histogram bars.

colors = ['#66FFDE', '#66FFDE']

#Apply colors

##In loop index `i`, variable `p`, using function `enumerate(variable `patches`)`; iterate over each bar in `patches`, and apply method `set_facecolor` with colors selected from variable `colors` using modulo index 2.

for i, p in enumerate(patches):
    p.set_facecolor(colors[i % 2])

#Apply fonts

##For each font file, call fm.fontManager.addfont("path") to load it into Matplotlib.

fm.fontManager.addfont("/content/Century Gothic.ttf")
fm.fontManager.addfont("/content/Century Gothic Bold.ttf")
fm.fontManager.addfont("/content/Century Gothic Italic.ttf")
fm.fontManager.addfont("/content/Century Gothic Bold Italic.ttf")

#Set as global default

#In submodule `plt`, dictionary `rcParams`, key `'font.family'`; assign font "Century Gothic".

plt.rcParams['font.family'] = "Century Gothic"

#Title

#submodule.method('text', parameter1=value,  parameter2=value,  parameter3=value )

plt.title('Deaths Over Time', fontsize=12.5, fontweight='bold', fontname='Century Gothic')

#Y-axis label
plt.ylabel('Number of Deaths', fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.5)

#Remove top + right border lines

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

#Display

plt.show()

<img width="562" height="433" alt="1" src="https://github.com/user-attachments/assets/a738837d-6c4e-4a97-904b-cf4787406247" />

'5. Histogram of DataFrame "injuries", Column "Fecha"' # to visualize distribution of Continuous (Numeric) values.

#1. Create the Histogram structure

##Syntax Structure

library.function(variable["argument"], parameter1=argument, parameter2="argument", parameter3="argument")

##Syntax Template

plt.hist(dataset["column"], bins=#, facecolor="#color_code1", edgecolor="#color_code2")

##Code Read: plot, histogram, of DataFrame `injuries`, column `FECHA`, using 20 bins, and custom colors.

plt.hist(injuries['Fecha'], bins=20, facecolor='#66FFDE', edgecolor='#00664D')

#2. Set a Font as the global default

##Syntax Structure

submodule.dictionary['key'] = "value"

##Syntax Template

plt.rcParams['font.family'] = "Font Name"

##Code Read: plot, access (.), dictionary, key 'font.family', assign (=), value "Century Gothic"

plt.rcParams['font.family'] = "Century Gothic"

#3. Create the Title

##Syntax Structure

submodule.method("argument", parameter1=argument, parameter2="argument", parameter3="argument")

##Syntax Template

plt.title("Text", fontsize=#, fontweight="bold", fontname="Font Name")

##Code Read: plot, access title, text assing, size assign, weight assign, font assign.

plt.title("Injuries Over Time", fontsize=12.5, fontweight='bold', fontname='Century Gothic')

#4. Create the Y-axis Label

##Syntax Structure

submodule.method("argument", parameter=argument)

##Syntax Template

plt.ylabel("Label", fontsize=#)

##Code Read: plot, access y-axis label, text, size assign.

plt.ylabel('Number of Injuries', fontsize=10)

#5. Rotate the X-axis Ticks

##Syntax Structure

submodule.method(parameter=argument)

##Syntax Template

plt.xticks(rotation=#)

##Code Read: plot, access x-axis tick, rotation assign.

plt.xticks(rotation=45)

#6. Create the Grid lines

##Syntax Structure

submodule.method(parameter1="argument", parameter2="argument", parameter3=argument)

##Syntax Template

plt.grid(axis="y", linestyle="--", alpha=#)

##Code Read: plot, access grid, axis assing, linestyle assign, transparency assign.

plt.grid(axis='y', linestyle='--', alpha=0.5)

#7. Remove top + right Border lines

##Syntax Structure

submodule.method().dictionary["argument"].method(argument)

##Syntax Template

plt.gca().spines["border_remove"].set_visible(False)

##Code Read: plot, access get-current-axes, access spines "top", access set_visible False.
##Code Read: plot, access get-current-axes, access spines "right", access set_visible False.

plt.gca().spines['top'].set_visible(False)
plt.gca().spines["right"].set_visible(False)

#8. Display the Plot

##Syntax Structure

submodule.method()

##Syntax Template

plt.show()

##Code Read: plot, access show.

plt.show()

<img width="576" height="465" alt="2" src="https://github.com/user-attachments/assets/71b8edeb-04fc-4efc-9549-530181c7fc19" />
