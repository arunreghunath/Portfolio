import urllib.request
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

temperatureReading = []
timeReading = []
response = urllib.request.urlopen("http://localhost:8080/")
data = response.read().decode()
root = ET.fromstring(data.strip("\n"))

for reading in root.findall('reading'):
    time = reading.find('time').text
    temperatureReading.append(time[time.find(' '):])
    timeReading.append(int(reading.find('temperature').text))

plt.plot(time_readings, temperatureReading,'green')
title_obj = plt.title("Temperature Vs Time")
plt.setp(title_obj, color='green', fontsize=20,fontname="Times New Roman",fontweight="bold")
plt.xticks(time_readings, rotation='horizontal')
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.show()
