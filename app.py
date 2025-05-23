import streamlit as st
import pandas as pd

# Uygulama başlığı
st.title("\U0001F4BC Maaş Tahmin Uygulaması")

# CSV dosyası yolu
csv_path = "data/output/predicted_salaries.csv"

# CSV okuma ve gösterme
try:
    df = pd.read_csv(csv_path)
    df = df.rename(columns={"id": "ID", "title": "Pozisyon", "prediction": "Maaş Tahmini (USD)"})

    st.success("Tahmin verisi başarıyla yüklendi!")

    # Tüm veriyi göster
    st.subheader("Önceden Tahmin Edilmiş Veriler")
    st.dataframe(df)

    # Arama kutusu
    pozisyon_ara = st.text_input("Pozisyon Ara (\"Data Scientist\" gibi):")

    if pozisyon_ara:
        filtreli_df = df[df["Pozisyon"].str.contains(pozisyon_ara, case=False, na=False)]
        st.subheader("\U0001F4CA Filtrelenmiş Sonuçlar")
        st.dataframe(filtreli_df)

except FileNotFoundError:
    st.warning("CSV dosyası bulunamadı. Lütfen doğru yolda .csv dosyasını yerleştirin.")

# Kullanıcı girdisi formu (Tahmin yok)
st.subheader("\u2728 Yeni Pozisyon Bilgisi Girişi")
with st.form("form"):
    pozisyon = st.text_area("Pozisyon Açıklaması", "We are looking for a data scientist...")
    deneyim = st.selectbox("Deneyim Seviyesi", ["Junior", "Orta", "Kıdemli"])
    calisma = st.selectbox("Çalışma Tipi", ["Tam Zamanlı", "Yarı Zamanlı", "Hibrit"])
    buyukluk = st.selectbox("Şirket Büyüklüğü", ["Küçük", "Orta", "Büyük"])
    ulke = st.selectbox("Şirket Ülkesi", ["Türkiye", "ABD", "Almanya", "Hindistan"])
    remote = st.selectbox("Remote Tipi", ["Uzaktan", "Hibrit", "Ofis"])
    kita = st.selectbox("Kıta", ["Avrupa", "Kuzey Amerika", "Asya"])
    yil = st.slider("Yıl", 2018, 2025, 2024)
    submit = st.form_submit_button("Tahmin Et")

if submit:
    st.info("Bu demo sürümde tahmin işlemi aktif değildir. Girdiğiniz bilgiler başarıyla alındı.")
