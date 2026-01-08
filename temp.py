import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. LIVE DATA INPUT [cite: 14]
# Expanded with diverse Indian state capitals for better analysis
live_data = [
    # North India
    {"City": "New Delhi", "Month": 1, "Day": 1, "Year": 2022, "AvgTemperature": 55.4},
    {"City": "New Delhi", "Month": 1, "Day": 2, "Year": 2022, "AvgTemperature": 54.8},
    {"City": "New Delhi", "Month": 6, "Day": 1, "Year": 2022, "AvgTemperature": 102.5},
    {"City": "Lucknow", "Month": 1, "Day": 1, "Year": 2022, "AvgTemperature": 52.3},
    {"City": "Lucknow", "Month": 6, "Day": 1, "Year": 2022, "AvgTemperature": 105.1},
    {"City": "Shimla", "Month": 1, "Day": 1, "Year": 2022, "AvgTemperature": 38.0},
    {"City": "Shimla", "Month": 6, "Day": 1, "Year": 2022, "AvgTemperature": 72.0},
    
    # West India
    {"City": "Mumbai", "Month": 1, "Day": 1, "Year": 2022, "AvgTemperature": 78.2},
    {"City": "Mumbai", "Month": 1, "Day": 2, "Year": 2022, "AvgTemperature": 77.5},
    {"City": "Mumbai", "Month": 6, "Day": 1, "Year": 2022, "AvgTemperature": 88.4},
    {"City": "Jaipur", "Month": 1, "Day": 1, "Year": 2022, "AvgTemperature": 58.0},
    {"City": "Jaipur", "Month": 6, "Day": 1, "Year": 2022, "AvgTemperature": 108.3},
    
    # South India
    {"City": "Bengaluru", "Month": 1, "Day": 1, "Year": 2022, "AvgTemperature": 72.1},
    {"City": "Bengaluru", "Month": 1, "Day": 2, "Year": 2022, "AvgTemperature": 71.5},
    {"City": "Bengaluru", "Month": 6, "Day": 1, "Year": 2022, "AvgTemperature": 78.5},
    {"City": "Chennai", "Month": 1, "Day": 1, "Year": 2022, "AvgTemperature": 79.5},
    {"City": "Chennai", "Month": 6, "Day": 1, "Year": 2022, "AvgTemperature": 94.1},
    {"City": "Hyderabad", "Month": 1, "Day": 1, "Year": 2022, "AvgTemperature": 74.5},
    {"City": "Hyderabad", "Month": 6, "Day": 1, "Year": 2022, "AvgTemperature": 85.2},
    
    # East India
    {"City": "Kolkata", "Month": 1, "Day": 1, "Year": 2022, "AvgTemperature": 68.0},
    {"City": "Kolkata", "Month": 6, "Day": 1, "Year": 2022, "AvgTemperature": 92.3},
    {"City": "Patna", "Month": 1, "Day": 1, "Year": 2022, "AvgTemperature": 54.2},
    {"City": "Patna", "Month": 6, "Day": 1, "Year": 2022, "AvgTemperature": 104.5}
]

# 2. CONVERT & PREPARE DATA [cite: 28, 38]
df = pd.DataFrame(live_data)
df['Date'] = pd.to_datetime(df[['Year', 'Month', 'Day']]) # date handling [cite: 38]
df = df[df['AvgTemperature'] > -70] # logical conditions/cleaning [cite: 29]
df.set_index('Date', inplace=True)

# 3. CALCULATE WEEKLY & MONTHLY AVERAGES [cite: 35, 39]
# averaging [cite: 39]
weekly_avg = df.groupby('City')['AvgTemperature'].resample('W').mean()
monthly_avg = df.groupby('City')['AvgTemperature'].resample('ME').mean()

# 4. VISUALIZATION: TEMPERATURE VARIATION [cite: 36, 45, 49]
# 
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 7))

# Plot A: Monthly Average Trend (Bar Chart) [cite: 49]
monthly_avg.unstack(level=0).plot(kind='bar', ax=ax1)
ax1.set_title('Monthly Average Temperature by City')
ax1.set_ylabel('Temperature (°F)')
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Plot B: Daily Temperature Variation (Line Plot) [cite: 36, 40]
sns.lineplot(data=df.reset_index(), x='Date', y='AvgTemperature', hue='City', marker='o', ax=ax2)
ax2.set_title('Daily Temperature Variation Plot')
ax2.set_ylabel('Temperature (°F)')
ax2.set_xlabel('Timeline')
plt.xticks(rotation=45)
ax2.grid(True, alpha=0.3)
ax2.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()

# 5. OUTPUT RESULTS [cite: 48]
print("--- WEEKLY AVERAGES ---")
print(weekly_avg)
print("\n--- MONTHLY AVERAGES ---")
print(monthly_avg)
