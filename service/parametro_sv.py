from models.parametro import ParametroModel
from models.banco import session_local


@staticmethod
def salvar_parametros(
    qtd_neuronios_camada_oculta:int,
    apredizagem:float,
    porcentagem_erro:float
):
    parametro_model = ParametroModel(
        qtd_neuronios_camada_oculta=qtd_neuronios_camada_oculta,
        apredizagem=apredizagem,
        porcentagem_erro=porcentagem_erro
    )
    session_local.add(parametro_model)
    session_local.commit()
    session_local.refresh(parametro_model)
