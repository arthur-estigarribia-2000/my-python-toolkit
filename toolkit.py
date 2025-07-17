# Observação: este código contém trechos gerados por IA, mas devidamente revisados por mim.

def sequencia(inicio, fim, passo):
    """Gera uma sequência de números com um passo específico."""

    if not isinstance(inicio, (int, float)) or not isinstance(fim, (int, float)) or not isinstance(passo, (int, float)) or passo == 0:
        raise ValueError("Valores inválidos.")
    
    sequencia = []

    if inicio < fim:
        while inicio <= fim:
            sequencia.append(round(inicio, 10))
            inicio += passo
    else:
        while inicio >= fim:
            sequencia.append(round(inicio, 10))
            inicio += passo
    
    return sequencia

def interpolacao(inicio, fim, meios):
    """Realiza a interpolação linear entre dois números com um número específico de meios."""

    if not isinstance(inicio, (int, float)) or not isinstance(fim, (int, float)) or not isinstance(meios, int) or meios < 1:
        raise ValueError("Valores inválidos.")
    
    passo = (fim - inicio) / (meios + 1)

    return [round(inicio + i * passo, 10) for i in range(1, meios + 1)]

def estatisticas(lista):
    """Calcula as principais medidas estatísticas de uma lista de números."""

    elementos = len(lista)

    if not isinstance(lista, list):
        raise ValueError("Lista inválida.")

    max = lista[0]
    min = lista[0]
    soma = 0
    somaquad = 0

    for i in lista:
        if not isinstance(i, (int, float)):
            raise ValueError("Elementos inválidos.")
        
        soma += i
        somaquad += i ** 2

        if i > max:
            max = i
        
        if i < min:
            min = i

    resultados = {
        "quantidade": elementos,
        "soma": soma,
        "media": soma / elementos if elementos > 0 else float('nan'),
        "variancia": somaquad / elementos if elementos > 0 else float('nan'),
        "maximo": max if elementos > 0 else float('nan'),
        "minimo": min if elementos > 0 else float('nan'),
    }

    for i in resultados:
        resultados[i] = round(resultados[i], 10) if isinstance(resultados[i], float) else resultados[i]
    
    return resultados

def base_numerica(numero, base):
    """Converte um número para uma base específica."""

    if not isinstance(numero, (int, float)) or not isinstance(base, int) or base < 2:
        raise ValueError("Valores inválidos.")
    
    if isinstance(numero, float):
        numero = int(numero)

    if numero == 0:
        return "0"

    resultado = ""
    negativo = numero < 0
    numero = abs(numero)

    while numero > 0:
        resultado = str(numero % base) + resultado
        numero //= base
    
    return "-" + resultado if negativo else resultado