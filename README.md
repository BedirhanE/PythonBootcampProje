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

#Kod Açıklaması
Fonksiyon Tanımı: tas_kagit_makas_BEDIRHAN_ELCIN() ana fonksiyondur ve oyun mantığını yönetir.
Oyun Başlatma: Oyuncuyu karşılar ve kuralları açıklar.
Oyun Döngüsü: Genel oyun ve bireysel turlar için iki iç içe döngü içerir.
Oyuncu ve Bilgisayar Seçimleri: Oyuncu seçim yapar ve bilgisayarın seçimi rastgele üretilir.
Sonuç Değerlendirmesi: Seçimleri karşılaştırarak her tur kazananını belirler ve zaferleri takip eder.
Yeniden Oynama Seçeneği: Oyuncunun tekrar oynamak isteyip istemediğini sorar ve yanıtı işler.




   
