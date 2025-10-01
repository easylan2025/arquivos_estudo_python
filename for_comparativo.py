produtos = ['iphone','ipad','macbook','fone']
vendas_2023= [558147,712350,951,2]
vendas_2024= [951642,702349,985,10]

for i, produto in enumerate(produtos):
    #print(produtos, vendas_2023[i], vendas_2024[i])
    resultado =  (vendas_2024[i]/vendas_2023[i])-1
    print('O crescimento da venda do produto: {} foi de: {:.1%}'.format(produto, resultado))