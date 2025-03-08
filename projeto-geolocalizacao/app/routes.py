from flask import Blueprint, render_template, request, jsonify
import datetime
import os

# Cria um Blueprint para as rotas principais
main = Blueprint('main', __name__)

# Define o nome do arquivo de log
LOG_FILE = "log.txt"

# Rota para a página inicial
@main.route('/')
def home():
    return render_template('index.html')

# Rota para registrar a localização
@main.route('/log', methods=['POST'])
def log_location():
    data = request.json  # Recebe os dados enviados pelo JavaScript

    # Verifica se os dados são válidos
    if not data or 'latitude' not in data or 'longitude' not in data:
        return jsonify({"error": "Dados inválidos"}), 400

    # Cria uma entrada de log com a data e hora atuais, latitude e longitude
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    log_entry = f"{timestamp}|{data['latitude']}|{data['longitude']}\n"

    # Verifica se o arquivo de log já existe e se tem cabeçalho
    if not os.path.exists(LOG_FILE) or os.stat(LOG_FILE).st_size == 0:
        with open(LOG_FILE, "w") as log_file:
            log_file.write("Data verificação|Latitude|Longitude\n")  # Adiciona o cabeçalho
    
    # Adiciona a nova entrada ao arquivo de log
    with open(LOG_FILE, "a") as log_file:
        log_file.write(log_entry)

    # Retorna uma resposta de sucesso
    return jsonify({"message": "Localização registrada com sucesso!"}), 200
