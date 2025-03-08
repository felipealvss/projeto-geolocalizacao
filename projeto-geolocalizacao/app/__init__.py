from flask import Flask

def create_app():
    # Cria uma instância da aplicação Flask
    app = Flask(__name__)

    # Importa o Blueprint das rotas principais
    from .routes import main
    # Registra o Blueprint na aplicação Flask
    app.register_blueprint(main)

    # Retorna a instância da aplicação Flask
    return app
