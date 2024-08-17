import random

def tas_kagit_makas_BEDIRHAN_ELCIN():
    print("Taş, Kağıt, Makas oyununa hoş geldiniz!")
    print("Kurallar: Taş makası, makas kağıdı, kağıt da taşı yener.")
    print("İlk iki turu kazanan oyunu kazanır.")
    print("Bol şans! 🎉\n")

    oyun_sayisi = 1  # Kaç oyun oynandığını takip etmek için sayaç

    while True:
        print(f"\n{oyun_sayisi}. Oyun başlıyor.................")  # Hangi oyunun başladığını gösteriyoruz
        oyuncu_galibiyet = 0
        bilgisayar_galibiyet = 0
        tur_sayisi = 1  # Her oyun başında tur sayısını sıfırlıyoruz

        while oyuncu_galibiyet < 2 and bilgisayar_galibiyet < 2:
            print(f"\n{oyun_sayisi}. oyun, {tur_sayisi}. tur başlıyor...")
            tur_sayisi += 1  # Tur sayısını her seferinde artırıyoruz

            # Oyuncu seçimi
            oyuncu_secimi = input("Lütfen birini seçin (Taş, Kağıt, Makas): ").lower()

            while oyuncu_secimi not in ["taş", "kağıt", "makas"]:
                oyuncu_secimi = input("Geçersiz seçim. Lütfen tekrar seçin (Taş, Kağıt, Makas): ").lower()

            # Bilgisayar seçimi
            bilgisayar_secimi = random.choice(["taş", "kağıt", "makas"])
            print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")

            # Sonuçları belirleme
            if oyuncu_secimi == bilgisayar_secimi:
                print("Beraberlik! Her iki taraf da eşit.")
            elif (oyuncu_secimi == "taş" and bilgisayar_secimi == "makas") or \
                    (oyuncu_secimi == "makas" and bilgisayar_secimi == "kağıt") or \
                    (oyuncu_secimi == "kağıt" and bilgisayar_secimi == "taş"):
                print("Bu turu kazandınız! 👏")
                oyuncu_galibiyet += 1

                # Özel kazanç mesajları
                if oyuncu_galibiyet == 1:
                    print("İlk turu kazandınız, iyi başlangıç!")
                elif oyuncu_galibiyet == 2:
                    print("İkinci turu da kazandınız, harikasınız!")
            else:
                print("Bu turu bilgisayar kazandı! 🤖")
                bilgisayar_galibiyet += 1

                # Özel bilgisayar kazanç mesajları
                if bilgisayar_galibiyet == 1:
                    print("Bu gün şanslı günündeyim sanırım!")
                elif bilgisayar_galibiyet == 2:
                    print("Bilgisayar bu oyunu kazandı, belki bir dahaki sefere.")

            print(f"Durum - Oyuncu: {oyuncu_galibiyet}, Bilgisayar: {bilgisayar_galibiyet}")

        # Genel galibi belirleme
        if oyuncu_galibiyet == 2:
            print("\nTebrikler, oyunu kazandınız! 🎉")
        else:
            print("\n Bilgisayar oyunu kazandı. Şans Benden yana sanırım :), bir dahaki sefere! 🍀")

        # Devam etmek isteyip istememe kontrolü
        devam_etme = input("Başka bir oyun oynamak ister misiniz? (Evet/Hayır): ").lower()
        bilgisayar_devam = random.choice(["evet", "hayir"])

        if devam_etme == "hayir" or bilgisayar_devam == "hayir":
            print("Oyun sona erdi. Teşekkürler! 🖐️")
            if bilgisayar_devam == "hayir":
                print("Bilgisayar: Bu benim için çok zevkliydi 🎮 görüşmek üzere Bedirhan 🖐️! ")
            break
        else:
            oyun_sayisi += 1  # Yeni bir oyun başlarsa, oyun sayısını artırıyoruz
            print("Oyun yeniden başlıyor...\n")

# Fonksiyonu çalıştırmak için:
tas_kagit_makas_BEDIRHAN_ELCIN()
