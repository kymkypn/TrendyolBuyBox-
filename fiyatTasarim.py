import tkinter as tk
from tkinter import *


def trendyol():
    print("Trendyol Geldi")


def hepsiBurada():
    print("hepsiburada geldi")


def gittiGidiyor():
    print("gittigidiyor geldi")


def n11():
    print("n11 geldi")


def temizle():
    print("Temizle Geldi")
    sagBolge.delete("1.0", tk.END)


def cik():
    anaPencere.destroy()



anaPencere=tk.Tk()
anaPencere.geometry("760x440")
anaPencere.title("Pazar Yeri Fiyatları")
anaPencere.iconbitmap(r'C:\Users\pc\Desktop\den\venv\icon.ico')

sagBolge=Text(anaPencere)
sagBolge.grid(column=0,row=0,padx=5,pady=5)

solDugmeler=Frame(anaPencere)
solDugmeler.grid()

trenyolDugme=Button(solDugmeler,command=trendyol,text="Trendyol",height=1,width=15)
trenyolDugme.grid(column=1,row=1,padx=5,pady=5)

hepsiBuradaDugme=Button(solDugmeler,command=hepsiBurada,text="Hepsi Burada",height=1,width=15)
hepsiBuradaDugme.grid(column=2,row=1,padx=5,pady=5)

n11Dugme=Button(solDugmeler,command=n11,text="N11",height=1,width=15)
n11Dugme.grid(column=3,row=1,padx=5,pady=5)

gittiGidiyorDugme=Button(solDugmeler,command=gittiGidiyor,text="Gitti Gidiyor",height=1,width=15)
gittiGidiyorDugme.grid(column=4,row=1,padx=5,pady=5)

temizleDugme=Button(solDugmeler,command=temizle,text="Listeyi Temizle",height=1,width=15)
temizleDugme.grid(column=5,row=1,padx=5,pady=5)

cikDugme=Button(solDugmeler,command=cik,text="Çıkış Yap",height=1,width=15)
cikDugme.grid(column=6,row=1,padx=5,pady=5)







anaPencere.protocol('WM_DELETE_WINDOW',cik)

anaPencere.mainloop()
