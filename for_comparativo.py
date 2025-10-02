#calcula o crescimento de vendas entre anos

produtos = ['iphone','ipad','macbook','fone']
vendas_2023= [558147,712350,951,2]
vendas_2024= [951642,702349,985,10]

for i, produto in enumerate(produtos):
    resultado =  (vendas_2024[i]/vendas_2023[i])-1
    print('O crescimento da venda do produto: {} foi de: {:.1%}'.format(produto, resultado))

''' -outro programa com 2 for lendo lista dentro de lista-
fabricas = ['Marcelo industries', 'china in box', 'marvel', 'ifood']
nivel_minimo = 50
estoque = [
    [225,322,7457,11,685,3249,854,33,7861],
    [325,422,8457,211,685,3249,854,33,7862],
    [425,5227,97,311,685,3249,854,33,7863],
    [525,622,10457,41,685,3249,854,33,11],
]

for i, estoque_fabrica in enumerate(estoque):
    fabrica = fabricas[i]
       
    for j, qtd in enumerate(estoque_fabrica, start= 1):
        if qtd < nivel_minimo:
            print('A Fabrica: {}, possui o item: {} com estoque atual: {}'.format(fabrica, j, qtd))
'''

#mais codigo 
            #mais codigo 