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
peso = float(input("Digite o peso do paciente (em kg): "))

# Calcula a dose recomendada (2 mg por kg)
dose = peso * 2

# Exibe o resultado
print(f"Dose recomendada: {dose:.2f} mg")
"""
