# 📘 Beni Oku – Hızlı Bakış

Bu proje, öğretmenlerin öğrenci notlarını ve yoklama verilerini sistematik bir şekilde takip edebilmesini; öğrencilerin ise kendi akademik performanslarını görüntüleyebilmesini sağlayan SQL tabanlı bir eğitim takip sistemidir.

Proje kapsamında:
- Gerçekçi ve yapılandırılmış bir veri seti oluşturulmuştur,
- SQL Server ortamında veri aktarımı gerçekleştirilmiştir,
- Sistem gereksinimleri analiz edilip dokümante edilmiştir,
- Kodlama öncesi tüm analiz aşamaları tamamlanmıştır.

Bu proje, veri bilimi ve yazılım mühendisliği süreçlerini bir araya getiren uygulamalı bir örnektir.
## 💡 Bu Projeden Ne Öğrenebilirsiniz?

- SQL Server ile CSV veri aktarımı
- Veri analizi için veritabanı hazırlığı
- Yazılım geliştirme sürecinin(SDLC) 5 Fazı
- Fonksiyonel gereksinim yazımı ve dökümantasyon
## 👨‍💻 Bu Proje Kimler İçin Uygundur?

- Veri bilimi öğrencileri
- Yazılım geliştirme sürecini öğrenmek isteyenler
- SQL tabanlı uygulama yapmak isteyen geliştiriciler
- Eğitim sektörü için dijital çözümler arayanlar                                                                                                                                                                                                                                                                                                                                                                                            Bu proje, yazılım geliştirme süreçlerini öğrenmek ve uygulamak amacıyla 5 fazlı yaklaşıma uygun olarak yapılandırılmıştır.
## Dockerized
Bu proje, öğrenci performans verilerini analiz etmek ve görselleştirmek amacıyla, tam bir yazılım geliştirme yaşam döngüsü (SDLC) simülasyonu ile geliştirilmiş, interaktif bir web uygulamasıdır. Proje, Docker ile paketlenerek her ortamda çalışmaya hazır hale getirilmiştir.

### 📸 Uygulama Ekran Görüntüsü

<!-- ![Proje-3 arayüzü](https://github.com/user-attachments/assets/7f4b4951-705a-4b40-a121-e26f939d1622)
 -->
---

### ✨ Canlı Uygulama ✨

Uygulamanın çalışan versiyonuna aşağıdaki linke tıklayarak erişebilirsiniz:

**[Uygulamayı Canlı Görüntülemek İçin Buraya Tıklayın](https://lenakeskin-veri-tabanli-egitim-takip-sistemi--app-n885b1.streamlit.app/)**

---

### 🔄 Proje Geliştirme Fazları

Bu proje, aşağıdaki beş ana fazda geliştirilmiştir:

#### **Faz 1: Analiz**
Bu ilk aşamada, projenin gereksinimleri ve hedefleri belirlenmiştir.
*   **Problem Tanımı:** Öğrenci not, devam ve performans verilerini tek bir yerden takip etme ve analiz etme ihtiyacı tespit edildi.
*   **Gereksinimler:** Sistemin veriyi gösterebilmesi, ders ve öğrenci adına göre filtrelenebilmesi, temel istatistiksel analizler sunabilmesi ve kullanıcı dostu bir arayüze sahip olması gerektiği kararlaştırıldı.
*   **Veri Seti:** Analiz için kullanılacak olan `education_tracking_dataset_clean_en.csv` veri seti incelendi ve yapısal özellikleri anlaşıldı.

#### **Faz 2: Tasarım**
Analiz fazında belirlenen gereksinimlere göre sistemin mimari ve arayüz tasarımı yapıldı.
*   **Mimari Tasarım:** Projenin hızlı bir şekilde prototiplenebilmesi için, tek bir `app.py` dosyası üzerinden çalışacak, veriyi CSV'den okuyacak basit ve etkili bir mimari seçildi.
*   **Arayüz Tasarımı (UI/UX):** Kullanıcı etkileşimini kolaylaştırmak amacıyla, kontrol elemanlarının (filtreler, arama kutusu) bir kenar çubuğunda (sidebar), sonuçların ise ana ekranda gösterildiği bir yerleşim planı tasarlandı.
*   **Teknoloji Seçimi:** Arayüz için Streamlit, veri işleme için Pandas kütüphanelerinin kullanılmasına karar verildi.

#### **Faz 3: Kodlama (Implementation)**
Tasarım doğrultusunda, uygulamanın fonksiyonları Python dili kullanılarak kodlandı.
*   Veri yükleme, filtreleme, arama ve analiz mantığı Pandas kütüphanesi ile yazıldı.
*   Tüm bu fonksiyonlar, Streamlit kütüphanesi kullanılarak interaktif bir web arayüzüne dönüştürüldü.
*   Bu fazın sonunda, projenin test edilmeye hazır ilk çalışan versiyonu (v1.0) ortaya çıktı.

#### **Faz 4: Test**
Kodlanan sistemin doğruluğunu, kararlılığını ve performansını ölçmek için sistematik bir test süreci yürütüldü.
*   **Planlama ve Dokümantasyon:** `test_plan.md`, `test_cases.md` gibi belgelerle test süreci planlandı.
*   **Hata Tespiti ve Giderme:** Uygulanan test senaryoları sonucunda `BUG-04` ve `BUG-05` gibi başlangıç hataları tespit edildi ve kod üzerinde gerekli düzeltmeler yapılarak giderildi.
*   **Raporlama:** Tüm test süreci, sonuçları ve çözümleriyle birlikte `Test_Sonuclari.xlsx` ve `test_sonuc_raporu.md` dosyaları ile belgelendi.

#### **Faz 5: Bakım**
Projenin ilk stabil sürümü yayınlandıktan sonraki yaşam döngüsünü simüle etmek amacıyla bir bakım fazından geçirilmiştir.
*   **İyileştirici Bakım (v1.1):** Kullanıcı talebine yanıt olarak, analiz paneli `.agg()` fonksiyonu kullanılarak daha detaylı bir tabloya dönüştürüldü.
*   **Düzeltici Bakım (v1.2):** Sonradan fark edilen bir arama hatası (`+` karakteri sorunu), `regex=False` parametresi ile giderilerek sistemin kararlılığı artırıldı.

---

### 🐳 Paketleme ve Dağıtım (Docker)

Geliştirme döngüsünün sonunda, uygulamanın her ortamda tutarlı bir şekilde çalışabilmesi için Docker teknolojisi kullanılarak bir container içine paketlenmiştir. `Dockerfile` ve `requirements.txt` dosyaları oluşturularak, proje tek bir komutla çalıştırılabilir, taşınabilir ve dağıtıma hazır bir hale getirilmiştir.

---

### 🛠️ Kullanılan Teknolojiler

*   **Arayüz & Framework:** Streamlit
*   **Programlama Dili:** Python
*   **Veri Analizi & Manipülasyonu:** Pandas
*   **Container Teknolojisi:** Docker

---

### 💻 Projeyi Yerel Olarak Çalıştırma

#### **Yöntem 1: Docker ile (Tavsiye Edilen)**
```bash
# 1. Docker imajını oluşturun
docker build -t egitim-takip-sistemi .

# 2. Container'ı çalıştırın
docker run -p 8501:8501 egitim-takip-sistemi
