from tkinter import *
from parsel import Selector
from openpyxl import load_workbook
import re , requests ,time
import tkinter as tk


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


def cik():
    anaPencere.destroy()



anaPencere=tk.Tk()
anaPencere.geometry("600x300")
anaPencere.title("Pazar Yeri Fiyatları")
anaPencere.iconbitmap(r'C:\Users\pc\Desktop\den\venv\icon.ico')

solDugmeler=Frame(anaPencere)
solDugmeler.grid()

trenyolDugme=Button(solDugmeler,command=trendyol,text="Trendyol",height=1,width=15)
trenyolDugme.grid(padx=10,pady=10)

hepsiBuradaDugme=Button(solDugmeler,command=hepsiBurada,text="Hepsi Burada",height=1,width=15)
hepsiBuradaDugme.grid(padx=10,pady=10)

n11Dugme=Button(solDugmeler,command=n11,text="N11",height=1,width=15)
n11Dugme.grid(padx=10,pady=10)

gittiGidiyorDugme=Button(solDugmeler,command=gittiGidiyor,text="Gitti Gidiyor",height=1,width=15)
gittiGidiyorDugme.grid(padx=10,pady=10)

temizleDugme=Button(solDugmeler,command=temizle,text="Listeyi Temizle",height=1,width=15)
temizleDugme.grid(padx=10,pady=10)

cikDugme=Button(solDugmeler,command=cik,text="Çıkış Yap",height=1,width=15)
cikDugme.grid(padx=10,pady=10)







anaPencere.protocol('WM_DELETE_WINDOW',cik)

anaPencere.mainloop()