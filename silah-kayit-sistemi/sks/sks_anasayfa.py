from tkinter import*
from tkinter import messagebox
import datetime
anasayfa=Tk()
anasayfa.title("Silah Kayıt Sistemi")
anasayfa.geometry("1000x600+200+50")
anasayfa.resizable(FALSE,FALSE)
class header():
    baslik=Label(
        anasayfa,
        text="Silah Kayıt Sistemi",
        fg="orangered",
        font=("Arial", "20")
    )
    baslik.place(relx=0.10, rely=0.10, anchor=W)
    anlik=datetime.datetime.now()
    tarihsaat=Label(
        anasayfa,
        text=anlik,
        font=("Arial", "10")
    )
    tarihsaat.place(relx=0.70, rely=0.10, anchor=W)
def gecis1():
    import sks_yenikayit
def gecis2():
    import sks_kayitguncelle
def gecis3():
    import sks_kayitkontrol
def gecis4():
    import sks_kayitsil
sks_yenikayit=Button(
    anasayfa,
    text="Yeni Kayıt",
    width="35",
    height="5",
    bg="darkslategrey",
    fg="white",
    font=("Arial"),
    bd=0,
    command=(gecis1)
)
sks_yenikayit.place(relx=0.10, rely=0.3, anchor=W)
sks_kayitguncelle=Button(
    anasayfa,
    text="Kayıt Güncelle",
    width="35",
    height="5",
    bg="darkslategrey",
    fg="white",
    font=("Arial"),
    bd=0,
    command=(gecis2)
)
sks_kayitguncelle.place(relx=0.54, rely=0.3, anchor=W)
sks_kayitkontrol=Button(
    anasayfa,
    text="Kayıt Kontrol",
    width="35",
    height="5",
    bg="darkslategrey",
    fg="white",
    font=("Arial"),
    bd=0,
    command=(gecis3)
)
sks_kayitkontrol.place(relx=0.10, rely= 0.60, anchor=W)
sks_kayitsil=Button(
    anasayfa,
    text="Kayıt Sil",
    width="35",
    height="5",
    bg="darkslategrey",
    fg="white",
    font=("Arial"),
    bd=0,
    command=(gecis4)
)
sks_kayitsil.place(relx=0.54, rely=0.60, anchor=W)
def cikis_mesaj():
    mesaj=messagebox.askquestion("İşlem Onayı", "Çıkış yapmak istiyor musun?")
    if mesaj=="yes":
        quit()
    else:
        pass
sks_cikis=Button(
    anasayfa,
    text="Çıkış",
    width="10",
    height="1",
    bg="brown",
    fg="white",
    font=("Arial"),
    bd=0,
    command=(cikis_mesaj),
)
sks_cikis.place(relx=0.76, rely=0.80, anchor=W)
class footer():
    footer_not=Label(
        anasayfa,
        text="Silah Kayıt Sistemi © 2020",
        font=("Arial", "12")
    )
    footer_not.place(relx=0.38, rely=0.90, anchor=W)
mainloop()