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

3. <u>Data Visualization</u>

3. 1. Histogram of DataFrame "homicides", Column "Fecha" ' # to visualize distribution of Continuous (Numeric) values.

<img width="562" height="433" alt="1" src="https://github.com/user-attachments/assets/a738837d-6c4e-4a97-904b-cf4787406247" />

3. 2. Histogram of DataFrame "injuries", Column "Fecha"' # to visualize distribution of Continuous (Numeric) values.

<img width="576" height="465" alt="2" src="https://github.com/user-attachments/assets/71b8edeb-04fc-4efc-9549-530181c7fc19" />
