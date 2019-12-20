# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 07:23:54 2019

@author: arunr
"""
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

plt.plot(temperatureReading,timeReading,'blue')
title_obj = plt.title("Weather")
plt.setp(title_obj, color='black')
plt.xticks(timeReading, rotation='vertical')
plt.xticks(temperatureReading,rotation='45')
plt.ylabel("Time")
plt.xlabel("Temperature")
plt.show()
