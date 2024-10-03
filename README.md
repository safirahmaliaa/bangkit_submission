## Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis data penyewaan sepeda dari sistem Capital Bikeshare di Washington D.C. pada tahun 2011 dan 2012. Analisis ini berfokus pada pengaruh kelembapan dan waktu sewa terhadap pola penyewaan sepeda. Dashboard interaktif yang dibuat menggunakan Streamlit memberikan visualisasi yang jelas tentang hasil analisis.

## Struktur Folder
```
submission
├───dashboard
|   ├───main_data.csv          # Data utama untuk dashboard
|   └───dashboard.py           # Skrip untuk menjalankan dashboard Streamlit
├───data
|   ├───data_1.csv             # Dataset pertama
|   └───data_2.csv             # Dataset kedua
├───notebook.ipynb             # Jupyter Notebook untuk analisis
├───README.md                   # Dokumentasi proyek
└───requirements.txt            # Daftar dependensi Python
└───url.txt                    # URL untuk data atau sumber lainnya
```

## Instalasi
Untuk menjalankan proyek ini, pastikan untuk menginstal semua dependensi yang diperlukan. Gunakan perintah berikut:

```bash
pip install -r requirements.txt
```

## Menjalankan Dashboard
Setelah semua dependensi terinstal, jalankan dashboard menggunakan perintah berikut:

```bash
streamlit run dashboard/dashboard.py
```

Dashboard akan terbuka di browser dan memberikan visualisasi analisis penyewaan sepeda.

## Analisis
### Pertanyaan Bisnis
1. **Bagaimana Pengaruh Kelembapan Terhadap Penyewaan Sepeda Berdasarkan Musim?**
   - Visualisasi interaktif menunjukkan bagaimana kelembapan mempengaruhi jumlah penyewaan sepeda di setiap musim.
  
2. **Jam Puncak Penyewaan Sepeda di Hari Kerja vs Akhir Pekan**
   - Analisis ini menggambarkan pola penyewaan sepeda berdasarkan waktu dalam sehari untuk hari kerja dan akhir pekan.

## Kontak
Nama: Safira Rahmalia Putri  
Email: M296B4KX4003@bangkit.academy  
ID Dicoding: safirahmalia
```
