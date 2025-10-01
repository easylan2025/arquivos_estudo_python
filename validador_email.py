email = input('Digite seu E-mail: ').casefold().strip().replace(' ', '')
email = email.replace(',', '.')

# Verificação de email simples
verificador_email = '@' in email and '.' in email.split('@')[-1]

if verificador_email:
    print('E-mail válido:', email)
else:
    print('E-mail inválido:', email)

cpf = input('Digite o CPF: ').strip().replace('.', '').replace('-', '').replace(' ', '')

# Verificação do CPF
cpf_valido = len(cpf) == 11 and cpf.isnumeric()

if cpf_valido:
    print(cpf, 'Válido')
else:
    print(cpf, 'CPF Inválido')

# Checagem final
if verificador_email and cpf_valido:
    print('Dados corretos:', email, cpf ,)
else:
    print('Algo foi preenchido incorretamente')

