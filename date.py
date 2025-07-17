# Observação: este código contém trechos gerados por IA, mas devidamente revisados por mim.

import datetime

class Data:
    def ano_bissexto(ano):
        """Verifica se um ano é bissexto."""
        if isinstance(ano, int):
            return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
        else:
            raise ValueError("Tipo inválido para o argumento.")

    def dias_no_mes(mes, ano):
        """Retorna o número de dias em um mês específico de um ano."""
        if not isinstance(mes, int) or not isinstance(ano, int):
            raise ValueError("Tipo inválido para o argumento.")
    
        if mes < 1 or mes > 12:
            raise ValueError("Valor inválido para o mês.")
    
        if mes == 2:
            return 29 if Data.ano_bissexto(ano) else 28
        elif mes in [4, 6, 9, 11]:
            return 30
        else:
            return 31
    
    def dias_no_ano(ano):
        """Retorna o número de dias em um ano específico."""
        if not isinstance(ano, int):
            raise ValueError("Tipo inválido para o argumento.")
        return 366 if Data.ano_bissexto(ano) else 365

    def dia_da_semana(dia, mes, ano):
        """Retorna o dia da semana de uma data específica."""
        if not isinstance(dia, int) or not isinstance(mes, int) or not isinstance(ano, int):
            raise ValueError("Tipos inválidos para dia, mês e ano.")
        if not Data.valida(dia, mes, ano):
            raise ValueError("Data inválida.")
        
        # Algoritmo de congruência de Zeller
        if mes < 3:
            mes += 12
            ano -= 1
        k = ano % 100
        j = ano // 100
        f = dia + (13 * (mes + 1)) // 5 + k + (k // 4) + (j // 4) - (2 * j)

        # Ajuste para o dia da semana (0 = sábado, 1 = domingo, ..., 6 = sexta-feira)
        v = f % 7 + 1

        nomes = ["domingo", "segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado"]

        return nomes[v]
    
    def mes_do_ano(mes):
        """Retorna o nome do mês do ano."""
        meses = [
            "janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
        ]

        if not isinstance(mes, int) or mes < 1 or mes > 12:
            raise ValueError("Mês inválido.")
        
        return meses[mes - 1]

    def valida(dia, mes, ano):
        """Valida se a data é válida."""
        if dia < 1 or dia > 31:
            return False
        if mes < 1 or mes > 12:
            return False
        if ano < 1582:
            return False
        if dia > Data.dias_no_mes(mes, ano):
            return False
        else:
            return True

    def __init__(self, dia, mes, ano, correcao = False):
        """Inicializa a classe Data com dia, mês e ano."""
        if not isinstance(dia, int) or not isinstance(mes, int) or not isinstance(ano, int):
            raise ValueError("Tipos inválidos para dia, mês e ano.")
        if ano < 1582:
            raise ValueError("Ano fora do calendário gregoriano (iniciado em 1582).")
        if not Data.valida(self):
            if correcao == True:
                self.dia = self.dia - Data.dias_no_mes(self.mes, self.ano)
                self.mes = (self.mes + 1) % 12
                self.ano = self.ano + (self.mes // 12)
            else:
                raise ValueError("Valores inválidos para data.")
        
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    def __str__(self):
        """Retorna a data no formato yyyy-mm-dd."""
        return f"{self.ano}/{self.mes:02d}/{self.dia:02d}"
    
    def exibe_regional(self):
        """Retorna a data no formato dd/mm/yyyy."""
        return f"{self.dia:02d}/{self.mes:02d}/{self.ano}"

    def exibe_extenso(self):
        """Retorna a data no formato extensivo."""
        return f"{Data.dia_da_semana(self)}, {self.dia:02d} de {Data.nome_do_mes(self)} de {self.ano}"

    def atual():
        """Retorna a data do sistema no formato dd/mm/aaaa."""
        return Data(datetime.datetime.now().day, datetime.datetime.now().month, datetime.datetime.now().year)
    
    def soma(self, dias, meses, anos):
        """Adiciona dias, meses e anos à data atual."""
        if not isinstance(dias, int) or not isinstance(meses, int) or not isinstance(anos, int):
            raise ValueError("Valores inválidos para data.")
        
        return Data(self.ano + anos, self.mes + meses, self.dia + dias, correcao=True)

    def subtrai(self, dias, meses, anos):
        return self.soma(-dias, -meses, -anos)

    def converte(dias):
        """Converte dias em anos, meses e dias com medidas padrão (12 meses de 30 dias)."""
        quantidade_dias = int(dias)
        quantidade_meses = 0
        quantidade_anos = 0

        medida_dias_mes = 30
        medida_meses_ano = 12

        while d >= medida_dias_mes:
            d -= medida_dias_mes
            m += 1

            if m >= medida_meses_ano:
                m -= medida_meses_ano
                a += 1

        return quantidade_anos, quantidade_meses, quantidade_dias

    def diferenca(self, outra):
        """Calcula a diferença em dias entre duas datas."""
        formato = "%d/%m/%Y"

        if not isinstance(outra, Data):
            raise ValueError("A outra data deve ser uma instância da classe Data.")
        
        contador = 0

        while self != outra:
            if self < outra:
                self = self.soma(1, 0, 0)
            else:
                outra = outra.soma(1, 0, 0)
            
            contador += 1

        return Data.converte(contador)

class Hora:
    def __init__(self, hora, minuto, segundo):
        """Inicializa a classe Hora com hora, minuto e segundo."""
        if not isinstance(hora, int) or not isinstance(minuto, int) or not isinstance(segundo, int):
            raise ValueError("Tipos inválidos para hora, minuto e segundo.")
        if hora < 0 or hora > 23:
            raise ValueError("A hora deve estar entre 0 e 23.")
        if minuto < 0 or minuto > 59:
            raise ValueError("O minuto deve estar entre 0 e 59.")
        if segundo < 0 or segundo > 59:
            raise ValueError("O segundo deve estar entre 0 e 59.")

        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo
    
    def __str__(self):
        """Retorna a hora no formato hh:mm:ss."""
        return f"{self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"
    
    def atual():
        """Retorna a hora do sistema no formato hh:mm:ss."""
        return Hora(datetime.datetime.now().hour, datetime.datetime.now().minute, datetime.datetime.now().second)
    
    def converte(segundos):
        """Converte segundos em horas, minutos e segundos."""
        quantidade_segundos = int(segundos)
        quantidade_minutos = quantidade_segundos // 60
        quantidade_horas = quantidade_minutos // 60

        quantidade_segundos %= 60
        quantidade_minutos %= 60

        return quantidade_horas, quantidade_minutos, quantidade_segundos
    
    def soma(self, horas, minutos, segundos):
        """Adiciona horas, minutos e segundos à hora atual."""
        if not isinstance(horas, int) or not isinstance(minutos, int) or not isinstance(segundos, int):
            raise ValueError("Valores inválidos para hora.")
        
        total_segundos = (self.hora * 3600 + self.minuto * 60 + self.segundo +
                          horas * 3600 + minutos * 60 + segundos)
        
        return Hora.converte(total_segundos)
    
    def subtrai(self, horas, minutos, segundos):
        """Subtrai horas, minutos e segundos da hora atual."""
        return self.soma(-horas, -minutos, -segundos)
    
    def diferenca(self, outra, correcao=False):
        """Calcula a diferença entre duas horas."""
        if not isinstance(outra, Hora):
            raise ValueError("Tipo inválido.")
        
        total_segundos_self = self.hora * 3600 + self.minuto * 60 + self.segundo
        total_segundos_outra = outra.hora * 3600 + outra.minuto * 60 + outra.segundo
        
        contador = abs(total_segundos_self - total_segundos_outra)

        seg = contador % 60
        contador //= 60
        min = contador % 60
        contador //= 60
        hora = contador

        if hora > 23:
            if correcao:
                hora = hora % 24
            else:
                raise ValueError("Diferença inválida.")
        else:
            return Hora(hora, min, seg)

def agora():
    """Retorna a data e a hora atuais."""
    return str(Data.atual()) + " " + str(Hora.atual())