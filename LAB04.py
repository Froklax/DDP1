import sys
#Fungsi untuk menampilkan table header
def print_headers():
    print("| {: <2} | {: <25} | {: <8} | {: <10} | {: <3} |".format("No", "Smartphone", "Price", "Screensize", "RAM"))
    print("================================================================")

#Fungsi untuk mengeprint table content
def print_table(filename):
    #Read text file
    with open(filename, "r") as f:
        lines = f.readlines()
        print_headers()
        number = 1
        #Memisahkan setiap baris menjadi bagian "Smartphone", "Price", "Screensize", dan "Ram"
        for line in lines:
            line = line.strip()
            kode_split = line.split()
            ram = kode_split[-1]
            screensize = kode_split[-2]
            price = kode_split[-3]
            smartphone = " ".join(kode_split[:-3])
            #Menampilkan tabel content penuh
            print("| {: <2} | {: <25} | {: <8} | {: <10} | {: <3} |".format(number, smartphone, price, screensize, ram))
            number += 1

#Fungsi untuk mengeprint table dari suatu keyword handphone tertentu dan memberikan ukuran data juga
def search_phone(filename, keyword):
    #Read text file
    with open(filename, "r") as f:
        lines = f.readlines()
        print()
        print_headers()
        number = 1
        #Memisahkan setiap baris menjadi bagian "Smartphone", "Price", "Screensize", dan "Ram"
        for line in lines:
            line = line.strip()
            kode_split = line.split()
            ram = kode_split[-1]
            screensize = kode_split[-2]
            price = kode_split[-3]
            smartphone = " ".join(kode_split[:-3])
            #Jika keyword di line, maka akan mencetak line yang terdapat keyword
            if keyword.lower() in line.lower():
                #Menampilkan tabel content yang hanya bagian yang terdapat keyword
                print("| {: <2} | {: <25} | {: <8} | {: <10} | {: <3} |".format(number, smartphone, price, screensize, ram))
                number +=1
        #Menampilkan ukuran data
        print(f"Ukuran data dari hasil pencarian: {number - 1} x 4")

#Fungsi untuk descriptive statistics
def desc_stat(filename, column):
    #Read text file
    with open(filename, "r") as f:
        lines = f.readlines()
        number = 0
        total = 0
        #Memisahkan setiap baris menjadi bagian "Smartphone", "Price", "Screensize", dan "Ram" 
        for line in lines:
            line = line.strip()
            kode_split = line.split()
            ram = float(kode_split[-1])
            screensize = float(kode_split[-2])
            price = float(kode_split[-3])
            #Kondisi sesuai column mana yang ingin di hitung
            if column == 1:
                indikator_pencarian = price
            elif column == 2:
                indikator_pencarian = screensize
            elif column == 3:
                indikator_pencarian = ram
            #Jika ini iterasi pertama, assign sebuah value terlebih dahulu agar tidak error
            if number == 0:  
                max_data = indikator_pencarian
                min_data = indikator_pencarian  
            #Mengloop max_data dan min_data sampai mendapatkan hasil paling kecil atau besar
            else:
                if indikator_pencarian > max_data:  
                    max_data = indikator_pencarian
                if indikator_pencarian < min_data: 
                    min_data = indikator_pencarian
            number += 1
            total += indikator_pencarian
        #Menampilkan min data, max data, dan rata-rata dari column yang dicari
        print(f"Min data: {min_data:.2f}")
        print(f"Max data: {max_data:.2f}")
        print(f"Rata - rata: {total / number:.2f}")
#Mengecek untuk error jika tidak terdapat file        
try:
    if __name__ == '__main__':
        if len(sys.argv) != 4:
            print("Usage: python script_name.py <file_path> <search_keyword> <column_num>")
            sys.exit(1)

        file_path = sys.argv[1]
        key = sys.argv[2]
        column_num = int(sys.argv[3])

        #Call functions yang sudah dibuat
        print_table(file_path)
        search_phone(file_path, key)
        desc_stat(file_path, column_num)
except FileNotFoundError:
    print("Maaf, file input tidak ada")