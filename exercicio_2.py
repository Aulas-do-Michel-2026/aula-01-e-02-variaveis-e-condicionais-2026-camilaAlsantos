"""
#### Exercício 2

Uma fórmula recomenda 2mg de medicamento por kg de peso do paciente.

Peça o peso de uma pessoa e calcule a dose recomendada.

Exemplo:

Digite o peso do paciente (em kg):
70
#Resposta:
Média: 140 mg
"""
# Solicita o peso do paciente
print("Digite o peso do paciente (em kg):")
peso = float(input())

# Calcula a dose recomendada (2 mg por kg)
dose = peso * 2

# Exibe o resultado
print("#Resposta:")
print(f"Média:{dose:.2f} mg")
