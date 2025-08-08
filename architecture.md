# Sistem Mimarisi (Architecture)

## 🎯 Amaç

Bu mimari, Eğitim Takip Sistemi’nin nasıl çalıştığını, hangi katmanlardan oluştuğunu ve veri akışının nasıl gerçekleştiğini açıklamak için oluşturulmuştur.

---

## 🧱 Katmanlı Yapı (Layered Architecture)

1. **Veri Katmanı (Data Layer)**
   - `education_tracking_dataset_clean_en.csv` dosyasındaki veriler.
   - SQL Server veritabanına aktarılmış hali.
   - CRUD işlemleri bu katmandan yapılır.

2. **İş Katmanı (Business Layer)**
   - Veri analizleri, istatistiksel işlemler, performans ölçümleri.
   - İlerleyen fazlarda makine öğrenmesi ve karar destek sistemleri burada yer alır.

3. **Sunum Katmanı (Presentation Layer)**
   - Veri görselleştirme (Power BI, Matplotlib vs.)
   - Web arayüzü (ileride Flask, HTML/CSS ile geliştirilebilir)
   - Kullanıcıya sonuçların sade şekilde sunulduğu arayüzdür.

---

## 🔄 Veri Akışı

