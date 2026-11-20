from flask import Flask, render_template, request
import requests 
import json
app = Flask(__name__)
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

@app.route("/", methods=["GET", "POST"])
def index():
    resultat = None
    erreur = None

    if request.method == "POST":
        ville = request.form.get("ville", "").strip()
        if ville == "":
            erreur = "Ekteb esm ville."
        else:
            try:
                coord = coordonee(ville)
                if coord is None:
                    erreur = "Ville introuvable."
                else:
                    latitude, longitude = coord
                    temperature, vent = get_meteo(latitude, longitude)
                    resultat = {
                        "ville": ville,
                        "temperature": temperature,
                        "vent": vent,
                    }
                    sauvegarder(resultat)
            except requests.exceptions.RequestException:
                erreur = "Erreur réseau, 3awed ba3d."

    return render_template("index.html", resultat=resultat, erreur=erreur)


if __name__ == "__main__":
    app.run(debug=True)