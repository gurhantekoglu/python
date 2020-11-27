from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
giris=Tk()
giris.title("Silah Kayıt Sistemi")
giris.geometry("1000x600+200+50")
giris.resizable(FALSE,FALSE)
baslik=Label(
        giris,
        text="Silah Kayıt Sistemi",
        fg="orangered",
        font=("Arial", "20")
)
baslik.place(relx=0.35, rely=0.30, anchor=W)
veritabani=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="silah_kayit_sistemi"
)
sicilNo=Label(
        giris,
        text="Sicil No",
        font=("Arial", "12")
)
sicilNo.place(relx=0.30, rely=0.40, anchor=W)
sicilNo_entry=Entry(
        giris,
        bd=1,
        width=35
)
sicilNo_entry.place(relx=0.38, rely=0.40, anchor=W)
sifre=Label(
        giris,
        text="Şifre",
        font=("Arial", "12")
)
sifre.place(relx=0.30, rely=0.45, anchor=W)
sifre2=StringVar
sifre_entry=Entry(
        giris,
        textvariable=sifre2,
        show='*',
        bd=1,
        width=35
)
sifre_entry.place(relx=0.38, rely=0.45, anchor=W)
def girisyap():
        mycursor=veritabani.cursor()
        mycursor.execute("SELECT * FROM personel WHERE personel_sicilNo="+sicilNo_entry.get() and "SELECT * FROM personel WHERE personel_sifre="+sifre_entry.get())
        sonuc=mycursor.fetchall()
        if sonuc:
                import sks_anasayfa
        else:
                hata=messagebox.showerror("Hata", "Giriş bilgilerinizi kontrol edin.")
uyari=Label(
        giris,
        text="Personel Sicil Numaranızı ve EGM tarafından size verilen Personel Şifrenizi kullanarak giriş yapın."
)
uyari.place(relx=0.20, rely=0.50, anchor=W)
uyari2=Label(
        giris,
        text="Personel Şifrenizi unuttuysanız, lütfen hemen bağlı olduğunuz müdürlük ile irtibata geçin."
)
uyari2.place(relx=0.22, rely=0.55, anchor=W)
sks_giris=Button(
        giris,
        text="Giriş",
        width=15,
        bg="forestgreen",
        fg="white",
        bd=0,
        command=(girisyap)
)
sks_giris.place(relx=0.42, rely=0.60, anchor=W)
mainloop()