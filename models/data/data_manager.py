import json
import os
from config import VIAGENS_DATA_FILE, USERS_DATA_FILE, BASE_DIR


### CRUD DE VIAGENS


def load_data_VIAGENS():
    if not os.path.exists(VIAGENS_DATA_FILE):
        return []
    
    with open(VIAGENS_DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)
    
def save_data_VIAGENS(data):
    with open(VIAGENS_DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def recupera_todos_VIAGENS():
    return(load_data_VIAGENS( ))

def add_viagem(form_data, user_id):

    # Pega os dados obtidos no formulário
    atual = form_data.get('atual')
    destino = form_data.get('destino')

    dia_ida, dia_volta = form_data.get('ida'), form_data.get('volta')
    observacoes = form_data.get('obs', default="Nenhuma observação acrescentada")
    
    # Confere se os dados necessários estão preenchidos
    if not atual or not destino or not dia_ida or not dia_volta:
        return False
    
    # Cria uma variável com o JSON
    VIAGENS = load_data_VIAGENS( )

    new_id_viagem = max([viagem['id'] for viagem in VIAGENS], default=0) + 1

    # Monta a viagem para ser adicionada ao JSON
    new_trip = {"id": new_id_viagem, 
                "local_atual": atual, 
                "local_destino": destino, 
                "dia_de_ida": dia_ida, 
                "dia_de_volta": dia_volta,
                "observacoes": observacoes
                    }
    
    # Adiciona a nova viagem ao JSON
    VIAGENS.append(new_trip)
    save_data_VIAGENS(VIAGENS)
    return True
    

### CRUD DE USUÁRIOS


def load_data_USERS():
    if not os.path.exists(USERS_DATA_FILE):
        return []
    
    with open(USERS_DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)
    
def save_data_USERS(data):
    with open(USERS_DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def recupera_todos_USERS():
    return(load_data_USERS( ))

def add_user(form_data):
    nome = form_data.get('nome')
    mail = form_data.get('email')
    password = form_data.get('senha')
    
    USERS = load_data_USERS( )

    if not nome or not mail or not password:
        return False

    new_id_user = max([user['id'] for user in USERS], default=0) + 1

    new_user = {"id": new_id_user, 
                "nome": nome,
                "email": mail,
                "senha": password
                    }
    
    # Adiciona o novo usuário ao JSON
    USERS.append(new_user)
    save_data_USERS(USERS)

def busca_user_email(email):
    USERS = load_data_USERS

    return next((user for user in USERS if user["email"].lower() == email.lower()), None)