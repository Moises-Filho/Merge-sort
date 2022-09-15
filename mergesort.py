import pandas as pd

def mergesort(lista, inicio = 0, fim = None):
    if fim is None:
        fim = len(lista)
    #se a lista contém mais de um elemento
    if(fim - inicio > 1):
        meio =  (fim + inicio)//2
        # print("inicio: ",inicio," meio: ",meio," fim: ",fim)
        #recursividade
        mergesort(lista, inicio, meio)
        # print("1-inicio: ",inicio," meio: ",meio," fim: ",fim)
        mergesort(lista, meio, fim)
        # print("2-inicio: ",inicio," meio: ",meio," fim: ",fim)
        merge(lista, inicio, meio, fim)

def merge(lista, inicio, meio, fim):
    # Divide o array 
    parte1 = lista[inicio:meio]
    parte2 = lista[meio:fim]
    # print("parte1:",parte1,"parte2", parte2)
    topo1,topo2 = 0,0 # elemento do topo da lista 
    for atual  in range(inicio, fim):
        if topo1 >= len(parte1):
            lista[atual] = parte2[topo2]
            topo2 += 1 
        elif topo2 >= len(parte2):
            lista[atual] = parte1[topo1]
            topo1 += 1
        elif parte1[topo1] < parte2[topo2]:
            lista[atual] = parte1[topo1]
            topo1 += 1
        else:
            lista[atual] = parte2[topo2]
            topo2 += 1 

# data = pd.read_csv("TopAnimatedImDb.csv")
# lista = data['Rating'].tolist()
# lista = data['Year'].tolist()

# data = pd.read_csv("avocado.csv")
# lista = data['ind'].tolist()

#lista = [round(float(i)) for i in lista]
lista = [42,324,534,53,541,23,354,33,245]
mergesort(lista)
print(lista)