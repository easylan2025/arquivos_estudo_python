quarto=[]
qtd_hospedes= int(input('Digite hospedes: '))

for i in range (qtd_hospedes):
    nome= input('nome')
    cpf= input('cpf')
    hospede= [nome, cpf]
    quarto.append(hospede)

print (quarto)