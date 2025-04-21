import pandas as pd
import matplotlib.pyplot as plt
import os

 # Set file path
file_path = "C:/Users/HABIB/PycharmProjects/RandomWebsites/all Events all versions.csv"  # you can also replace this with input() or sys.argv

#  Load Excel
df = pd.read_csv(file_path)

#  Clean Data
# Normalize column names
df.columns = df.columns.str.strip()
print(" Available columns:", df.columns.tolist())

# Drop rows with missing Event or User ID
df = df.dropna(subset=["event name", "total users"])

# Convert to lowercase for consistency
df["event name"] = df["event name"].str.strip().str.lower()

# Optional: Make sure User ID is string (if needed)
# df["Total users"] = df["Total users"].astype(str)

#  nly Specific Events
selected_events = [
    "splash_screen",
    "main_screen",
    "connect_vpn",
    "failed_to_connect",
    "connection_success_screen",
    "servers_screen",
    "app_remove",
    "hit_url1",
    "url1_failed",
    "hit_firebase",
]

df = df[df["event name"].isin(selected_events)]

#  Group by Event and count Users
event_counts = df.groupby("event name")["total users"].count().reset_index()
event_counts.columns = ["event name", "total users"]

#  Save cleaned data
df.to_csv("cleaned_event_data.csv", index=False)
event_counts.to_csv("event_user_counts.csv", index=False)

print("Cleaned data saved as 'cleaned_event_data.csv'")
print("Event count saved as 'event_user_counts.csv'")

#  Plot the chart
plt.figure(figsize=(10, 6))
plt.bar(event_counts["event name"], event_counts["total users"], color="skyblue")
plt.title("Total Users per Event")
plt.xlabel("Event name")
plt.ylabel("Total Users")
plt.xticks(rotation=45)
plt.tight_layout()

#  Save chart
plt.savefig("event_user_counts.png")
print("Chart saved as 'event_user_counts.png'")
plt.show()
