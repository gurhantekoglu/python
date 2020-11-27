from tkinter import*
from tkinter import messagebox
import mysql.connector
from tkinter.ttk import Combobox
import datetime
yenikayit=Tk()
yenikayit.title("Silah Kayıt Sistemi")
yenikayit.geometry("1000x600+200+50")
yenikayit.resizable(FALSE,FALSE)
class header():
    baslik=Label(
        yenikayit,
        text="Silah Kayıt Sistemi",
        fg="orangered",
        font=("Arial", "20")
    )
    baslik.place(relx=0.10, rely=0.10, anchor=W)
    anlik=datetime.datetime.now()
    tarihsaat=Label(
        yenikayit,
        text=anlik,
        font=("Arial", "10")
    )
    tarihsaat.place(relx=0.70, rely=0.10, anchor=W)
    islem_basligi=Label(
        yenikayit,
        text="Yeni Kayıt",
        font=("Arial", "15")
    )
    islem_basligi.place(relx=0.10, rely=0.20, anchor=W)
    def anasayfagecis():
        import sks_anasayfa
    anasayfa = Button(
        yenikayit,
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
def kayit_ekle():
    onay=messagebox.askquestion("İşlem Onayı", "Kayıt ekleme işlemi onaylansın mı?")
    if onay=="yes":
        global sorgu
        mycursor=veritabani.cursor()
        sorgu="INSERT INTO sahis_bilgileri (tc_no, ad, soyad, dogum_tarihi, telefon, e_posta, meslek, il, ev_adres, is_adres," \
              "silah_seri_no, silah_turu, silah_tipi, silah_markasi, silah_modeli, silah_kalibre_mm, silah_agirligi_gr, silah_uzunlugu_mm, silah_kapasitesi)" \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        deger=(tc_no_entry.get(), ad_entry.get(), soyad_entry.get(), guncombo.get() + aycombo.get() + yilcombo.get(),
               telefon_entry.get(), e_posta_entry.get(), meslek_combo.get(), il_combo.get(), ev_adres_entry.get(), is_adres_entry.get(),
               silah_seri_no_entry.get(), silah_turu_combo.get(), silah_tipi_combo.get(), silah_markasi_combo.get(), silah_modeli_combo.get(),
               silah_kalibre_mm_combo.get(), silah_agirligi_gr_entry.get(), silah_uzunlugu_mm_entry.get(), silah_kapasitesi_entry.get()
               )
        mycursor.execute(sorgu, deger)
        veritabani.commit()
        print(mycursor.rowcount, "Kayıt başarılı bir şekilde eklendi.")
        bilgi=messagebox.showinfo("İşlem Tamamlandı", "Kayıt başarılı bir şekilde eklendi.")
        if bilgi=="ok":
            pass
    else:
        pass
tc_no=Label(
    yenikayit,
    text="T.C. No"
)
tc_no.place(relx=0.10, rely=0.30, anchor=W)
tc_no_entry=Entry(
    yenikayit,
    bd=1,
    width=35
)
tc_no_entry.place(relx=0.25, rely=0.30, anchor=W)
ad=Label(
    yenikayit,
    text="Ad"
)
ad.place(relx=0.10, rely=0.35, anchor=W)
ad_entry=Entry(
    yenikayit,
    bd=1,
    width=35
)
ad_entry.place(relx=0.25, rely=0.35, anchor=W)
soyad=Label(
    yenikayit,
    text="Soyad"
)
soyad.place(relx=0.10, rely=0.40, anchor=W)
soyad_entry=Entry(
    yenikayit,
    bd=1,
    width=35
)
soyad_entry.place(relx=0.25, rely=0.40, anchor= W)
dogum_tarihi=Label(
    yenikayit,
    text="Doğum Tarihi"
)
dogum_tarihi.place(relx=0.10, rely=0.45, anchor=W)
guncombo=Combobox(yenikayit, width=5)
guncombo['values']=(
    "Gün", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
    "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"
)
guncombo.place(relx=0.25, rely=0.43)
guncombo.current(0)
aycombo=Combobox(yenikayit, width=8)
aycombo['values']=(
     "Ay", "Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"
)
aycombo.place(relx=0.315, rely=0.43)
aycombo.current(0)
yilcombo=Combobox(yenikayit, width=7)
yilcombo['values'] = (
    "Yıl", "2020", "2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010", "2009", "2008", "2007",
    "2006", "2005", "2004", "2003", "2002", "2001", "2000", "1999", "1998", "1997", "1996", "1995", "1994", "1993", "1992", "1991", "1990", "1989", "1988", "1988", "1987",
    "1986", "1985", "1984", "1983", "1982", "1981", "1980")
yilcombo.place(relx=0.40, rely=0.43)
yilcombo.current(0)
telefon=Label(
    yenikayit,
    text="Telefon (+90)"
)
telefon.place(relx=0.10, rely=0.50, anchor=W)
telefon_entry=Entry(
    yenikayit,
    bd=1,
    width=35
)
telefon_entry.place(relx=0.25, rely=0.50, anchor=W)
e_posta=Label(
    yenikayit,
    text="E-Posta"
)
e_posta.place(relx=0.10, rely=0.55, anchor=W)
e_posta_entry=Entry(
    yenikayit,
    bd=1,
    width=35
)
e_posta_entry.place(relx=0.25, rely=0.55, anchor=W)
meslek=Label(
    yenikayit,
    text="Meslek"
)
meslek.place(relx=0.10, rely=0.60, anchor=W)
meslek_combo=Combobox(yenikayit, width=32)
meslek_combo['values']=(
    "Seçiniz",
    "Emniyet Mensubu",
    "TSK Mensubu",
    "Özel Güvenlik",
    "Vali",
    "Belediye Başkanı",
    "İl Meclis Üyesi",
    "Muhtar",
    "HSK Mensubu",
    "Avukat",
    "Kuyumcu/Sarraf"
)
meslek_combo.place(relx=0.25, rely=0.60, anchor=W)
meslek_combo.current(0)
il=Label(
    yenikayit,
    text="İl"
)
il.place(relx=0.10, rely=0.65, anchor=W)
il_combo=Combobox(yenikayit, width=32)
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
il_combo.place(relx=0.25, rely=0.65, anchor=W)
il_combo.current(0)
ev_adres=Label(
    yenikayit,
    text="Ev Adres"
)
ev_adres.place(relx=0.10, rely=0.70, anchor=W)
ev_adres_entry=Entry(
    yenikayit,
    bd=1,
    width=30,
    font=("Arial", "10")
)
ev_adres_entry.place(relx=0.25, rely=0.70, anchor=W)
is_adres=Label(
    yenikayit,
    text="İş Adres"
)
is_adres.place(relx=0.10, rely=0.75, anchor=W)
is_adres_entry=Entry(
    yenikayit,
    bd=1,
    width=30,
    font=("Arial", "10")
)
is_adres_entry.place(relx=0.25, rely=0.75, anchor=W)
silah_seri_no=Label(
    yenikayit,
    text="Silah Seri No"
)
silah_seri_no.place(relx=0.50, rely=0.30, anchor=W)
silah_seri_no_entry=Entry(
    yenikayit,
    bd=1,
    width=35
)
silah_seri_no_entry.place(relx=0.65, rely=0.30, anchor=W)
silah_turu=Label(
    yenikayit,
    text="Silah Türü"
)
silah_turu.place(relx=0.50, rely=0.35, anchor=W)
silah_turu_combo=Combobox(yenikayit, width=32)
silah_turu_combo['values']=(
    "Seçiniz",
    "Piyade Silahları",
    "Hafif Silahlar",
    "Yivsiz Tüfekler"
)
silah_turu_combo.place(relx=0.65, rely=0.35, anchor=W)
silah_turu_combo.current(0)
silah_tipi=Label(
    yenikayit,
    text="Silah Tipi"
)
silah_tipi.place(relx=0.50, rely=0.40, anchor=W)
silah_tipi_combo=Combobox(yenikayit, width=32)
silah_tipi_combo['values']=(
    "Seçiniz",
    "Normal Piyade Tüfeği",
    "Keskin Nişancı Tüfeği",
    "Multi Kalibre Keskin Nişancı Tüfeği",
    "Tabanca",
    "Hafif Makineli",
    "Tek Atışlı Yivsiz Tüfek",
    "Sürgülü Yivsiz Tüfek",
    "Pompa Hareketli Yivsiz Tüfek",
    "Yarı Otomatik Yivsiz Tüfek",
    "Çift Namlulu Yivsiz Tüfek",
    "Süperpoze Yivsiz Tüfek"
)
silah_tipi_combo.place(relx=0.65, rely=0.40, anchor=W)
silah_tipi_combo.current(0)
silah_markasi=Label(
    yenikayit,
    text="Silah Markası"
)
silah_markasi.place(relx=0.50, rely=0.45, anchor=W)
silah_markasi_combo=Combobox(yenikayit, width=32)
silah_markasi_combo['values']=(
    "Seçiniz",
    "AKDAŞ",
    "AKKAR",
    "ATA ARMS",
    "BERETTA",
    "CANİK",
    "COLT",
    "CZ",
    "GİRSAN",
    "GLOCK",
    "HATSAN",
    "HECKLER KOCH",
    "HUĞLU",
    "HUSAN",
    "MKE",
    "IZHMASH",
    "KALE",
    "SARSILMAZ",
    "SİG SAUER",
    "SMİTH & WESSON",
    "TİSAŞ"
)
silah_markasi_combo.place(relx=0.65, rely=0.45, anchor=W)
silah_markasi_combo.current(0)
silah_modeli=Label(
    yenikayit,
    text="Silah Modeli"
)
silah_modeli.place(relx=0.50, rely=0.50, anchor=W)
silah_modeli_combo=Combobox(yenikayit, width=32)
silah_modeli_combo['values']=(
    "Seçiniz",
    "92 G",
    "612 TAC",
    "612 TAC FOLDING",
    "1911 CLASSIC",
    "AK-47",
    "AK-40GL BOMBAATAR",
    "ALTAY AR12",
    "APX",
    "ATA",
    "ATA1955",
    "ATROX",
    "B6",
    "CHURCHILL 206 ORCAP",
    "CHURCHILL 206 SAVUNMA",
    "CHURCHILL 206 TRAP",
    "CHURCHILL 512",
    "CM9 GEN2",
    "CY TAKTİK",
    "DELTA ELITE",
    "DW VALOR",
    "DWX",
    "DWX COMPACT",
    "ETRO",
    "G17",
    "G19",
    "G22",
    "G23",
    "G26",
    "G34",
    "G35",
    "G43",
    "G45",
    "G48",
    "GX TACTIC",
    "HK21",
    "HK33",
    "HK416",
    "JMK BORA-12",
    "K-12 SPORT",
    "K-12 SPORT X",
    "KAAN-717",
    "KARATAY 612",
    "KARATAY TELESKOBIK"
    "KCR-556",
    "KILINÇ 2000 LIGHT",
    "KILINÇ 2000 MEGA",
    "KNT-76",
    "KSR50",
    "M9A3",
    "M-2000",
    "M71",
    "MAMMUT",
    "MKA1919",
    "MKA1919PA",
    "MPT-55",
    "MPT-76",
    "NEO TAKTİK",
    "OVIS TACTICAL",
    "P8 L",
    "P8 S",
    "P320",
    "P320 XFULL",
    "P365",
    "SAR 9",
    "SAR 9T",
    "SAR 9X",
    "SAR 109C",
    "SAR 109T",
    "SR 38",
    "ST 9",
    "MC 9",
    "MODEL 19 CLASSIC",
    "MODEL 442",
    "MODEL 648",
    "MUSTANG POCKETLITE",
    "SAR-223C",
    "SAR-223T",
    "SAR-223P",
    "SAR-308",
    "TP9 ELITE COMBAT",
    "TP9 ELITE-S COMBAT",
    "TP9 SF",
    "TP9 SF ELITE/ELITE S",
    "TP9 SF METE",
    "TP9 SF METE-S",
    "TP9 SFX",
    "TP9 SFX METE",
    "TP9 SUB ELITE",
    "YAVUZ16 REGARD",
    "ZİGANA PX9",
    "XR7"
)
silah_modeli_combo.place(relx=0.65, rely=0.50, anchor=W)
silah_modeli_combo.current(0)
silah_kalibre_mm=Label(
    yenikayit,
    text="Silah Kalibre (mm)"
)
silah_kalibre_mm.place(relx=0.50, rely=0.55, anchor=W)
silah_kalibre_mm_combo=Combobox(yenikayit, width=32)
silah_kalibre_mm_combo['values']=(
    "Seçiniz",
    "0.45",
    "5.56",
    "6.35",
    "7.62",
    "7.65",
    "9"
)
silah_kalibre_mm_combo.place(relx=0.65, rely=0.55, anchor=W)
silah_kalibre_mm_combo.current(0)
silah_agirligi_gr=Label(
    yenikayit,
    text="Silah Ağırlığı (gr)"
)
silah_agirligi_gr.place(relx=0.50, rely=0.60, anchor=W)
silah_agirligi_gr_entry=Entry(
    yenikayit,
    bd=1,
    width=35
)
silah_agirligi_gr_entry.place(relx=0.65, rely=0.60, anchor=W)
silah_uzunlugu_mm=Label(
    yenikayit,
    text="Silah Uzunluğu (mm)"
)
silah_uzunlugu_mm.place(relx=0.50, rely=0.65, anchor=W)
silah_uzunlugu_mm_entry=Entry(
    yenikayit,
    bd=1,
    width=35
)
silah_uzunlugu_mm_entry.place(relx=0.65, rely=0.65, anchor=W)
silah_kapasitesi=Label(
    yenikayit,
    text="Silah Kapasitesi"
)
silah_kapasitesi.place(relx=0.50, rely=0.70, anchor=W)
silah_kapasitesi_entry=Entry(
    yenikayit,
    bd=1,
    width=35
)
silah_kapasitesi_entry.place(relx=0.65, rely=0.70, anchor=W)
onayla=Button(
    yenikayit,
    text="Onayla",
    width=15,
    bg="forestgreen",
    fg="white",
    bd=0,
    command=(kayit_ekle)
)
onayla.place(relx=0.75, rely=0.75, anchor=W)
class footer():
    footer_not=Label(
        yenikayit,
        text="Silah Kayıt Sistemi © 2020",
        font=("Arial", "12")
    )
    footer_not.place(relx=0.38, rely=0.90, anchor=W)
mainloop()