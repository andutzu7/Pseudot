import sys
from operator import itemgetter

prev_index = None
value_list = []
"""
Pasii urmati:
    - Parcurgem informatia obtinuta in urma mapperului (informatie trecuta prin procesul de combining/sorting)
    - Salvam in lista value_list toate valorile din ambele matrici care au aceiasi cheie, sub forma de tuple
    care contin indexul si valoarea care se gaseste la o anumita cheie
    - Calculam suma produselor elementelor cu aceiasi cheie(partea efectiva de calcul a matricii)
    - Pentru fiecare index din matricea reuzultat, afisam valoarea obtinuta.
"""
for line in sys.stdin:
    key,matrix_index,index, value = line.rstrip().split(" ")
    index, value = map(int,[index,value])
    if key == prev_index:
        value_list.append((index,value))
    else:
        if prev_index:
            value_list = sorted(value_list,key=itemgetter(0))
            i = 0
            result = 0
            while i < len(value_list) - 1:
                # Daca doua valori din lista au acelasi index inseamna ca acestea sunt termeni ai
                # corespondenti ai ecuatiei(pt M indexul j reprezinta nr coloanei
                # curente, pt N indexul j reprezinta nr liniei curente)
                if value_list[i][0] == value_list[i + 1][0]:
                    result += value_list[i][1]*value_list[i + 1][1]
                    i += 2
                else:
                    i += 1
            print(prev_index,str(result))
        prev_index = key
        value_list = [(index,value)]

# Repetam aceiasi pasi pentru ultima cheie
if  key == prev_index:
    value_list = sorted(value_list,key=itemgetter(0))
    i = 0
    result = 0
    while i < len(value_list) - 1:
        if value_list[i][0] == value_list[i + 1][0]:
            result += value_list[i][1]*value_list[i + 1][1]
            i += 2
        else:
            i += 1
    print(prev_index,str(result))
