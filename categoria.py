class CathegoryTech(Produto):
    qtd_tech = []
    def __init__(self, name, barcode, preco, marca, qtd, categoria):
        super().__init__(name, barcode, preco, marca, categoria = "Tecnologia")
        qtd_tech.append(name)

class CathegoryBeauty(Produto):
    qtd_beauty = []
    def __init__(self, name, barcode, preco, marca, qtd, categoria):
        super().__init__(name, barcode, preco, marca, categoria = "Beleza")
        qtd_beauty.append(name)

class CathegoryCloth(Produto):
     qtd_cloth = []
    def __init__(self, name, barcode, preco, marca, qtd, categoria):
        super().__init__(name, barcode, preco, marca, categoria = "Vestuário")
        qtd_cloth.append(name)