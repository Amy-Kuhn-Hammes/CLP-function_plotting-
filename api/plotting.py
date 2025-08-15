#Importando as bibliotecas necessárias
import matplotlib.pyplot as plt
import numpy as np
import base64
import io

#Gera a imagem do gráfico
#Recebe uma lista de funções, o valor mínimo e máximo do domínio, e retorna a imagem codificada em base64

def generateImg(funcs, min, max):
    fig, ax = plt.subplots()

    preparedfuncs = map(prepareFunc, funcs)
    
    for func in preparedfuncs:
        addFunc(func, min, max, ax)


    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    #plt.show()
    return base64.b64encode(buf.read())  

#Adiciona uma função ao gráfico
#Recebe uma função matemática em formato de string, o valor mínimo e máximo do domínio, e os eixos do gráfico

def addFunc(func, min, max, ax):
    x = np.arange(min, max, 0.01)
    y = eval(func)
    ax.plot(x, y)

#Prepara a função para ser avaliada pelo Python, substituindo sintaxe matemática.
#Recebe uma função matemática em formato de string e retorna uma string preparada para avaliação com numpy

def prepareFunc(func):
    func = func.replace('sin(x)', 'np.sin(x)')
    func = func.replace('cos(x)', 'np.cos(x)')
    func = func.replace('^', '**')
    return func