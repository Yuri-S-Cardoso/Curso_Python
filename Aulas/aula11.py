nome = 'Yuri Cardos'
altura = 1.70
peso = 95
imc = ... # Ellipsis
imc = peso / (altura * altura)

# f-strings

linha_1 = 'nome tem altura de altura'
print (linha_1)

# Ao colocar o f já habilita a possibilidade de usar variáveis dentro da string
# usando { }
linha_1 = f'{nome} tem altura de altura' 
print (linha_1)

# Formatação de casas decimais de um número float
linha_1 = f'{nome} tem {altura:.2f} de altura' 
print (linha_1)

linha_2 = f'Pesa {peso} quilos e seu IMC é:'
print("Pesa", peso, "quilos e seu IMC é:")

linha_3 = f'{imc:.2f}'
print(linha_3)
