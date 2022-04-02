import random
from tkinter import *
from os import system


symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789?,.;/:§!%ùµ*£$¨^+=}°)]0à@ç^_è`-|(['{\"#é~&"
password = ""

window = Tk()
window.title("Password Generator")
window.geometry("500x200")
window.configure(bg='#35d49c')

def result(password):
    # label = Label(window, text=f"Votre mot de passe est: {password}").pack()
    lenght = StringVar()
    lenght.set(f"Votre mot de passe est: {password}")
    entry1 = Entry(window, textvariable=lenght, width=64).pack()

def createPassword():
    password = ""
    for letter in range(int(lenght.get())):
        password += random.choice(symbols)
    result(password)

label = Label(window, text="Enter the lenght of the password: ", bg="#54a8f7").pack()
lenght = StringVar()
lenght.set("")
entry1 = Entry(window, textvariable=lenght, width=30, bg="#54a8f7").pack()

bouton = Button(window, text="Valider", command=createPassword, bg="#54a8f7").pack()
bouton = Button(window, text="Quitter", command=window.quit, bg="#54a8f7").pack()

window.mainloop()

label = Label(window, text=f"Votre mot de passe est: {password}", bg="#54a8f7").pack()