import tkinter as tk
import random as rnd
import time as tm
sayi = rnd.randrange(1,201)
def sorgula():
    gelen = sayi_kutusu.get()
    test = gelen.isdigit()
    if test==False:
        sonuc.config(text="ERROR. (Please Enter a Numeric Value.)")
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
pencere.geometry("300x300")
pencere.title("Sayı Tahmin Oyunu")
sayi_kutusu=tk.Entry(pencere, bd=10, bg="white", font=("Comic Sans",15))
sayi_kutusu.pack()
sayi_kutusu.place(x=35,y=50)
sayi_butonu=tk.Button(text="Sorgula", command=sorgula, activebackground="Red")
sayi_butonu.pack()
sayi_butonu.place(x=130,y=100)
sonuc=tk.Label(pencere)
sonuc.config(text="Sonucunuz burada yazacak")
sonuc.pack()
sonuc.place(x=50,y=150)

input = sayi_kutusu.get()
pencere.title("Sayı Bulma Oyunu")
pencere.mainloop()