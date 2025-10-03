'''produtos = ['doce de leite','canjica','quentão','pipoca']
quantidade = [100,185,212,7742]
for i, produto in enumerate(produtos):
    print(produto, quantidade[i]) '''

produtos = ['coca', 'pepsi','guarana','fanta','sukita','heineken', 'brahma', 'malzbier', 'itaipava', 'antartica', 'glacial', 'stella']
estoque = [1200,300,800,1500,1900,400,20,23,70,90,1100,19 ]
nivel_minimo = 50

for i, estoque in enumerate(estoque):
    if estoque < nivel_minimo:
        print('O estoque mínimo do produto: {} foi atingido, o estoque atual é: {}'. format(produtos[i], estoque ))

print('fim do programa')


'''meta= 10000
vendas= [
    ['marcelo', 99998],
    ['joão', 15000],
    ['pedro', 7000],
    ['gustavo', 85000]
]

for i, venda in enumerate(vendas) :
    if vendas[i][1] > meta:
        print(vendas[i])
'''

'''fabricas = ['Marcelo industries', 'china in box', 'marvel', 'ifood']
nivel_minimo = 50
estoque = [
    [225,322,7457,11,685,3249,854,33,7861],
    [325,422,8457,211,685,3249,854,33,7862],
    [425,5227,97,311,685,3249,854,33,7863],
    [525,622,10457,41,685,3249,854,33,20]
]

for i, estoque_fabrica in enumerate(estoque):
    fabrica = fabricas[i]
       
    for j, qtd in enumerate(estoque_fabrica, start= 1):
        if qtd < nivel_minimo:
            print('A Fabrica: {}, possui o item: {} com estoque atual: {}'.format(fabrica, j, qtd))
'''

meta = 1000
bateu_meta =[]
funcionarios =0
maior_venda_nome=None
maior_venda=0

vendas = [
    ['joao', 150],
    ['marcelo', 90000],
    ['pedro', 700],
    ['jorge', 9007],
    ['shirley', 20000]
]

for venda in vendas:
    funcionarios +=1
    if venda[1] > meta:
        bateu_meta.append(venda)
        
    if venda[1] > maior_venda:
        maior_venda_nome = venda[0]
        maior_venda = venda[1]

print("porcentagem {:.2%}".format(len(bateu_meta) / funcionarios), bateu_meta)
print("O maior vendedor foi: {} {}".format(maior_venda_nome, maior_venda))











