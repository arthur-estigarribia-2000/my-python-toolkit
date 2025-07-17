# Observação: este código contém trechos gerados por IA, mas devidamente revisados por mim.

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
    
        return raizes