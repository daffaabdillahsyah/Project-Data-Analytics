# Analisis Penyewaan Sepeda

Proyek ini bertujuan untuk menganalisis pola penyewaan sepeda berdasarkan data cuaca, musim, hari kerja vs libur, kecepatan angin, dan waktu dalam sehari. Analisis dilakukan menggunakan Python dan hasilnya divisualisasikan melalui aplikasi web interaktif menggunakan Streamlit.

## Struktur Proyek

- **app.py**: Script utama untuk menjalankan aplikasi Streamlit yang memvisualisasikan hasil analisis.
- **day.csv**: Dataset yang berisi data penyewaan sepeda yang diaggregasi per hari.
- **hour.csv**: Dataset yang berisi data penyewaan sepeda yang diaggregasi per jam.
- **README.md**: Dokumentasi proyek ini.
- **Proyek Analisis Data.ipynb**: Script Analisa Data
- **requirements.txt**: Daftar dependensi yang diperlukan untuk menjalankan proyek ini.

## Cara Menjalankan Aplikasi

1. **Clone repositori ini**:
    ```bash
    git clone https://github.com/daffaabdillahsyah/Project-Data-Analytics.git
    ```

2. **Install dependensi**:
    Pastikan Anda berada di dalam direktori proyek, lalu jalankan:
    ```bash
    pip install -r requirements.txt
    ```

3. **Jalankan aplikasi Streamlit**:
    ```bash
    streamlit run app.py
    ```

4. **Buka aplikasi**:
    Aplikasi akan terbuka secara otomatis di browser Anda, atau Anda bisa membukanya secara manual melalui URL yang diberikan di terminal.

## Deskripsi Analisis

### Pertanyaan Bisnis yang Dijawab

1. **Bagaimana pengaruh kondisi cuaca terhadap jumlah penyewaan sepeda?**
   - Analisis ini menunjukkan bahwa suhu yang lebih tinggi dan cuaca cerah meningkatkan jumlah penyewaan sepeda.

2. **Apakah ada perbedaan pola penyewaan sepeda antara hari kerja dan hari libur?**
   - Meskipun ada sedikit peningkatan dalam penyewaan sepeda pada hari kerja, perbedaannya tidak terlalu signifikan.

3. **Bagaimana pengaruh musim terhadap tren penyewaan sepeda sepanjang tahun?**
   - Musim gugur dan musim panas adalah periode yang paling diminati untuk penyewaan sepeda.

4. **Apakah ada hubungan antara kecepatan angin dan jumlah penyewaan sepeda?**
   - Kecepatan angin yang tinggi dapat mengurangi jumlah penyewaan sepeda, terutama dalam kondisi cuaca buruk.

5. **Bagaimana tren penyewaan sepeda berubah pada waktu tertentu dalam sehari?**
   - Terdapat dua puncak utama dalam penyewaan sepeda: pagi hari dan sore hari, terutama pada hari kerja.

<!-- ## Lisensi

Proyek ini dilisensikan di bawah [Nama Lisensi]. Anda dapat melihat lisensi lengkap di [LICENSE]. -->

## Kontak

Untuk informasi lebih lanjut, hubungi [Gusti Muhammad Daffa Abdillahsyah] di [daffaabdillahsyah49@gmail.com].
