from product import Produto


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


class CathegoryBeauty(Produto):
    # Variáveis de classe para manter o total de produtos de beleza e uma lista de produtos de beleza
    total_beauty = 0
    prod_beauty = []

    def __init__(self, name, barcode, preco, marca):
        # Chamando o inicializador da classe Produto com os argumentos fornecidos
        super().__init__(name, barcode, preco, marca, categoria = "Beleza")
        # Incrementando o total de produtos de beleza
        CathegoryBeauty.total_beauty += 1
    
    # Método para adicionar um produto de beleza à lista
    def add_beauty(self, name):
        self.prod_beauty.append(name)


class CathegoryCloth(Produto):
    # Variáveis de classe para manter o total de produtos de vestuário e uma lista de produtos de vestuário
    total_cloth = 0
    prod_cloth = []

    def __init__(self, name, barcode, preco, marca):
        # Chamando o inicializador da classe Produto com os argumentos fornecidos
        super().__init__(name, barcode, preco, marca, categoria = "Vestuário")
        # Incrementando o total de produtos de vestuário
        CathegoryCloth.total_cloth += 1
    
    # Método para adicionar um produto de vestuário à lista
    def add_cloth(self, name):
        self.prod_cloth.append(name)

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
    def vender_produto(self, categoria, quantidade):
        # Verifica a categoria do produto
        if categoria == 'tech':
            # Verifica se há produtos suficientes na categoria 'tech'
            if quantidade <= len(self.tech):
                # Remove a quantidade de produtos vendidos da lista de produtos 'tech'
                self.tech = self.tech[quantidade:]
                # Atualiza o total de produtos de tecnologia vendidos
                CathegoryTech.total_tech -= quantidade
            else:
                # Gera uma exceção se não houver produtos suficientes
                raise Exception(f"Não há produtos suficientes na categoria tecnologia para vender {quantidade} unidades.")
        elif categoria == 'beauty':
            if quantidade <= len(self.beauty):
                self.beauty = self.beauty[quantidade:]
                CathegoryBeauty.total_beauty -= quantidade
            else:
                raise Exception(f"Não há produtos suficientes na categoria beleza para vender {quantidade} unidades.")
        elif categoria == 'cloth':
            if quantidade <= len(self.cloth):
                self.cloth = self.cloth[quantidade:]
                CathegoryCloth.total_cloth -= quantidade
            else:
                raise Exception(f"Não há produtos suficientes na categoria vestuário para vender {quantidade} unidades.")
        else:
            raise Exception("Categoria inválida.")
        
# Método repor produtos no estoque
def repor_produto(self, categoria, quantidade):
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
