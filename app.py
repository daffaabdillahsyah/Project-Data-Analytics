import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Fungsi untuk memuat data
@st.cache
def load_data():
    df_day = pd.read_csv('datasets/day.csv')
    df_hour = pd.read_csv('datasets/hour.csv')
    return df_day, df_hour

# Memuat data
df_day, df_hour = load_data()

# Judul aplikasi
st.title("Analisis Penyewaan Sepeda")

# Pertanyaan 1: Dinamika Penyewaan Sepeda dan Cuaca
st.header("Pertanyaan 1: Bagaimana dinamika penyewaan sepeda berubah seiring perubahan cuaca?")
plt.figure(figsize=(12, 6))
sns.scatterplot(data=df_hour, x='temp', y='cnt', hue='weathersit', palette='coolwarm', size='windspeed', sizes=(20, 200))
plt.title('Dinamika Penyewaan Sepeda dan Cuaca')
plt.xlabel('Temperatur (Celsius)')
plt.ylabel('Jumlah Sepeda Disewakan')
plt.legend(title='Cuaca', loc='upper right', labels=['Cerah', 'Berawan', 'Hujan/Salju'])
st.pyplot(plt)

# Pertanyaan 2: Penyewaan Sepeda pada Hari Kerja vs Hari Libur
st.header("Pertanyaan 2: Apakah ada perbedaan pola penyewaan sepeda antara hari kerja dan hari libur?")
plt.figure(figsize=(8, 5))
sns.barplot(x='workingday', y='cnt', data=df_day, palette='pastel')
plt.title('Rata-rata Penyewaan Sepeda pada Hari Kerja vs Hari Libur')
plt.xlabel('Hari Kerja (0: Libur, 1: Hari Kerja)')
plt.ylabel('Rata-rata Jumlah Penyewaan')
st.pyplot(plt)

# Pertanyaan 3: Pengaruh Musim terhadap Penyewaan Sepeda
st.header("Pertanyaan 3: Bagaimana pengaruh musim terhadap tren penyewaan sepeda sepanjang tahun?")
plt.figure(figsize=(10, 6))
sns.barplot(x='season', y='cnt', data=df_day, palette='Blues')
plt.title('Rata-rata Penyewaan Sepeda Berdasarkan Musim')
plt.xlabel('Musim')
plt.ylabel('Rata-rata Jumlah Penyewaan')
plt.xticks(ticks=[0, 1, 2, 3], labels=['Spring', 'Summer', 'Fall', 'Winter'])
st.pyplot(plt)

# Pertanyaan 4: Hubungan Kecepatan Angin dan Penyewaan Sepeda
st.header("Pertanyaan 4: Apakah ada hubungan antara kecepatan angin dan jumlah penyewaan sepeda?")
plt.figure(figsize=(12, 6))
sns.scatterplot(data=df_hour, x='windspeed', y='cnt', hue='weathersit', palette='coolwarm', size='temp', sizes=(20, 200))
plt.title('Hubungan Kecepatan Angin dan Penyewaan Sepeda')
plt.xlabel('Kecepatan Angin')
plt.ylabel('Jumlah Sepeda Disewakan')
st.pyplot(plt)

# Pertanyaan 5: Tren Penyewaan Sepeda Berdasarkan Jam
st.header("Pertanyaan 5: Bagaimana tren penyewaan sepeda berubah pada waktu tertentu dalam sehari?")
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_hour, x='hr', y='cnt', hue='workingday', palette='Set1')
plt.title('Rata-rata Penyewaan Sepeda Berdasarkan Jam dalam Sehari')
plt.xlabel('Jam')
plt.ylabel('Rata-rata Jumlah Penyewaan')
plt.xticks(ticks=range(0, 24))
plt.grid(True)
st.pyplot(plt)
