from unittest.mock import patch, mock_open
from faker import Faker
from classes.log import Log

faker = Faker()
sut = Log

def test_data_atual_string_ok():
    retorno = sut._data_atual_string()
    assert isinstance(retorno, str)


def test_data_atual_string_txt_ok():
    retorno = sut._data_atual_string_txt()
    assert isinstance(retorno, str)
