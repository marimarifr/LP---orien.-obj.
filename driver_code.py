from product import Produto, Marcas
from Inventario import CathegoryBeauty, CathegoryCloth, CathegoryTech, Inventario

tablet = CathegoryTech("Tablet", 1235, 1000.00, Marcas.Amazon)
batom = CathegoryBeauty("Batom", 2455, 55.26, Marcas.Avon)
blusa = CathegoryCloth("Blusa", 6598, 25.69,Marcas.Renner)
jaqueta = CathegoryCloth("Jaqueta", 3357, 152.02,Marcas.Renner)

invent = Inventario()
print(invent.get_info())

print(CathegoryCloth.prod_cloth)
print(CathegoryBeauty.prod_beauty)
print(CathegoryTech.prod_tech)

#Testando venda de produtos
invent.vender_produto("Jaqueta", "Vestuário")
print(invent.get_info())


#Testando reposição de produtos
invent.repor_produto("Tablet", "Tecnologia")
invent.repor_produto("Tablet", "Tecnologia")
print(invent.get_info())

# Exemplo de erro
invent.vender_produto("Blusa", "Beleza")