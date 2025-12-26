♟️ Deep Learning Based Chess Piece Detection & Board Analysis

Bu proje, sanal bir satranç tahtası üzerindeki taşları Evrişimli Sinir Ağları (CNN) kullanarak %97 doğrulukla tespit eden ve konumlarını (a8, h1 vb.) belirleyen uçtan uca bir bilgisayarlı görü (computer vision) çalışmasıdır.

📌 Proje Özeti
Projenin temel amacı, 710x710 piksel boyutundaki sanal satranç tahtası görsellerini analiz ederek tahta üzerindeki taşların türünü, rengini ve koordinatlarını belirlemektir. Sistem, büyük resmi 680x680 boyutuna normalize eder ve 8x8'lik bir ızgara yapısında her hücreyi bağımsız olarak sınıflandırır.

🚀 Öne Çıkan Özellikler
13 Sınıflı Sınıflandırma: 12 farklı taş türü ve "Boş Kare" tespiti.

Grid Classification: Nesne tespiti yerine, tahta geometrisinden faydalanan optimize edilmiş tarama algoritması.

Koordinat Dönüşümü: Tespit edilen her taşı uluslararası satranç notasyonuna (a1-h8) çevirme.

Gelişmiş Eğitim Teknikleri: Class Weighting, Data Augmentation, EarlyStopping ve ModelCheckpoint entegrasyonu.

📊 Veri Seti Bilgileri
Projede Kaggle - Chess Pieces Dataset (85x85) veri seti temel alınmış ve chess.com sayfası üzerinde çeşitli taş biçimleri ve satranç tahalarının kombinasyonlarıyla genişletilmiştir.

Toplam Görsel: 807 adet 85x85 piksel görsel.

Dağılım: %80 Eğitim (651 görsel), %20 Doğrulama (156 görsel).

Sınıflar: beyaz_at, siyah_at, beyaz_fil, siyah_fil, beyaz_kale, siyah_kale, beyaz_piyon, siyah_piyon, beyaz_sah, siyah_sah, beyaz_vezir, siyah_vezir, empty.


🛠️ Kurulum ve Kullanım
1. Gereksinimler
pip install tensorflow opencv-python numpy matplotlib scikit-learn

📂 Dosya Yapısı
chess_data/: Eğitim ve test görselleri.

satranc_modelim_en_iyi.h5: Kaydedilmiş en başarılı model ağırlıkları.

sinif_isimleri.json: Sınıf etiketleri haritası.






