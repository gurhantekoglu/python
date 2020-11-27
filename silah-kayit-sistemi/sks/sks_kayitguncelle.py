from tkinter import*
from tkinter import messagebox
import mysql.connector
from tkinter.ttk import Combobox
import datetime
kayitguncelle=Tk()
kayitguncelle.title("Silah Kayıt Sistemi")
kayitguncelle.geometry("1000x600+200+50")
kayitguncelle.resizable(FALSE,FALSE)
class header():
    baslik=Label(
        kayitguncelle,
        text="Silah Kayıt Sistemi",
        fg="orangered",
        font=("Arial", "20")
    )
    baslik.place(relx=0.10, rely=0.10, anchor=W)
    anlik=datetime.datetime.now()
    tarihsaat=Label(
        kayitguncelle,
        text=anlik,
        font=("Arial", "10")
    )
    tarihsaat.place(relx=0.70, rely=0.10, anchor=W)
    islem_basligi=Label(
        kayitguncelle,
        text="Kayıt Güncelle",
        font=("Arial", "15")
    )
    islem_basligi.place(relx=0.10, rely=0.20, anchor=W)
    def anasayfagecis():
        import sks_anasayfa
    anasayfa = Button(
        kayitguncelle,
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
def bilgi_goster():
    mycursor=veritabani.cursor()
    mycursor.execute("SELECT * FROM sahis_bilgileri WHERE id="+id_entry.get())
    sonuclar=mycursor.fetchall()
    for g in sonuclar:
        print(g)
    bilgiler=Label(
        kayitguncelle,
        text="Bilgiler"
    )
    bilgiler.place(relx=0.10, rely=0.35, anchor=W)
    bilgilendirme=Label(
        kayitguncelle,
        text="Yalnızca güncellenebilecek bilgiler gösterilmektedir.",
        fg="brown"
    )
    bilgilendirme.place(relx=0.10, rely=0.40, anchor=W)
    telefon=Label(
        kayitguncelle,
        text="Telefon (+90)"
    )
    telefon.place(relx=0.10, rely=0.45, anchor=W)
    global telefon_entry
    telefon_entry=Entry(
        kayitguncelle,
        bd=1,
        width=35
    )
    telefon_entry.place(relx=0.25, rely=0.45, anchor=W)
    telefon_entry.insert(0, sonuclar[0][5])
    e_posta=Label(
        kayitguncelle,
        text="E-Posta"
    )
    e_posta.place(relx=0.10, rely=0.50, anchor=W)
    global e_posta_entry
    e_posta_entry=Entry(
        kayitguncelle,
        bd=1,
        width=35
    )
    e_posta_entry.place(relx=0.25, rely=0.50, anchor=W)
    e_posta_entry.insert(0, sonuclar[0][6])
    il=Label(
        kayitguncelle,
        text="İl"
    )
    il.place(relx=0.10, rely=0.55, anchor=W)
    global il_combo
    il_combo=Combobox(kayitguncelle, width=32)
    il_combo['values']=(
        "Seçiniz",
        "Adana",
        "Adıyaman",
        "Afyonkarahisar",
        "Ağrı",
        "Aksaray",
        "Amasya",
        "Ankara",
        "Antalya",
        "Ardahan",
        "Artvin",
        "Aydın",
        "Balıkesir",
        "Bartın",
        "Batman",
        "Bayburt",
        "Bilecik",
        "Bingöl",
        "Bitlis",
        "Bolu",
        "Burdur",
        "Bursa",
        "Çanakkale",
        "Çankırı",
        "Çorum",
        "Denizli",
        "Diyarbakır",
        "Düzce",
        "Edirne",
        "Elazığ",
        "Erzincan",
        "Erzurum",
        "Eskişehir",
        "Gaziantep",
        "Giresun",
        "Gümüşhane",
        "Hakkâri",
        "Hatay",
        "Iğdır",
        "Isparta",
        "İstanbul",
        "İzmir",
        "Kahramanmaraş",
        "Karabük",
        "Karaman",
        "Kars",
        "Kastamonu",
        "Kayseri",
        "Kilis",
        "Kırıkkale",
        "Kırklareli",
        "Kırşehir",
        "Kocaeli",
        "Konya",
        "Kütahya",
        "Malatya",
        "Manisa",
        "Mardin",
        "Mersin",
        "Muğla",
        "Muş",
        "Nevşehir",
        "Niğde",
        "Ordu",
        "Osmaniye",
        "Rize",
        "Sakarya",
        "Samsun",
        "Şanlıurfa",
        "Siirt",
        "Sinop",
        "Sivas",
        "Şırnak",
        "Tekirdağ",
        "Tokat",
        "Trabzon",
        "Tunceli",
        "Uşak",
        "Van",
        "Yalova",
        "Yozgat",
        "Zonguldak"
    )
    il_combo.place(relx=0.25, rely=0.55, anchor=W)
    il_combo.insert(0, sonuclar[0][8])
    ev_adres=Label(
        kayitguncelle,
        text="Ev Adres"
    )
    ev_adres.place(relx=0.10, rely=0.60, anchor=W)
    global ev_adres_entry
    ev_adres_entry=Entry(
        kayitguncelle,
        bd=1,
        width=30,
        font=("Arial", "10")
    )
    ev_adres_entry.place(relx=0.25, rely=0.60, anchor=W)
    ev_adres_entry.insert(0, sonuclar[0][9])
    is_adres=Label(
        kayitguncelle,
        text="İş Adres"
    )
    is_adres.place(relx=0.10, rely=0.65, anchor=W)
    global is_adres_entry
    is_adres_entry=Entry(
        kayitguncelle,
        bd=1,
        width=30,
        font=("Arial", "10")
    )
    is_adres_entry.place(relx=0.25, rely=0.65, anchor=W)
    is_adres_entry.insert(0, sonuclar[0][10])
    guncelle = Button(
        kayitguncelle,
        text="Güncelle",
        width=15,
        bg="forestgreen",
        fg="white",
        bd=0,
        command=(kayit_guncelle)
    )
    guncelle.place(relx=0.55, rely=0.65, anchor=W)
def kayit_guncelle():
    id_entry2=id_entry.get()
    telefon2=telefon_entry.get()
    e_posta2=e_posta_entry.get()
    il2=il_combo.get()
    ev_adres2=ev_adres_entry.get()
    is_adres2=is_adres_entry.get()
    mesaj=messagebox.askquestion("İşlem Onayı", "Kayıt güncellensin mi?")
    if mesaj=="yes":
        mycursor2=veritabani.cursor()
        mycursor2.execute("UPDATE sahis_bilgileri SET telefon='"+telefon2+"', e_posta='"+e_posta2+"', il='"+il2+"', ev_adres='"+ev_adres2+"', is_adres='"+is_adres2+"' WHERE id='"+id_entry2+"'")
        veritabani.commit()
        bilgi = messagebox.showinfo("İşlem Tamamlandı", "Kayıt başarılı bir şekilde güncellendi.")
        if bilgi == "ok":
            pass
    else:
        pass
id=Label(
    kayitguncelle,
    text="ID"
)
id.place(relx=0.10, rely=0.30, anchor=W)
id_entry=Entry(
    kayitguncelle,
    bd=1,
    width=35
)
id_entry.place(relx=0.25, rely=0.30, anchor=W)
bilgileri_goster=Button(
    kayitguncelle,
    text="Bilgileri Göster",
    width=15,
    bg="black",
    fg="white",
    bd=0,
    command=(bilgi_goster)
)
bilgileri_goster.place(relx=0.55, rely=0.30, anchor=W)
class footer():
    footer_not=Label(
        kayitguncelle,
        text="Silah Kayıt Sistemi © 2020",
        font=("Arial", "12")
    )
    footer_not.place(relx=0.38, rely=0.90, anchor=W)
mainloop()