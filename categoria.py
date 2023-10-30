from product import Produto

class CathegoryTech(Produto):
    total_tech = 0
    def __init__(self, name, barcode, preco, marca, qtd):
        super().__init__(name, barcode, preco, marca, qtd, categoria = "Tecnologia")
        CathegoryTech.total_tech += self.qtd

class CathegoryBeauty(Produto):
    total_beauty = 0
    def __init__(self, name, barcode, preco, marca, qtd):
        super().__init__(name, barcode, preco, marca, qtd, categoria = "Beleza")
        CathegoryBeauty.total_beauty += self.qtd

class CathegoryCloth(Produto):
    total_cloth = 0
    def __init__(self, name, barcode, preco, marca, qtd):
        super().__init__(name, barcode, preco, marca, qtd, categoria = "Vestuário")
        CathegoryCloth.total_cloth += self.qtd