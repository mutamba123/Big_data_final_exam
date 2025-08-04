Big Data Final Exam

Title Slide:Global Secondary School Enrollment Analysis

Capstone Project   INSY 8413: Introduction to Big Data Analytics

Sector: Education

Student: Mutamba Alice

ID:27688

Instructor: Eric Maniraguha

Date: August 2025

Project Introduction

Many countries face challenges achieving universal secondary school enrollment.
Goal: Identify countries and regions where enrollment lags.
Explore socio-economic factors driving these gaps (e.g., GDP, literacy, urbanization).
Use big data analytics & visualization to uncover actionable insights.

Dataset & Methodology

Dataset:https://data.uis.unesco.org

Source: UNESCO UIS Data

Structured CSV, ~2500 rows × 10 columns

Variables: Country, Region, Year, Enrollment Rate, GDP per capita, Literacy Rate, Urbanization, Population, etc.

Methodology:

1.Data cleaning & preprocessing

2.Exploratory Data Analysis (EDA)

3.Clustering (KMeans)

4.Visualization & dashboard in Power BI

<img width="991" height="320" alt="image" src="https://github.com/user-attachments/assets/5bd6b8b6-9bac-48b8-87a7-b304867e74b5" />

EDA Results

- Histograms & boxplots: Show distribution & detect outliers.
 
- Correlation heatmap: Found positive correlation between:
 
- GDP per capita & Enrollment Rate
  
- Literacy Rate & Enrollment Rate
  
- Regional comparison: Some regions consistently below global average.

 <img width="1016" height="477" alt="image" src="https://github.com/user-attachments/assets/fdb55284-2820-41fc-b060-00f787080caf" />

Most countries have high enrollment rates, but some still lag behind highlighting regional inequality

Boxplots

<img width="919" height="402" alt="image" src="https://github.com/user-attachments/assets/a3c84b36-1208-4c82-a3ad-7196999a9775" />

Regions differ in both median enrollment and variability. Some regions show wide gaps among countries, highlighting unequal education opportunities.



Heatmap 

<img width="830" height="402" alt="image" src="https://github.com/user-attachments/assets/e1378dbd-78cc-425b-b799-72f74a0a54e7" />

Higher GDP and literacy strongly relate to better enrollment rates. Urbanization also contributes, though to a lesser extent.


Clustering & Insights

- Used KMeans to group countries with similar profiles.
  
- Evaluated with silhouette score.
  
- Identified clusters:

- High GDP & high enrollment
  
- Medium GDP & medium enrollment
  
- Low GDP & low enrollment
  
- Helps policymakers target similar countries together

  Clustering scatter plot

  <img width="918" height="402" alt="image" src="https://github.com/user-attachments/assets/5743388b-5b53-4559-bd4d-0b123f752cb5" />

  Dashboard Walkthrough (Power BI)
  
Visuals included:

Line chart: Enrollment trend over years

Bar chart: Enrollment by region (with drill-down to countries)

Scatter plot: GDP vs Enrollment Rate (colored by cluster, sized by population)

Map: Enrollment by country

Summary card: Avg Global Enrollment Rate

Tooltips: Literacy Rate & Urbanization Rate

Slicers: Year & Region

AI Visual: Decomposition tree (factors explaining low enrollment)

<img width="831" height="444" alt="image" src="https://github.com/user-attachments/assets/0d1b0af8-a27a-497f-a5dd-67a6dd2258a4" />






