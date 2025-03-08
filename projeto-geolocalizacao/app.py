# Importa a função create_app do módulo app
from app import create_app

# Cria uma instância da aplicação Flask
app = create_app()

# Executa a aplicação Flask no modo de depuração
if __name__ == '__main__':
    app.run(debug=True)