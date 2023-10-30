from categoria import CathegoryBeauty, CathegoryCloth, CathegoryTech

class Inventario(CathegoryBeauty, CathegoryCloth, CathegoryTech):
    def __init__(self, tech = [], beauty = [], cloth = []):
        self.tech = tech
        self.beauty = beauty
        self.cloth = cloth

    def entrada_prod(self, total_cat, qtd):
        super().total_beauty += qtd
        
    # def saida_prod(self, total_cat, qtd):
    #     super().total_cat +- qtd
    

invent = Inventario()
invent.entrada_prod("total_tech", 5)