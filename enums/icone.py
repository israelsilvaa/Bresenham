from enum import Enum


class Icone(Enum):
    
    # Cores
    COR_VERMELHO = "\033[31m" #VERMELHO 1
    COR_VERDE = "\033[32m" #VERDE 2
    COR_AMARELO = "\033[33m" #AMARELO 3
    COR_ROXO = "\033[35m" #ROXO 4
    FIM_COR = "\033[m"
