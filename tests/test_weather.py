from src.weather import obter_clima


def test_obter_clima():
    resultado = obter_clima()

    assert "Temperatura" in resultado
