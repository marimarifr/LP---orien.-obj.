from enum import Enum

class Produto:
    qtd_prod = 0
    def __init__(self, barcode, preco, marca, categoria):
        self.barcode = barcode
        self.preco = preco
        self.marca = marca
        self.categoria = categoria
        qtd_prod += 1 

class CathegoryTech(Produto):
    def __init__(self, categoria = "Tecnologia")


class Inventario():
   
class Marcas(Enum):
    Marca_1 = 1
    Marca_2 = 2
    Marca_3 = 3
    Marca_4 = 4










