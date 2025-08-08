# app.py - Nihai Sürüm v1.2
import streamlit as st
import pandas as pd

# ----------------- SAYFA YAPILANDIRMASI -----------------
# Bu komut her zaman en başta çağrılmalıdır.
st.set_page_config(page_title="Eğitim Takip Sistemi", layout="wide")


# ----------------- UYGULAMA BAŞLIĞI -----------------
st.title("📚 Eğitim Takip Sistemi")
st.write("Öğrencilerin gelişimini takip etmek için hazırlanan sistem.")


# ----------------- VERİ YÜKLEME FONKSİYONU -----------------
# @st.cache_data, performansı artırmak için veri setini hafızada tutar.
@st.cache_data
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        st.error(f"HATA: '{file_path}' adında bir dosya bulunamadı. Lütfen dosyanın doğru klasörde olduğundan emin olun.")
        return pd.DataFrame()


# ----------------- ANA VERİ SETİNİ YÜKLEME -----------------
# CSV dosyasının app.py ile aynı klasörde olduğundan emin olun.
df = load_data('education_tracking_dataset_clean_en.csv')


# ----------------- UYGULAMANIN ANA GÖVDESİ -----------------
# Sadece veri seti başarıyla yüklendiyse çalışır.
if not df.empty:
    
    # --- KENAR ÇUBUĞU (SIDEBAR) ---
    st.sidebar.header("Filtreleme ve Arama")
    
    # 1. Ders Filtresi
    course_list = ["Tümü"] + sorted(df['Course_Name'].unique())
    selected_course = st.sidebar.selectbox("Ders Seçin:", course_list)

    # 2. İsim Arama
    search_name = st.sidebar.text_input("Öğrenci Adı ile Ara:")

    
    # --- FİLTRELEME MANTIĞI ---
    # Adım A: Orijinal verinin temiz bir kopyasıyla başla. (BUG-04 Düzeltmesi)
    filtered_df = df.copy() 

    # Adım B: Ders filtresini uygula.
    if selected_course != "Tümü":
        filtered_df = filtered_df[filtered_df['Course_Name'] == selected_course]

    # Adım C: Arama filtresini uygula (sadece kutu doluysa). (BUG-05 Düzeltmesi)
    if search_name:
        # v1.2 BAKIM GÜNCELLEMESİ: regex=False parametresi, özel karakterlerin hataya yol açmasını engeller.
        filtered_df = filtered_df[filtered_df['Student_Name'].str.contains(search_name, case=False, na=False, regex=False)]

    
    # --- ANALİZ VE GÖRSELLEŞTİRME BÖLÜMÜ ---
    st.subheader("Genel Analizler")
    if not filtered_df.empty:
        # v1.1 BAKIM GÜNCELLEMESİ: Grafik yerine detaylı analiz tablosu eklendi.
        analysis_df = filtered_df.groupby('Course_Name')['Score'].agg(['mean', 'max', 'min']).round(2)
        analysis_df = analysis_df.rename(columns={'mean': 'Ortalama Puan', 'max': 'En Yüksek Puan', 'min': 'En Düşük Puan'})
        
        st.markdown("#### Ders Performans Özeti")
        st.dataframe(analysis_df)
    else:
        st.info("Analiz için gösterilecek veri bulunmamaktadır.")


    # --- FİLTRELENMİŞ KAYITLARI GÖSTERME BÖLÜMÜ ---
    st.subheader("Filtrelenmiş Kayıtlar")
    st.markdown(f"**Toplam {len(filtered_df)} kayıt bulundu.**")
    st.dataframe(filtered_df)

# Veri seti yüklenemezse gösterilecek uyarı
else:
    st.warning("Gösterilecek veri bulunamadı.")
