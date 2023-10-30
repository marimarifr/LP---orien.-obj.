from product import Produto, Marcas
from Inventario import CathegoryBeauty, CathegoryCloth, CathegoryTech, Inventario

tablet = CathegoryTech("Tablet", 1235, 1000.00, Marcas.Amazon)
batom = CathegoryBeauty("Batom", 2455, 55.26, Marcas.Avon)
blusa = CathegoryCloth("Blusa", 6598, 25.69,Marcas.Renner)
jaqueta = CathegoryCloth("Jaqueta", 3357, 152.02,Marcas.Renner)

invent = Inventario()
#print(invent.get_info())
#invent.repor_produto(blusa, 'cloth', 1)
#print(invent.get_info())
#print(invent.get_info())

invent.vender_produto(tablet, 'tech', 1)