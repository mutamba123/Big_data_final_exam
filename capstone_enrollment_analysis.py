"""
Capstone Project: Exploring Global Secondary School Enrollment Rates
Course: INSY 8413 | Introduction to Big Data Analytics
Sector: Education
Objective: Identify countries/regions where secondary school enrollment rates lag behind, and explore influencing factors.
"""

print("✅ Script started running...")

# 1️⃣ Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

sns.set(style="whitegrid", palette="muted")
print("✅ Libraries loaded.")

# 2️⃣ Load dataset
try:
    df = pd.read_csv("unesco_secondary_enrollment.csv")
    print("✅ Dataset loaded successfully! First rows:")
    print(df.head())
except Exception as e:
    print("❌ Error loading dataset:", e)
    exit()

# 3️⃣ Data cleaning
print("\n🔍 Checking missing values:")
print(df.isnull().sum())

df.drop_duplicates(inplace=True)
df['Country'] = df['Country'].str.strip()

print("\n✅ Data cleaned. New shape:", df.shape)

# 4️⃣ Descriptive statistics
print("\n📊 Descriptive statistics:")
print(df.describe())

# 5️⃣ Exploratory Data Analysis (EDA)

# a) Distribution plot
plt.figure(figsize=(8,6))
sns.histplot(df['Secondary Enrollment Rate'], bins=30, kde=True, color='skyblue')
plt.title("Distribution of Secondary Enrollment Rate")
plt.xlabel("Enrollment Rate (%)")
plt.ylabel("Count")
plt.show()

# b) Enrollment by region (latest year)
latest_year = df['Year'].max()
df_latest = df[df['Year'] == latest_year]

plt.figure(figsize=(12,6))
sns.boxplot(x='Region', y='Secondary Enrollment Rate', data=df_latest)
plt.title(f"Secondary Enrollment Rate by Region ({latest_year})")
plt.xticks(rotation=45)
plt.show()

# c) Correlation heatmap
features = ['Secondary Enrollment Rate', 'GDP per capita', 'Population',
            'Urbanization Rate (%)', 'Government Education Spending', 'Literacy Rate (%)']

plt.figure(figsize=(8,6))
sns.heatmap(df[features].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

# 6️⃣ Clustering with KMeans
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[features])

kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)

print("\n✅ Clustering done. Cluster counts:")
print(df['Cluster'].value_counts())

# 7️⃣ Evaluate clustering
score = silhouette_score(X_scaled, df['Cluster'])
print(f"\n📊 Silhouette Score: {score:.2f} (closer to 1 is better)")

# 8️⃣ Innovation: custom scatter plots
def plot_clusters(dataframe, x_col, y_col):
    plt.figure(figsize=(10,6))
    sns.scatterplot(x=dataframe[x_col], y=dataframe[y_col], hue=dataframe['Cluster'],
                    palette='Set1', alpha=0.8)
    plt.title(f"{x_col} vs {y_col} by Cluster")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.legend(title='Cluster')
    plt.show()

# Plot Enrollment vs GDP per capita
plot_clusters(df, 'Secondary Enrollment Rate', 'GDP per capita')

# Plot Enrollment vs Literacy Rate
plot_clusters(df, 'Secondary Enrollment Rate', 'Literacy Rate (%)')

df.to_csv("cleaned_enrollment_data.csv", index=False)
print("✅ Cleaned data exported for Power BI.")
