import requests


def obter_clima():
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=-15.78&longitude=-47.93&current_weather=true"
    )

    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        return "Erro ao consultar clima."

    dados = response.json()

    temperatura = dados["current_weather"]["temperature"]
    vento = dados["current_weather"]["windspeed"]

    return (
        f"Clima atual:\n"
        f"Temperatura: {temperatura}°C\n"
        f"Velocidade do vento: {vento} km/h"
    )
