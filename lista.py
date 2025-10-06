pessoas= {'marcelo':'trabalhador, onesto, dedicado',
          'eduardo':'fanfarrão, amigo, careca',
          'patrick':'atrazado, amigo, careca'}

pessoas.update({'amanda':'sumida, estranha, mulher'})
pessoas['jose']= 'nunca vi'

mulher= pessoas.get('amanda')

pessoas['marcelo'] +='lindo'
print(pessoas['marcelo'])