# Kanban — Aplikasi Presensi Praktikum

**Sprint 2 · Fokus: US8 — Pencarian nama mahasiswa**  
**Sprint Goal:** Menambahkan pencarian nama tanpa merusak fitur Sprint 1.

Status berikut mengikuti simulasi pada [laporan](LAPORAN.md), bukan pelacakan pekerjaan secara langsung.

## Papan akhir Sprint 2

| 📋 Backlog | 🔧 Dikerjakan · maks. 2 | 🧪 Review/Uji · maks. 1 | ✅ Selesai |
|---|---|---|---|
| **US9 · Presensi per pertemuan**<br>Prioritas sedang · 5 SP | — | — | **US1 · Input NIM dan nama** · 3 SP |
| **US10 · Edit status presensi**<br>Prioritas sedang · 3 SP | | | **US2 · Pilih hadir/izin/alpa** · 2 SP |
| | | | **US3 · Validasi NIM** · 2 SP |
| | | | **US4 · Cegah presensi ganda** · 2 SP |
| | | | **US5 · Lihat daftar presensi** · 2 SP |
| | | | **US6 · Rekap per status** · 2 SP |
| | | | **US7 · Simpan data ke CSV** · 3 SP |
| | | | **US8 · Cari nama mahasiswa** · 2 SP |

## Pergerakan US8 selama Sprint 2

| Tahap | Backlog | Dikerjakan | Review/Uji | Selesai |
|---|---|---|---|---|
| Awal sprint | US9, US10 | **US8** | — | US1–US7 |
| Pertengahan sprint | US9, US10 | — | **US8** | US1–US7 |
| Akhir sprint | US9, US10 | — | — | US1–US8 |

## Detail kartu US8

> Sebagai dosen, saya ingin mencari nama mahasiswa agar dapat menemukan data presensi dengan cepat tanpa membaca seluruh daftar.

**Prioritas:** Tinggi · **Estimasi:** 2 story point · **Sprint:** 2

### Kriteria penerimaan

- Pencarian tersedia melalui menu 4, **Cari nama**.
- Mendukung pencarian sebagian nama.
- Tidak membedakan huruf besar dan kecil.
- Kata kunci kosong atau hanya spasi menampilkan seluruh data.
- Hasil yang tidak cocok menampilkan pesan data tidak ditemukan.
- Berkas CSV yang belum ada menghasilkan daftar kosong tanpa error.
- Urutan hasil mengikuti urutan data dalam berkas.

### Syarat pindah ke Selesai

- Seluruh kriteria penerimaan terpenuhi.
- Tes pencarian dan tes fitur lama lulus.
- Fitur berhasil didemonstrasikan melalui terminal.
- Laporan dan video demonstrasi diunggah.

**Catatan:** Status US8 mengikuti laporan. Tautan unggahan laporan dan video masih perlu diisi pada laporan untuk melengkapi bukti Definition of Done.

## Aturan papan

1. Alur kartu: **Backlog → Dikerjakan → Review/Uji → Selesai**.
2. Maksimal dua kartu berada di Dikerjakan dan satu kartu di Review/Uji.
3. Selesaikan pengujian US8 sebelum menarik pekerjaan berikutnya, sesuai kebijakan tim dalam laporan.
4. Kartu yang gagal diuji dikembalikan ke Dikerjakan dengan catatan perbaikan.
5. US9 dan US10 tetap di Backlog sampai dipilih dalam perencanaan sprint berikutnya.
