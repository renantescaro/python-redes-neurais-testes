from flask import render_template, jsonify, Blueprint
from app.service.registro import Registro


bp = Blueprint(
    'inical',
    __name__,
    template_folder='templates' )


class LogCtrl:
    @bp.route('/', methods=['GET'])
    def inicial_template():
        return render_template(
            'inicial.html',
            titulo = 'inicial',
            dados = Registro().listar()
        )


    @bp.route('/json', methods=['GET'])
    def inicial_json():
        return jsonify({'pagina':'inicial'})
