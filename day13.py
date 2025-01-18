# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 04:12:22 2025

@author: Triddles lamar
"""

import requests


#assugn your api key
api_key = "43daef8559705998e9d146044f436dd7"


#input city name
city_name = input("Type the city you want to find it's weather: ")
city_name = city_name.capitalize()

#paste url with api variable
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"


#print url and parse result iin json format
print(url)
req = requests.get(url)
data = req.json()
print(data)


#assign name, longitude and latitde using your parsed json results 
name = data['name']
lon = data['coord'] ['lon']
lat = data['coord'] ['lat']
weather = data['weather'][0]['description']
humidity = data['main'] ['humidity']
sea_level = data['main'] ['sea_level']
country = data['sys'] ['country']
string = f'[{city_name} - WEATHER REQUEST REPORT]'

#print name of city and it's coordinate
print(string)
print("""====================================================
      
      """)
print(f""" 
      The weather for the city '{name}', {country}
      With longitude '{lon}' and latitude '{lat}' is  {weather},
      The humidity is {humidity} above sea level of {sea_level}m """)
      
      
      
      
      
      
      
'''exclude the hourly and minute results
exclude = "hourly, minute"
#set the url for weather excluding the hourly and minute reports and print it out
url2 = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={exclude}&appid={api_key}"
print(url2)
#parse the second url to a json format
req2 = requests.get(url2)
data2 = req2.json()
print(data2)
#get report 
days = []
night = []
descr = []
#we need to access daily
for i in data2['daily']:
    #we noticed that the temperature is in kelvin, so we add -273.15 for every datapoint
    #lets start with day
    days.append(round(i['temp'] ['day'] -273.15))
    #let's do the niight
    night.append(round(i['temp'] ['night'] -273.15))
    
    #get weather condition and description
    descr.append(i['weather'][0]['main'] + ": " + i['weathher'][0]['description'])
    
    
print(days)
print(night)
    
    '''


