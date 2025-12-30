**<h1>Mitigate Road Accidents</h1>**

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

#### 3. 5. Time Scatter of DataFrame "homicides", Column "Fecha" # to visualize events over Time (Datetime) against Continuous or Categorical values.

<img width="637" height="433" alt="5" src="https://github.com/user-attachments/assets/07bf1279-7642-45a5-8936-d60f63154036" />

#### 3. 6. Time Scatter of DataFrame "injuries", Column "Fecha" # to visualize events over Time (Datetime) against Continuous or Categorical values.

<img width="671" height="465" alt="6" src="https://github.com/user-attachments/assets/5f5575be-7a02-47b4-8681-14f0e0c66753" />

#### 3. 7. Heatmap of DataFrame "homicides", Numeric Columns # to visualize correlation between Continuous (numeric) variables.

<img width="528" height="433" alt="7" src="https://github.com/user-attachments/assets/43220e74-e351-4fc5-ba98-c72a54d4e45c" />

#### 3. 8. Heatmap of DataFrame "injuries", Numeric Columns # to visualize correlation between Continuous (numeric) variables.

<img width="528" height="433" alt="8" src="https://github.com/user-attachments/assets/b9711e8a-7a0b-4120-95c7-bffd936a222b" />

#### 3. 9. Pie Chart of DataFrame "homicides", Column "Acusado" # to visualize proportion of Categorical values.
