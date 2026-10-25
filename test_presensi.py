"""Contoh praktik XP: tes otomatis untuk user story presensi."""
import tempfile
import unittest
from pathlib import Path
from presensi import catat_presensi, cari_presensi, daftar_presensi, rekap_presensi

class TestPresensi(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.file = Path(self.folder.name) / 'uji.csv'

    def tearDown(self):
        self.folder.cleanup()

    def test_input_presensi_valid(self):
        catat_presensi('22001', 'Ayu', 'hadir', self.file)
        self.assertEqual(daftar_presensi(self.file)[0]['status'], 'HADIR')

    def test_nim_harus_angka(self):
        with self.assertRaises(ValueError):
            catat_presensi('A001', 'Ayu', 'hadir', self.file)

    def test_status_harus_valid(self):
        with self.assertRaises(ValueError):
            catat_presensi('22001', 'Ayu', 'datang', self.file)

    def test_nama_tidak_boleh_kosong(self):
        with self.assertRaises(ValueError):
            catat_presensi('22001', '', 'hadir', self.file)

    def test_nim_tidak_boleh_duplikat(self):
        catat_presensi('22001', 'Ayu', 'hadir', self.file)
        with self.assertRaises(ValueError):
            catat_presensi('22001', 'Ayu', 'izin', self.file)

    def test_rekap_presensi(self):
        catat_presensi('22001', 'Ayu', 'hadir', self.file)
        catat_presensi('22002', 'Bima', 'izin', self.file)
        catat_presensi('22003', 'Cici', 'alpa', self.file)
        self.assertEqual(rekap_presensi(self.file), {'HADIR': 1, 'IZIN': 1, 'ALPA': 1})


class TestPencarianNama(unittest.TestCase):
    """US8 — Sebagai dosen, saya ingin mencari nama agar menemukan presensi dengan cepat."""

    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.file = Path(self.folder.name) / 'uji.csv'
        catat_presensi('22001', 'Ayu Lestari', 'hadir', self.file)
        catat_presensi('22002', 'Bima Saputra', 'izin', self.file)
        catat_presensi('22003', 'Ayuningtyas', 'alpa', self.file)

    def tearDown(self):
        self.folder.cleanup()

    def test_cari_sebagian_nama(self):
        hasil = cari_presensi('Ayu', self.file)
        self.assertEqual([b['nim'] for b in hasil], ['22001', '22003'])

    def test_cari_tidak_bedakan_huruf_besar_kecil(self):
        self.assertEqual(
            [b['nim'] for b in cari_presensi('ayu', self.file)],
            [b['nim'] for b in cari_presensi('AYU', self.file)],
        )

    def test_cari_nama_tidak_ditemukan(self):
        self.assertEqual(cari_presensi('Zaki', self.file), [])

    def test_cari_kata_kunci_kosong_mengembalikan_semua(self):
        self.assertEqual(len(cari_presensi('   ', self.file)), 3)

    def test_cari_pada_berkas_belum_ada(self):
        kosong = Path(self.folder.name) / 'belum_ada.csv'
        self.assertEqual(cari_presensi('Ayu', kosong), [])


if __name__ == '__main__':
    unittest.main(verbosity=2)
