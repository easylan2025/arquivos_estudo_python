contador = 0

while True:
    tecla = input('Pressione Enter para girar o dado: ')
    if tecla == '':
        contador += 1
        dado = set()

        for i in range(1, 7):
            dado.add(f'Lado {i}-{contador}')

        print('Dado girando... girando...')
        lado_sorteado = list(dado)[0]   
        print('Saiu:', lado_sorteado.split('-')[0])  
    else:
        print('O programa acabou')
        break
