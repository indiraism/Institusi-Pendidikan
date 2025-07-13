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
- Proyek ini dapat dijalankan dengan mudah menggunakan Google Colabolatory (Colab), yang menyediakan *environment* siap pakai dengan sebagian besar dependensi yang sudah **terinstal**.
- Namun jika ingin menjalankan proyek ini secara local di komputer pribadi, disarankan untuk menggunakan virtual environment untuk mengelola dependensi proyek:

**1. Membuat _Virtual Environment_ (opsional, untuk lokal)**:
Buka terminal atau command prompt, lalu navigasikan ke direktori proyek Anda. Jalankan perintah berikut:

```Bash
python -m venv venv
```

**2. Mengaktifkan _Virtual Environment_ (opsional, untuk lokal)** :
- Windows:
```Bash
.\venv\Scripts\activate
```

- macOS / Linux:
```Bash
    source venv/bin/activate
```

**3. Instalasi Dependensi** :
- Baik di Google Colab maupun di _environment_ lokal (setelah mengaktifkan _virtual environment_), Anda mungkin perlu menginstal beberapa _library_ tambahan yang tidak tersedia secara _default_. Pastikan Anda berada di direktori proyek dan jalankan perintah berikut:
```Bash
    pip install -r requirements.txt
```
- Catatan: Jika ada _library_ yang perlu diinstal di Colab, Anda bisa menambahkannya di sel kode awal _notebook_ Colab Anda dengan:
```Bash
!pip install nama_library
```
- Catatan: Untuk menjalankan _prediction notebook_ dibutuhkan file yang ada di folder model.

## **Cara Menjalankan Proyek**
**Menggunakan Google Colaboratory (Direkomendasikan)**
1. **Buka Notebook** : Unggah atau buka file _notebook_ .ipynb proyek ini di Google Colab.
2. **Jalankan Semua Sel** : Pastikan Anda menjalankan semua sel kode secara berurutan, dari atas ke bawah. Ini akan memproses data, melatih model (jika ada), dan menyiapkan _dashboard_.
3. **Akses _Dashboard_** : Untuk mengakses _dashboard_ di Looker Studio, gunakan tautan yang disediakan di bagian "_Business Dashboard_" di bawah ini.

## **Menjalankan Secara Lokal (Opsional)**
Jika telah melakukan langkah-langkah _Setup Environment_ di atas untuk menjalankan proyek secara lokal:
1. Pastikan _Virtual Environment_ Aktif: Di terminal atau _command prompt_, pastikan Anda telah mengaktifkan _virtual environment_.
2. Jalankan Skrip Utama: Navigasikan ke direktori utama proyek Anda. Kemudian, jalankan file Python utama proyek Anda. Jika file utama Anda adalah main.py, app.py, atau dashboard.py (sesuaikan dengan nama file Anda):

```Bash
    python nama_file_utama_anda.py
```

3. Akses Dashboard: Setelah skrip berhasil dijalankan, jika dashboard Anda di-hosting secara lokal, alamat akses biasanya akan ditampilkan di terminal (misalnya, http://127.0.0.1:8050/ atau http://localhost:5000/). Namun, untuk dashboard Looker Studio, Anda cukup mengakses tautan [_Jaya Jaya Institute Student Performance Dashboard_](https://lookerstudio.google.com/reporting/cf8b5153-87d7-47cc-8ee7-72aa9b5fb083).

**Cara Menjalankan Skrip Prediksi Python (.py)** :

Menggunakan streamlit:
```Bash
    streamlit run ml-dropout/app.py
```


## _Business Dashboard_

_Dashboard_ "_Jaya Jaya Institute Student Performance Dashboard_" yang ditampilkan berfungsi sebagai alat bantu visual untuk monitoring performa siswa secara keseluruhan, terutama dalam hal status pendidikan, _dropout_, dan demografi. Tujuan utama dari _business dashboard_ tersebut untuk:

1. Memantau fluktuasi _dropout_ dari waktu ke waktu.
2. Menganalisis faktor yang berkaitan dengan _dropout_.
3. Menghitung dan menyajikan tingkat _dropout_.

[_Jaya Jaya Institute Student Performance Dashboard_](https://lookerstudio.google.com/reporting/cf8b5153-87d7-47cc-8ee7-72aa9b5fb083)


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

Berdasarkan hasil eksplorasi dan visualisasi data pada *dashboard*, dapat disimpulkan bahwa permasalahan **_dropout_ siswa di Jaya Jaya Institute** bukan sekadar persoalan individu, tetapi merupakan **masalah sistemik** yang melibatkan berbagai faktor akademik dan non-akademik.

Tingginya proporsi msiswa _dropout_ (**49,93% dari total 4.424 mahasiswa**) mengindikasikan perlunya perhatian serius. Analisis mendalam menunjukkan bahwa:

- 🔹 **Karakteristik umum siswa yang _dropout_:**
  - Mayoritas berada pada kelompok usia **<20 tahun** saat masuk kuliah.
  - Memiliki nilai akademik rata-rata yang justru **lebih tinggi** dibanding siswa aktif dan yang pindah.
  - Cenderung tidak melanjutkan studi meski secara performa akademik tergolong baik.

- 🔹 **Faktor-faktor yang berkontribusi pada _dropout_:**
  - **Usia saat masuk kuliah** (terutama siswa sangat muda yang belum siap secara mental dan sosial).
  - **Kondisi non-akademik** seperti motivasi, dukungan sosial, dan beban pribadi.
  - **Kurangnya sistem deteksi dini** terhadap mahasiswa berisiko.

### ✅ Rekomendasi Tindak Lanjut:

- **Evaluasi menyeluruh terhadap program akademik dan layanan dukungan siswa**, termasuk beban studi awal dan sistem orientasi kampus.
- **Intervensi preventif** tidak hanya difokuskan pada mahasiswa berprestasi rendah, tetapi juga pada mahasiswa yang menunjukkan performa akademik baik namun berisiko keluar karena faktor eksternal.

---

Dashboard ini diharapkan dapat menjadi dasar dalam pengambilan keputusan strategis untuk meningkatkan **retensi dan keberhasilan studi mahasiswa** di masa mendatang.


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
    
