import pandas as pd
import matplotlib.pyplot as plt

#   Load both cleaned event data files
file_old = "C:/Users/HABIB/PycharmProjects/RandomWebsites/prog/cleaned_event_data_1.csv"
file_new = "C:/Users/HABIB/PycharmProjects/RandomWebsites/prog/cleaned_event_data_2.csv"

df_old = pd.read_csv(file_old)[["event name", "total users"]].copy()
df_new = pd.read_csv(file_new)[["event name", "total users"]].copy()

# Rename columns for clarity
df_old.columns = ["event name", "Users Old"]
df_new.columns = ["event name", "Users New"]

#   Merge data on event name
merged = pd.merge(df_old, df_new, on="event name", how="outer").fillna(0)

# Ensure numeric values
merged["Users Old"] = merged["Users Old"].astype(int)
merged["Users New"] = merged["Users New"].astype(int)

#   Calculate change
merged["Change"] = merged["Users New"] - merged["Users Old"]
merged["% Change"] = (merged["Change"] / merged["Users Old"].replace(0, 1)) * 100

#   Save and Plot
merged.to_csv("event_progression_comparison.csv", index=False)
print("Comparison saved to 'event_progression_comparison.csv'")

#   Plot chart
plt.figure(figsize=(12, 6))
plt.bar(merged["event name"], merged["Change"], color='teal')
plt.title("Event User Progression (New - Old)")
plt.xlabel("Event Name")
plt.ylabel("User Count Change")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("event_progression_chart.png")
plt.show()
print("Chart saved as 'event_progression_chart.png'")
