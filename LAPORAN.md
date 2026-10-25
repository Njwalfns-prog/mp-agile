# Laporan Tugas Kelompok: Implementasi Agile Bab 4

**Mata kuliah:** Manajemen Proyek, Teknik Informatika
**Studi kasus:** Aplikasi Presensi Praktikum satu sesi
**Sprint yang dilaporkan:** Sprint 2 (penambahan fitur US8)

---

## 1. Identitas Kelompok

| No | Nama | NIM | Peran |
|---|---|---|---|
| 1 | (isi nama) | (isi NIM) | Product Owner |
| 2 | (isi nama) | (isi NIM) | Scrum Master |
| 3 | (isi nama) | (isi NIM) | Developer |
| 4 | (isi nama) | (isi NIM) | Developer |

---

## 2. Fitur yang Dikembangkan

**US8: Pencarian mahasiswa berdasarkan nama.**

Fitur ini dipilih karena ada di Product Backlog yang belum selesai, memberi nilai langsung bagi dosen saat memeriksa kehadiran, dan ukurannya cukup kecil sehingga dapat diselesaikan dalam satu Sprint.

### 2.1 User Story

> **US8.** Sebagai **dosen**, saya ingin **mencari nama mahasiswa** agar **saya dapat menemukan data presensi dengan cepat tanpa membaca seluruh daftar**.

**Prioritas:** Tinggi (nilai langsung ke pengguna utama)
**Estimasi:** 2 story point
**Sprint:** Sprint 2

### 2.2 Kriteria Penerimaan

Fitur dinyatakan diterima apabila seluruh kondisi berikut terpenuhi:

1. Pencarian dapat dilakukan dari menu aplikasi (menu nomor 4, "Cari nama").
2. Pencocokan dilakukan pada kolom `nama` dan bersifat **substring**, bukan hanya sama persis.
3. Pencarian **tidak membedakan huruf besar dan kecil** (`ayu` = `AYU` = `Ayu`).
4. Kata kunci kosong atau hanya spasi mengembalikan seluruh data.
5. Bila tidak ada yang cocok, aplikasi menampilkan pesan bahwa data tidak ditemukan.
6. Bila berkas `presensi.csv` belum ada, pencarian mengembalikan daftar kosong tanpa error.
7. Urutan hasil mengikuti urutan data pada berkas, sehingga konsisten dengan menu daftar.

### 2.3 Definition of Done untuk US8

- Seluruh kriteria penerimaan terpenuhi.
- Tes otomatis untuk fitur pencarian dibuat dan lulus.
- Tes lama (Sprint 1) tetap lulus, tidak ada regresi.
- Program dapat dijalankan dari terminal dan fitur didemonstrasikan.
- Laporan dan video demonstrasi diunggah.

---

## 3. Product Backlog (Diperbarui)

| ID | User story (ringkas) | Prioritas | Estimasi | Sprint 1 | Sprint 2 |
|---|---|---|---|---|---|
| US1 | Sebagai mahasiswa, saya ingin mengisi NIM dan nama agar identitas tercatat. | Tinggi | 3 | Selesai | Selesai |
| US2 | Sebagai mahasiswa, saya ingin memilih status hadir/izin/alpa agar kehadiran jelas. | Tinggi | 2 | Selesai | Selesai |
| US3 | Sebagai dosen, saya ingin NIM diperiksa agar data tidak salah. | Tinggi | 2 | Selesai | Selesai |
| US4 | Sebagai dosen, saya ingin NIM tidak dapat presensi dua kali agar rekap akurat. | Tinggi | 2 | Selesai | Selesai |
| US5 | Sebagai dosen, saya ingin melihat daftar presensi agar dapat memeriksa siapa yang tercatat. | Tinggi | 2 | Selesai | Selesai |
| US6 | Sebagai dosen, saya ingin melihat rekap per status agar mudah memantau kehadiran. | Sedang | 2 | Selesai | Selesai |
| US7 | Sebagai dosen, saya ingin presensi tersimpan di CSV agar tidak hilang saat program ditutup. | Tinggi | 3 | Selesai | Selesai |
| **US8** | **Sebagai dosen, saya ingin mencari nama agar menemukan presensi dengan cepat.** | **Tinggi** | **2** | **Belum** | **Selesai** |
| US9 | Sebagai dosen, saya ingin presensi dibedakan per pertemuan agar data tidak tercampur. | Sedang | 5 | Belum | Belum |
| US10 | Sebagai dosen, saya ingin mengedit kesalahan status agar data dapat dikoreksi. | Sedang | 3 | Belum | Belum |

**Sprint Goal Sprint 2:** Menambahkan kemampuan pencarian nama pada aplikasi presensi tanpa merusak fitur Sprint 1.

---

## 4. Papan Kanban

### 4.1 Papan Awal Sprint 2 (Sprint Planning)

| Backlog | Dikerjakan (WIP maks 2) | Review/Uji (WIP maks 1) | Selesai |
|---|---|---|---|
| US9, US10 | US8 | (kosong) | US1, US2, US3, US4, US5, US6, US7 |

### 4.2 Papan Pertengahan Sprint 2

| Backlog | Dikerjakan (WIP maks 2) | Review/Uji (WIP maks 1) | Selesai |
|---|---|---|---|
| US9, US10 | (kosong) | US8 | US1 sampai US7 |

### 4.3 Papan Akhir Sprint 2

| Backlog | Dikerjakan (WIP maks 2) | Review/Uji (WIP maks 1) | Selesai |
|---|---|---|---|
| US9, US10 | (kosong) | (kosong) | US1 sampai US8 |

**Catatan penerapan WIP limit:** saat kolom Review/Uji sudah terisi US8, tidak ada pekerjaan baru yang ditarik dari Backlog. Tim menyelesaikan pengujian US8 lebih dahulu, baru kemudian memutuskan apakah kapasitas Sprint masih cukup untuk US10.

---

## 5. Simulasi Lima Hari Sprint 2

| Hari | Kegiatan | Hasil |
|---|---|---|
| Senin | Sprint Planning: memilih US8, menyusun kriteria penerimaan | Sprint Goal dan daftar tugas disepakati |
| Selasa | Daily Scrum, menulis tes yang gagal (Red) | `test_cari_sebagian_nama` gagal karena fungsi belum ada |
| Rabu | Daily Scrum, implementasi `cari_presensi` (Green) | Tes pencarian lulus |
| Kamis | Daily Scrum, integrasi menu, Refactor, uji regresi | 11 tes lulus, tidak ada regresi |
| Jumat | Sprint Review (demo) dan Sprint Retrospective | Fitur diterima Product Owner, umpan balik dicatat |

### 5.1 Contoh Catatan Daily Scrum

**Hari Selasa:**
> "Kemarin saya menyelesaikan Sprint Planning dan menulis tes pencarian. Hari ini saya mengerjakan tes untuk pencarian yang tidak membedakan huruf besar dan kecil. Hambatan saya: belum ada keputusan apakah kata kunci kosong harus mengembalikan semua data atau dianggap error. Saya akan konfirmasi ke Product Owner setelah pertemuan."

**Hari Rabu:**
> "Kemarin tes pencarian sudah ditulis dan semuanya gagal seperti yang diharapkan. Hari ini saya mengimplementasikan fungsi `cari_presensi` sampai tes lulus. Tidak ada hambatan."

**Hari Kamis:**
> "Kemarin fungsi pencarian sudah lulus tes. Hari ini saya mengerjakan integrasi ke menu dan menjalankan ulang seluruh tes untuk memastikan tidak ada regresi. Hambatan: tidak ada."

### 5.2 Contoh Sprint Review

Product Owner mencoba tiga skenario langsung di depan tim:

1. Mencari `Ayu` ketika data berisi `Ayu Lestari` dan `Ayuningtyas`. Hasil: kedua data muncul.
2. Mencari `ayu` dengan huruf kecil. Hasil: sama dengan pencarian `Ayu`.
3. Mencari `Zaki` yang tidak ada di data. Hasil: pesan "Tidak ada mahasiswa dengan nama mengandung Zaki".

Product Owner menyatakan fitur **diterima** karena seluruh kriteria penerimaan terpenuhi.

### 5.3 Contoh Sprint Retrospective

**Yang berjalan baik:** tes ditulis sebelum implementasi, sehingga batas perilaku fungsi jelas sejak awal.

**Yang perlu diperbaiki:** pada Sprint 1 sempat terjadi kesalahan penulisan status (`hadri`). Pada Sprint 2 validasi dan tes otomatis menangkap kelas kesalahan yang sama.

**Tindakan perbaikan:** menyepakati struktur data dan format CSV di awal Sprint berikutnya, sebelum pekerjaan pengembangan dimulai.

---

## 6. Praktik Lean

Pemborosan yang teridentifikasi beserta tindakan perbaikannya:

| Jenis pemborosan | Kejadian | Tindakan |
|---|---|---|
| Menunggu | Integrasi tertunda karena format CSV belum disepakati | Sepakati format CSV di Sprint Planning |
| Berganti tugas | Developers memulai terlalu banyak tugas sekaligus | Terapkan WIP limit pada papan Kanban |
| Cacat | Status salah tulis seperti `hadri` | Validasi input dan tes otomatis |
| Pengerjaan ulang | Menu harus diubah dua kali karena integrasi ditunda | Integrasikan menu bersamaan dengan implementasi fungsi |

**Contoh perhitungan efisiensi aliran Sprint 2:**
Pekerjaan aktif 1 hari dari total lead time 4 hari menghasilkan efisiensi aliran **25 persen**. Sisanya adalah waktu tunggu, misalnya menunggu keputusan Product Owner mengenai perilaku kata kunci kosong.

---

## 7. Praktik XP

### 7.1 Test-Driven Development

**Red:** tes `test_cari_sebagian_nama` ditulis lebih dahulu. Dijalankan ketika `cari_presensi` belum ada, hasilnya `ImportError` atau gagal.

**Green:** fungsi `cari_presensi` diimplementasikan dengan pencocokan substring dan normalisasi huruf kecil. Tes lulus.

**Refactor:** fungsi dirapikan, docstring ditambahkan, lalu seluruh tes dijalankan ulang. Semua lulus.

### 7.2 Pair Programming

Satu mahasiswa berperan sebagai **driver** (mengetik kode), satu sebagai **navigator** (memeriksa logika dan kemungkinan kesalahan), kemudian bertukar peran pada sesi berikutnya. Praktik ini menangkap kasus tepi seperti kata kunci berisi spasi dan berkas CSV yang belum ada.

### 7.3 Hasil Pengujian

Perintah:

```bash
python3 -m unittest test_presensi.py -v
```

Hasil: **11 tes lulus, 0 gagal.**

| No | Nama tes | Cakupan | Hasil |
|---|---|---|---|
| 1 | `test_input_presensi_valid` | Input dasar (Sprint 1) | Lulus |
| 2 | `test_nim_harus_angka` | Validasi NIM | Lulus |
| 3 | `test_status_harus_valid` | Validasi status | Lulus |
| 4 | `test_nama_tidak_boleh_kosong` | Validasi nama | Lulus |
| 5 | `test_nim_tidak_boleh_duplikat` | Anti duplikat | Lulus |
| 6 | `test_rekap_presensi` | Rekap per status | Lulus |
| 7 | `test_cari_sebagian_nama` | US8, pencarian substring | Lulus |
| 8 | `test_cari_tidak_bedakan_huruf_besar_kecil` | US8, normalisasi huruf | Lulus |
| 9 | `test_cari_nama_tidak_ditemukan` | US8, hasil kosong | Lulus |
| 10 | `test_cari_kata_kunci_kosong_mengembalikan_semua` | US8, kata kunci kosong | Lulus |
| 11 | `test_cari_pada_berkas_belum_ada` | US8, berkas belum ada | Lulus |

### 7.4 Uji Manual End-to-End

Skenario yang dijalankan:

1. Input tiga data: `22001 Ayu Lestari hadir`, `22002 Bima Saputra izin`, `22003 Ayuningtyas alpa`.
2. Menu 2 (daftar) menampilkan tiga data sesuai urutan input.
3. Menu 4 dengan kata kunci `ayu` menampilkan dua data: `22001` dan `22003`.
4. Menu 3 (rekap) menampilkan `{'HADIR': 1, 'IZIN': 1, 'ALPA': 1}` dengan total 3.

Seluruh langkah berjalan sesuai harapan.

---

## 8. Perubahan Kode

### 8.1 Fungsi baru

```python
def cari_presensi(kata_kunci, lokasi=LOKASI_DEFAULT):
    """Cari presensi berdasarkan nama."""
    kata_kunci = kata_kunci.strip().lower()
    data = daftar_presensi(lokasi)
    if not kata_kunci:
        return data
    return [baris for baris in data if kata_kunci in baris['nama'].lower()]
```

### 8.2 Perubahan menu

Menu bertambah satu pilihan sehingga menjadi:

```
1. Input presensi
2. Lihat daftar
3. Lihat rekap
4. Cari nama
5. Keluar
```

Pilihan `Keluar` berpindah dari nomor 4 ke nomor 5.

### 8.3 Kompatibilitas

Fungsi `daftar_presensi`, `catat_presensi`, dan `rekap_presensi` tidak diubah. Format CSV tetap `nim,nama,status`. Data lama tetap dapat dibaca tanpa migrasi.

---

## 9. Refleksi: Manfaat Umpan Balik Cepat

Umpan balik cepat mengubah cara tim bekerja pada Sprint 2 dalam tiga hal.

**Pertama, kesalahan ditemukan saat masih murah diperbaiki.** Tes ditulis sebelum implementasi. Ketika fungsi pencarian belum ada, tes langsung gagal dan tim tahu persis apa yang harus dibangun. Tidak ada waktu terbuang untuk menebak perilaku yang diinginkan.

**Kedua, keputusan produk menjadi lebih cepat.** Sprint Review di hari Jumat membuat Product Owner dapat mencoba fitur secara langsung, bukan membaca laporan. Pertanyaan seperti "apakah kata kunci kosong harus mengembalikan semua data" dijawab dalam hitungan menit, bukan menunggu akhir proyek.

**Ketiga, regresi tercegah.** Menjalankan seluruh 11 tes setiap kali kode berubah membuat fitur Sprint 1 tetap aman saat fitur baru ditambahkan. Tim tidak perlu takut menyentuh kode lama.

**Yang masih perlu diperbaiki:** umpan balik cepat tidak berguna bila tidak ada yang menindaklanjuti. Pada Sprint 1, keputusan format CSV ditunda sehingga integrasi tertunda. Retrospective Sprint 2 memperbaikinya dengan menyepakati keputusan teknis di awal Sprint.

---

## 10. Batasan Prototipe

- Hanya menangani satu sesi presensi, belum dibedakan per pertemuan (US9 belum dikerjakan).
- Belum ada login maupun pembagian peran pengguna.
- Belum ada keamanan data tingkat lanjut, berkas CSV disimpan apa adanya.
- Belum ada fitur edit status (US10 belum dikerjakan).
- Antarmuka berbasis terminal, bukan aplikasi grafis.

---

## 11. Lampiran

### 11.1 Struktur berkas

```
presensi.py          # aplikasi utama
test_presensi.py     # 11 tes otomatis
PANDUAN_PRAKTIKUM.md # panduan praktikum asli
presensi.csv         # dibuat otomatis saat input pertama
```

### 11.2 Cara menjalankan

```bash
python3 presensi.py
python3 -m unittest test_presensi.py -v
```

### 11.3 Tautan

- Video demonstrasi: (isi tautan YouTube)
- Laporan ini: (isi tautan Google Drive)
