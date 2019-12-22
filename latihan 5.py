data = {}

cetak ( " ╔══════════════════════════════════════════════ ═══════════════════════════╗ " )
cetak ( " ╠════════════════════ PROGRAM DATA MAHASISWA DATA INPUT ══════════════════════ ═╣ " )
cetak ( " ╠═══════════╦════════════╦════════════╦════════ ═════╦══════════╦══════════╣ " )
cetak ( " ║ (A) dd ║ (E) dit ║ (D) hapus ║ (S) earch ║ (L) ist ║ (Q) uit ║ " )
cetak ( " ╚═══════════╩════════════╩════════════╩════════ ═════╩══════════╩══════════╝ " )

sementara Benar :

    c =  input ( " \ n Pilih Opsi: " )

# PROGRAM KELUAR
    if c.lower () ==  ' q ' :
        istirahat

# CETAK DATA
    elif c.lower () ==  ' l ' :
        cetak ( " \ n ╔════════════════════════════════════════════ ═════════════════════════════╗ " )
        print ( " ╠═════════════════════════ DAFTAR DATA MAHASISWA ══════════════════ ═══════╣ " )
        cetak ( " ╠════╦═════════════════╦══════════════════╦════ ═══╦═══════╦═══════╦═══════╣ " )
        cetak ( " ║ TIDAK ║ NAMA ║ NIM ║ TUGAS ║ UTS ║ UAS ║ AKHIR ║ " )
        cetak ( " ╠════╬═════════════════╬══════════════════╬════ ═══╬═══════╬═══════╬═══════╣ " )
        tidak =  1
        untuk tabel di data.values ​​():
            cetak ( " ║ {0 : 3 } ║ {1 : 15 } ║ {2 : 16 } ║ {3 : 5 } ║ {4 : 5 } ║ {5 : 5 } ║ {6 : 5 } ║ "
              .format (no, tabel [ 0 ], tabel [ 1 ], tabel [ 2 ], tabel [ 3 ], tabel [ 4 ], tabel [ 5 ]))
            no + =  1
        cetak ( " ╚════╩═════════════════╩══════════════════╩════ ═══╩═══════╩═══════╩═══════╝ " )
        cetak ( " \ n     (A) dd (E) dit (D) hilangkan (S) earch (L) ist (Q) uit    " )


# DATA MENAMBAH
    elif c.lower () ==  ' a ' :
        print ( " \ n ════Masukan Data Mahasiswa════ " )

        sementara ( Benar ):
            nama =  input ( " NAMA: " )
            jika nama ==  ' ' :
                print ( ' Nama tidak boleh kosong ' )
            lain :
                istirahat
        sementara ( Benar ):
            coba :
                nim   =  int ( input ( " NIM: " ))
                jika nim ==  ' ' :
                    print ( ' tambah Nim dengan Angka ' )
            kecuali  ValueError :
                print ( ' tambah Nim dengan Angka ' )
            lain :
                istirahat
        sementara ( Benar ):
            coba :
                tugas   =  int ( input ( " TUGAS: " ))
                jika tugas ==  ' ' :
                    print ( ' tambahkan TUGAS dengan Angka ' )
            kecuali  ValueError :
                print ( ' tambahkan TUGAS dengan Angka ' )
            lain :
                istirahat
        sementara ( Benar ):
            coba :
                uts   =  int ( input ( " UTS: " ))
                jika uts ==  ' ' :
                    print ( ' tulis UTS dengan Angka ' )
            kecuali  ValueError :
                print ( ' tulis UTS dengan Angka ' )
            lain :
                istirahat
        sementara ( Benar ):
            coba :
                uas   =  int ( input ( " UAS: " ))
                jika uas ==  ' ' :
                    p ( ' diterbitkan UAS dengan Angka ' )
            kecuali  ValueError :
                print ( ' masukkan UAS dengan Angka ' )
            lain :
                istirahat
        akhir =  round (( float (tugas) *  0.3 ) + ( float (uts) *  0.35 ) + ( float (uas) *  0.35 ), 2 )
        data [nama] = [nama, nim, tugas, uts, uas, akhir]

        cetak ( " \ n     (A) dd (E) dit (D) hilangkan (S) earch (L) ist (Q) uit    " )


# EDIT DATA
    elif c.lower () ==  ' e ' :
        nama =  input ( " dipindahkan nama untuk mengedit data: " )

        jika nama dalam data.keys ():
            data del [nama]
            print ( " \ n ═══Masukan Data Pembaruan═══ " )

            sementara ( Benar ):
                nama =  input ( " NAMA: " )
                jika nama ==  ' ' :
                    print ( ' Nama tidak boleh kosong ' )
                lain :
                    istirahat
            sementara ( Benar ):
                coba :
                    nim =  int ( input ( " NIM: " ))
                    jika nim ==  ' ' :
                        print ( ' tambah Nim dengan Angka ' )
                kecuali  ValueError :
                    print ( ' tambah Nim dengan Angka ' )
                lain :
                    istirahat
            sementara ( Benar ):
                coba :
                    tugas =  int ( input ( " TUGAS: " ))
                    jika tugas ==  ' ' :
                        print ( ' tambahkan TUGAS dengan Angka ' )
                kecuali  ValueError :
                    print ( ' tambahkan TUGAS dengan Angka ' )
                lain :
                    istirahat
            sementara ( Benar ):
                coba :
                    uts =  int ( input ( " UTS: " ))
                    jika uts ==  ' ' :
                        print ( ' tulis UTS dengan Angka ' )
                kecuali  ValueError :
                    print ( ' tulis UTS dengan Angka ' )
                lain :
                    istirahat
            sementara ( Benar ):
                coba :
                    uas =  int ( input ( " UAS: " ))
                    jika uas ==  ' ' :
                        print ( ' masukkan UAS dengan Angka ' )
                kecuali  ValueError :
                    print ( ' masukkan UAS dengan Angka ' )
                lain :
                    istirahat
            akhir =  round (( float (tugas) *  0.3 ) + ( float (uts) *  0.35 ) + ( float (uas) *  0.35 ), 2 )
            data [nama] = [nama, nim, tugas, uts, uas, akhir]

        lain :
            cetak ( " ________________________ " )
            print ( " | Data {} tidak ditemukan | " .format (nama))
            cetak ( " ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ " )
        cetak ( " \ n     (A) dd (E) dit (D) hilangkan (S) earch (L) ist (Q) uit    " )



# DATA MENCARI
    elif c.lower () ==  ' s ' :
        nama =  input ( " dipindahkan nama yang di cari: " )
        jika nama dalam data.keys ():

            cetak ( " \ n ╔═════════════════╦══════════════════╦═══════ ╦═══════╦═══════╦═══════╗ " )
            cetak ( " ║ NAMA ║ NIM ║ TUGAS ║ UTS ║ UAS ║ AKHIR ║ " )
            cetak ( " ╠═════════════════╬══════════════════╬═══════╬═ ══════╬═══════╬═══════╣ " )
            mencetak ( " ║ {0 : 15 } ║ {1 : 16 } ║ {2 : 5 } ║ {3 : 5 } ║ {4 : 5 } ║ {5 : 5 } ║ " .format (nama, data yang [nama di] [ 1 ], data [nama] [ 2 ], data [nama] [ 3 ], data [nama] [ 4 ], data [nama] [ 5 ])))
            cetak ( " ╚═════════════════╩══════════════════╩═══════╩═ ══════╩═══════╩═══════╝ " )
        lain :
            cetak ( " ________________________ " )
            print ( " | Data {} tidak ditemukan | " .format (nama))
            cetak ( " ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ " )

        cetak ( " \ n     (A) dd (E) dit (D) hilangkan (S) earch (L) ist (Q) uit    " )

# DATA HAPUS
    elif c.lower () ==  ' d ' :
        nama =  input ( " mentransfer nama untuk menyimpan data: " )
        jika nama dalam data.keys ():
            data del [nama]
            print ( " Data {} dipindahkan " .format (nama))
        lain :
            cetak ( " ________________________ " )
            print ( " | Data {} tidak ditemukan | " .format (nama))
            cetak ( " ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ " )

        cetak ( " \ n     (A) dd (E) dit (D) hilangkan (S) earch (L) ist (Q) uit    " )


    lain :
        cetak ( " __________________________ " ))
        print ( " | Pilih opsi yang tersedia | " )
        cetak ( " ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ " )
        cetak ( "     (A) dd (E) dit (D) elete (S) earch (L) ist (Q) uit    " )
