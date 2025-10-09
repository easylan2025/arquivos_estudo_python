funcionarios = {}

while True:
    nome = input('Digite o nome do funcionário (ou deixe em branco para terminar): ')
    if nome == '':
        break
    cargo = input('Digite o cargo do funcionário: ')
    funcionarios[nome] = cargo

print("\nFuncionários cadastrados:")
for nome, cargo in funcionarios.items():
    print(f"{nome} - {cargo}")