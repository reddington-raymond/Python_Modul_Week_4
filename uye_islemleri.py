import json
import zaman
from datetime import datetime
import os


def dosya_yukle(yuklenecek_dosya):
    try:
        if not os.path.exists(yuklenecek_dosya):
            # Create an empty file if it doesn't exist
            with open(yuklenecek_dosya, 'w', encoding='utf-8') as file:
                file.write('[]')
            return []
            
        with open(yuklenecek_dosya, 'r', encoding='utf-8') as file:
            return json.load(file)
            
    except json.JSONDecodeError:
        print(f"Hata: {yuklenecek_dosya} dosyası geçerli bir JSON formatında değil.")
        return []
        
    except Exception as e:
        print(f"Dosya yüklenirken bir hata oluştu: {e}")
        return []

def dosya_kaydet(kaydedilecek_liste, kaydedilecek_dosya):
    
    with open(kaydedilecek_dosya, 'w') as file:
        json.dump(kaydedilecek_liste, file, indent=4)

def uye_listele():
    uyeler = dosya_yukle('uyeler.json')
    if not uyeler:
        print("Kayıtlı üye bulunamadı.")
        return
    print("\n--- Kayıtlı Üyeler ---")
    for uye in uyeler:
        print(f"ID: {uye['uye_ID']}, Ad: {uye['uye_adi']}, Telefon: {uye['uye_telefon']}, Adres: {uye['uye_adres']}")
    print()

def uye_ekle():
    uyeler=dosya_yukle('uyeler.json')
    while True:
        uye={}    
        if not uyeler:
            uye['uye_ID']=1
        else:
            uye['uye_ID']=max([x['uye_ID'] for x in uyeler]) + 1
        uye['uye_adi']=input('Uye ismini giriniz:  ').strip()
        if not uye['uye_adi']:
            print("İsim boş olamaz!")
            continue
        uye['uye_telefon']=input('Uye telefon numarasini giriniz:  ').strip()
        if not uye['uye_telefon'].isdigit():
            print("Telefon numarası sadece rakamlardan oluşmalı!")
            continue
        uye['uye_adres']=input('Uye adresini giriniz:  ').strip()
        if not uye['uye_adres']:
            print("Adres boş olamaz!")
            continue
        uyeler.append(uye)
        secim=input('Baska bir uye daha girmek istermisiniz: (E/H)').strip().lower()
        if secim!='e':
            break
    dosya_kaydet(uyeler, 'uyeler.json')
    print("Üye(ler) başarıyla kaydedildi...")             
    
def uye_ara():
    uyeler = dosya_yukle('uyeler.json')
    arama = input("Aramak istediğiniz üyenin adını veya ID'sini giriniz: ").strip().lower()
    bulundu = False
    for uye in uyeler:
        if arama == str(uye['uye_ID']) or arama in uye['uye_adi'].lower():
            print(f"ID: {uye['uye_ID']}, Ad: {uye['uye_adi']}, Telefon: {uye['uye_telefon']}, Adres: {uye['uye_adres']}")
            bulundu = True
    if not bulundu:
        print("Aradığınız kriterlere uygun üye bulunamadı.")    

def uye_sil():
    uyeler = dosya_yukle('uyeler.json')
    uye_id = input("Silmek istediğiniz üyenin ID'sini giriniz: ").strip()
    for uye in uyeler[:]:  # Liste kopyası üzerinde işlem yap
        if str(uye['uye_ID']) == uye_id:
            uyeler.remove(uye)
            dosya_kaydet(uyeler, 'uyeler.json')
            print(f"ID {uye_id} olan üye silindi.")
            return
    print("Belirtilen ID'ye sahip üye bulunamadı.")

def kitap_odunc_verme():
    
    uyeler = dosya_yukle('uyeler.json')
    kitaplar = dosya_yukle('kitap.json')
    takip = dosya_yukle('takip.json')
    
    uye_id = int(input("Üyenin ID'sini giriniz: ").strip())
    barkod = int(input("Kitabın barkod numarasini giriniz: ").strip())
    
    # Üye kontrolü
    uye_var = False
    for uye in uyeler:
        if uye['uye_ID'] == uye_id:
            uye_var = True
            break
    if not uye_var:
        print("Belirtilen ID'ye sahip üye bulunamadı.")
        return
    
    for kitap in kitaplar[:]:
        if kitap['Barkod']==barkod:
            takip_girdisi = {
                'uye_ID': uye_id,
                'Barkod': barkod,
                'Kitap_Adi': kitap['Kitap_Adi'],
                'Yazar':kitap['Yazar'],
                'Yayinevi':kitap['Yayinevi'],
                'Dil':kitap['Dil'],
                'Fiyat':kitap['Fiyat'],                
                'Odunc_Tarihi': zaman.zaman_damgasi(),
                'Iade_Tarihi': zaman.iade_tarihi()
                
            }
            takip.append(takip_girdisi)
            kitaplar.remove(kitap)
            dosya_kaydet(kitaplar, 'kitap.json')
            dosya_kaydet(takip, 'takip.json')
            print(f"Kitap ({kitap['Kitap_Adi']}) üye ID {uye_id} için ödünç verildi.")
            return
    print("Belirtilen barkod numarasina sahip kitap bulunamadi.")
            
    
def kitap_iade():
    takip = dosya_yukle('takip.json')
    kitaplar = dosya_yukle('kitap.json')
    
    barkod = int(input("İade edilecek kitabın barkod numarasini giriniz: ").strip())
    
    for giris in takip[:]:
        if giris['Barkod'] == barkod:
            kitap = {
                'Barkod': giris['Barkod'],
                'Kitap_Adi': giris['Kitap_Adi'],
                'Yazar':giris['Yazar'],
                'Yayinevi':giris['Yayinevi'],
                'Dil':giris['Dil'],
                'Fiyat':giris['Fiyat']
            }
            kitaplar.append(kitap)
            takip.remove(giris)
            dosya_kaydet(kitaplar, 'kitap.json')
            dosya_kaydet(takip, 'takip.json')
            print(f"Kitap ({giris['Kitap_Adi']}) iade edildi.")
            return
    print("Belirtilen ID'ye sahip kitap ödünç listesinde bulunamadı.")
    
def kitap_takibi():
    takip = dosya_yukle('takip.json')
    if not takip:
        print("Ödünç alınmış kitap bulunamadı.")
        return
    print("\n--- Ödünç Alınmış Kitaplar ---")
    for giris in takip:
        print(f"Üye ID: {giris['uye_ID']}, Kitap ID: {giris['Barkod']}, Kitap Adı: {giris['Kitap_Adi']}, Ödünç Tarihi: {giris['Odunc_Tarihi']}, iade Tarihi: {giris['Iade_Tarihi']}" )
    print()
    
    iade_tarihi_gecen_kitaplar=[]
    for giris in takip:
        if  giris['Iade_Tarihi'] < datetime.now().strftime("%Y-%m-%d %H:%M:%S") :
            iade_tarihi_gecen_kitaplar.append(giris)
    
    if iade_tarihi_gecen_kitaplar:
        print()
        print('-----------------IADE TARIHI GECEN KITAPLAR-----------------')
        for i in iade_tarihi_gecen_kitaplar:
            print(i)
    
    if not iade_tarihi_gecen_kitaplar:
        print()
        print('Iade tarihi gecen kitap bulunmamaktadir.')
        
