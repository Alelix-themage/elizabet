'''
Módulo responsável por ler e escrever arquivos csv
'''

import pandas as pd


def read_csv(arquivo: str):
    
    # Le e retorna o csv convertido
    # args: arquivo
    
    #caminho do arquivo csv
    jogos_da_semana_csv = arquivo

    jogos_semana = pd.read_csv(jogos_da_semana_csv)

    return jogos_semana


df = read_csv("../cache/teste.csv")
print(df)
