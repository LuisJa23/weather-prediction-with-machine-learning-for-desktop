import requests

def get_climate_values():
    url = "https://api.tomorrow.io/v4/weather/forecast?apikey=52fLhwPLm23oXDwXN64IHU0C6l6h7SR1&location=5.542167, -73.363059"

    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Obtener el contenido JSON de la respuesta
        data = response.json()

        # Acceder al primer objeto del arreglo 'minutely'
        humidity = data["timelines"]["minutely"][0]["values"]["humidity"]
        precipitationProbability = data["timelines"]["minutely"][0]["values"]["precipitationProbability"]
        temperature = data["timelines"]["minutely"][0]["values"]["temperature"]
        windSpeed = data["timelines"]["minutely"][0]["values"]["windSpeed"]
        return humidity, precipitationProbability, temperature, windSpeed


def calculete_weather():
    humidity, precipitationProbability, temperature, windSpeed = get_climate_values()
    weather_status = ""
    if (humidity < 50 and precipitationProbability < 20) or precipitationProbability < 20:
        weather_status = "soleado"
        icon = "../../resources/icons/soleado.png"
    elif (20 < precipitationProbability < 50 and 50 < humidity < 70) or 20 < precipitationProbability < 70:
        weather_status = "nublado"
        icon = "../../resources/icons/nublado.png"
    elif (70 < humidity and 50 < precipitationProbability) or precipitationProbability > 70:
        weather_status = "lluvioso"
        icon = "../../resources/icons/luvioso.png"

    return weather_status, icon

calculete_weather()