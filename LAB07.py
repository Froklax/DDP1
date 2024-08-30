#Menyimpan data relasi dalam dictionary
relasi = {}
print("Masukkan data relasi:")
#Meminta data relasi
while True:
    data = input()
    #Loop untuk input data berhenti jika SELESAI dimasukkan
    if data == "SELESAI":
        print()
        break
    else:
        #Memisahkan input menjadi dua bagian yaitu nama_parent dan nama_child
        nama_parent, nama_child = data.split()
        #Jika nama_parent sudah ada dalam relasi, tambahkan nama_child ke list anak-anaknya
        if nama_parent in relasi:
            relasi[nama_parent].append(nama_child)
        #Jika nama_parent belum ada dalam relasi, buat list baru yang berisi nama_child
        else:
            relasi[nama_parent] = [nama_child]
#Fungsi cek_keturunan 
def cek_keturunan(nama_parent, nama_child):
    if nama_parent in relasi:
         #Jika nama_child adalah anak langsung dari nama_parent akan return True
        if nama_child in relasi[nama_parent]:
            return True
        else:
            #Jika tidak akan memeriksa setiap anak dari nama_parent
            for child in relasi[nama_parent]:
                #Jika nama_child adalah keturunan dari salah satu anak akan return True
                if cek_keturunan(child, nama_child):
                    return True
    #Jika nama_parent tidak ada dalam relasi atau nama_child bukan keturunan
    return False
#Fungi cetak_keturunan
def cetak_keturunan(nama_parent):
    keturunan = ""
    if nama_parent in relasi:
        #Tambahkan setiap anak dan keturunan anak dari nama_parent ke output keturunan
        for child in relasi[nama_parent]:
            keturunan += "- " + child + "\n"
            keturunan += cetak_keturunan(child)
    #Return output keturunan
    return keturunan
#Fungsi jarak_generasi
def jarak_generasi(nama_parent, nama_child):
    #Jika nama_parent dan nama_child orang yang sama program akan return 0
    if nama_parent == nama_child:
        return 0
    #Jika nama_parent ada dalam relasi
    elif nama_parent in relasi:
        #Jika nama_child adalah anak langsung dari nama_parent maka program akan return 1
        if nama_child in relasi[nama_parent]:
            return 1
        #Jika bukan anak langsung
        else:
            #Jika nama_child adalah keturunan dari salah satu anak program akan return jarak + 1
            for child in relasi[nama_parent]:
                jarak = jarak_generasi(child, nama_child)
                if jarak is not None:
                    return jarak + 1
    #Jika nama_parent tidak ada dalam relasi atau nama_child bukan keturunan dari nama_parent
    return None
#Loop utama dari program
while True:
    #Pembuka program dan menu
    print("=====================================================================")
    print("Selamat Datang di Relation Finder! Pilihan yang tersedia:")
    print("1. CEK_KETURUNAN")
    print("2. CETAK_KETURUNAN")
    print("3. JARAK_GENERASI")
    print("4. EXIT")
    #Input untuk pilihan
    pilihan = input("Masukkan pilihan: ")
    #Kondisi untuk pilihan
    if pilihan == "1":
        nama_parent = input("Masukkan nama parent: ")
        nama_child = input("Masukkan nama child: ")
        if cek_keturunan(nama_parent, nama_child):
            print(f"{nama_child} benar merupakan keturunan dari {nama_parent}\n")
        else:
            print(f"{nama_child} bukan merupakan keturunan dari {nama_parent}\n")
    elif pilihan == "2":
        nama_parent = input("Masukkan nama parent: ")
        print(cetak_keturunan(nama_parent))
    elif pilihan == "3":
        nama_parent = input("Masukkan nama parent: ")
        nama_child = input("Masukkan nama child: ")
        jarak = jarak_generasi(nama_parent, nama_child)
        if jarak is not None:
            print(f"{nama_parent} memiliki hubungan dengan {nama_child} sejauh {jarak}\n")
        else:
            print(f"Tidak ada hubungan antara {nama_parent} dengan {nama_child}\n")
    elif pilihan == "4":
        print("Terima kasih telah menggunakan Relation Finder!")
        break
