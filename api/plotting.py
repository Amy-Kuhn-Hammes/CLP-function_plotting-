import matplotlib.pyplot as plt
import numpy as np
import base64
import io

def generateImg(funcs, min, max):
    fig, ax = plt.subplots()

    preparedfuncs = map(prepareFunc, funcs)
    
    for func in preparedfuncs:
        addFunc(func, min, max, ax)


    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return base64.b64encode(buf.read())  

    #plt.show()

def addFunc(func, min, max, ax):
    x = np.arange(min, max, 0.01);
    y = eval(func)
    ax.plot(x, y)

def prepareFunc(func):
    func = func.replace('sin(x)', 'np.sin(x)')
    func = func.replace('cos(x)', 'np.cos(x)')
    func = func.replace('^', '**')
    return func