import random

escolhas = ["pedra","papel","tesoura"]
on=0

while(on<2):
    cpu = random.choice(escolhas)
    print("1-Pedra 2-Papel 3-Tesoura")
    esc=int(input(""))
    
    if(cpu=="pedra"):
        if(esc==1):
            clear_console()
            print(" ")
            print("Computador escolheu pedra!")
            print("Empate!")
            print(" ")
            
            print("Deseja jogar novamente? 1-Sim 2-Não")
            on=int(input(""))
            
        if(esc==2):
            print(" ")
            print("Computador escolheu pedra!")
            print("Ganhou!")
            print(" ")
                        
            print("Deseja jogar novamente? 1-Sim 2-Não")
            on=int(input(""))
            
        if(esc==3):
            print(" ")
            print("Computador escolheu pedra!")
            print("Perdeu!")
            print(" ")
                        
            print("Deseja jogar novamente? 1-Sim 2-Não")
            on=int(input(""))
            
            
    if(cpu=="papel"):
        if(esc==1):
            print(" ")
            print("Computador escolheu papel!")
            print("Perdeu!")
            print(" ")
                        
            print("Deseja jogar novamente? 1-Sim 2-Não")
            on=int(input(""))
            
        if(esc==2):
            print(" ")
            print("Computador escolheu papel!")
            print("Empate!")
            print(" ")
                        
            print("Deseja jogar novamente? 1-Sim 2-Não")
            on=int(input(""))
            
        if(esc==3):
            print(" ")
            print("Computador escolheu papel!")
            print("Ganhou!")
            print(" ")
                        
            print("Deseja jogar novamente? 1-Sim 2-Não")
            on=int(input(""))
            
            
    if(cpu=="tesoura"):
        if(esc==1):
            print(" ")
            print("Computador escolheu tesoura!")
            print("Ganhou!")
            print(" ")
                        
            print("Deseja jogar novamente? 1-Sim 2-Não")
            on=int(input(""))
            
        if(esc==2):
            print(" ")
            print("Computador escolheu tesoura!")
            print("Perdeu!")
            print(" ")
                        
            print("Deseja jogar novamente? 1-Sim 2-Não")
            on=int(input(""))
            
        if(esc==3):
            print(" ")
            print("Computador escolheu tesoura!")
            print("Empate!")
            print(" ")
                        
            print("Deseja jogar novamente? 1-Sim 2-Não")
            on=int(input(""))
            
    
            
