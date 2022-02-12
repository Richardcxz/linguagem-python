import random

#random.seed(1)
num= random.randint(1,200)
print(num)

#lista[1,2,3,4,5]
#random.choice(lista)
print("")

a=5
b=0

try:
    print(a/b)
    
except:
    print("Division by 0 is not permitted.")
    
z= input("Insira um texto: ")

print("Texto inserido: {0}".format(z))