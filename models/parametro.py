from sqlalchemy import Column, Integer, String, Float, TIMESTAMP
from models.banco import base as Base


class ParametroModel(Base):
    __tablename__ = 'parametro'

    id = Column(Integer, primary_key=True, index=True)
    qtd_neuronios_camada_oculta = Column(String, unique=False, index=False)
    apredizagem = Column(Float, unique=False, index=False)
    porcentagem_erro = Column(Float, unique=False, index=False)
    # data_inserido = Column(TIMESTAMP, unique=False, index=False)
