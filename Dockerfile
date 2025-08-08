# -------------------------------------------------------------------
# AŞAMA 1: TEMEL İMAJI BELİRLEME
# -------------------------------------------------------------------
# Python'ın resmi, hafif (slim) bir versiyonunu temel olarak kullanıyoruz.
# Bu, imaj boyutunu küçük tutarak daha hızlı indirme ve başlatma sağlar.
FROM python:3.9-slim


# -------------------------------------------------------------------
# AŞAMA 2: ÇALIŞMA ORTAMINI HAZIRLAMA
# -------------------------------------------------------------------
# Container (sanal makine) içinde kodlarımızın yaşayacağı /app adında
# bir çalışma dizini oluşturuyoruz. Sonraki tüm komutlar bu dizin içinden çalışır.
WORKDIR /app


# -------------------------------------------------------------------
# AŞAMA 3: KÜTÜPHANE GEREKSİNİMLERİNİ KURMA
# -------------------------------------------------------------------
# Önce sadece gereksinim dosyasını container'a kopyalıyoruz.
# Bu bir optimizasyon tekniğidir. Kodunuz değişse bile, gereksinimler değişmediği
# sürece Docker bu adımı cache'ten (önbellekten) alarak her seferinde
# kütüphaneleri yeniden indirmekle zaman kaybetmez.
COPY requirements.txt .

# requirements.txt içindeki tüm kütüphaneleri pip kullanarak kuruyoruz.
# --no-cache-dir parametresi, gereksiz cache dosyaları oluşturmayarak imaj boyutunu küçük tutar.
RUN pip install --no-cache-dir -r requirements.txt


# -------------------------------------------------------------------
# AŞAMA 4: PROJE DOSYALARINI KOPYALAMA
# -------------------------------------------------------------------
# Kütüphaneler kurulduktan sonra, geriye kalan tüm proje dosyalarını
# (app.py, .csv dosyası, .md dosyaları vb.) yerel makineden
# container'ın içindeki /app dizinine kopyalıyoruz.
# Sondaki nokta, "bu dizindeki her şeyi" anlamına gelir.
COPY . .


# -------------------------------------------------------------------
# AŞAMA 5: PORTU VE ÇALIŞMA KOMUTUNU AYARLAMA
# -------------------------------------------------------------------
# Streamlit uygulamasının varsayılan olarak çalıştığı 8501 portunu
# container'ın dış dünyaya açmasını söylüyoruz.
EXPOSE 8501

# Container başarıyla oluşturulup başlatıldığında çalıştırılacak olan nihai komut.
# Bu komut, Streamlit uygulamasını başlatır.
# --server.address=0.0.0.0 parametresi, container'ın dışarıdan (yani kendi bilgisayarınızdan)
# erişilebilir olmasını sağlar. Bu parametre olmadan localhost'tan bağlanamazsınız.
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]