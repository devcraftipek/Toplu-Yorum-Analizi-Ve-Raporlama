# 📊 Toplu Yorum Analizi Ve Raporlama Sistemi

Bu proje, yapay zeka (Gemini API) kullanarak metin tabanlı müşteri yorumlarını analiz eden ve bunları detaylı bir duygu raporuna dönüştüren bir Python aracıdır.
## ✨ Özellikler
- **Yapay Zeka Destekli:** Google Gemini 2.5 Flash modeli ile yüksek doğrulukta duygu tespiti.
- **Toplu İşleme:** `yorumlar.txt` dosyasındaki yüzlerce satırı tek seferde okur.
- **Detaylı Raporlama:** Analiz sonunda Pozitif/Negatif/Nötr dağılımını ve en uç örnekleri (en mutlu/en kızgın) raporlar.
- **JSON Yapısı:** API yanıtlarını standart JSON formatında işleyerek hata payını minimize eder.

- Kullanım
1. yorumlar.txt dosyasına analiz etmek istediğiniz yorumları her satıra bir tane gelecek şekilde ekleyin.

2. Ana programı çalıştırın:

Bash
python main.py

3. İşlem bittiğinde analiz_raporu.txt dosyasını kontrol edin.
4. Dosya Yapısı
main.py: Dosya okuma, döngü yönetimi ve raporlama mantığı.

analyzer.py: Gemini API bağlantısı ve duygu analizi sınıfı.

yorumlar.txt: Giriş verileri.

analiz_raporu.txt: Çıktı raporu.

👩‍💻 Geliştirici
İpek Nur Günümdoğdu
<img width="1399" height="822" alt="2" src="https://github.com/user-attachments/assets/6b9a8a11-491b-4902-b58a-025ae4717500" />
<img width="1022" height="798" alt="1" src="https://github.com/user-attachments/assets/14ddb525-22f3-4c32-ba1c-26e834476e4e" />
