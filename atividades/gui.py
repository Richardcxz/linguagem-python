from tkinter import *

window = Tk()
window.geometry("500x420")
window.title("Primeiro programa")
window.configure(bg='black')

#icon = PhotoImage(file='xx.png')
#window.iconphoto(True,icon)
#photo = PhotoImage(file='')

count = 0

def greetings():
    username= entry.get()
    print("Greetings "+username)

def click():
    global count
    count+=1
    print(count)

button = Button(window,
                text="Clique aqui!",
                command=click,
                font=("Arial",30),
                fg="#00FF00",
                bg="black")
button.pack()

label = Label(window,
              text="BRABO",
              font=("Arial",40,"bold"),
              fg="#00FF00",
              bg="black",
              relief=RAISED,
              #bd=10,
              padx=20,
              pady=20)
label.pack()

entry= Entry(window,
font=("Arial",50))
entry.pack(side=LEFT)

greetings_button = Button(window,text="greetings",command=greetings)
greetings_button.pack(side=RIGHT)


window.mainloop()