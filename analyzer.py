from google import genai
import json
import time

MY_API_KEY = "BURAYA_API_KEY_GELECEK"

class SentimentAnalyzer:
    def __init__(self):
        try:
            self.client = genai.Client(api_key=MY_API_KEY)
            self.model_id = "gemini-2.5-flash"
        except Exception as e:
            print(f"Connection error: {e}")

    def analyzer_text(self,text):
        if not text:
            return{"error": "Boş metin gönderildi."}
        
        prompt = f"""
                Sen profesyonel bir duygu anazili ve uzmanısın.
                Aşağıdaki metni analiz et.

                {text}

                Lütfen yanıtını SADECE (başka hiçbir açıklama olmadan ) aşağıdaki JSON formatında ver:

                    {
                        {
                            "sentiment": "Pozitif, Negatif, Nötr",
                            "score": "0 ile 100 arasında bir sayı (100 = Çok olumlu)",
                            "summary": "Metnin ana fikri (Maksimum 10 kelime)",
                            "language": "Metnin dili (tr, en, de vb.)"
                        }
                    }

        """
        try:
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=prompt,
                config={
                    'response_mime_type':'application/json'
                })
            clean_text = response.text.replace("```json","").replace("```","").strip()
            result = json.loads(clean_text)
            return result
        except Exception as ex:
            print(f"Hata oluştu: {ex}")

            return {
                 "sentiment": "Hata",
                 "score": 0,
                 "summary": "Analiz sırasında bir hata oluştu",
                 "language": "Bilinmiyor",
                 "error detail": str(ex)
            }



if __name__ == "__main__":
    analizci = SentimentAnalyzer()

    ornek_yorum = "Ürünü çok beğendim, kargo çok hızlı geldi. Teşekkürler.!"

    sonuc = analizci.analyzer_text(ornek_yorum)

    print(sonuc)