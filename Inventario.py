from product import Produto

class CathegoryTech(Produto):
    # Variáveis de classe para manter o total de produtos de tecnologia e uma lista de produtos de tecnologia
    total_tech = 0
    prod_tech = []

    
    def __init__(self, name, barcode, preco, marca):
        # Chamando o inicializador da classe Produto com os argumentos fornecidos
        super().__init__(name, barcode, preco, marca, categoria = "Tecnologia")
        # Incrementando o total e a ista de produtos de tecnologia
        CathegoryTech.total_tech += 1
        CathegoryTech.prod_tech.append(self.name)


class CathegoryBeauty(Produto):
    # Variáveis de classe para manter o total de produtos de beleza e uma lista de produtos de beleza
    total_beauty = 0
    prod_beauty = []

    def __init__(self, name, barcode, preco, marca):
        # Chamando o inicializador da classe Produto com os argumentos fornecidos
        super().__init__(name, barcode, preco, marca, categoria = "Beleza")
        # Incrementando o total de produtos de beleza
        CathegoryBeauty.total_beauty += 1
        CathegoryBeauty.prod_beauty.append(self.name)


class CathegoryCloth(Produto):
    # Variáveis de classe para manter o total de produtos de vestuário e uma lista de produtos de vestuário
    total_cloth = 0
    prod_cloth = []

    def __init__(self, name, barcode, preco, marca):
        # Chamando o inicializador da classe Produto com os argumentos fornecidos
        super().__init__(name, barcode, preco, marca, categoria = "Vestuário")
        # Incrementando o total de produtos de vestuário
        CathegoryCloth.total_cloth += 1
        CathegoryCloth.prod_cloth.append(self.name)

# Definindo uma classe Inventario que herda de CathegoryBeauty, CathegoryCloth, CathegoryTech
class Inventario(CathegoryBeauty, CathegoryCloth, CathegoryTech):
    
    def __init__(self, tech = [], beauty = [], cloth = []):
        # Inicializando as listas de produtos para cada categoria (tecnologia, beleza, vestuário)
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
    def repor_produto(self, name, categoria, quantidade):
        # Verifica a categoria do produto
        if categoria == 'tech':
            # Remove a quantidade de produtos da categoria 'tech'
            self.tech = self.tech[quantidade:]
            # Atualiza o total de produtos de tecnologia vendidos
            CathegoryTech.total_tech += quantidade
        
        elif categoria == 'beauty':
            # Remove a quantidade de produtos da categoria 'beauty'
            self.beauty = self.beauty[quantidade:]
            # Atualiza o total de produtos de beleza vendidos
            CathegoryBeauty.total_beauty += quantidade
    
        elif categoria == 'cloth':
            # Remove a quantidade de produtos da categoria 'cloth'
            self.cloth = self.cloth[quantidade:]
            # Atualiza o total de produtos de vestuário vendidos
            CathegoryCloth.total_cloth += quantidade

