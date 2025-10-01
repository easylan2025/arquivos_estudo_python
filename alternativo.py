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
