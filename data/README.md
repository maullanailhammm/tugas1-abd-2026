**Nama: Maullana Ilham Ar Rosyiid Mariandi**
**Nim: 20231037031109**
**Kelas: Analisis Big Data (B)**

# Dokumentasi Dataset: Indonesian News Dataset
Dokumen ini menjelaskan sumber, cara mengunduh, dan karakteristik dataset yang digunakan pada Tugas 1 milestone 1 Analisis Big Data 2026.

## 1. Ringkasan Dataset

| Item | Keterangan |
| --- | --- |
| Nama | indonesian_news_dataset |
| Pemilik di Kaggle | iqbalmaulana |
| Sumber | https://www.kaggle.com/datasets/iqbalmaulana/indonesian-news-dataset |
| Deskripsi singkat | Kumpulan artikel berita yang diagregasi dari 7 situs berita di Indonesia (antara lain Tempo, CNN Indonesia, CNBC Indonesia, Okezone, dan Suara) |
| Topik/tag di Kaggle | computer science, text, text classification, summarization |
| File utama | `data.csv` |
| Ukuran file | sekitar 738 MB (tidak terkompresi); unduhan Kaggle sekitar 285 MB (terkompresi) |
| Format | CSV |
| Bahasa | Indonesia |
| Lisensi | [CC BY-NC-SA 4.0] |
| Tanggal unduh | [15-10-2026] |

**Pemenuhan syarat Milestone 1:** ukuran `data.csv` sekitar 738 MB

## 2. Cara Mengunduh

### Opsi A: Kaggle CLI (disarankan, bisa direproduksi)

1. Pasang Kaggle CLI dan siapkan API token (Kaggle > Settings > API > Create New Token), simpan sebagai `~/.kaggle/kaggle.json`.
2. Jalankan dari root repository:

```bash
pip install kaggle
kaggle datasets download -d iqbalmaulana/indonesian-news-dataset -p data/raw --unzip
```

### Opsi B: Unduh manual

1. Buka https://www.kaggle.com/datasets/iqbalmaulana/indonesian-news-dataset (perlu login Kaggle).
2. Klik **Download**, lalu ekstrak arsipnya.
3. Letakkan `data.csv` di folder `data/raw/`.

### Hasil akhir yang diharapkan

```
data/
├── README.md
└── raw/
    └── data.csv       
```

Pada notebook profiling, atur:

```python
DATA_PATH = "data/raw/data.csv"
```

## 3. Cara Memverifikasi Unduhan

Jalankan perintah berikut (DuckDB) untuk memastikan file terbaca dan mengetahui jumlah barisnya:

```python
import duckdb

DATA_PATH = "data/raw/data.csv"
duckdb.sql(f"SELECT count(*) AS jumlah_baris FROM read_csv_auto('{DATA_PATH}')").show()
duckdb.sql(f"DESCRIBE SELECT * FROM read_csv_auto('{DATA_PATH}')").show()
```

Untuk memeriksa ukuran file:

```bash
ls -lh data/raw/data.csv
```

## 4. Karakteristik Data (diisi setelah profiling)

Bagian ini diisi dari hasil `notebooks/01_data_profiling.ipynb`.

| Item | Nilai |
| --- | --- |
| Jumlah baris | 32.735 |
| Jumlah kolom | 11 |
| Rentang waktu data | 2018-08-10 05:11:58+00 sampai 2023-04-11 20:13:25+00 |
| Jumlah sumber berita | 7 (`tempo`, `cnbcindonesia`, `cnnindonesia`, `kumparan`, `okezone`, `jawapos`, `suara`) |

### Kamus kolom

| Kolom | Tipe | Deskripsi |
| --- | --- | --- |
| `id` | `Int64` | Identitas unik artikel berita. |
| `source` | `String` | Nama sumber atau situs berita. |
| `title` | `String` | Judul artikel berita. |
| `image` | `String` | URL gambar yang terkait dengan artikel; dapat kosong. |
| `url` | `String` | URL artikel berita. |
| `content` | `String` | Isi lengkap artikel berita; dapat kosong. |
| `date` | `String` | Waktu publikasi artikel dalam format `YYYY-MM-DD HH:MM:SS+00`; perlu dikonversi ke tipe waktu saat analisis. |
| `embedding` | `String` | Representasi embedding artikel yang tersimpan sebagai teks. |
| `created_at` | `String` | Waktu pembuatan record dalam format teks. |
| `updated_at` | `String` | Waktu terakhir pembaruan record dalam format teks. |
| `summary` | `String` | Ringkasan artikel; sebagian kecil record dapat kosong. |

Catatan: berdasarkan inferensi skema Polars pada file CSV, kolom `date`, `created_at`, dan
`updated_at` terbaca sebagai `String`, bukan `DateTime`. Kolom-kolom tersebut perlu diparse
secara eksplisit sebelum analisis temporal.

## 5. Rencana Analisis

- **Analisis temporal:** tren jumlah berita per hari/bulan, perbedaan pola antar-sumber berita, dan pola musiman atau lonjakan pada tanggal tertentu.
- **Cleaning dan data quality (Milestone 2):** missing values, artikel duplikat, nilai waktu tidak valid, serta outlier seperti panjang teks yang ekstrem.
- **Analisis lanjutan (opsional):** frekuensi topik atau kata kunci per periode, bergantung pada kolom yang tersedia.

Dataset ini tidak diketahui memiliki kolom lokasi, sehingga analisis yang dipilih adalah analisis temporal. Perbarui bagian ini jika profiling menemukan kolom lain yang relevan.

## 6. Sitasi

> iqbalmaulana. *indonesian_news_dataset*. Kaggle. https://www.kaggle.com/datasets/iqbalmaulana/indonesian-news-dataset .
