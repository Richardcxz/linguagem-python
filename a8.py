import functools

say=print
say("hello world")

add= lambda x,y,z:x+y+z

print(add(5,10,15))

nomecompleto = lambda nome,sobrenome: nome + " " + sobrenome

print(nomecompleto("John","Wick"))
print(" ")

lista = ["panetone","tomate","uva","cereja","champanhe"]

lista.sort()

for i in lista:
    print(i)

print(" ")

palavra = ["W","I","C","K"]
pala = functools.reduce(lambda x,y:x+y,palavra)
print(pala)

