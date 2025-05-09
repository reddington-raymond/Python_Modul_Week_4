# çalışacağımız dosyanın ön tanımlı olarak kitap.json dosyasının bir kopyası üzerinden çalışıyor.
# Ana program bittiğinde bu değiştirilecek.
import json

dosya_name= 'kitap.json'

def dosya_yukle(yuklenecek_dosya):
    """Belirtilen JSON dosyasını yükler.
    Dosya bulunamazsa boş bir liste döndürür.
    """      
    try:                                
        with open(yuklenecek_dosya, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def dosya_kaydet(kaydedilecek_liste, kaydedilecek_dosya):
    
    with open(kaydedilecek_dosya, 'w', encoding='utf-8') as file:
        json.dump(kaydedilecek_liste, file, indent=4)


def kitap_ekle():
    import json
       
    kitap_liste = dosya_yukle(dosya_name)

    while True:
        
        kitap = {}

        kitap["Kitap_Adi"]= input("Lütfen kitabın adını giriniz: (çıkmak için 'quit' yazın)")

        if kitap["Kitap_Adi"] == "quit":
            break
        
        kitap["Barkod"] = int(input("Lütfen kitabın barkod numarasını giriniz: "))
        kitap["Dil"] = input("Lütfen kitabın dilini giriniz: ")
        kitap["Fiyat"] = float(input("Lütfen kitabın fiyatını giriniz: "))
        kitap["Yayinevi"] = input("Lütfen kitabın yayın evini giriniz: ")
        kitap["Yazar"] = input("Lütfen kitabın yazarını giriniz: ")

        kitap_liste.append(kitap)

        print(f"Kitap eklendi. {len(kitap_liste)} adet kitap var")

    dosya_kaydet(kitap_liste,dosya_name)


def kitap_listele():
    import json
    
    kitap_liste = dosya_yukle(dosya_name)

    for kitap in kitap_liste:
        print(kitap)

    print(f"{len(kitap_liste)} adet kitap var")


def kitap_ara():
    import json
    
    kitap_liste = dosya_yukle(dosya_name)

    while True:

        barcode= int(input("Lütfen kitabın barkod numarasını giriniz: (çıkmak için '123' yazın)   "))
        if barcode== 123:
            break
        
        bulundu=False

        for kitap in kitap_liste:
            if kitap['Barkod'] == barcode:
                print(kitap)
                bulundu=True
                
        if not bulundu:
            print('Aradiginiz kitap bulunamadi....')
        
        break


def kitap_sil():
    import json
    
    kitap_liste = dosya_yukle(dosya_name)
    
    while True:
        barcode= int(input("Lütfen kitabın barkod numarasını giriniz: (çıkmak için '123' yazın)"))
        if barcode== 123:
            break

        for kitap in kitap_liste:
            if kitap['Barkod'] == barcode:
                kitap_liste.remove(kitap)

        print(f"{barcode} barkod numaralı kitap silindi. {len(kitap_liste)} adet kitap var")
        break        
    
    dosya_kaydet(kitap_liste,dosya_name)