from typing import List
from faker import Faker
from app.service import Imagem
from app.service import Parametro

faker = Faker()
sut = Parametro(
    Imagem()
)


def test_carregar_assets_treinamento_ok():
    entradas, saidas = sut.executar()
    assert isinstance(entradas, List)
    assert isinstance(saidas, List)


def test_carregar_assets_treinamento_caracter_ok():
    sut._caracter_entrada_para_binario('a')
    entradas, saidas = sut.executar()
    assert isinstance(entradas, List)
    assert isinstance(saidas, List)