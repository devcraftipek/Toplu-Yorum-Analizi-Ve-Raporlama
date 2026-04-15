from analyzer import SentimentAnalyzer
import os

analizci = SentimentAnalyzer()
dosya_yolu = "yorumlar.txt"
rapor_yolu ="analiz_raporu.txt"

print("Analiz sistemi başlatılıyor...")

sonuclar = []

if os.path.exists(dosya_yolu):
    with open(dosya_yolu,"r", encoding ="utf-8") as f:
        satirlar = f.readlines()

    print(f"Toplam {len(satirlar)} adet yorum bulundu. İşleniyor...")


    for  satir in satirlar:
        yorum = satir.strip()
        if not yorum: continue

        print(f"İnceleniyor: {yorum}")

        analiz_sonucu = analizci.analyzer_text(yorum)
        sonuclar.append(analiz_sonucu)


    print("\n Tüm yorumlar analiz edildi. Rapor hazırlanıyor...")

    toplam_yorum = len(sonuclar)
    pozitif_sayisi = sum(1 for x in sonuclar if x ['sentiment'] == 'Pozitif')
    negatif_sayisi = sum(1 for x in sonuclar if x ['sentiment'] == 'Negatif')
    notr_sayisi = toplam_yorum - (pozitif_sayisi + negatif_sayisi)

    en_mutlu = max(sonuclar, key = lambda x: int(x['score']))
    en_kızgın = min(sonuclar, key = lambda x: int(x['score']))

    #raporu dosyaya yaz

    rapor_icerigi = f"""
        --- DUYGU ANALİZİ RAPORU ---

        Genel Durum
        -----------------
        Toplam Yorum: {toplam_yorum}
        Pozitif     : {pozitif_sayisi}
        Negatif     : {negatif_sayisi}
        Nötr     : {notr_sayisi}

        En Mutlu Müşteri ({en_mutlu['score']} Puan)

        En Kızgın Müşteri ({en_kızgın['score']} Puan)

    """

    with open(rapor_yolu,"w", encoding="utf-8") as f:
        f.write(rapor_icerigi)

    print(f"Rapor oluşturuldu.")

else:
    print("Dosya bulunamadı.")

    