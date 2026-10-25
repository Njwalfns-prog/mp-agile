"""Sprint 2: aplikasi presensi satu sesi praktikum + fitur pencarian (US8)."""
import csv
from pathlib import Path

LOKASI_DEFAULT = Path(__file__).with_name('presensi.csv')
STATUS = {'HADIR', 'IZIN', 'ALPA'}


def daftar_presensi(lokasi=LOKASI_DEFAULT):
    lokasi = Path(lokasi)
    if not lokasi.exists():
        return []
    with lokasi.open('r', encoding='utf-8', newline='') as file:
        return list(csv.DictReader(file))


def catat_presensi(nim, nama, status, lokasi=LOKASI_DEFAULT):
    lokasi = Path(lokasi)
    nim, nama, status = nim.strip(), nama.strip(), status.strip().upper()
    if not nim.isdigit():
        raise ValueError('NIM harus angka dan tidak boleh kosong.')
    if not nama:
        raise ValueError('Nama tidak boleh kosong.')
    if status not in STATUS:
        raise ValueError('Status harus HADIR, IZIN, atau ALPA.')
    if any(baris['nim'] == nim for baris in daftar_presensi(lokasi)):
        raise ValueError('NIM sudah tercatat pada sesi ini.')
    tulis_header = not lokasi.exists() or lokasi.stat().st_size == 0
    with lokasi.open('a', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['nim', 'nama', 'status'])
        if tulis_header:
            writer.writeheader()
        writer.writerow({'nim': nim, 'nama': nama, 'status': status})


def rekap_presensi(lokasi=LOKASI_DEFAULT):
    hitung = {'HADIR': 0, 'IZIN': 0, 'ALPA': 0}
    for data in daftar_presensi(lokasi):
        hitung[data['status']] += 1
    return hitung


# ---------- US8: pencarian mahasiswa berdasarkan nama ----------
def cari_presensi(kata_kunci, lokasi=LOKASI_DEFAULT):
    """Cari presensi berdasarkan nama.

    Pencarian tidak membedakan huruf besar/kecil dan mencocokkan
    sebagian nama (substring). Kata kunci kosong mengembalikan semua data.
    Urutan hasil tetap sesuai urutan data di berkas.
    """
    kata_kunci = kata_kunci.strip().lower()
    data = daftar_presensi(lokasi)
    if not kata_kunci:
        return data
    return [baris for baris in data if kata_kunci in baris['nama'].lower()]


def main():
    print('=== APLIKASI PRESENSI PRAKTIKUM ===')
    while True:
        print('\n1. Input presensi\n2. Lihat daftar\n3. Lihat rekap'
              '\n4. Cari nama\n5. Keluar')
        menu = input('Pilih menu: ').strip()
        if menu == '1':
            nim = input('NIM   : ')
            nama = input('Nama  : ')
            status = input('Status (Hadir/Izin/Alpa): ')
            try:
                catat_presensi(nim, nama, status)
                print('Presensi berhasil disimpan.')
            except ValueError as error:
                print('Gagal:', error)
        elif menu == '2':
            data = daftar_presensi()
            if not data:
                print('Belum ada data.')
            for i, row in enumerate(data, 1):
                print(f"{i}. {row['nim']} - {row['nama']} - {row['status']}")
        elif menu == '3':
            rekap = rekap_presensi()
            print('Rekap:', rekap, '| Total:', sum(rekap.values()))
        elif menu == '4':
            kata_kunci = input('Cari nama: ')
            hasil = cari_presensi(kata_kunci)
            if not hasil:
                print(f'Tidak ada mahasiswa dengan nama mengandung "{kata_kunci.strip()}".')
            else:
                print(f'Ditemukan {len(hasil)} data:')
                for i, row in enumerate(hasil, 1):
                    print(f"{i}. {row['nim']} - {row['nama']} - {row['status']}")
        elif menu == '5':
            print('Selesai.')
            break
        else:
            print('Pilih menu 1-5.')


if __name__ == '__main__':
    main()
