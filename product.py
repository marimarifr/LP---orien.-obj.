from enum import Enum

class Produto:
    def __init__(self, name, barcode, preco, marca, qtd, categoria):
        self.name = name
        self.barcode = barcode
        self.preco = preco
        self.marca = marca
        self.qtd = qtd
        self.categoria = categoria

class Marcas(Enum):
    Amazon = 1
    Renner = 2
    Avon = 3