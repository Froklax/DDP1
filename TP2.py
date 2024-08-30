import os
import sys
import time
mulai_time = time.time()
#Tempat dataset disimpan
directory = "C:\\Users\\bertr\\Downloads\\indo-law-main\\indo-law-main\\dataset"
#Jika tidak memasukkan kata kunci apa apa akan mengeluarkan error
if len(sys.argv) < 3:
    print("\nArgumen program tidak benar")
    sys.exit()
#Berbagai input untuk command line argument
section = sys.argv[1]
kata_kunci1 = sys.argv[2]
#Kalau kata kunci yang ingin dimasukkan lebih dari satu
if len(sys.argv) > 3:
    operator = sys.argv[3]
    kata_kunci2 = sys.argv[4]
    #Jika operator yang digunakan tidak sesuai
    if operator not in ["AND", "OR", "ANDNOT", None]:
        print("\nMode harus berupa AND, OR atau ANDNOT.")
        sys.exit()
else:
    operator = None
    kata_kunci2 = None
banyak_file = 0
#Loop untuk file di dataset
for files in os.listdir(directory):
    with open(os.path.join(directory, files), "r") as file:
        #Menggabungkan line yang sebelumnya terpisah-pisah menjadi satu line saja
        lines = file.read().replace("\n", " ")
        #Mencari letak variable dan membuang depan variable
        mulai_pembagian = lines.find('klasifikasi="') + len('klasifikasi="')
        akhir_pembagian = lines.find('"', mulai_pembagian)
        klasifikasi = lines[mulai_pembagian:akhir_pembagian]
        
        mulai_pembagian = lines.find('lembaga_peradilan="') + len('lembaga_peradilan="')
        akhir_pembagian = lines.find('"', mulai_pembagian)
        lembaga_peradilan = lines[mulai_pembagian:akhir_pembagian]

        mulai_pembagian = lines.find('provinsi="') + len('provinsi="')
        akhir_pembagian = lines.find('"', mulai_pembagian)
        provinsi = lines[mulai_pembagian:akhir_pembagian]

        mulai_pembagian = lines.find('sub_klasifikasi="') + len('sub_klasifikasi="')
        akhir_pembagian = lines.find('"', mulai_pembagian)
        sub_klasifikasi = lines[mulai_pembagian:akhir_pembagian]
        #Argumen untuk jika section adalah "all"
        if section == "all":
            #Argumen jika operator yang digunakan "AND", "OR", "ANDNOT", atau hanya menggunakan satu kata kunci
            if operator == "AND":
                if kata_kunci1 in lines and kata_kunci2 in lines:
                    print(files + " " + provinsi.rjust(15) + " " + klasifikasi.rjust(15) + " " + sub_klasifikasi[:30].rjust(30) + " " + lembaga_peradilan[:20].rjust(20))
                    banyak_file += 1
            elif operator == "OR":
                if kata_kunci1 in lines or kata_kunci2 in lines:
                    print(files + " " + provinsi.rjust(15) + " " + klasifikasi.rjust(15) + " " + sub_klasifikasi[:30].rjust(30) + " " + lembaga_peradilan[:20].rjust(20))
                    banyak_file += 1
            elif operator == "ANDNOT":
                if kata_kunci1 in lines and not kata_kunci2 in lines:
                    print(files + " " + provinsi.rjust(15) + " " + klasifikasi.rjust(15) + " " + sub_klasifikasi[:30].rjust(30) + " " + lembaga_peradilan[:20].rjust(20))
                    banyak_file += 1
            elif operator == None:
                if kata_kunci1 in lines:
                    print(files + " " + provinsi.rjust(15) + " " + klasifikasi.rjust(15) + " " + sub_klasifikasi[:30].rjust(30) + " " + lembaga_peradilan[:20].rjust(20))
                    banyak_file += 1
        #Kalau bukan all tetapi menggunakan section tertentu
        else:
            #Mencari letak section yang ingin dilihat
            kepala_section = lines.find("<" + section + ">")
            ekor_section = lines.find("</" + section + ">")
            text = lines[kepala_section:ekor_section].strip()
            #Membuang bagian section dan hanya melihat isinya saja
            text = text.replace("<" + section + ">", "").replace("</" + section + ">", "")
            #Argumen jika operator yang digunakan "AND", "OR", "ANDNOT", atau hanya menggunakan satu kata kunci
            if operator == "AND":
                if kata_kunci1 in text and kata_kunci2 in text:
                    print(files + " " + provinsi.rjust(15) + " " + klasifikasi.rjust(15) + " " + sub_klasifikasi[:30].rjust(30) + " " + lembaga_peradilan[:20].rjust(20))
                    banyak_file += 1
            elif operator == "OR":
                if kata_kunci1 in text or kata_kunci2 in text:
                    print(files + " " + provinsi.rjust(15) + " " + klasifikasi.rjust(15) + " " + sub_klasifikasi[:30].rjust(30) + " " + lembaga_peradilan[:20].rjust(20))
                    banyak_file += 1 
            elif operator == "ANDNOT":
                if kata_kunci1 in text and not kata_kunci2 in text:
                    print(files + " " + provinsi.rjust(15) + " " + klasifikasi.rjust(15) + " " + sub_klasifikasi[:30].rjust(30) + " " + lembaga_peradilan[:20].rjust(20))
                    banyak_file += 1
            elif operator == None:
                if kata_kunci1 in text:
                    print(files + " " + provinsi.rjust(15) + " " + klasifikasi.rjust(15) + " " + sub_klasifikasi[:30].rjust(30) + " " + lembaga_peradilan[:20].rjust(20))
                    banyak_file += 1
#Memberitahu berapa banyak dokumen yang ditemukan dan total waktu pencarian
print(f"\nBanyaknya dokumen yang ditemukan = {banyak_file}")
stop_time = time.time()
waktu_pencarian = stop_time - mulai_time
print(f"Total waktu pencarian            = {waktu_pencarian:.3f} detik")
