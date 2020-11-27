from tkinter import*
from tkinter import ttk
import mysql.connector
import datetime
kayitkontrol=Tk()
kayitkontrol.title("Silah Kayıt Sistemi")
kayitkontrol.geometry("1000x600+200+50")
kayitkontrol.resizable(FALSE,FALSE)
class header():
    baslik=Label(
        kayitkontrol,
        text="Silah Kayıt Sistemi",
        fg="orangered",
        font=("Arial", "20")
    )
    baslik.place(relx=0.10, rely=0.10, anchor=W)
    anlik=datetime.datetime.now()
    tarihsaat=Label(
        kayitkontrol,
        text=anlik,
        font=("Arial", "10")
    )
    tarihsaat.place(relx=0.70, rely=0.10, anchor=W)
    islem_basligi=Label(
        kayitkontrol,
        text="Kayıt Kontrol",
        font=("Arial", "15")
    )
    islem_basligi.place(relx=0.10, rely=0.20, anchor=W)
    def anasayfagecis():
        import sks_anasayfa
    anasayfa = Button(
        kayitkontrol,
        text="Anasayfa",
        width=15,
        bg="darkslategrey",
        fg="white",
        bd=0,
        command=(anasayfagecis)
    )
    anasayfa.place(relx=0.75, rely=0.20, anchor=W)
tc_no=Label(
    kayitkontrol,
    text="T.C. No"
)
tc_no.place(relx=0.10, rely=0.30, anchor=W)
tc_no_entry=Entry(
    kayitkontrol,
    bd=1,
    width=35
)
tc_no_entry.place(relx=0.25, rely=0.30, anchor=W)
veritabani=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="silah_kayit_sistemi"
)
def kayit_listele():
    mycursor=veritabani.cursor()
    mycursor.execute("SELECT * FROM sahis_bilgileri WHERE tc_no="+tc_no_entry.get())
    sonuclar=mycursor.fetchall()
    for g in sonuclar:
        kayit_goruntule.insert("", 'end', values=g)
        print(g)
kayit_goruntule=ttk.Treeview(kayitkontrol)
kayit_goruntule['columns']=(
    "sut1", "sut2", "sut3", "sut4", "sut5", "sut6", "sut7", "sut8", "sut9", "sut10",
    "sut11", "sut12", "sut13", "sut14", "sut15", "sut16", "sut17", "sut18", "sut19", "sut20"
)
kayit_goruntule.place(relx=0.10, rely=0.60, anchor=W, width=760, height=300)
kayit_goruntule['show']='headings'
kayit_goruntule.heading("sut1", text="ID")
kayit_goruntule.column("sut1", width=50, minwidth=50)
kayit_goruntule.heading("sut2", text="T.C. No")
kayit_goruntule.heading("sut3", text="Ad")
kayit_goruntule.heading("sut4", text="Soyad")
kayit_goruntule.heading("sut5", text="Doğum Tarihi")
kayit_goruntule.heading("sut6", text="Telefon (+90)")
kayit_goruntule.heading("sut7", text="E-Posta")
kayit_goruntule.heading("sut8", text="Meslek")
kayit_goruntule.heading("sut9", text="İl")
kayit_goruntule.heading("sut10", text="Ev Adres")
kayit_goruntule.heading("sut11", text="İş Adres")
kayit_goruntule.heading("sut12", text="Silah Seri No")
kayit_goruntule.heading("sut13", text="Silah Türü")
kayit_goruntule.heading("sut14", text="Silah Tipi")
kayit_goruntule.heading("sut15", text="Silah Markası")
kayit_goruntule.heading("sut16", text="Silah Modeli")
kayit_goruntule.heading("sut17", text="Silah Kalibre (mm)")
kayit_goruntule.heading("sut18", text="Silah Ağırlığı (gr)")
kayit_goruntule.heading("sut19", text="Silah Uzunluğu (mm)")
kayit_goruntule.heading("sut20", text="Silah Kapasitesi")
xscrollbar=ttk.Scrollbar(kayit_goruntule, orient="horizontal", command=kayit_goruntule.xview)
xscrollbar.pack(side='bottom', fill='x')
kayit_goruntule.configure(xscrollcommand=xscrollbar.set)
yscrollbar=ttk.Scrollbar(kayit_goruntule, orient="vertical", command=kayit_goruntule.yview)
yscrollbar.pack(side='right', fill='y')
kayit_goruntule.configure(yscrollcommand=yscrollbar.set)
ara=Button(
    kayitkontrol,
    text="Ara",
    width=15,
    bg="forestgreen",
    fg="white",
    bd=0,
    command=(kayit_listele)
)
ara.place(relx=0.55, rely=0.30, anchor=W)
class footer():
    footer_not=Label(
        kayitkontrol,
        text="Silah Kayıt Sistemi © 2020",
        font=("Arial", "12")
    )
    footer_not.place(relx=0.38, rely=0.90, anchor=W)
mainloop()