a = 'A'
b = 'B'
c = 1.1

formato = 'a={} b={} c={}'.format(a, b, c)
print(formato)

string = 'a={} b={} c={:.2f}'
formato = string.format(a, b, c)
print(formato)

# usando indice
string = 'b={1} a={0} a={0} a={0} c={2:.2f}'
formato = string.format(a, b, c)
print(formato)

# usando parâmetro nomeado
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
# Tudo o que vier depois de uma parâmetro nomeado, precisa ser nomeado
formato = string.format(
    nome1=a, nome2=b, nome3=c
)
print(formato)