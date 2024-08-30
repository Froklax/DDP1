#Membuat loop untuk pilihan fitur
while True:
    #Pembuka awal program
    print("Selamat Datang di Toko Buku Place Anak Chill")
    print("============================================")
    print("1. Pinjam Buku")
    print("2. Keluar")
    print("============================================")
    #Pilih fitur yang ingin digunakan
    fitur = int(input("Apa yang ingin anda lakukan: "))
    if fitur == 1:
        #Masukkan berbagai input yang diminta
        nama = input("Masukkan nama anda: ").strip()
        saldo = int(input("Masukkan saldo anda (Rp): ").strip())
        membership = input("Apakah anda member? [Y/N]: ").strip().upper()
        #Menghitung kalau ID berjumlah 23 saat memiliki membership    
        if membership == "Y":
            percobaan_login = 0
            #Menghitung total angka ID
            while percobaan_login < 3:
                identitas = int(input("Masukkan ID anda: "))
                jumlah = 0
                for angka in str(identitas):
                    jumlah += int(angka)
                #Jika jumlah angka ID sama dengan 23, login member berhasil
                if jumlah == 23:
                    print("Login member berhasil!\n")
                    break
                elif jumlah != 23:
                    print("ID anda salah!")
                percobaan_login += 1
            #Jika jumlah angka ID tidak berjumlah 23 sebanyak 3 kali, kembali ke menu utama
            else:
                print("ID salah sebanyak 3 kali, kembali ke menu utama")
                continue

        #Kalau tidak memiliki membership
        elif membership == "N":
            print("Login non-member berhasil!\n")
            
        #Loop untuk peminjaman buku
        while True:
            #Katalog peminjaman buku
            print("============================================")
            print("Katalog Buku Place Anak Chill")
            print("============================================")
            print("X-Man (Rp 7.000/hari)")
            print("Doraemoh (Rp 5.500/hari")
            print("Nartoh (Rp 4.000/hari)")
            print("============================================")
            print("Exit")
            print("============================================")
            #Masukkan jenis buku
            jenis_buku = input("Buku yang dipilih: ").strip().lower()
            if jenis_buku == "x-man" or jenis_buku == "doraemoh" or jenis_buku == "nartoh" or jenis_buku == "exit":
                #Jika memilih fitur exit, kembali ke menu utama
                if jenis_buku == "exit":
                    print()
                    break
                #Masukkan durasi peminjaman
                waktu_peminjaman = int(input("Ingin melakukan peminjaman untuk berapa hari: ").strip())
                #Diskon untuk member
                if membership == "Y":
                    diskon = 0.2
                else:
                    diskon = 0
                #Kondisi jika buku x-man, doraemoh, atau nartoh
                if jenis_buku == "x-man":
                    harga = waktu_peminjaman * 7000
                elif jenis_buku == "doraemoh":
                    harga = waktu_peminjaman * 5500
                elif jenis_buku == "nartoh":
                    harga = waktu_peminjaman * 4000
                #Hitung harga sewa buku
                total_harga = harga * (1 - diskon)
                #Hitung saldo sekarang
                if saldo >= total_harga:
                    saldo -= total_harga   
                    #Memberitahu saldo sekarang
                    print(f"Berhasil meminjam buku {jenis_buku} selama {waktu_peminjaman} hari. Saldo anda saat ini Rp{saldo}\n")
                else:
                    #Memberitahu saldo yang dibutuhkan jika tidak mencukupi
                    print(f"Tidak berhasil meminjam buku {jenis_buku}! Saldo anda kurang Rp{harga - saldo}\n")
            else:
                print("Komik tidak ditemukan. Masukkan kembali judul komik sesuai katalog!\n")
    #Keluar dari program
    elif fitur == 2:
        print("Terima kasih telah mengunjungi Toko Buku Place Anak Chill!")
        break
    #Jika memilih fitur diluar 1 atau 2
    else:
        print("Perintah tidak diketahui! Silahkan pilih 1 atau 2.\n")






            
