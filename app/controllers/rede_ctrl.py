import json
import os
from flask import (
    Response,
    render_template,
    jsonify, Blueprint, request)
from app.service.ativacoes import (
    Sigmoid, Tanh, LeakyRelu)
from app.service import (
    Imagem, Parametro,
    Dados, Grafico,
    PerceptronMultiCamadas)
from app.utils.config import Config

bp = Blueprint(
    'rede',
    __name__,
    template_folder='templates'
)


class RedeCtrl:
    @bp.route('/reconhecer', methods=['POST'])
    def reconhecer():
        placa = request.form.get('placa')
        foto_placa = request.files.get('foto_placa')

        if placa is None or foto_placa is None:
            return Response(
                json.dumps({'error':'place not found'}),
                status=404,
                mimetype='application/json'
            )

        caminho_salvar = os.path.join(
            f'{Config.get("caminho_sistema")}assets\\uploads',
            f'foto_placa_{placa}.png'
        )
        upload_foto_placa = request.files['foto_placa']
        upload_foto_placa.save(caminho_salvar)

        rede = PerceptronMultiCamadas(
            dados=Dados(versao=5),
            parametro=Parametro(
                ativacao=Tanh(),
                imagem=Imagem(),
                imagem_unica=f'assets/uploads/foto_placa_{placa}.png'
            )
        )
        resultado = rede.executar()
        return jsonify({'resultado':resultado})
