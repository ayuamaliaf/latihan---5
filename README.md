Program Penjelasan 5 :.
1.Deklarasi data kamus
2.Input untuk memilih opsi
(A) dd (E) dit (D) elete (S) earch (L) ist (Q) uit

3.Jika Input A
•	3.1 Masukkan nama, nim, tugas, uts, uas
•	3.2 Nilai akhir perpaduan nilai tugas, uts, uas
•	3.3 Jika nilai nim, tugas, uts, uas, kosong / tidak di isi dengan angka maka ValueError dan meminta input ulang
•	3.4 semua data akan di tambahkan menjadi nilai dan kunci menggunakan nama
4.Jika Input E
•	4.1 Masukkan nama / kunci yg di cari
•	4.2 Jika nama ada di data.keys
o	4.2.1 Masukkan data yang dimasukkan
o	4.2.2 Jika nilai nim, tugas, uts, uas, kosong / tidak di isi dengan angka maka ValueError dan meminta input ulang
o	4.2.3 Input akan menimpa data yang lama
•	4.3 Jika tidak
o	4.3.1 Data tidak di temukan
5.Jika Input D
•	5.1 Masukkan nama / kunci yg di cari
•	5.2 Jika nama ada di data.keys
o	5.2.1 Maka datanya akan di hapus
•	5.3 Jika tidak
o	5.3.1 Data tidak di temukan
6.Jika Input S
•	6.1 Masukkan nama / kunci yg di cari
•	6.2 Jika nama ada di data.keys
o	6.2.1 Cetak nama, nim, uts, tugas, akhir
•	6.3
o	6.3.1 Data tidak di temukan
7.Jika Input L
•	7.1 Cetak data. Nilai / bawa semua nilai
8.Jika Input Q
•	8.1 Program Berhenti
9.Jika Input Luar, A, E, D, S, L, Q
•	9.1 Pilih opsi yang tersedia
