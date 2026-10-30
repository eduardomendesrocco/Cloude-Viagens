import json
import os
from config import DATA_FILE, BASE_DIR

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)
    
def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def recupera_todos():
    return(load_data( ))

def buscar_item(item_id):
    items = load_data()
    return next((item for item in items if item['id'] == item_id), None)

def add_viagem(form_data):
    atual = form_data.get('atual')
    destino = form_data.get('destino')

    dia_ida, dia_volta = form_data.get('ida'), form_data.get('volta')
    observacoes = form_data.get('obs', default="Nenhuma observação acrescentada")
    
    if not atual and not destino and not dia_ida and not dia_volta:
        return False
    
    viagens = load_data( )

    new_id = max([viagem['id'] for viagem in viagens], default=0) + 1

    new_trip = {"id": new_id, 
                "local_atual": atual, 
                "local_destino": destino, 
                "dia_de_ida": dia_ida, 
                "dia_de_volta": dia_volta,
                "observacoes": observacoes
                    }