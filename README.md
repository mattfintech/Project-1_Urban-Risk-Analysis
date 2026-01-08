**<h1>Mitigate Road Accidents</h1>**

## **Introduction**

Video: https://www.tiktok.com/@mattfintech/video/7589456808859798798

## **Mind Map**

├── 1. Problem (Business Problem)

            ├── Context → Urban areas face daily risks, and government agencies need data-driven insights to allocate resources and reduce them.
            └── Defining → How to Mitigate Road Accidents in Buenos Aires? 
            
├── 2. Data Pipeline

            └── ETL (Extract Transform Load)

                        ├── Data Collection (Extract)

                            └── Internal → Public government datasets.

                        ├── Data Wrangling (Transform)
                        └── Load - transformed dataset.

├── 3. Data Visualization

            └── EDA (Exploratory Data Analysis) → Histograms, KDE, Scatter Plots, Heatmaps, Pie Chart.

├── 4. Hypothesis
      
            * Who causes risk? Cars (53%), Public Transport (11%), Pickup (10%), Motorcycles (7%), Taxis (6%).
            * Who is most affected? Motorcyclists (42%), Pedestrians (17%), Cyclists (16%).
            * Trends: Histogram quite unclear; KDE suggests risk decline toward 2023.
            * Correlations: No strong relationship between victims, commune, or victim type.
  
└── 5. Solution (Results)

            └── Recommendation (Business Recommendation)
                        
                        1. Target the Perpetrators → Cars ≈53%: Strengthen speed tickets, Launch awareness campaigns, Intensify traffic law enforcement.
                        2. Protect the Victims → Motorcyclists ≈42%: Enforce helmet compliance, Create dedicated safe lanes, Expand rider safety training.
                        3. Monitor Continuously → KPIs and update interventions accordingly.

## **References**

### 3. Data Visualization

#### 3. 1. Histogram of DataFrame "homicides", Column "Fecha" # to visualize distribution of Continuous (Numeric) values.

<img width="562" height="433" alt="1" src="https://github.com/user-attachments/assets/a738837d-6c4e-4a97-904b-cf4787406247" />

#### 3. 2. Histogram of DataFrame "injuries", Column "Fecha" # to visualize distribution of Continuous (Numeric) values.

<img width="576" height="465" alt="2" src="https://github.com/user-attachments/assets/71b8edeb-04fc-4efc-9549-530181c7fc19" />

#### 3. 3. KDE (Kernel Density Estimation) of DataFrame "homicides", Column "Fecha" # to visualize smooth distribution of Continuous values.

<img width="587" height="433" alt="3" src="https://github.com/user-attachments/assets/080a2e72-2c5f-4479-9dfd-3d5499cdf12b" />

#### 3. 4. KDE of DataFrame "injuries", Column "Fecha" # to visualize smooth distribution of Continuous values.

<img width="587" height="433" alt="4" src="https://github.com/user-attachments/assets/1c8ea15c-4e83-40bb-9785-8cf3a62d9955" />

#### 3. 5. Scatter Plot of DataFrame "homicides", Column "Fecha" # to visualize Categorical or Continuous values against Time (datetime).

<img width="697" height="433" alt="5" src="https://github.com/user-attachments/assets/66e33bd5-716b-40ed-bc07-d9088df7bf7c" />

#### 3. 6. Scatter Plot of DataFrame "injuries", Column "Fecha" # to visualize Categorical or Continuous values against Time (datetime).

<img width="651" height="465" alt="6" src="https://github.com/user-attachments/assets/8126eecd-df26-43dd-bac3-9cad9deae34d" />

#### 3. 7. Heatmap of DataFrame "homicides", Numeric Columns # to visualize correlation between Continuous (numeric) variables.

<img width="528" height="433" alt="7" src="https://github.com/user-attachments/assets/3d45d471-769d-4b7a-a8b2-ee96339b2f38" />

#### 3. 8. Heatmap of DataFrame "injuries", Numeric Columns # to visualize correlation between Continuous (numeric) variables.

<img width="528" height="433" alt="8" src="https://github.com/user-attachments/assets/20604671-b768-43d6-b78d-ed70b67df15e" />

#### 3. 9. Pie Chart of DataFrame "homicides", Column "Acusado" # to visualize proportion of Categorical values.

<img width="690" height="575" alt="9" src="https://github.com/user-attachments/assets/62c4528b-93bf-4f57-b422-ccf765b8e39b" />
