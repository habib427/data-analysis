import pandas as pd
import matplotlib.pyplot as plt
import os


file_path = "C:/Users/HABIB/PycharmProjects/RandomWebsites/24 to 1st may.csv"

df = pd.read_csv(file_path)

df.columns = df.columns.str.strip()
print(" Available columns:", df.columns.tolist())

df = df.dropna(subset=["event name", "total users"])

df["event name"] = df["event name"].str.strip().str.lower()

selected_events = [
    "splash_screen",
    "main_screen",
    "connect_vpn",
    "failed_to_connect",
    "connect_shadowsocks",
    "failed_to_connect_shadowsocks",
    "connection_success_screen",
    "servers_screen",
    "app_remove",
    "hit_url1",
    "url1_failed",
    "hit_firebase",
]

df = df[df["event name"].isin(selected_events)]

event_counts = df.groupby("event name")["total users"].count().reset_index()
event_counts.columns = ["event name", "total users"]

df.to_csv("cleaned_event_data24 to 1st may.csv", index=False)
event_counts.to_csv("event_user_counts.csv", index=False)

print("Cleaned data saved as 'cleaned_event_data24 to 1st may.csv'")
print("Event count saved as 'event_user_counts.csv'")


# plt.figure(figsize=(10, 6))
# plt.bar(event_counts["event name"], event_counts["total users"], color="skyblue")
# plt.title("Total Users per Event")
# plt.xlabel("Event name")
# plt.ylabel("Total Users")
# plt.xticks(rotation=45)
# plt.tight_layout()
#
# #  Save chart
# plt.savefig("event_user_counts.png")
# print("Chart saved as 'event_user_counts.png'")
# plt.show()
