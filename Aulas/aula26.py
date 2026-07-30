# Formatação básica de Strings
# s - string
# d - int
# f - float
# .<número de dígitos>f
# x ou X - Hexadecimal
# (Caractere)(><^)(quantidade)
# > - Esquerda
# < - Direita
# ^ - Centro
# = - Força o número a aparecer antes do zero
# Sinal - + ou -
# Ex.: 0>100,.1f
# conversion flags - !r !s !az

varialvel = 'ABC'

print(f'{varialvel}')
print(f'{varialvel: >10}')
print(f'{varialvel: <10}.')
print(f'{varialvel: ^10}.')
print(f'{varialvel:0^10}.')
print(f'{varialvel:$^10}.')
print(f'{1000.2582439750983475}')
print(f'{1000.2582439750983475:.2f}')
print(f'{1000.2582439750983475:+.2f}')
print(f'{1000.2582439750983475:0>+10.2f}')
print(f'{1000.2582439750983475:0=+10.2f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{varialvel!r}')