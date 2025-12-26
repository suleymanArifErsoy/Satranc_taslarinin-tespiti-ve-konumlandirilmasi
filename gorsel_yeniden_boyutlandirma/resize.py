import os
from PIL import Image

def resize_images(input_folder, output_folder, size=(680, 680)):
    """
    Belirtilen klasördeki tüm görselleri hedef piksel boyutuna getirir ve yeni bir klasöre kaydeder.

    :param input_folder: Görsellerin bulunduğu klasör yolu.
    :param output_folder: Yeniden boyutlandırılmış görsellerin kaydedileceği klasör yolu.
    :param size: Hedef piksel boyutu (genişlik, yükseklik). Varsayılan: (85, 85).
    """
    
    # Çıktı klasörünü oluştur, zaten varsa sorun değil (exist_ok=True)
    os.makedirs(output_folder, exist_ok=True)

    # Girdi klasöründeki dosyalar arasında döngü yap
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # Klasörleri atla
        if os.path.isdir(input_path):
            continue

        try:
            # Görseli aç
            img = Image.open(input_path)

            # Görseli yeniden boyutlandır. Image.LANCZOS, yüksek kaliteli yeniden boyutlandırma sağlar.
            resized_img = img.resize(size, Image.LANCZOS)

            # Yeniden boyutlandırılmış görseli kaydet (orijinal dosya formatını koruyarak)
            resized_img.save(output_path)
            print(f"Yeniden boyutlandırıldı ve kaydedildi: {filename}")

        except Exception as e:
            # Görsel olmayan dosyaları veya bozuk görselleri atla
            print(f"Atlandı (Görsel değil veya hata oluştu): {filename}. Hata: {e}")

# --- KULLANIM ÖRNEĞİ ---

# 1. 'girdi_klasoru' adında bir klasör oluşturun ve içine görsellerinizi koyun.
# 2. Aşağıdaki fonksiyonu çağırın:

# resize_images("girdi_klasoru", "cikti_klasoru", size=(85, 85))

resize_images("Satranc_tahtasi","yeni_tahta")