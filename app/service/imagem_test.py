import numpy as np
from faker import Faker
from app.service.imagem import Imagem

faker = Faker()
sut = Imagem()


def test_array_ok():
    list_np_array = sut.converter_np_array(
        caminho_arquivo=faker.word()
    )
    assert isinstance(list_np_array, np.ndarray)
