# Importações
import sys
import os
import numpy as np

# A função realiza a leitura de um arquivo .txt e carrega os dados em uma lista
# retorna os dados no formato numpy.ndarray

def leitura(nome_instancia):
    caminho = r"C:\Users\joser\Documents\3 semestre\Algoritmos em Grafos\datasets"
    caminho = os.path.join(caminho, f"{nome_instancia}.txt")
    with open(caminho, 'r') as f:

        mat = []
        for i in f.readlines():
            mat.append(list(map(int, i.split())))
        
        return np.array(mat)


# A função salva os resultados passados por parametros em um arquivo .txt
# além de exibir na tela no formato nome_instancia qtd_linhas qtd_colunas

def salvaResultado(nome_instancia, qtd_linhas, qtd_colunas):
    with open("resultados.txt", 'a+') as arq:
        arq.write(f'{nome_instancia} {qtd_linhas} {qtd_colunas}\n')
    print(f'{nome_instancia} {qtd_linhas} {qtd_colunas}')
    arq.close()
   

# Função main para chamada das funções 

def main(nome_instancia):
    mat = leitura(nome_instancia)
    qtd_linhas, qtd_colunas = mat.shape
    salvaResultado(nome_instancia, qtd_linhas, qtd_colunas)




# Necessário para executar o programa pelo terminal
if(__name__ == '__main__'):
    main(sys.argv[1])