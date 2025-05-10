from kategori_secim import kategori_secimi
from test import Quiz
from soru_yukleyici import soru_yukle


def basla(kategori_dosyasi):
    sorular = soru_yukle(kategori_dosyasi)
    quiz = Quiz(sorular)
    quiz.sorulari_goster()


kategori = kategori_secimi()
basla(kategori)

