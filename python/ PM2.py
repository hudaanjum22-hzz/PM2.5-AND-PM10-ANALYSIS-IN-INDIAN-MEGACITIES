# PM2.5 and PM10 Analysis in Indian Megacities
# Using Pandas, Seaborn, and Matplotlib

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# Load Dataset
# -------------------------------

# Replace with your dataset path
df = pd.read_csv("india_air_quality.csv")

# Display first few rows
print("Dataset Preview:")
print(df.head())

# -------------------------------
# Data Cleaning
# -------------------------------

# Convert date column into datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Remove missing values
df = df.dropna(subset=['PM2.5', 'PM10'])

# -------------------------------
# Filter Indian Megacities
# -------------------------------

megacities = ['Delhi', 'Mumbai', 'Kolkata', 'Chennai', 'Bangalore', 'Hyderabad']

df = df[df['City'].isin(megacities)]

# -------------------------------
# Basic Information
# -------------------------------

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df[['PM2.5', 'PM10']].describe())

# -------------------------------
# Average Pollution Levels
# -------------------------------

avg_pollution = df.groupby('City')[['PM2.5', 'PM10']].mean()

print("\nAverage Pollution Levels:")
print(avg_pollution)

# -------------------------------
# Visualization 1:
# Average PM2.5 and PM10 by City
# -------------------------------

avg_pollution.plot(kind='bar', figsize=(10,6))

plt.title('Average PM2.5 and PM10 Levels in Indian Megacities')
plt.xlabel('City')
plt.ylabel('Pollution Level')
plt.xticks(rotation=45)
plt.grid(True)

plt.show()

# -------------------------------
# Visualization 2:
# Monthly PM2.5 Trend
# -------------------------------

# Extract month
df['Month'] = df['Date'].dt.month

monthly_pm25 = df.groupby(['Month', 'City'])['PM2.5'].mean().reset_index()

plt.figure(figsize=(12,6))

sns.lineplot(data=monthly_pm25,
             x='Month',
             y='PM2.5',
             hue='City',
             marker='o')

plt.title('Monthly PM2.5 Trend in Indian Megacities')
plt.xlabel('Month')
plt.ylabel('Average PM2.5')

plt.show()

# -------------------------------
# Visualization 3:
# Monthly PM10 Trend
# -------------------------------

monthly_pm10 = df.groupby(['Month', 'City'])['PM10'].mean().reset_index()

plt.figure(figsize=(12,6))

sns.lineplot(data=monthly_pm10,
             x='Month',
             y='PM10',
             hue='City',
             marker='o')

plt.title('Monthly PM10 Trend in Indian Megacities')
plt.xlabel('Month')
plt.ylabel('Average PM10')

plt.show()

# -------------------------------
# Visualization 4:
# Correlation Heatmap
# -------------------------------

plt.figure(figsize=(6,4))

corr = df[['PM2.5', 'PM10']].corr()

sns.heatmap(corr,
            annot=True,
            cmap='coolwarm')

plt.title('Correlation between PM2.5 and PM10')

plt.show()

# -------------------------------
# Visualization 5:
# Distribution Plot
# -------------------------------

plt.figure(figsize=(10,5))

sns.histplot(df['PM2.5'],
             bins=30,
             kde=True)

plt.title('Distribution of PM2.5 Levels')
plt.xlabel('PM2.5')

plt.show()

# -------------------------------
# Highest Polluted City
# -------------------------------

highest_pm25 = avg_pollution['PM2.5'].idxmax()
highest_pm10 = avg_pollution['PM10'].idxmax()

print("\nCity with Highest PM2.5:", highest_pm25)
print("City with Highest PM10:", highest_pm10)

# -------------------------------
# Conclusion
# -------------------------------

print("\nAnalysis Completed Successfully!")