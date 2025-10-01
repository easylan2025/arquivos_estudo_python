prudutos = ['armario', 'tv', 'geladeira','microondas','fogao', 'ceular', 'fone', 'furadeira', 'notebook']
estoque = [10, 50, 20, 35, 55, 19, 58, 47, 22]

consulta = str(input('Digite o nome do produto para consultar o estoque: ')).strip().casefold()
i = prudutos.index(consulta)

#outra opção de comparação é if consunta in produtos:

if consulta == prudutos[i]:
    print(f'A quantidade do produto: {consulta} é de {estoque[i]}')
else:
    print('O produto não existe na lista')    

