from faker import Faker
from unittest.mock import patch 
from classes.grafico import Grafico

faker = Faker()
sut = Grafico()


@patch('matplotlib.pyplot.show')
def test_medias_absolutas_ok(mock_show):
    sut.medias_absolutas(
        dados=[1, 2, 3]
    )
