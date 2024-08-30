#List untuk menyimpan data nama siswa dan nilai lab
list_penyimpanan = []
#Loop untuk aksi
while True:
    #Pembuka
    print("Selamat datang di Database Nilai Dek Depe")
    print("1. Tambah data ke database")
    print("2. Baca data dari database")
    print("3. Update data di database")
    print("4. Hapus data dari database")
    print("5. Keluar")
    input_aksi = input("Masukkan kegiatan yang ingin dilakukan: ")
    #Kondisi untuk kegiatan 1
    if input_aksi == "1":
        siswa = input("Masukkan nama: ")
        #Jika menambahkan nama yang sudah terdapat di database
        for data_siswa in list_penyimpanan:
            if siswa.lower() == data_siswa[0]:
                print("Nama sudah terdapat di dalam database\n")
                break
        #Menambahkan data ke list_penyimpanan
        else:
            list_penyimpanan.append([siswa.lower()])
            counter = 1
            while True:
                input_nilai = input(f"Masukkan nilai Lab {counter} (ketik STOP untuk selesai): ")
                if input_nilai.upper() == "STOP":
                    print(f"Berhasil menambahkan {counter - 1} nilai untuk {siswa} ke database\n")
                    break
                elif int(input_nilai) in range(0, 101):
                    list_penyimpanan[-1].append(int(input_nilai))
                    counter += 1
                    pass
                else:
                    print("Masukkan nilai yang valid")
    #Kondisi untuk kegiatan 2
    elif input_aksi == "2":
        siswa2 = input("Masukkan nama: ")
        #Membaca data yang terdapat di database
        for data_siswa in list_penyimpanan:
            if siswa2.lower() == data_siswa[0]:
                nilai_dicari = int(input("Masukkan nilai Lab ke berapa yang ingin dilihat: "))
                #Jika nilai telah diremove
                if data_siswa[nilai_dicari] == None:
                    print(f"Tidak terdapat nilai untuk Lab {nilai_dicari}\n")
                    break
                #Jika nilai yang ingin dicari di dalam jangkauan nilai lab yang terdapat di database
                elif nilai_dicari < len(data_siswa):
                    print(f"Nilai Lab {nilai_dicari} {siswa2} adalah {data_siswa[nilai_dicari]:.1f}\n")
                    break
                else:
                    print(f"Tidak terdapat nilai untuk Lab {nilai_dicari}\n")
                    break
        else:
            print("Nama tidak ada dalam database\n")
            continue
    #Kondisi untuk kegiatan 3
    elif input_aksi == "3":
        siswa3 = input("Masukkan nama: ")
        #Mengupdate data yang ada di database
        for data_siswa in list_penyimpanan:
            if siswa3.lower() == data_siswa[0]:
                nilai_update = int(input("Masukkan nilai Lab ke berapa yang ingin diupdate: "))
                #Jika nilai yang ingin diupdate di dalam jangkauan nilai lab yang terdapat di database
                if nilai_update < len(data_siswa):
                    nilai_baru = int(input("Masukkan nilai baru untuk Lab 3: "))
                    print(f"Berhasil mengupdate nilai Lab {nilai_update} {siswa2} dari {data_siswa[int(nilai_update)]:.1f} ke {nilai_baru:.1f}\n")
                    #Mengupdate nilai baru
                    data_siswa[nilai_update] = nilai_baru
                    break
                else:
                    print(f"Tidak terdapat nilai untuk Lab {nilai_update}\n")
                    break
        else:
            print("Nama tidak ada dalam database\n")
            continue
    #Kondisi untuk kegiatan 4
    elif input_aksi == "4":
        siswa4 = input("Masukkan nama: ")
        #Mengremove data yang terdapat di database
        for data_siswa in list_penyimpanan:
            if siswa4.lower() == data_siswa[0]:
                nilai_hapus = int(input("Masukkan nilai Lab ke berapa yang ingin dihapus: "))
                #Jika nilai yang ingin dihapus di dalam jangkauan nilai lab yang terdapat di database
                if nilai_hapus < len(data_siswa):
                    nilai_dihapus = data_siswa[nilai_hapus]
                    #Mengremove nilai yang ingin di remove
                    data_siswa[nilai_hapus] = None
                    print(f"Berhasil menghapus nilai Lab {nilai_hapus} {siswa4} dari database\n")
                    break
                else:
                    print(f"Tidak terdapat nilai untuk Lab {nilai_hapus}")
                    break
        else:
            print("Nama tidak ada dalam database\n")
            continue
    #Jika input aksi == "5", maka program akan berhenti
    elif input_aksi == "5":
        print("Terimakasih telah menggunakan Database Nilai Dek Depe")
        break