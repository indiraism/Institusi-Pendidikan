# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech


## _Business Understanding_

Jaya Jaya Institut adalah sebuah institusi pendidikan tinggi yang telah beroperasi sejak tahun 2000. Selama perjalanannya, institusi ini telah berhasil mencetak banyak lulusan berkualitas dengan reputasi yang sangat baik. Namun, di balik keberhasilan tersebut, Jaya Jaya Institut menghadapi tantangan serius: tingginya angka _dropout_ siswa. Fenomena ini menjadi perhatian utama karena berdampak pada reputasi, efisiensi operasional, dan keberlangsungan institusi.

### Permasalahan Bisnis

Tantangan utama yang dihadapi oleh Jaya Jaya Institute adalah tingginya tingkat _dropout_, yang menunjukkan bahwa sejumlah siswa tidak berhasil menyelesaikan pendidikannya. Kondisi ini dipengaruhi oleh banyaknya program studi yang perlu diawasi serta berbagai faktor lain. Situasi ini mendorong pihak institusi untuk mengidentifikasi akar penyebab dari tingginya angka _dropout_ guna mengurangi kemungkinan terjadinya kasus serupa di masa mendatang.

### Cakupan Proyek

1. Menganalisis faktor penyebab tingginya _dropout rate_
2. Membuat model _machine learning_ dan prediksi sederhana dan di-_deploy_ pada Streamlit
3. Membangun _dashboard_ menggunakan Streamlit

### Persiapan

Sumber data: [_Student's Performance Dataset_](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

_Setup environment_:
1. Membuat _environment_ baru bernama newenv
```
python -m venv newenv
```
2. Aktivasi _environment_
```
.\newenv\Scripts\activate
```
3. Menginstal _package_ yang dibutuhkan
```
pip install -r requirements.txt
```

## _Business Dashboard_

_Dashboard_ "_Jaya Jaya Institute Student Performance Dashboard_" yang ditampilkan berfungsi sebagai alat bantu visual untuk monitoring performa Siswa secara keseluruhan, terutama dalam hal status pendidikan, _dropout_, dan demografi. Tujuan utama dari _business dashboard_ tersebut untuk:

1. Memantau fluktuasi _dropout_ dari waktu ke waktu.
2. Menganalisis faktor yang berkaitan dengan _dropout_.
3. Menghitung dan menyajikan tingkat _dropout_.

[_Jaya Jaya Institute Student Performance Dashboard_](https://lookerstudio.google.com/s/s-g6JbVbrPU)


## Menjalankan Sistem Machine Learning

Aplikasi ini digunakan untuk memprediksi apakah seorang Siswa **_Dropout_**, **Masih Kuliah**, atau **Lulus** berdasarkan data historis.

### 📂 Cara Penggunaan

1. 👉 [Prediksi _Dropout_ Siswa](https://institusi-pendidikan-nfsrs4mm4mzs5s6ctrcpvb.streamlit.app/)  
2. Unggah _file CSV_ yang memiliki struktur fitur seperti dataset _training_.
3. Aplikasi akan menampilkan hasil prediksi dalam bentuk tabel.
4. Klik tombol **Unduh Hasil Prediksi** untuk menyimpan hasil ke _file_ lokal.

### 🧪 Model

- Model akan memproses seluruh baris.
- Kolom hasil prediksi (Prediksi) akan ditambahkan.
- Label prediksi:

    1. `Enrolled` → Masih aktif
    2. `Internally Transferred` → Pindah prodi
    3. `Dropout` → Berhenti kuliah


## _Conclusion_

Berdasarkan hasil eksplorasi dan visualisasi data yang ditampilkan dalam _dashboard_, dapat disimpulkan beberapa hal penting terkait pola dan karakteristik siswa yang mengalami _dropout_ yaitu bahwa _dropout_ di Jaya Jaya Institute bukan hanya masalah individu, tapi masalah sistemik. Tingginya proporsi msiswa yang keluar dari sistem menandakan perlunya tindakan:

- **Evaluasi menyeluruh terhadap program akademik, dukungan siswa, dan faktor eksternal** yang mempengaruhi keberlanjutan studi.
- **Intervensi preventif** harus diarahkan tidak hanya pada siswa dengan nilai rendah, tetapi juga pada mereka yang menunjukkan performa akademik baik namun berisiko keluar.

### Rekomendasi _Action Items_

1. Bentuk Tim Khusus _Monitoring Dropout_
    - Tugas: memantau dan menganalisis siswa berisiko keluar setiap semester.
    - Melibatkan: dosen wali, bagian akademik, dan konselor.

2. Bangun Sistem Peringatan Dini (_Early Warning System_)
    - Gunakan data usia masuk, nilai semester, dan kehadiran untuk mendeteksi risiko _dropout_.
    - Terapkan intervensi awal sebelum siswa benar-benar berhenti.

3. Wawancara dan Survei _Dropout_
    - Lakukan _follow-up_ pada siswa yang _dropout_ untuk mengetahui alasan sebenarnya.
    - Gunakan hasil untuk memperbaiki sistem akademik dan layanan kampus.

4. Perkuat Layanan Bimbingan dan Konseling
    - Sediakan konseling akademik dan psikologis yang aktif, terutama untuk mahasiswa baru dan usia non-tradisional.

5. Evaluasi Beban Akademik dan Kurikulum
    - Pastikan kurikulum tidak terlalu membebani di awal semester.
    - Beri fleksibilitas bagi siswa yang bekerja atau memiliki tanggung jawab keluarga.

6. Fokus pada Siswa Usia <20 tahun
    - Meski masih muda, kelompok ini memiliki jumlah _dropout_ tinggi.
    - Sediakan program orientasi dan pendampingan khusus untuk transisi dari sekolah ke perguruan tinggi.

7. Kampanye Retensi dan Motivasi
    - Luncurkan program yang menumbuhkan semangat menyelesaikan studi: mentoring, penghargaan, testimoni alumni sukses, dll.
    