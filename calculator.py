# Observação: este código contém trechos gerados por IA, mas devidamente revisados por mim.

import math

class OperacaoBinaria:
    """Classe base para operações binárias."""
    def __init__(self, numero1, numero2, precisao = 10):
        self.numero1 = float(numero1)
        self.numero2 = float(numero2)
        self.precisao = precisao

    def calcula(self):
        """Retorna os resultados das principais operações binárias entre dois números."""
        n1 = self.numero1
        n2 = self.numero2
        precisao = 10  # Precisão para arredondamento

        l = {
            "soma": n1 + n2,
            "subtracao": n1 - n2,
            "multiplicacao": n1 * n2,
            "divisao": n1 / n2 if n2 != 0 else float('inf'),
            "quociente": n1 // n2 if n2 != 0 else float('inf'),
            "resto": n1 % n2 if n2 != 0 else float('inf'),
            "potencia": n1 ** n2 if (n2 > 0) or (n2.is_integer() and n2 != 0 and n2 != 0) else float('nan'),
        }

        for key in l:
            l[key] = str(round(l[key], self.precisao)) if isinstance(l[key], float) else l[key]

        return l
    
    def __str__(self):
        """Retorna uma representação em string das operações binárias."""
        return str(self.calcula())

class OperacaoUnaria:
    """Classe base para operações unárias."""
    def __init__(self, numero, precisao = 10):
        self.numero = float(numero)
        self.precisao = precisao

    def calcula(self):
        """Retorna os resultados das principais operações unárias de um número."""
        n = self.numero

        l = {
            "modulo": abs(n),
            "oposto": -n,
            "inverso": 1 / n if n != 0 else float('inf'),
            "raiz_quadrada": n ** 0.5 if n >= 0 else float('nan'),
            "logaritmo": float('nan') if n <= 0 else math.log(n),
            "fatorial": math.factorial(n) if n >= 0 and n.is_integer() else float('nan'),
            "exp": math.exp(n),
            "log": math.log(n) if n > 0 else float('nan'),
            "log10": math.log10(n) if n > 0 else float('nan'),
            "log2": math.log2(n) if n > 0 else float('nan'),
            "sin": math.sin(n),
            "cos": math.cos(n),
            "tan": math.tan(n),
            "asin": math.asin(n) if -1 <= n <= 1 else float('nan'),
            "acos": math.acos(n) if -1 <= n <= 1 else float('nan'),
            "atan": math.atan(n),
        }

        for key in l:
            l[key] = str(round(l[key], self.precisao)) if isinstance(l[key], float) else l[key]

        return l

    def __str__(self):
        return str(self.calcula())

def inicia():
    entrada1 = input("Digite o primeiro número: ")
    entrada2 = input("Digite o segundo número: ")

    try:
        numero1 = float(entrada1)
        numero2 = float(entrada2)

        resultado_binario = OperacaoBinaria(numero1, numero2).calcula()
        resultado_unario_1 = OperacaoUnaria(numero1).calcula()
        resultado_unario_2 = OperacaoUnaria(numero2).calcula()

        print("Operações binárias:", str(resultado_binario))
        print("Operações unárias do primeiro número:", str(resultado_unario_1))
        print("Operações unárias do segundo número:", str(resultado_unario_2))
    except ValueError as e:
        print(f"Erro: {e}")