nome = input('Qual o seu nome? ')
print(f'O seu nome é {nome}')

# Se colocarmos = na variável o sistema irá mostrar o nome
# da variável + o valor que está dentro dela
print(f'O seu nome é {nome=}')


# Deste modo a leitura dos dados estão em str e o calculo não será
# exato pois ele irá concatenar em vez de somar os números.
num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')
print(f'A soma dos números é: {num1 + num2}')

# Para que seja efetuada a soma é precisa fazer a coersão da função
# porém desta forma se o usuário digitar uma letra o código irá dar erro
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
print(f'A soma dos números é: {num1 + num2}')

# Para que não de erro deverá ser feita a checagem de converção de tipo 
# da variável onde o usuário digitou

num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

int_num1 = int(num1)
int_num2 = int(num2)

print(f'A soma dos números é: {int_num1 + int_num2}')