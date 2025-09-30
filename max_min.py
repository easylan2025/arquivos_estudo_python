meses = ['jan', 'fev', 'mar', 'abr','maio','jun','jul','ago','set','out','nov','dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

# tambem funciona em vez de usar ano usado abaixo vendas_1sem.extend(vendas_2sem)
ano= vendas_1sem + vendas_2sem

max_vendas = max(ano)
i= ano.index(max_vendas)
min_vendas = min(ano)
j= ano.index(min_vendas)

print(f'O melhor mes de vendas foi: {meses[i]} e com o total de {max_vendas} vendas')
# outro modo: print('o total de vendas foi {} com total de {}'.format(meses[i], max_vendas))

print(f'O pior mes de vendas foi: {meses[j]} e com o total de: {min_vendas} vendas')
faturamento= sum(ano)
print('O Faturamento total foi: ', faturamento)
