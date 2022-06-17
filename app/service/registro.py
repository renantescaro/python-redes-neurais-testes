from typing import Any
from sqlalchemy import select, update
from app.models import session_local, RegistroModel
from app.service.ativacoes import AtivacaoContract
from app.utils.datas import Datas


class Registro:
    def __init__(self, cpu:str='', vga:str='') -> None:
        self.cpu:str = cpu
        self.vga:str = vga


    def salvar(
        self,
        qtd_neuronios_camada_oculta:int,
        apredizagem:float,
        funcao_ativacao:AtivacaoContract,
    ) -> Any:
        parametro_model = RegistroModel(
            qtd_neuronios_camada_oculta=qtd_neuronios_camada_oculta,
            apredizagem=apredizagem,
            funcao_ativacao=str(funcao_ativacao),
            cpu=self.cpu,
            vga=self.vga,
            data_inserido=Datas.data_hora_atual()
        )
        session_local.add(parametro_model)
        session_local.commit()
        session_local.refresh(parametro_model)

        return parametro_model.id


    def atualizar(
        self,
        porcentagem_erro:float,
        parametro_id: int
    ) -> None:
        query = update(RegistroModel).\
            where(RegistroModel.id == parametro_id).\
            values(
                porcentagem_erro=porcentagem_erro,
                data_finalizado=Datas.data_hora_atual()
            )
        session_local.execute(query)
        session_local.commit()


    def listar(self):
        query = select(RegistroModel)
        return session_local.execute(query).scalars().all()
