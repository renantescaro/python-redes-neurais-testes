from sqlalchemy import Column, Integer, String, Float, DateTime
from app.models.banco import base as Base


class RegistroModel(Base):
    __tablename__ = 'registro'

    id = Column(Integer, primary_key=True, index=True)
    qtd_neuronios_camada_oculta = Column(String, unique=False, index=False)
    apredizagem = Column(Float, unique=False, index=False)
    porcentagem_erro = Column(Float, unique=False, index=False)
    data_inserido = Column(DateTime, default=None)
    data_finalizado = Column(DateTime, default=None)
