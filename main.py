from cafe import Cafe,Latte,Frappucino
from decoradores import CremaBatida,Leche

def ver_detalle(cafe: Cafe) ->None:
    print(f"{cafe.get_descripcion()} cuesta {cafe.calcular_costo()}")


if __name__ == "__main__":
    cafe01 = Frappucino()

    ver_detalle(cafe01)