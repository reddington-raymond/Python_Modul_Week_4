
import kitap_islemleri
import uye_islemleri 
import json
import zaman
import datetime



def menu(secim):
    if secim=='1':
        print(75*'-')
        print('-    UYELER      = 1             =               KITAP ODUNC VERME= 5        ')
        print('-    UYE EKLEME  = 2             =               KITAP IADE       = 6        ')   
        print('-    UYE ARA     = 3             =               KITAP TAKIBI     = 7        ')   
        print('-    UYE SIL     = 4             =               CIKIS            = 0        ')
        print(75*'-')   
    elif secim=='2':
        print(75*'-')
        print('-    KITAPLAR    = 1                                                         ')
        print('-    KITAP EKLEME= 2                                                         ')   
        print('-    KITAP ARA   = 3                                                         ')   
        print('-    KITAP SIL   = 4             =               CIKIS            = 0        ')
        print(75*'-')   
    print()
    
    
def main():
    while True:
        try:
        
            print(75*'-')
            print("\n--- Kütüphane Yönetim Sistemi ---")
            print('1- UYELIK ISLEMLERI      1')
            print('2- KITAP  ISLEMLERI      2')
            print('0- CIKIS                 0')
            print(75*'-')
            print()
            secim=input('Lutfen yapmak istediginiz islemin kodunu giriniz :  ')
            if secim=='0':
                break
            if secim not in ['1', '2']:
                print("Geçersiz seçim! Lütfen 1, 2 veya 0 giriniz.")
                continue
            menu(secim)
            islem=input('Islem Seciniz :    ')
            if secim=='1':
                if islem=='1':
                    uye_islemleri.uye_listele()
                elif islem=='2':
                    uye_islemleri.uye_ekle()
                elif islem=='3':
                    uye_islemleri.uye_ara()
                elif islem=='4':
                    uye_islemleri.uye_sil()
                elif islem=='5':
                    uye_islemleri.kitap_odunc_verme()
                elif islem=='6':
                    uye_islemleri.kitap_iade()
                elif islem=='7':
                    uye_islemleri.kitap_takibi()
                elif islem=='0':
                    print("Çıkış yapılıyor...")
                    break
                else:
                    print('Gecersiz bir islem sectiniz! Lütfen geçerli bir seçenek giriniz.')
            if secim=='2':
                if islem=='1':
                    kitap_islemleri.kitap_listele()
                elif islem=='2':
                    kitap_islemleri.kitap_ekle()
                elif islem=='3':
                    kitap_islemleri.kitap_ara()
                elif islem=='4':
                    kitap_islemleri.kitap_sil()

                elif islem=='0':
                    print("Çıkış yapılıyor...")
                    break
                else:
                    print('Gecersiz bir islem sectiniz! Lütfen geçerli bir seçenek giriniz.')
        
        except ValueError as ve:
            print(f"Değer hatası: {ve}")        
          
        except Exception as hata:
            print('Beklenmeyen bir hata oluştu:   ', hata, end='\n\n')

if __name__=='__main__':
    main()
    

