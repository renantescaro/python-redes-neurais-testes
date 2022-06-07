from waitress import serve
from app import create_app
from app.utils.config import Config


app = create_app()
serve(app, host=Config.get('IP_APLICACAO'), port=Config.get('PORTA_APLICACAO'))
