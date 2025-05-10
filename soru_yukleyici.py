import json

from soru import Soru

def soru_yukle(kategori_dosyasi):
    # Sorular klasörü altında doğru yolu belirtiyoruz
    kategori_dosyasi = f"Sorular/{kategori_dosyasi}"

    try:
        with open(kategori_dosyasi, 'r', encoding='utf-8') as file:
            sorular_data = json.load(file)
        
        sorular = []
        for veri in sorular_data:
            soru = Soru(veri["metin"], veri["secenekler"], veri["dogru_cevap"], veri["zorluk"])
            sorular.append(soru)

        return sorular

    except FileNotFoundError:
        print(f"Dosya bulunamadı: {kategori_dosyasi}")
        return []
