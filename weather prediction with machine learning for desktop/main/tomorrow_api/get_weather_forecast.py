import requests
from datetime import datetime
def get_weather_forecast():
    url = "https://api.tomorrow.io/v4/weather/forecast?apikey=52fLhwPLm23oXDwXN64IHU0C6l6h7SR1&location=5.542167, -73.363059&timesteps=1d"

    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)
    days = {}

    if response.status_code == 200:
        # Obtener el contenido JSON de la respuesta
        data = response.json()



        for i in range(5):
            temperatureAvg = data["timelines"]["daily"][i + 1]["values"]["temperatureAvg"]
            precipitationProbabilityAvg = data["timelines"]["daily"][i + 1]["values"]["precipitationProbabilityAvg"]
            humidityAvg = data["timelines"]["daily"][i + 1]["values"]["humidityAvg"]
            time = data["timelines"]["daily"][i + 1]["time"]
            date_object = datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ")


            day_of_week = date_object.strftime("%A")

            icon = ""

            if (humidityAvg < 50 and precipitationProbabilityAvg < 20) or precipitationProbabilityAvg < 20:
                icon = "../resources/icons/soleado.png"
            elif (20 < precipitationProbabilityAvg < 50 and 50 < humidityAvg < 70) or 20 < precipitationProbabilityAvg < 70:
                icon = "../resources/icons/nublado.png"
            elif (70 < humidityAvg and 50 < precipitationProbabilityAvg) or precipitationProbabilityAvg> 70:
                icon = "../resources/icons/luvioso.png"

            day = {"day_of_week": day_of_week, "icon": icon, "temperatureAvg": temperatureAvg}
            days[i] = day
        return days
    else:
        print("Error al realizar la solicitud:", response.status_code)
        return None








