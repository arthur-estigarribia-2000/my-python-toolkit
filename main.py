# Observação: este código contém trechos gerados por IA, mas devidamente revisados por mim.

import date
import calculator
import toolkit
import equacoes

coeficientes = []

for coeficiente in toolkit.sequencia(1, 3, 1):
    entrada = input(f"Digite um número real para calcular operações com o coeficiente {coeficiente}: ")
    coeficiente = round(float(entrada), 10)

    coeficientes.append(coeficiente)

polinomio = equacoes.Polinomio(coeficientes=coeficientes)

print(f"Grau do polinômio: {polinomio.grau()}")

try:
    print(f"Raízes do polinômio: {polinomio.raizes()}")
except ValueError as e:
    print(f"Erro ao calcular as raízes do polinômio: {e}")