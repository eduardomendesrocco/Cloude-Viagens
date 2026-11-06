import os

# Diretório base dos arquivos JSON
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# JSON de viagens cadastradas
VIAGENS_DATA_FILE = os.path.join(
    BASE_DIR, 
    "models", 
    "data", 
    "viagens_cadastradas.json"
    )

# JSON de usuários cadastrados
USERS_DATA_FILE = os.path.join(
    BASE_DIR, 
    "models", 
    "data", 
    "usuarios_cadastrados.json"
    )

# Links da API
GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"