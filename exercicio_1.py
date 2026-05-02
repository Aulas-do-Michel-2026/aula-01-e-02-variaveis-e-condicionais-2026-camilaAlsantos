"""
#### Exercício 1

Receba três notas (números decimais) de um aluno e imprima a média.

Exemplo:

Digite a primeira nota:
8.5
Digite a segunda nota:
7.0
Digite a terceira nota:
9.0

Resposta:
Média: 8.17

Dica: Use inputs para receber os dados! 
Lembre de converter ele para o tipo necessário!
"""
print("Digite a primeira nota:")
nota1 = float(input())

print("Digite a segunda nota:")
nota2 = float(input())

print("Digite a terceira nota:")
nota3 = float(input())

media = (nota1 + nota2 + nota3) / 3

print("Resposta:")
print(f"Média:{media:.2f}")

