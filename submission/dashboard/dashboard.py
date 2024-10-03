import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load dataset
DATA_PATH = 'submission/data/hour.csv'  # Path absolut
bike_data = pd.read_csv(DATA_PATH)

# Menambahkan kolom day_type berdasarkan weekday
bike_data['day_type'] = bike_data['weekday'].apply(lambda x: 'Weekend' if x in [5, 6] else 'Weekday')

# Set title
st.title("Analisis Penyewaan Sepeda")

# Fungsi untuk menampilkan data berdasarkan kategori musim
def display_data_by_season(season):
    return bike_data[bike_data['season'] == season]

# Pilih kategori musim
season_options = {
    1: 'Musim Semi',
    2: 'Musim Panas',
    3: 'Musim Gugur',
    4: 'Musim Dingin'
}
selected_season = st.selectbox("Pilih Musim:", list(season_options.keys()), format_func=lambda x: season_options[x])

# Tombol untuk menampilkan data penyewaan berdasarkan musim yang dipilih
if st.button("Tampilkan Data Penyewaan untuk Musim Terpilih"):
    selected_data = display_data_by_season(selected_season)
    st.write(selected_data)

# Pertanyaan 1
st.subheader("Pertanyaan 1: Bagaimana Pengaruh Kelembapan Terhadap Penyewaan Sepeda Berdasarkan Musim?")
season_totals = bike_data.groupby('season', as_index=False)['cnt'].sum()

# Visualisasi kelembapan dan jumlah penyewaan
st.write("Visualisasi Rata-rata Penyewaan Sepeda berdasarkan Kelembapan dan Musim")
plt.figure(figsize=(10, 5))
sns.lineplot(data=bike_data, x='hum', y='cnt', hue='season', palette='viridis', marker='o')
plt.title('Rata-rata Penyewaan Sepeda berdasarkan Kelembapan di Setiap Musim')
plt.xlabel('Kelembapan (%)')
plt.ylabel('Rata-rata Jumlah Penyewaan Sepeda')
plt.legend(title='Musim')
plt.grid(True)
st.pyplot(plt)

# Visualisasi total penyewaan per musim
st.write("Total Penyewaan Sepeda per Musim")
plt.figure(figsize=(10, 6))
sns.barplot(x='season', y='cnt', data=season_totals, palette='viridis')
plt.title('Total Penyewaan Sepeda per Musim', fontsize=16)
plt.xlabel('Musim', fontsize=14)
plt.ylabel('Total Penyewaan', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(plt)

# Pertanyaan 2
st.subheader("Pertanyaan 2: Jam Puncak Penyewaan Sepeda di Hari Kerja vs Akhir Pekan")
peak_hours = bike_data.groupby(['hr', 'day_type'], as_index=False)['cnt'].mean()

# Visualisasi jam puncak
st.write("Visualisasi Jam Puncak Penyewaan Sepeda: Hari Kerja vs Akhir Pekan")
plt.figure(figsize=(12, 6))
sns.lineplot(data=peak_hours, x='hr', y='cnt', hue='day_type', marker='o')
plt.title('Jam Puncak Penyewaan Sepeda: Hari Kerja vs Akhir Pekan', fontsize=16)
plt.xlabel('Jam dalam Sehari', fontsize=14)
plt.ylabel('Rata-rata Penyewaan Sepeda', fontsize=14)
plt.xticks(range(0, 24))
plt.legend(title='Tipe Hari')
plt.grid(True)
st.pyplot(plt)
