import tkinter as tk
import random as rnd
import time as tm
sayi = rnd.randrange(1,201)
health = 5
def sorgula():
    global health
    health-=1
    can.config(text="Kalan Can Sayınız :   " + str(health))
    gelen = sayi_kutusu.get()
    test = gelen.isdigit()
    if health==1:
        can.config(bg="red", fg="white")
    if health==0:
        can.config(text="Game Over :(")
        sayi_butonu.destroy()
        pencere.after(1000, lambda: pencere.destroy())
    else:
        if test==False:
            sonuc.config(text="ERROR. \n (Please Enter a Numeric Value.)")
        else:
            if gelen == "":
                sonuc.config(text="Can't be null.")
            else:
                if int(gelen) > 200 or int(gelen) < 0:
                    sonuc.config(text="Enter a Number Between 1 and 200")
                else:
                    if int(gelen) == int(sayi):
                        sonuc.config(text="Congratulations!!")
                        pencere.after(1000, lambda: pencere.destroy())
                    elif int(gelen) > int(sayi):
                        sonuc.config(text="You guessed too high!")
                    elif int(gelen) < int(sayi):
                        sonuc.config(text="You Guessed too small!")
pencere = tk.Tk()
pencere.geometry("400x350")
pencere.title("Sayı Tahmin Oyunu")
danger=tk.Label(pencere)
danger.config(text="Enter a Number Between 1 and 200 \n (You have a 5 health)",font = ('Comic Sans MS',15))
danger.pack()
danger.place(x=35,y=10)
sayi_kutusu=tk.Entry(pencere, bd=10, bg="white", font=("Comic Sans",15), width=29)
sayi_kutusu.pack()
sayi_kutusu.place(x=35,y=90)
sayi_butonu=tk.Button(text="Sorgula", command=sorgula, activebackground="Red",font = ('Comic Sans MS',15))
sayi_butonu.pack()
sayi_butonu.place(x=130,y=140)
sonuc=tk.Label(pencere)
sonuc.config(text="Sonucunuz burada yazacak",font = ('Comic Sans MS',15))
sonuc.pack()
sonuc.place(x=50,y=190)
can=tk.Label(pencere)
can.pack()
can.place(x=50,y=260)
can.config(text="Kalan Can Sayınız :   " + str(health), font = ('Comic Sans MS',15))
input = sayi_kutusu.get()
pencere.title("Sayı Bulma Oyunu")
pencere.mainloop()