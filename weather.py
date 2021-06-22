import requests
#import os
from datetime import datetime

api_key = '232ff9bf52a3b7e5ffd075382d8ab135'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')

file = open("weather_data.txt","w")
file.writelines("Weather Stats for - {}  || {}\n".format(location.upper(), date_time))
file.writelines("Current temperature is: {:.2f} deg C\n".format(temp_city))
file.writelines("Current weather desc  :"+weather_desc+"\n")
file.writelines("Current Humidity      :"+str(hmdt)+ '%\n')
file.writelines("Current wind speed    :"+str(wind_spd) +'kmph\n')
file.close()