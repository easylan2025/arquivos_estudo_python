'''produtos = ['doce de leite','canjica','quentão','pipoca']
quantidade = [100,185,212,7742]
for i, produto in enumerate(produtos):
    print(produto, quantidade[i])
    '''

produtos = ['coca', 'pepsi','guarana','fanta','sukita','heineken', 'brahma', 'malzbier', 'itaipava', 'antartica', 'glacial', 'stella']
estoque = [1200,300,800,1500,1900,400,20,23,70,90,1100,19 ]
nivel_minimo = 50


for i, estoque in enumerate(estoque):
    if estoque < 50:
        print('O estoque mínimo do produto : {} foi atingido, o estoque atual é : {}'. format(produtos[i], estoque ))

print('fim do programa')