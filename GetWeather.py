import requests

key = "YOUR_API_KEY_HERE"
country = "Greece"
api = f"https://api.weatherapi.com/v1/current.json?key={key}&q={country}&aqi=yes"

res = requests.get(api)
data = res.json()

name = data["location"]["name"]
region = data["location"]["region"]
country_name = data["location"]["country"]
localtime = data["location"]["localtime"]

is_day = data["current"]["is_day"]
weather = data["current"]["condition"]["text"]
wind_kph = data["current"]["wind_kph"]
wind_dir = data["current"]["wind_dir"]
temperature = data["current"]["temp_c"]
feelslike = data["current"]["feelslike_c"]


co = data["current"]["air_quality"]["co"]
no2 = data["current"]["air_quality"]["no2"]
o3 = data["current"]["air_quality"]["o3"]
pm2_5 = data["current"]["air_quality"]["pm2_5"]
pm10 = data["current"]["air_quality"]["pm10"]
so2 = data["current"]["air_quality"]["so2"]

if res:
    print("Successfully connected with api")
else:
    print(f"Error: {res.status_code}")

print(f"""
    Country Information:
        Name: {name}
        Region: {region}
        Country: {country_name}
        Local Time: {localtime}
    
    Weather Information: 
        Weather: {weather}
        Wind Direction: {wind_dir}
        Wind Speed: {wind_kph} kph
        Temperature C: {temperature} °C
        Temperature Feels Like: {feelslike} °C
        
    Air Quality: 
        Carbon monoxide: {int(co)}
        Nitrogen dioxide: {no2}
        Ozone: {o3}
        Particulate Matter 2.5: {int(pm2_5)}
        Particulate matter 10: {int(pm10)}
        Sulfur dioxide: {int(so2)}
""")
