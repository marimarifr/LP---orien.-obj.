from product import Produto, Marcas


class CathegoryTech(Produto):
    total_tech = 0
    prod_tech = []

    
    def __init__(self, name, barcode, preco, marca):
        super().__init__(name, barcode, preco, marca, categoria = "Tecnologia")
        CathegoryTech.total_tech += 1
        CathegoryTech.prod_tech.append(self.name)

    def add_tech(self, name):
        self.prod_tech.append(name)


class CathegoryBeauty(Produto):
    total_beauty = 0
    prod_beauty = []

    def __init__(self, name, barcode, preco, marca):
        super().__init__(name, barcode, preco, marca, categoria = "Beleza")
        CathegoryBeauty.total_beauty += 1
    
    def add_beauty(self, name):
        self.prod_beauty.append(name)


class CathegoryCloth(Produto):
    total_cloth = 0
    prod_cloth = []

    def __init__(self, name, barcode, preco, marca):
        super().__init__(name, barcode, preco, marca, categoria = "Vestuário")
        CathegoryCloth.total_cloth += 1
    
    def add_cloth(self, name):
        self.prod_cloth.append(name)

class Inventario(CathegoryBeauty, CathegoryCloth, CathegoryTech):
    
    def __init__(self, tech = [], beauty = [], cloth = []):
        self.tech = tech
        self.beauty = beauty
        self.cloth = cloth

    # Método para obter informações sobre o inventário
    def get_info(self):
        # Obtendo os totais de produtos em cada categoria
        beauty = CathegoryBeauty.total_beauty
        cloth = CathegoryCloth.total_cloth
        tech = CathegoryTech.total_tech
        # Calculando o total de itens no estoque
        total = tech + cloth + beauty
        # Retornando uma string formatada com as informações
        return f"  Total de itens no estoque: {total} \n  Total na categoria tecnologia: {tech} \n  Total na categoria vestuário: {cloth} \n  Total na categoria beleza: {beauty}"







    # Método para vender um produto
    def vender_produto(self, name, categoria):

    # Verifica a categoria do produto
        if categoria == "Tecnologia":
            # Acessando os dados da respectiva categoria
            prod = CathegoryTech.prod_tech
            total = CathegoryTech.total_tech
            # Verifica se o proudto está em estoque e levanta a exceção própria
            if name not in prod:
                raise ProductError
            # Se não houver erros retira o produto e diminui a quantidade
            prod.remove(name)
            total -= 1
        
        # Verifica a categoria do produto
        if categoria == "Beleza":
            # Acessando os dados da respectiva categoria
            prod = CathegoryBeauty.prod_beauty
            total = CathegoryBeauty.total_beauty
            # Verifica se o proudto está em estoque e levanta a exceção própria
            if name not in prod:
                raise ProductError
            # Se não houver erros retira o produto e diminui a quantidade
            prod.remove(name)
            total -= 1
        
        # Verifica a categoria do produto    
        if categoria == "Vestuário":
            # Acessando os dados da respectiva categoria
            prod = CathegoryCloth.prod_cloth
            total = CathegoryCloth.total_cloth
            # Verifica se o proudto está em estoque e levanta a exceção própria
            if name not in prod:
                raise ProductError
            # Se não houver erros retira o produto e diminui a quantidade
            prod.remove(name)
            total -= 1
    

    # Método repor produtos no estoque
    def repor_produto(self, name, categoria):
       # Verifica a categoria do produto
        if categoria == "Tecnologia":
            # Acessando os dados da respectiva categoria
            prod = CathegoryTech.prod_tech
            total = CathegoryTech.total_tech
            # Adiciona o nome do produto na lista e aumenta a quantidade
            prod.append(name)
            total += 1
        
        # Verifica a categoria do produto
        if categoria == "Beleza":
            # Acessando os dados da respectiva categoria
            prod = CathegoryBeauty.prod_beauty
            total = CathegoryBeauty.total_beauty
            # Adiciona o nome do produto na lista e aumenta a quantidade
            prod.append(name)
            total += 1
        
        # Verifica a categoria do produto    
        if categoria == "Vestuário":
            # Acessando os dados da respectiva categoria
            prod = CathegoryCloth.prod_cloth
            total = CathegoryCloth.total_cloth
            # Adiciona o nome do produto na lista e aumenta a quantidade
            prod.append(name)
            total += 1
    
    

tablet = CathegoryTech("Tablet", 1235, 1000.00, Marcas.Amazon)
print(CathegoryTech.prod_tech)
invent = Inventario()
invent.vender_produto("Tablet", "Tecnologia")
print(CathegoryTech.prod_tech)