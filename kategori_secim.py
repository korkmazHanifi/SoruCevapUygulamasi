#Kategori Seçimi 

def kategori_secimi():
    print("Lütfen bir kategori seçin:")
    print("1. Bilim")
    print("2. Genel Kültür")
    print("3. Spor")
    print("4. Tarih")
    
    try:
        secim = int(input("Kategori numarasını girin: "))
        if secim == 1:
            kategori = 'bilim_sorular.json'
        elif secim == 2:
            kategori = 'genel_kültür_sorular.json'
        elif secim == 3:
            kategori = 'spor_sorular.json'
        elif secim == 4:
            kategori = 'tarih_sorular.json'
        else:
            print("Geçersiz seçim!")
            return kategori_secimi()
        return kategori
        
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")
        return kategori_secimi()
