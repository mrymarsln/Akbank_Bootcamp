class Kutuphane:
    def __init__(self):
        # Dosya adını ve dosyayı açma modunu tanımla
        self.dosya_adi = "kitaplar.txt"
        self.dosya = open(self.dosya_adi, "a+")

    def dosyaya_yaz(self, kitap_bilgisi):
        # Kitap bilgisini dosyaya yaz
        self.dosya.write(kitap_bilgisi)

    def __del__(self):
        # Nesne yok edildiğinde dosyayı kapat
        self.dosya.close()

    def kitaplari_listele(self):
        # Dosyadaki kitapları listele
        self.dosya.seek(0)
        kitaplar = self.dosya.read().splitlines()
        if kitaplar:
            for kitap in kitaplar:
                # Her kitabın başlık, yazar, yayın tarihi ve sayfa sayısını ekrana yaz
                kitap_bilgisi = kitap.split(',')
                print("Başlık:", kitap_bilgisi[0])
                print("Yazar:", kitap_bilgisi[1])
                print("Yayın tarihi:", kitap_bilgisi[2])
                print("Sayfa sayısı:", kitap_bilgisi[3])
        else:
            # Eğer dosyada kitap yoksa bildirim ver
            print("Mevcut kitap yoktur.")

    def kitap_ekle(self):
        # Kullanıcıdan yeni bir kitap bilgisi al ve dosyaya ekle
        baslik = input("Kitap başlığını girin: ")
        yazar = input("Kitap yazarını girin: ")
        yayin_yili = input("Kitabın yayın yılını girin: ")
        numarasi = input("Kitap numarasını girin: ")
        kitap_bilgisi = f"{baslik},{yazar},{yayin_yili},{numarasi}\n"
        self.dosyaya_yaz(kitap_bilgisi)
        print("Kitap başarıyla eklendi.")

    def kitap_sil(self):
        # Kullanıcıdan silinecek kitabın başlığını al ve dosyadan sil
        baslik = input("Silmek istediğiniz kitabın başlığını girin: ")
        self.dosya.seek(0)
        kitaplar = self.dosya.readlines()
        guncellenmis_kitaplar = []
        for kitap in kitaplar:
            if baslik not in kitap:
                guncellenmis_kitaplar.append(kitap)
        self.dosya.seek(0)
        self.dosya.truncate()
        self.dosya.writelines(guncellenmis_kitaplar)
        print("Kitap başarıyla silindi.")

kutuphane = Kutuphane()
while True:
    print("\n*** MENÜ ***")
    print("1) Kitapları Listele")
    print("2) Kitap Ekle")
    print("3) Kitap Sil\n")
    secim = input("Lütfen seçiminizi yapın (1/2/3/q): ")
    if secim == '1':
        kutuphane.kitaplari_listele()
    elif secim == '2':
        kutuphane.kitap_ekle()
    elif secim == '3':
        kutuphane.kitap_sil()
    elif secim.lower() == 'q':
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim. Lütfen 1, 2 veya 3'ü seçin.")

            
            