from enum import Enum


class Icone(Enum):
    
    # Cores
    COR_VERMELHO = "\033[31m" #VERMELHO
    COR_VERDE = "\033[32m" #VERDE
    COR_AMARELO = "\033[33m" #AMARELO
    COR_ROXO = "\033[35m" #ROXO
    FIM_COR = "\033[m"
