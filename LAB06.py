#Pembuka
print("Selamat datang di program Plagiarism Checker!")
#Membuka file "Lab6.txt" untuk membaca data tugas mahasiswa
with open("Lab6.txt", "r") as file:
    data = file.read().split("\n\n")
#Membuat dictionary data info_siswa untuk menyimpan informasi mahasiswa dan tugasnya
info_siswa = {}
npm_ke_nama = {}
#Memproses data mahasiswa
for data_siswa in data:
    lines = data_siswa.split("\n")
    if len(lines) >= 3:
        nama, npm, mata_pelajaran = lines[0].split(";")
        isi_text = lines[2:]
        #Mencatat nama dan npm mahasiwa ke dictionary info_siswa
        if nama not in info_siswa:
            info_siswa[nama] = {}
        if npm not in info_siswa:
            info_siswa[npm] = {}
        mata_pelajaran = mata_pelajaran.strip()
        #Mengisi data tugas ke dalam dictionary
        info_siswa[nama][mata_pelajaran] = isi_text
        info_siswa[npm][mata_pelajaran] = isi_text
        npm_ke_nama[npm] = nama
#Loop untuk program
while True:
    print("=====================================================================")
    #Input mata pelajaran dan mengecek apakah mata pelajaran yang dimasukkan ada atau tidak
    mata_pelajaran = input("Masukkan nama mata kuliah yang ingin diperiksa: ")
    mata_pelajaran_ditemukan = False
    for data_siswa in data:
        lines = data_siswa.split("\n")
        if len(lines) >= 3 and mata_pelajaran == lines[0].split(";")[2].strip():
            mata_pelajaran_ditemukan = True
            break
    #Jika input adalah exit maka program akan berhenti
    if mata_pelajaran.lower() == "exit":
        print("Terima kasih telah menggunakan program Plagiarism Checker!")
        break
    #Jika mata pelajaran yang dimasukkan tidak ada
    if not mata_pelajaran_ditemukan:
        print(f"{mata_pelajaran} tidak ditemukan.\n")
        continue
    #Input untuk nama/npm siswa
    siswa1 = input("Masukkan nama/NPM mahasiswa pertama: ")
    #Jika nama/npm siswa tidak ada, maka akan mengeluarkan pesan tidak ditemukan
    if siswa1 not in info_siswa:
        print("Informasi mahasiswa tidak ditemukan.\n")
        continue
    
    siswa2 = input("Masukkan nama/NPM mahasiswa kedua: ")
    if siswa2 not in info_siswa:
        print("Informasi mahasiswa tidak ditemukan.\n")
        continue
    #Mengambil text tugas mahasiswa pertama dan kedua untuk mata pelajaran tertentu
    task1_lines = info_siswa[siswa1][mata_pelajaran]
    task2_lines = info_siswa[siswa2][mata_pelajaran]
    
    #Memisahkan kata-kata dalam teks tugas
    task1_words = []
    for line in task1_lines:
        words = line.split()
        task1_words += words
    task2_words = []
    for line in task2_lines:
        words = line.split()
        task2_words += words
    
    #Menggunakan set untuk menghilangkan duplikat
    set_keyword_unik = set(task1_words)
    #Membuat set yang berisi kata-kata yang sama antara tugas mahasiswa pertama dan kedua
    set_keyword_sama = set(task1_words) & set(task2_words)  
    #Menghitung jumlah keyword sama dan keyword unik
    keyword_sama = len(set_keyword_sama)
    keyword_unik = len(set_keyword_unik)
    #Menghitung persentase plagiarisme
    persentase_plagiarisme = (keyword_sama / keyword_unik) * 100

    #Kasus-kasus untuk persentase plagiarisme
    if persentase_plagiarisme < 31:
        plagiarisme = "tidak terindikasi plagiarisme"
    elif 30 < persentase_plagiarisme < 71:
        plagiarisme = "terindikasi plagiarisme ringan"
    else:
        plagiarisme = "terindikasi plagiarisme"
    #Jika siswa1 atau siswa2 menggunakan npm, ganti ke nama dahulu baru mencetak
    try:
        int(siswa1)  
        siswa1 = npm_ke_nama[siswa1]  
    except ValueError:  
        pass
    #Cetak hasil
    print("============================= Hasil =================================")
    print(f"Tingkat kemiripan tugas {mata_pelajaran} {siswa1} dan {siswa2} adalah {persentase_plagiarisme:.2f}%.")
    print(f"{siswa1} dan {siswa2} {plagiarisme}.\n")
