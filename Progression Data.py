import pandas as pd
import matplotlib.pyplot as plt

file_old = "C:/Users/HABIB/PycharmProjects/RandomWebsites/prog/cleaned_event_data1-11April.csv"
file_new = "C:/Users/HABIB/PycharmProjects/RandomWebsites/prog/cleaned_event_data12-23April.csv"

df_old = pd.read_csv(file_old)[["event name", "total users"]].copy()
df_new = pd.read_csv(file_new)[["event name", "total users"]].copy()

df_old.columns = ["event name", "Users Old"]
df_new.columns = ["event name", "Users New"]

merged = pd.merge(df_old, df_new, on="event name", how="outer").fillna(0)

merged["Users Old"] = merged["Users Old"].astype(int)
merged["Users New"] = merged["Users New"].astype(int)

merged["Change"] = merged["Users New"] - merged["Users Old"]
merged["% Change"] = (merged["Change"] / merged["Users Old"].replace(0, 1)) * 100

# select event sequence
selected_events = [
    "splash_screen",
    "main_screen",
    "connect_vpn",
    "connection_success_screen",
    "failed_to_connect",
    "servers_screen",
    "app_remove",
    "hit_url1",
    "url1_failed",
    "hit_firebase"
]

merged = merged[merged["event name"].isin(selected_events)]
merged["event name"] = pd.Categorical(merged["event name"], categories=selected_events, ordered=True)
merged = merged.sort_values("event name")

# Save to CSV
merged.to_csv("C:/Users/HABIB/PycharmProjects/RandomWebsites/prog/event_progression_comparison_april.csv", index=False)
print("Comparison saved to 'event_progression_comparison_april.csv'")


# chart
plt.figure(figsize=(12, 6))

colors = merged["Change"].apply(lambda x: "green" if x > 0 else ("red" if x < 0 else "blue"))
bar_width = 0.3
x_positions = range(len(merged["event name"]))
plt.bar(x_positions, merged["Change"], color=colors, width=bar_width)
plt.title("Event User Progression (1st April - 23rd April)")
plt.xlabel("Event Name")
plt.ylabel("User Count Change")
plt.xticks(ticks=x_positions, labels=merged["event name"], rotation=45, ha='right')
plt.axhline(0, color='black', linewidth=0.8)  # horizontal line at y=0
plt.tight_layout()
plt.savefig("C:/Users/HABIB/PycharmProjects/RandomWebsites/prog/event_progression_chart.png")
plt.show()
print("Chart saved as 'event_progression_chart.png'")
