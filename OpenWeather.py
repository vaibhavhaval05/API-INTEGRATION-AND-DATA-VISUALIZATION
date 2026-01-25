import requests
import matplotlib.pyplot as plt

# ---------------------------
# API Configuration
# ---------------------------
API_KEY = "8b08d88b84c27ef7e5e0a2a8d4324a19"
CITY = "Kolhapur"
URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# ---------------------------
# Fetch Data
# ---------------------------
response = requests.get(URL)
data = response.json()

# Error Handling
if response.status_code != 200:
    print("API Error:", data)
    exit()

# ---------------------------
# Extract Data
# ---------------------------
dates = []
temperatures = []
humidity = []

for item in data["list"]:
    dates.append(item["dt_txt"])
    temperatures.append(item["main"]["temp"])
    humidity.append(item["main"]["humidity"])
print(data)
# ---------------------------
# Combined Dashboard
# ---------------------------
plt.figure(figsize=(12, 8))

# Temperature subplot
plt.subplot(1, 2, 1)
plt.plot(dates, temperatures)
plt.title(f"Temperature Forecast - {CITY}")
plt.ylabel("Temperature (°C)")
plt.xticks(dates[0::4],rotation=90)

# Humidity subplot
plt.subplot(1, 2, 2)
plt.plot(dates, humidity)
plt.title(f"Humidity Forecast - {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Humidity (%)")
plt.xticks(dates[::4],rotation=90)

plt.tight_layout()
plt.show()
