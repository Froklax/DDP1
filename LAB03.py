#Loop untuk input file
while True:
    print("Selamat datang! Masukkan dua nama file yang berisi daftar makanan yang kamu miliki.")
    #Membaca nama file input dan output dari pengguna
    nama_file_input = input("Masukkan nama file input daftar makanan: ")
    nama_file_output = input("Masukkan nama file output: ")
    #Membaca isi dari file input
    try:
        file_input = open(nama_file_input, "r")
        lines = file_input.readlines()
        file_input.close()
        break
    #Mengecek apakah input file ada atau tidak
    except FileNotFoundError:
        print("File input tidak ditemukan.")
        continue

#Variabel daftar makanan pertama dan kedua
daftar_makanan_1 = ""
daftar_makanan_2 = ""
#Variabel untuk menandai jenis daftar yang sedang dibaca
daftar_sekarang = None
#Mengisi daftar makanan pertama dan kedua
for line in lines:
    #Menghilangkan karakter newline dan spasi ekstra
    line = line.strip().lower() 
    #Menghapus "Daftar Makanan 1:" dari awal line
    if line[:17] == "daftar makanan 1:":
        daftar_sekarang = "1"
        line = line[17:].strip()  
        daftar_makanan_1 = line
    #Menghapus "Daftar Makanan 2:" dari awal line
    elif line[:17] == "daftar makanan 2:":
        daftar_sekarang = "2"
        line = line[17:].strip()  
        daftar_makanan_2 = line

#Menggabungkan makanan dari kedua daftar dengan "," jika tidak kosong
gabungan_makanan = ""
if daftar_makanan_1 and daftar_makanan_2:
    gabungan_makanan += daftar_makanan_1 + "," + daftar_makanan_2
elif daftar_makanan_1:
    gabungan_makanan += daftar_makanan_1
elif daftar_makanan_2:
    gabungan_makanan += daftar_makanan_2

#Menemukan makanan yang sama dari kedua daftar
makanan_sama = ""
makanan_temp = ""
for char in daftar_makanan_1:
    if char != ",":
        makanan_temp += char
    else:
        if makanan_temp in daftar_makanan_2 and makanan_temp not in makanan_sama:
            if makanan_sama != "":
                makanan_sama += ","
            makanan_sama += makanan_temp
        makanan_temp = ""
#Cek untuk makanan terakhir di daftar
if makanan_temp in daftar_makanan_2 and makanan_temp not in makanan_sama:
    if makanan_sama != "":
        makanan_sama += ","
    makanan_sama += makanan_temp

#Menghapus duplikat dari daftar_makanan_1
makanan_unik_1 = ""
makanan_temp = ""
for char in daftar_makanan_1:
    if char != ",":
        makanan_temp += char
    else:
        if makanan_temp not in makanan_unik_1:
            if makanan_unik_1 != "":
                makanan_unik_1 += ","
            makanan_unik_1 += makanan_temp
        makanan_temp = ""
#Cek untuk makanan terakhir di daftar
if makanan_temp not in makanan_unik_1:
    if makanan_unik_1 != "":
        makanan_unik_1 += ","
    makanan_unik_1 += makanan_temp
#Daftar makanan 1 sekarang tidak memiliki duplikat
daftar_makanan_1 = makanan_unik_1

#Menghapus duplikat dari daftar_makanan_2
makanan_unik_2 = ""
makanan_temp = ""
for char in daftar_makanan_2:
    if char != ",":
        makanan_temp += char
    else:
        if makanan_temp not in makanan_unik_2:
            if makanan_unik_2 != "":
                makanan_unik_2 += ","
            makanan_unik_2 += makanan_temp
        makanan_temp = ""
#Cek untuk makanan terakhir di daftar
if makanan_temp not in makanan_unik_2:
    if makanan_unik_2 != "":
        makanan_unik_2 += ","
    makanan_unik_2 += makanan_temp
#Daftar makanan 2 sekarang tidak memiliki duplikat
daftar_makanan_2 = makanan_unik_2

#Menghapus duplikat dari gabungan_maken
makanan_unik_gabungan = ""
makanan_temp = ""
for char in gabungan_makanan:
    if char != ",":
        makanan_temp += char
    else:
        if makanan_temp not in makanan_unik_gabungan:
            if makanan_unik_gabungan != "":
                makanan_unik_gabungan += ","
            makanan_unik_gabungan += makanan_temp
        makanan_temp = ""
#Cek untuk makanan terakhir di daftar
if makanan_temp not in makanan_unik_gabungan:
    if makanan_unik_gabungan != "":
        makanan_unik_gabungan += ","
    makanan_unik_gabungan += makanan_temp
#Gabungan makanan sekarang tidak memiliki duplikat
gabungan_makanan = makanan_unik_gabungan

#Menampilkan menu, menerima input dari pengguna dan menyimpan hasil ke file output
file_output = open(nama_file_output, "w")
while True:
    print("Apa yang ingin kamu lakukan?")
    print("================================================")
    print("1. Tampilkan daftar makanan pertama")
    print("2. Tampilkan daftar makanan kedua")
    print("3. Tampilkan gabungan makanan dari dua daftar")
    print("4. Tampilkan makanan yang sama dari dua daftar")
    print("5. Keluar")
    print("================================================")
    #Input aksi
    aksi = input("Masukkan aksi yang ingin dilakukan: ")
    #Kondisi untuk aksi yang dipilih
    if aksi == "1":
        if daftar_makanan_1:
            print("\nDaftar makanan pertama:")
            print(daftar_makanan_1 + "\n")
            file_output.write("Daftar makanan pertama:\n")
            file_output.write(daftar_makanan_1 + "\n\n")
        else:
            print("\nTidak ada makanan dalam daftar pertama\n")
            file_output.write("Tidak ada makanan dalam daftar pertama\n\n")
    elif aksi == "2":
        if daftar_makanan_2:
            print("\nDaftar makanan kedua:")
            print(daftar_makanan_2 + "\n")
            file_output.write("Daftar makanan kedua:\n")
            file_output.write(daftar_makanan_2 + "\n\n")
        else:
            print("\nTIdak ada makanan dalam daftar kedua\n")
            file_output.write("Tidak ada makanan dalam daftar kedua\n\n")
    elif aksi == "3":
        if gabungan_makanan:
            print("\nGabungan makanan favorit dari kedua daftar:")
            print(gabungan_makanan + "\n")
            file_output.write("Gabungan makanan favorit dari kedua daftar:\n")
            file_output.write(gabungan_makanan + "\n\n")
        else:
            print("\nTidak ada makanan dalam gabungan makanan \n")
            file_output.write("Tidak ada makanan dalam gabungan makanan \n\n")
    elif aksi == "4":
        if makanan_sama:
            print("\nMakanan yang sama dari dua daftar:")
            print(makanan_sama + "\n")
            file_output.write("Makanan yang sama dari dua daftar:\n")
            file_output.write(makanan_sama + "\n\n")
        else:
            print("\nTidak ada makanan yang sama dalam kedua daftar\n")
            file_output.write("Tidak ada makanan yang sama dalam kedua daftar\n\n")
    elif aksi == "5":
        print("\nTerima kasih telah menggunakan program ini!")
        break
    else:
        print("Aksi tidak valid. Silakan pilih aksi yang sesuai.")
print(f"Semua keluaran telah disimpan pada file {nama_file_output}")
file_output.close()
