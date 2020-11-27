from tkinter import*
from tkinter import messagebox
import mysql.connector
import datetime
kayitsil=Tk()
kayitsil.title("Silah Kayıt Sistemi")
kayitsil.geometry("1000x600+200+50")
kayitsil.resizable(FALSE,FALSE)
class header():
    baslik=Label(
        kayitsil,
        text="Silah Kayıt Sistemi",
        fg="orangered",
        font=("Arial", "20")
    )
    baslik.place(relx=0.10, rely=0.10, anchor=W)
    anlik=datetime.datetime.now()
    tarihsaat=Label(
        kayitsil,
        text=anlik,
        font=("Arial", "10")
    )
    tarihsaat.place(relx=0.70, rely=0.10, anchor=W)
    islem_basligi=Label(
        kayitsil,
        text="Kayıt Sil",
        font=("Arial", "15")
    )
    islem_basligi.place(relx=0.10, rely=0.20, anchor=W)
    def anasayfagecis():
        import sks_anasayfa
    anasayfa = Button(
        kayitsil,
        text="Anasayfa",
        width=15,
        bg="darkslategrey",
        fg="white",
        bd=0,
        command=(anasayfagecis)
    )
    anasayfa.place(relx=0.75, rely=0.20, anchor=W)
veritabani=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="silah_kayit_sistemi"
)
def kayit_sil():
    mesaj=messagebox.askquestion("İşlem Onayı", "Kayıt silinsin mi?")
    if mesaj=="yes":
        mycursor = veritabani.cursor()
        mycursor.execute("DELETE FROM sahis_bilgileri WHERE id="+id_entry.get())
        veritabani.commit()
        print(mycursor.rowcount, "Kayıt silindi.")
        bilgi=messagebox.showinfo("İşlem Tamamlandı", "Kayıt başarılı bir şekilde silindi.")
        if bilgi=="ok":
            pass
    else:
        pass
id=Label(
    kayitsil,
    text="ID"
)
id.place(relx=0.10, rely=0.30, anchor=W)
id_entry=Entry(
    kayitsil,
    bd=1,
    width=35
)
id_entry.place(relx=0.25, rely=0.30, anchor=W)
bilgilendirme1=Label(
    kayitsil,
    text="Silmek istediğiniz kayda ait 'ID' girdikten sonra 'Sil' butonuna tıklayın.",
    fg="brown"
)
bilgilendirme1.place(relx=0.10, rely=0.35, anchor=W)
bilgilendirme2=Label(
    kayitsil,
    text="Silme işlemi onaylandığında, şahsa ait ilgili silahın bütün bilgileri silinir.",
    fg="brown"
)
bilgilendirme2.place(relx=0.10, rely=0.40, anchor=W)
bilgilendirme3=Label(
    kayitsil,
    text="Eğer silmek istediğiniz kayda ait 'ID' bilmiyorsanız, 'Anasayfa' butonuna tıkladıktan sonra 'Kayıt Kontrol' sayfasına gidip,",
    fg="black"
)
bilgilendirme3.place(relx=0.10, rely=0.45, anchor=W)
bilgilendirme3_devam=Label(
    kayitsil,
    text="T.C. No üzerinden sorgulama yaparak kayda ait 'ID' öğrenebilirsiniz.",
    fg="black"
)
bilgilendirme3_devam.place(relx=0.10, rely=0.48, anchor=W)
sil=Button(
    kayitsil,
    text="Sil",
    width=15,
    bg="brown",
    fg="white",
    bd=0,
    command=(kayit_sil)
)
sil.place(relx=0.55, rely=0.30, anchor=W)
class footer():
    footer_not=Label(
        kayitsil,
        text="Silah Kayıt Sistemi © 2020",
        font=("Arial", "12")
    )
    footer_not.place(relx=0.38, rely=0.90, anchor=W)
mainloop()