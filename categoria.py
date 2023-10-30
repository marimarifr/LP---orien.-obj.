from product import Produto

class CathegoryTech(Produto):
    def __init__(self, barcode, preco, marca, categoria):
        super().__init__(barcode, preco, marca, categoria = "Tecnologia")

class CathegoryBeauty(Produto):
    def __init__(self, barcode, preco, marca, categoria):
        super().__init__(barcode, preco, marca, categoria = "Beleza")

class CathegoryCloth(Produto):
    def __init__(self, barcode, preco, marca, categoria):
        super().__init__(barcode, preco, marca, categoria = "Vestuário")


