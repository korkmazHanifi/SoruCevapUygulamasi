from soru import Soru

class Quiz:
    def __init__(self, sorular):
        self.sorular = sorular
        self.skor = 0

    def sorulari_goster(self):
        for soru in self.sorular:
            print(soru.metin)
            for secenek in soru.secenekler:
                print(secenek)
            cevap = input("Cevabınızı girin (çıkmak için 'q'): ")

            if cevap.lower() == "q":
                print("Quizden çıkılıyor.")
                break
            elif cevap.upper() == soru.dogru_cevap:
                self.skor += 1
                print("Doğru cevap!")
            else:
                print(f"Yanlış cevap! Doğru cevap: {soru.dogru_cevap}")
                print()  # Her sorudan sonra boşluk bırak

        print(f"Quiz bitti! Toplam puanınız: {self.skor}/{len(self.sorular)}")

