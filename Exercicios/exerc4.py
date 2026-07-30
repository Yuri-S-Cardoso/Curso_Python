# # Exercícios

# Peça ao usuário para digitar seu nome
# Peça ao usuário para digitar sua idade
# se nome e idade forem digitados:
#     Exiba:
#         Seu nome é {nome}
#         Seu nome invertido é {noem invertido}
#         se nome contém (ou não) espaços
#         Seu nome tem {n} letras
#         A primeira letra do seu nome é {letra}
#         A última letra do seu nome é {letra}
# se nada for digitado em nome ou idade:
#     exiba "Desculpe, você deixou campos vazios."

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if nome and idade:

    print('Seu nome é ', nome)
    print('Seu nome invertido é ', nome[::-1])

    if ' ' in nome:
        print('seu nome contém espaços')
    else:
        print('Seu nome NÃO contém espaço')

    print(f'Seu nome tem {len(nome)} letras')
    print('A primeira letra do seu nome é ', nome[0])
    print('A última letra do seu nome é ', nome[-1])

else:
    print("Desculpe, você deixou campos vazios.")