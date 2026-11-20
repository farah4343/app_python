import requests 
import json
import tkinter as tk 
def coordonee(ville):
   url = 'https://geocoding-api.open-meteo.com/v1/search'
   pram= {"name": ville, "count": 1}
   response = requests.get(url, params=pram, timeout=5)
   response.raise_for_status()     
   data=response.json()  
   if "results" not in data:            
           return None
   lat=data["results"][0]["latitude"]
   lon=data["results"][0]["longitude"]
   return lat , lon
def get_meteo(lat,lon):
   url2="https://api.open-meteo.com/v1/forecast"
   params={"latitude":lat, "longitude":lon, "current_weather": True }
   response2=requests.get(url2, params=params,timeout=7 )
   response2.raise_for_status()
   meteo = response2.json()["current_weather"]
   temp = meteo["temperature"]
   vent = meteo["windspeed"]
   return temp,vent
def sauvegarder(result):
    with open("meteo.json","w", encoding="utf-8") as f :
        json.dump(result, f ,indent=4, ensure_ascii=False)
    
def main():
   ville=input("saisir la ville:  ")
   coord= coordonee(ville) 
   if coord is None :
       print("ville intruvable")
       return
   latitude , longitude = coordonee(ville)
   temperature , vent = get_meteo(latitude,longitude)
   print("Température:", temperature , "°C")
   print("Vent:", vent, "km/h")
   data={
       "ville" : ville,
       "temperature": temperature,
       "vent" : vent
   }
   sauvegarder(data)
main()