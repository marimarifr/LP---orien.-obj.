from product import Produto

# Definindo uma classe CathegoryTech que herda de Produto
class CathegoryTech(Produto):
    # Variáveis de classe para manter o total de produtos de tecnologia e uma lista de produtos de tecnologia
    total_tech = 0
    prod_tech = []

    
    def __init__(self, name, barcode, preco, marca):
        # Chamando o inicializador da classe Produto com os argumentos fornecidos
        super().__init__(name, barcode, preco, marca, categoria = "Tecnologia")
        # Incrementando o total de produtos de tecnologia
        CathegoryTech.total_tech += 1

    # Método para adicionar um produto de tecnologia à lista
    def add_tech(self, name):
        self.prod_tech.append(name)

# Definindo uma classe CathegoryBeauty que herda de Produto
class CathegoryBeauty(Produto):
    # Variáveis de classe para manter o total de produtos de beleza e uma lista de produtos de beleza
    total_beauty = 0
    prod_beauty = []

    
    def __init__(self, name, barcode, preco, marca):
        # Chamando o inicializador da classe Produto com os argumentos fornecidos
        super().__init__(name, barcode, preco, marca, categoria = "Beleza")
        # Incrementando o total de produtos de beleza
        CathegoryBeauty.total_beauty += self.qtd
    
    # Método para adicionar um produto de beleza à lista
    def add_beauty(self, name):
        self.prod_beauty.append(name)

# Definindo uma classe CathegoryCloth que herda de Produto
class CathegoryCloth(Produto):
    # Variáveis de classe para manter o total de produtos de vestuário e uma lista de produtos de vestuário
    total_cloth = 0
    prod_cloth = []

    
    def __init__(self, name, barcode, preco, marca):
        # Chamando o inicializador da classe Produto com os argumentos fornecidos
        super().__init__(name, barcode, preco, marca, categoria = "Vestuário")
        # Incrementando o total de produtos de vestuário
        CathegoryCloth.total_cloth += self.qtd
    
    # Método para adicionar um produto de vestuário à lista
    def add_cloth(self, name):
        self.prod_cloth.append(name)
