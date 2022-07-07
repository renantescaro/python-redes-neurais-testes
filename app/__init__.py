from flask import Flask
from app.controllers.inicial_ctrl import bp as bp_inicial
from app.controllers.rede_ctrl import bp as bp_rede


def create_app(test_config=None):
    app = Flask(
        __name__,
        static_url_path = '/static',
        static_folder   = 'static',
        instance_relative_config = True
    )

    app.config.from_mapping(
        SECRET_KEY   = 'super secret key',
        SESSION_TYPE = 'filesystem',
        JSONIFY_PRETTYPRINT_REGULAR = False
    )

    # adicionar rotas
    app.register_blueprint(bp_inicial)
    app.register_blueprint(bp_rede)
    return app
