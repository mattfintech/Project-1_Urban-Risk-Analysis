# Project 1 **Mitigate Road Accidents**

├── Problem (Business Problem)

            ├── Context → Urban areas face daily risks, and government agencies need data-driven insights to allocate resources and reduce them.
            └── Defining → How to Mitigate Road Accidents in Buenos Aires? 
            
├── Data Pipeline

            └── ETL (Extract Transform Load)

                        ├── Data Collection (Extract)

                            └── Internal → Public government datasets.

                        ├── Data Wrangling (Transform)
                        └── Load - transformed dataset.

├── Data Visualization

            └── EDA (Exploratory Data Analysis) → Histograms, KDE, Scatter Plots, Heatmaps, Pie Chart.

├── Hypothesis
      
            * Who causes risk? Cars (53%), Public Transport (11%), Pickup (10%), Motorcycles (7%), Taxis (6%).
            * Who is most affected? Motorcyclists (42%), Pedestrians (17%), Cyclists (16%).
            * Trends: Histogram quite unclear; KDE suggests risk decline toward 2023.
            * Correlations: No strong relationship between victims, commune, or victim type.
  
└── Solution (Results)

            └── Recommendation (Business Recommendation)
                        
                        1. Target the Perpetrators → Cars ≈53%: Strengthen speed tickets, Launch awareness campaigns, Intensify traffic law enforcement.
                        2. Protect the Victims → Motorcyclists ≈42%: Enforce helmet compliance, Create dedicated safe lanes, Expand rider safety training.
                        3. Monitor Continuously → KPIs and update interventions accordingly.
