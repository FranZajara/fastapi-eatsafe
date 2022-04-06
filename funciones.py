from sklearn import tree
import pandas as pd
import numpy

#función para calcular el índice metabólico basal
def IMB(sexo,altura,peso, edad):
    if(sexo == "Hombre"):
        return 10*peso + 6.25*altura - 5*edad + 5
    else:
        return 10*peso + 6.25*altura - 5*edad -161

#función para identificar si el paciente posee el trastorno alimenticio de Pica
def Pica(C1, C2):
    if(((C1 == 1) & (C2 == 1)) | ((C1 == 1) & (C2 == 0))):
        return True
    elif((C1 == 0) & (C2 == 1)):
        return False
    else:
        return False

#función para identificar si el paciente posee el trastorno alimenticio de Rumiación
def Rumiacion(C3):
    if(C3 == 1):
        return True
    else:
        return False

#función para identificar si el paciente posee el trastorno alimenticio de Evitación
def Evitacion(C4,C5):
    if((C4 == 1) & (C5 == 1) | (C4 == 0) & (C5 == 1) ):
        return True
    else:
        return False

#función para identificar si el paciente posee el trastorno alimenticio de Anorexia Nerviosa
def Anorexia(C4,C6,C7,C8,C9):
    datos = pd.read_csv('datos_anorexia.csv', sep = ';' , header=0)
    datos = pd.read_csv('datos_anorexia.csv', sep = ';' , header=0)
    datos2  = datos
    res = datos['R'].to_list()
    del(datos2['R'])
    pro = datos2.to_numpy().tolist()
    datos = pd.read_csv('datos_anorexia.csv',header=0)
    classifier = tree.DecisionTreeClassifier()
    classifier.fit(pro,res)
    return classifier.predict(numpy.array([[C4,C6,C7,C8,C9]]))

#función para identificar si el paciente posee el trastorno alimenticio de Bulimia Nerviosa
def Bulimia(C4,C6,C7,C8,C9,C10):
    datos = pd.read_csv('datos_bulimia.csv', sep = ';' , header=0)
    datos = pd.read_csv('datos_bulimia.csv', sep = ';' , header=0)
    datos2  = datos
    res = datos['R1'].to_list()
    del(datos2['R1'])
    pro = datos2.to_numpy().tolist()
    datos = pd.read_csv('datos_bulimia.csv',header=0)
    classifier = tree.DecisionTreeClassifier()
    classifier.fit(pro,res)
    return classifier.predict(numpy.array([[C4,C6,C7,C8,C9,C10]]))

#función para identificar si el paciente posee el trastorno alimenticio de Atracón
def Atracon(C4,C6,C7,C8):
    datos = pd.read_csv('datos_atracon.csv', sep = ';' , header=0)
    datos = pd.read_csv('datos_atracon.csv', sep = ';' , header=0)
    datos2  = datos
    res = datos['R1'].to_list()
    del(datos2['R1'])
    pro = datos2.to_numpy().tolist()
    datos = pd.read_csv('datos_atracon.csv',header=0)
    classifier = tree.DecisionTreeClassifier()
    classifier.fit(pro,res)
    return classifier.predict(numpy.array([[C4,C6,C7,C8]]))


#función para identificar si el paciente posee el Síndrome de ingesta nocturna

def Nocturno(C15):
    if (C15 == 1):
        return True
    else:
        return False



