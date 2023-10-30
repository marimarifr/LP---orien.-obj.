from categoria import CathegoryBeauty, CathegoryCloth, CathegoryTech

class Inventario(CathegoryBeauty, CathegoryCloth, CathegoryTech):
    
    def __init__(self, tech = [], beauty = [], cloth = []):
        self.tech = tech
        self.beauty = beauty
        self.cloth = cloth

    def get_info(self):
        beauty = CathegoryBeauty.total_beauty
        cloth = CathegoryCloth.total_cloth
        tech = CathegoryTech.total_tech
        total =  tech + cloth + beauty
        return f"  Total de itens no estoque: {total} \n  Total na categoria tecnologia: {tech} \n  Total na categoria vestuário: {cloth} \n  Total na categoria beleza: {beauty}"

    # def entrada_prod(self, total_cat, qtd):
    #     super().total_beauty += qtd
        
    # def saida_prod(self, total_cat, qtd):
    #     super().total_cat +- qtd
    

invent = Inventario()
print(invent.get_info())
