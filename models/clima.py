import requests
from config import GEOCODING_URL, WEATHER_URL

def buscar_previsao(cidade, dias=5):
    # transforma o nome da cidade em latitude e longitude?
    res = requests.get(GEOCODING_URL, params={"name": cidade, "count": 1, "language": "pt"}, timeout=10)
    res.raise_for_status()

    resultados = res.json().get("results")
    if not resultados:
        return None
        # Não achou a cidade

    local = resultados[0] # nome da cidade

    # pega a previsao pras coordenadas obtidas acima
    res = requests.get(WEATHER_URL, params={
        "latitude": local["latitude"],
        "longitude": local["longitude"],
        "daily": "weather_code,temperature_2m_max,temperature_2m_min",
        "timezone": "auto",
        "forecast_days": dias
    }, timeout=10)
    res.raise_for_status()

    diario = res.json()["daily"]

    previsao = []
    for i in range(len(diario["time"])):
        previsao.append({
            "data": diario["time"][i],
            "maxima": diario["temperature_2m_max"][i],
            "minima": diario["temperature_2m_min"][i],
            "codigo": diario["weather_code"][i],
            "imagem": escolha_img(diario["weather_code"][i])
        })

    return {
        "cidade": local["name"],
        "pais": local.get("country", ""),
        "dias": previsao
    }

def escolha_img(number):
    if number == 0:
        return "sol.png"
    if number in (1, 2):
        return "nuvem_branca.png"
    if number in (51, 53, 55, 61, 63, 65, 80, 81, 82):
        return "chuva.png"
    if number in (95, 96, 99):
        return "tempestade.png"
    else:
        return "nuvem_cinza.png"

if __name__ == "__main__":
    print(buscar_previsao("Araraquara"))