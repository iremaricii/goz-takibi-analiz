# 👁️ Göz Takibi ile Dikkat Algılama Sistemi

Bu proje, MediaPipe Face Mesh ve OpenCV kullanarak gerçek zamanlı olarak göz takibi yapar.  
Kullanıcının dikkatinin dağılması durumunda sesli ve görsel uyarılar verir.

## 🎯 Özellikler

- Gerçek zamanlı göz takibi
- Göz iris konumuna göre dikkat analizi (yukarı, aşağı, sağa, sola bakış algılama)
- Göz kapanması veya kameradan çıkılması durumunda uyarı
- Sesli uyarı (🔔 `uyari.wav` dosyası)
- Pygame ile sürekli çalan/duran uyarı mekanizması

## 🧠 Kullanılan Teknolojiler

- [MediaPipe Face Mesh](https://google.github.io/mediapipe/)
- [OpenCV](https://opencv.org/)
- [Pygame](https://www.pygame.org/) (sesli uyarı için)
- Python


## 📷 Örnek Ekran Görüntüsü

### ✅ Odaktayken (sistem sessiz)

  
![image](https://github.com/user-attachments/assets/e1bbe0be-899a-454a-a1c0-889e32e7fe3e)  

"Göz takip ediliyor" mesajı görünür, kullanıcı ekrana bakıyordur. Sistem sessizdir.

### ❌ Dikkat Dağınıklığında (uyarı mesajı + ses)

![image](https://github.com/user-attachments/assets/61e275b2-26af-4ddb-bf12-9d4e00c389e6)

"Dikkatin dağıldı!" uyarısı çıkar ve sesli alarm çalar. Göz algılanmamış olabilir veya iris merkezde değildir
