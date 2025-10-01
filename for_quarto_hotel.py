qtde_pessoas = int(input('Digite a quantidade de pessoas: '))
quarto = []
cpf_valido = False

for i in range (qtde_pessoas):
    print('Para o hospede {} Informe os dados a seguir: '.format(i))
    nome = input('Digite nome do hospede: ')
    cpf = input('Dite o cpf: ')
    cpf_valido = len(cpf) == 11 and cpf.isnumeric()
      
    while cpf_valido == False :
        print('O CPF foi digitado incorretamente, preencha novamente o ultimo hospede: ')
        nome = input('Digite o nome: ')
        cpf = input('Dite o cpf: ')
        cpf_valido = len(cpf) == 11 and cpf.isnumeric()
    else:
        hospede = [nome, cpf]
        quarto.append(hospede)
        
print(f'Os dados informados para o quarto foram: {quarto}')
print('Fim do programa')

