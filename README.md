# Taş, Kağıt, Makas Oyunu 🎮

Aygaz Python Bootcamp 2024 için Bedirhan Elçin tarafından geliştirilen Taş, Kağıt, Makas oyununa hoş geldiniz! 🤗

## Proje Genel Bakış

Bu Python tabanlı Taş, Kağıt, Makas oyunu, oyuncuların bilgisayara karşı mücadele edebileceği bir oyundur. Oyun, etkileşimli bir konsol arayüzü ile tasarlanmıştır ve oyuncu ile bilgisayar sonuçları için kişiselleştirilmiş mesajlar içerir.

## Oyun Kuralları

- **Taş**, **Makas**'ı yener ✊✂️
- **Makas**, **Kağıt**'ı yener ✂️📄
- **Kağıt**, **Taş**'ı yener 📄✊

İlk olarak 2 turu kazanan oyuncu (veya bilgisayar) oyunu kazanır. 🏆

## Özellikler

- **Etkileşimli Konsol Arayüzü**: Oyun, oyuncuya her turda açık talimatlar ve sonuçlar sunar.
- **Hata Yönetimi**: Oyuncu seçimlerini doğrulamak için giriş validasyonu sağlar.
- **Kişiselleştirilmiş Mesajlar**: Hem oyuncu hem de bilgisayarın zaferleri ve özel koşullar için özel mesajlar içerir.
- **Yeniden Oynama Seçeneği**: Oyuncuya oyunu bitirdikten sonra yeni bir oyun başlatma seçeneği sunar.

## Nasıl Çalıştırılır ?

1. Sistemde Python yüklü olduğundan emin olun.
2. Bu repository'yi bilgisayarınıza indirin veya klonlayın.
3. `tas_kagit_makas_BEDIRHAN_ELCIN.py` dosyasının bulunduğu dizine gidin.
4. Python ile script'i çalıştırın:

   ```bash
   python tas_kagit_makas_BEDIRHAN_ELCIN.py

## Kod Açıklaması

- **Fonksiyon Tanımı**: `tas_kagit_makas_BEDIRHAN_ELCIN()` ana fonksiyon olup oyun mantığını yönetir.
- **Oyun Başlatma**: Oyuncuya hoş geldin mesajı ile oyun kurallarını açıklar.
- **Oyun Döngüsü**: İki iç içe döngü ile genel oyun ve her bir turu yönetir.
  - **Genel Oyun Döngüsü**: Oyuncu veya bilgisayar 2 tur kazanana kadar devam eder.
  - **Tur Döngüsü**: Her turda oyuncunun ve bilgisayarın seçimini alır ve sonucu değerlendirir.
- **Oyuncu ve Bilgisayar Seçimleri**: Oyuncudan giriş alır, bilgisayarın seçimi ise rastgele belirlenir.
- **Sonuç Değerlendirmesi**: Seçimleri karşılaştırarak her tur için kazananı belirler. Galibiyet sayısını takip eder ve kişiselleştirilmiş mesajlar gösterir.
- **Yeniden Oynama Seçeneği**: Oyuncuya oyunu tekrar oynamak isteyip istemediğini sorar ve verilen cevaba göre oyunu yeniden başlatır veya sonlandırır.

### Kod Örnekleri

İşte oyunun ana fonksiyonundan bazı önemli kod bölümleri:

```python
# Oyuncu seçimi yapılması
oyuncu_secimi = input("Lütfen birini seçin (Taş, Kağıt, Makas): ").lower()

# Bilgisayarın rastgele seçim yapması
bilgisayar_secimi = random.choice(["taş", "kağıt", "makas"])
print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")

# Sonuç değerlendirme ve mesajların gösterimi
if oyuncu_secimi == bilgisayar_secimi:
    print("Beraberlik! Her iki taraf da eşit.")
elif (oyuncu_secimi == "taş" and bilgisayar_secimi == "makas") or \
     (oyuncu_secimi == "makas" and bilgisayar_secimi == "kağıt") or \
     (oyuncu_secimi == "kağıt" and bilgisayar_secimi == "taş"):
    print("Bu turu kazandınız! 👏")
else:
    print("Bu turu bilgisayar kazandı! 🤖")




## Katkı ve Geri Bildirimler 🤝

Projeye ait katkı ve geri bildirimlerinizi bekliyorum. 🤝








   
