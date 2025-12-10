# Observação: contém código gerado por IA, mas o arquivo ainda está sendo revisado por mim.

# Dependências do Python

import math

# Modelagem

class Polinomio:
    def __init__(self, coeficientes):
        """Inicializa o polinômio com uma lista de coeficientes."""
        if not isinstance(coeficientes, list) or not all(isinstance(c, (int, float)) for c in coeficientes):
            raise ValueError("Coeficientes devem ser uma lista de números.")
        self.coeficientes = coeficientes

    def grau(self):
        """Retorna o grau do polinômio."""
        return len(self.coeficientes) - 1
    
    def raizes(self):
        """Calcula as raízes de um polinômio."""
        raizes = []

        if self.grau() == 1:
            a = self.coeficientes[0]
            b = self.coeficientes[1]
            
            raiz1 = -b / a if a != 0 else float('inf')

            raizes.append(raiz1)
        elif self.grau() == 2:
            a = self.coeficientes[0]
            b = self.coeficientes[1]
            c = self.coeficientes[2]
    
            delta = b ** 2 - 4 * a * c

            if delta >= 0:
                raiz1 = (-b + delta ** 0.5) / (2 * a) if a != 0 else float('inf')
                raiz2 = (-b - delta ** 0.5) / (2 * a) if a != 0 else float('inf')

                raizes.append(raiz1)
                raizes.append(raiz2)
        else:
            raise ValueError("Polinômio não suportado.")
    
        return 

    def soma(self, outro):
        """Soma dois polinômios."""
        if not isinstance(outro, Polinomio):
            raise ValueError("Tipo inválido.")
        
        grau_maximo = max(self.grau(), outro.grau())
        coeficientes_soma = [0] * (grau_maximo + 1)

        for i in range(grau_maximo + 1):
            coeficiente_self = self.coeficientes[i] if i <= self.grau() else 0
            coeficiente_outro = outro.coeficientes[i] if i <= outro.grau() else 0
            coeficientes_soma[i] = coeficiente_self + coeficiente_outro
        
        return Polinomio(coeficientes_soma)
    
    def produto(self, outro):
        """Calcula o produto de dois polinômios."""
        if not isinstance(outro, Polinomio):
            raise ValueError("Tipo inválido.")
        
        grau_maximo = self.grau() + outro.grau()
        coeficientes_produto = [0] * (grau_maximo + 1)

        for i in range(len(self.coeficientes)):
            for j in range(len(outro.coeficientes)):
                coeficientes_produto[i + j] += self.coeficientes[i] * outro.coeficientes[j]
        
        return Polinomio(coeficientes_produto)
