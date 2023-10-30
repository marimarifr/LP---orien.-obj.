from enum import Enum

class Produto:
    qtd_prod = 0
    def __init__(self, barcode, preco, marca, categoria):
        self.barcode = barcode
        self.preco = preco
        self.marca = marca
        self.categoria = categoria
        qtd_prod += 1 


class Marcas(Enum):
    Amazon = 1
    Renner = 2
    Avon = 3
    












