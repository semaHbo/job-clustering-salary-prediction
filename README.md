# 💼 Job Clustering & Salary Prediction

Bu proje, gerçek dünyadaki iş ilanlarını analiz ederek, pozisyon açıklamalarına göre pozisyonları kümeler ve makine öğrenmesi ile maaş tahmini yapar. Doğal dil işleme (NLP), Word2Vec ve PySpark ML modelleri kullanılarak gerçekleştirilmiştir. Streamlit ile etkileşimli arayüz sunulmuştur.

---

## ⚠️ Uyarı – Bu Proje Bir Demodur

Bu uygulama, **eğitim ve gösterim amaçlı bir demo projedir**. Yapay zeka ve makine öğrenmesi teknikleriyle maaş tahmini yapılmaktadır.

---

## 🧠 Projenin Amacı

- 📌 İş ilanlarını pozisyon açıklamasına göre analiz etmek
- 📌 Word2Vec ile pozisyon açıklamalarını vektörleştirmek
- 📌 Spark ML ile maaş tahmini yapmak
- 📌 Tahmin sonuçlarını kullanıcıya sade ve şık bir arayüzle sunmak

---

## 🧰 Kullanılan Teknolojiler

| Katman | Teknoloji |
|--------|-----------|
| Backend (model) | PySpark, Google Colab |
| Frontend | Streamlit |
| ML Model | `GBTRegressor` (Gradient Boosted Trees) |
| NLP | `Tokenizer`, `Word2Vec` |
| Özellik mühendisliği | `StringIndexer`, `VectorAssembler` |
| Veri işleme | pandas, numpy |
| Ortam | Windows + Colab + GitHub |

---

## 🔍 Kullanılan Python Kütüphaneleri

```
pyspark
pandas
numpy
streamlit
```

requirements.txt ile yüklenebilir.

---

## 🗂️ Klasör Yapısı

```
job-clustering-salary-prediction/
│
├── app.py                          # Streamlit arayüz dosyası
├── data/
│   └── output/
│       └── predicted_salaries.csv # Colab'da üretilen maaş tahmin çıktısı
│
├── models/
│   └── gbt_salary_model/          # Kaydedilmiş Spark GBTRegressor modeli
│
├── notebooks/
│   └── model_training_2.ipynb     # Model eğitimi ve kayıt
│   └── predict_jobs.ipynb         # Yeni ilanlara tahmin uygulama
│
└── README.md                      # Bu dosya
```

---

## ⚙️ Kurulum ve Çalıştırma

### 1. Reponun klonlanması

```
git clone https://github.com/kullanici_adi/job-clustering-salary-prediction.git
cd job-clustering-salary-prediction
```

### 2. Sanal ortam (isteğe bağlı)

```
python -m venv venv
.env\Scriptsctivate
```

### 3. Gerekli kütüphanelerin kurulumu

```
pip install -r requirements.txt
```

### 4. Streamlit uygulamasını başlat

```
streamlit run app.py
```

---

## 🧪 Model Eğitimi Süreci (Google Colab)

1. `model_training_2.ipynb` notebook'u açılır
2. Spark kurulumu yapılır
3. Pozisyon açıklaması `Word2Vec` ile vektörleştirilir
4. Kategorik değişkenler `StringIndexer` ile encode edilir
5. Özellikler `VectorAssembler` ile birleştirilir
6. `GBTRegressor` ile model eğitilir
7. Model `.save()` ile `models/gbt_salary_model/` dizinine kaydedilir

---

## 🔍 Yeni İlanlara Tahmin (Colab)

1. `predict_jobs.ipynb` dosyası açılır
2. Yeni ilanlar aynı öznitelikler ile hazırlanır
3. Eğitilen model ile tahmin yapılır
4. Tahminler `.csv` olarak `data/output/predicted_salaries.csv` dosyasına kaydedilir
5. Bu dosya Streamlit uygulaması tarafından okunur

---

## 🔄 Canlı Tahmin Özelliği Hakkında

Bu uygulama şu anda **canlı tahmin yapmamaktadır.**  
Kullanıcı tarafından girilen yeni ilanlar, doğrudan sistem tarafından değerlendirilip tahmin edilmez.

Tahmin süreci şu şekilde çalışmaktadır:

- Maaş tahminleri, Spark modelleri kullanılarak **Google Colab üzerinde** yapılır.
- Elde edilen sonuçlar `.csv` formatında dışa aktarılır.
- Bu tahmin çıktısı (`predicted_salaries.csv`), Streamlit arayüzüne manuel olarak yüklenir.
- Uygulama sadece bu `.csv` dosyasındaki verileri gösterir ve filtreleme yapar.

🔧 Canlı tahmin özelliği, ileride bir REST API veya Spark destekli servis ile entegre edilebilir.

---

## 🌐 Yayınlama (Streamlit Cloud)

Projeyi GitHub’a yükledikten sonra:

1. [https://streamlit.io/cloud](https://streamlit.io/cloud) adresine git
2. “New App” → Reponu seç
3. `app.py` dosyasını göster → `Deploy`

🎯 **Uygulaman artık internetten erişilebilir.**

---

## 📌 Bilinen Sınırlamalar

- Spark modelleri Windows’ta `UnsatisfiedLinkError` hatası verebilir.
- Bu nedenle model eğitimi ve tahmini **Colab üzerinden yapılır.**
- Streamlit uygulaması sadece `.csv` üzerinden veri gösterir (demo ortamda).

---

## 🤝 Katkıda Bulun

Pull request’ler her zaman kabul edilir. Hataları, önerileri ve katkıları bekliyorum!

---
