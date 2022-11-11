import pandas as pd

def normalizar_bandeira(titulo):
    if titulo in ['BRANCA', 'IPIRANGA', 'RAIZEN']:
        return titulo
    elif titulo == 'PETROBRAS DISTRIBUIDORA S.A.':
        return 'PETROBRAS'
    else:
        return 'OUTRAS'

# função para retornar um dataframe preparado para uso
def preparar_dataframe(qtd_linhas=5000):

    # ler os dados do arquivo CSV
    df = pd.read_csv("ge-cv-2015-2020.csv.bz2",
                     dtype={'regiao': 'category', 'uf': 'category', 
                            'municipio': 'category', 'bairro': 'category',
                            'produto': 'category', 'imputado': 'category',
                            'venda': 'float32', 'compra': 'float32',
                            'ano': 'uint16', 'mes': 'uint8'})

    # limitar a quantidade de linhas
    if qtd_linhas:
        df = df.sample(n=qtd_linhas, random_state=42)
    
    # criar coluna ano/mês da coleta
    df['ams'] = df['ano'].astype('int') * 100 + df['mes'].astype('int')
    
    # criar coluna data da coleta
    df['data'] = pd.to_datetime(df['ams'], format='%Y%m')

    # criar colunas lucro e %lucro
    df['lucro'] = round(df['venda'] - df['compra'], 3)
    df['plucro'] = round((df['venda'] / df['compra'] - 1) * 100, 2)

    # normalizar bandeira do posto
    df['bandeira'] = df['bandeira'].apply(normalizar_bandeira)

    return df


'''
def titulo(coluna):
    
    COLUNAS = {
        'regiao': 'Região',
        'uf': 'UF',
        'municipio': 'municipio',
        'bairro': 'bairro',
        'produto': 'produto',
        'venda': '',
        'compra': '',
        'ano': '',
        'mes': '',
        'bandeira': '',
        'revenda': '',
        'imputado': '',
        'ams': '',
        'lucro': '',
        'plucro': ''
    }
    
    return COLUNAS[coluna]
'''
