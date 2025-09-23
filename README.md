# Project 1 **Urban Risk Analysis**

├── Business Problem

            ├── Context → Urban areas face daily risks, and government agencies need data-driven insights to allocate resources and reduce them.
            ├── Defining → How can I reduce urban risk?
            └── Solving → ETL to clean and unify data, EDA to uncover patterns, Visualizations to identify hotspots.
            
├── Data Pipeline

            ├── ETL (Extract Transform Load)

                        ├── Data Collection (Extract)

                            └── (Internal) Business Databases

                        ├── Data Wrangling (Transform)
                        └── Load - transformed dataset.

            └── EDA (Exploratory Data Analysis) → Identified main causers and victims of Urban Risk.

├── Data Visualization

            └── Histograms, KDE, Scatter plots, Heatmaps.

├── Hypothesis
      
            * Who causes risk? Cars (53%), Public Transport (11%), Pickup (10%), Motorcycles (7%), Taxis (6%).
            * Who is most affected? Motorcyclists (42%), Pedestrians (17%), Cyclists (16%).
            * Trends: Histogram unclear; KDE suggests risk decline toward 2023.
            * Correlations: No strong relationship between victims, commune, or victim type.
  
└── Results

            └── Business Recommendation
            * Target Car Drivers with stricter policies.  
            * Protect Motorcyclists & Pedestrians with infrastructure & safety programs.  
            * Focus resources on High-Risk Areas.  
            * Track KPIs.
