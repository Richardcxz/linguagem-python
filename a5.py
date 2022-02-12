lista=["morango","melancia","abacate"]

for item in lista:
    print(item)
    
size=len(lista)
print(size)

lista.append("abacaxi")

for item in lista:
    print(item)
    
if "melancia" in lista:
    print("melancia na lista")
    
#del lista[1:]

#ordenar
lista2=[5,4,3,2,1]
lista2.sort()
#lista2.sort(reverse=True)
print(lista2)

lista2.reverse()
print(lista2)