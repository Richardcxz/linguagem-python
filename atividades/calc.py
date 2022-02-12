# -*- coding: utf-8 -*-
prog=0
while prog<1:
    print("")
    print("Escolha qual operação deseja fazer:")
    print("1-Adição")
    print("2-Subtração")
    print("3-Multiplicação")
    print("4-Divisão")
    print("5-Potenciação")
    print("6-Resto")
    print("")
    ent=int(input("Digite qual opção deseja escolher: "))
    if(ent==1):
        a=int(input("Informe o número A: "))
        b=int(input("Informe o número B: "))
        c=a+b
        print("A soma dos dois números é: {0}".format(c))
    if(ent==2):
        a=int(input("Informe o número A: "))
        b=int(input("Informe o número B: "))
        c=a-b
        print("A subtração dos dois números é: {0}".format(c))
    if(ent==3):
        a=int(input("Informe o número A: "))
        b=int(input("Informe o número B: "))
        c=a*b
        print("A multiplicação dos dois números é: {0}".format(c))
    if(ent==4):
        a=int(input("Informe o número A: "))
        b=int(input("Informe o número B: "))
        c=a/b
        print("A divisão dos dois números é: {0}".format(c))
    if(ent==5):
        a=int(input("Informe o número A: "))
        b=int(input("Informe o número B: "))
        c=pow(a,b)
        print("A potenciação dos dois números é: {0}".format(c))
    if(ent==6):
        a=int(input("Informe o número A: "))
        b=int(input("Informe o número B: "))
        c=a%b
        print("O resto dos dois números é: {0}".format(c))
        
    print("")
    print("Deseja realizar outra operação?")
    prog=int(input("0-Sim 1-Não = "))