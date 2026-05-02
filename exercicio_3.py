"""
#### Exercício 3

Receba um número inteiro de um usuário. Se ele for par, imprima "Par". Se não, imprima "Ímpar".

Exemplo:

Digite um número:
10

Par
--------
Digite um número:
1

Ímpar

Dica: Lembre do comando de resto da divisão inteira!
""" 
# Solicita um número inteiro ao usuário
print("Digite um número:")
numero = int(input(""))

# Verifica se é par ou ímpar usando o resto da divisão
if numero % 2 == 0:
    print()
    print("Par")
else:
    print()
    print("Ímpar")
