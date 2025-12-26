import cv2
import os
import glob
import random

# --- AYARLAR ---
KAYNAK_KLASOR = "Satranc_tahtasi"    # Tahta resimlerinin olduğu klasör
HEDEF_KLASOR = "Empty"  # Çıktı klasörü
HEDEF_BOYUT = (85, 85)            # Model giriş boyutu
ORNEK_SAYISI = 10                 # Her resimden kaç tane rastgele kare alınacak

def rastgele_kare_uret():
    # Hedef klasör yoksa oluştur
    if not os.path.exists(HEDEF_KLASOR):
        os.makedirs(HEDEF_KLASOR)

    # Klasördeki tüm resim formatlarını bul
    resim_listesi = glob.glob(os.path.join(KAYNAK_KLASOR, "*.jpg")) + \
                    glob.glob(os.path.join(KAYNAK_KLASOR, "*.png")) + \
                    glob.glob(os.path.join(KAYNAK_KLASOR, "*.jpeg"))

    print(f"Toplam {len(resim_listesi)} adet tahta görseli bulundu.")
    toplam_kaydedilen = 0

    for resim_yolu in resim_listesi:
        img = cv2.imread(resim_yolu)
        if img is None:
            continue

        dosya_adi = os.path.basename(resim_yolu).split('.')[0]
        h, w, _ = img.shape
        
        # Kare boyutlarını hesapla (Margin yok, tam bölme)
        step_x = w // 8
        step_y = h // 8

        # --- RASTGELE SEÇİM MANTIĞI ---
        # Olası tüm koordinatları (0,0)'dan (7,7)'ye kadar listele
        tum_kareler = [(row, col) for row in range(8) for col in range(8)]
        
        # Bu listeden rastgele 10 tanesini seç
        secilen_kareler = random.sample(tum_kareler, ORNEK_SAYISI)
        
        print(f"İşleniyor: {dosya_adi} -> Rastgele {ORNEK_SAYISI} kare seçiliyor...")

        for (row, col) in secilen_kareler:
            # Koordinatları hesapla
            x1 = col * step_x
            y1 = row * step_y
            x2 = (col + 1) * step_x
            y2 = (row + 1) * step_y
            
            # Kırp
            kare = img[y1:y2, x1:x2]
            
            # Hata önleyici kontrol
            if kare.size == 0: continue
            
            # Boyutlandır
            kare_resized = cv2.resize(kare, HEDEF_BOYUT)
            
            # Kaydet (Dosya ismine random kod eklemeye gerek yok, row/col yeterli)
            yeni_isim = f"Empty_{dosya_adi}_r{row}_c{col}.jpg"
            kayit_yolu = os.path.join(HEDEF_KLASOR, yeni_isim)
            
            cv2.imwrite(kayit_yolu, kare_resized)
            toplam_kaydedilen += 1

    print(f"\nİşlem Tamamlandı!")
    print(f"Toplam {toplam_kaydedilen} adet rastgele boş kare '{HEDEF_KLASOR}' içine kaydedildi.")

if __name__ == "__main__":
    rastgele_kare_uret()