import matplotlib.pyplot as plt

def get_type(a_str):  
  #Fungsi ini akan mengembalikan tipe dari literal string a_str
  try:
    int(a_str)
    return "int"
  except:
    try:
      float(a_str)
      return "float"
    except:
      return "str"
    
def read_csv(file_name, delimiter = ','):
 #Membuat Dataframe
  with open(file_name, "r") as file:
    lines = file.readlines()
    #Membuat list of lists untuk data
    data = []
    #Mengecek apakah jumlah semua kolom sama
    for i in range(1, len(lines)):
      line_sekarang = lines[i].strip().split(delimiter)
      line_sebelumnya = lines[i - 1].strip().split(delimiter)
      if len(line_sekarang) != len(line_sebelumnya):
        raise Exception(f"Banyaknya kolom pada baris {i + 1} tidak konsisten.")
      
      #Membuat list data
      line_ubah = []
      for cell in line_sekarang:
        #Convert setiap data menjadi tipe yang sesuai
        tipe_cell = get_type(cell)
        if tipe_cell == "int":
          cell_ubah = int(cell)
        elif tipe_cell == "float":
          cell_ubah = float(cell)
        else:
          cell_ubah = cell
        line_ubah.append(cell_ubah)
      data.append(line_ubah)
    
    #Mengecek apakah tabel kosong  
    if len(data) == 0:
      raise Exception("Tabel tidak boleh kosong.")
    
    #Membuat list untuk nama kolom
    nama_kolom = lines[0].strip().split(delimiter)
    
    #Membuat list untuk tipe tipe data
    tipe_data = []
    for j in lines[1].strip().split(delimiter):
      tipe_data.append(get_type(j))
    return (data, nama_kolom, tipe_data)

#Mengembalikan bagian list of lists of items atau tabel data pada dataframe
def to_list(dataframe):
  return dataframe[0]

#Fungsi untuk mengakses daftar nama kolom
def get_column_names(dataframe):
  return dataframe[1]
  
#Fungsi untuk mengakses tipe data pada setiap kolom tabel  
def get_column_types(dataframe):
  return dataframe[2]

#Mengembalikan string yang merupakan representasi tabel (top_n baris pertama)
def head(dataframe, top_n = 10):
  cols = get_column_names(dataframe)
  out_str = ""
  out_str += "|".join([f"{col:>15}" for col in cols]) + "\n"
  out_str += ("-" * (15 * len(cols) + (len(cols) - 1))) + "\n"
  for row in to_list(dataframe)[:top_n]:
    out_str += "|".join([f"{col:>15}" for col in row]) + "\n"
  return out_str
  
#Mengembalikan string yang merupakan representasi informasi dataframe  
def info(dataframe):
  #Mengunnakan to_list untuk mengakses list of lists data
  data = to_list(dataframe)
  total_baris = len(data)
  
  #Mengakses daftar nama kolom dan tipe data
  cols_1 = get_column_names(dataframe)
  cols_2 = get_column_types(dataframe)
  
  #Membuat representasi informasi
  hasil = ""
  hasil += f"Total Baris = {total_baris} baris\n\n"
  #Judul dari representasi informasi
  hasil += "Kolom".ljust(15) + " " + "Tipe".ljust(15) + "\n"
  hasil += "-" * 30 + "\n"
  #Menreturn informasi yang ingin dibuat dalam bentuk nama kolom dan tipe data 
  for i in range(len(cols_1)):
    hasil += cols_1[i].ljust(15) + " " + cols_2[i].ljust(15) + "\n"
  return hasil 

#Fungsi untuk kondisi yang akan dipakai di select_rows
def satisfy_cond(value1, condition, value2):
  if condition == "<":
    return value1 < value2
  elif condition == "<=":
    return value1 <= value2
  elif condition == ">":
    return value1 > value2
  elif condition == ">=":
    return value1 >= value2
  elif condition == "!=":
    return value1 != value2
  elif condition == "==":
    return value1 == value2
  else:
    raise Exception(f"Operator {condition} tidak dikenal.")

#Mengembalikan dataframe baru dimana baris-baris sudah dipilih hanya yang nilai col_name memenuhi 'condition' terkait 'value' tertentu
def select_rows(dataframe, col_name, condition, value):
  nama_kolom = get_column_names(dataframe)
  #Mengecek apakah col_name ada di dataframe
  if col_name not in nama_kolom:
    raise Exception(f"Kolom {col_name} tidak ditemukan.")
  #Mendapatkan indeks dari nama kolom
  col_index = nama_kolom.index(col_name)
  #list untuk menyimpan data yang memenuhi kondisi
  list_dipilih = []
  data = to_list(dataframe)
  tipe_data = get_column_types(dataframe)
  #Looping melalui setiap list di data
  for lists in data:
    #Jika baris memenuhi kondisi, tambahkan ke list list_dipilih
    if satisfy_cond(lists[col_index], condition, value):
        list_dipilih.append(lists)
  return (list_dipilih, nama_kolom, tipe_data)
  
#Mengembalikan dataframe baru dimana kolom-kolom sudah dipilih hanya yang terdapat pada 'selected_cols' saja  
def select_cols(dataframe, selected_cols):
  nama_kolom = get_column_names(dataframe)
  #Mengecek apakah setiap kolom yang dipilih ada di dataframe
  for selected_col in selected_cols:
    if selected_col not in nama_kolom:
      raise Exception(f"Kolom {selected_col} tidak ditemukan.")
  
  #Membuat list untuk menyimpan indeks dari nama kolom
  index_selected_cols = []
  for col in selected_cols:
    index = nama_kolom.index(col)
    index_selected_cols.append(index)
  
  #Membuat data baru yang hanya memuat kolom yang diinginkan
  data_terpilih = []
  data = to_list(dataframe)
  #Looping melalui list baris di data
  for lists in data:
    #list untuk menyimpan kolom yang dipilih
    kolom_terpilih = []
    #Looping melalui setiap indeks di index_selected_col
    for index in index_selected_cols:
        #Menambahkan elemen ke kolom_terpilih berdasarkan indeks
        kolom_terpilih.append(lists[index])
    data_terpilih.append(kolom_terpilih)
  
  #Mendapatkan tipe data dari setiap kolom yang dipilih
  tipe_data_terpilih = []
  for i in data_terpilih[0]:
    tipe_data_terpilih.append(get_type(str(i)))
  
  #Return dataframe baru
  return (data_terpilih, selected_cols, tipe_data_terpilih)

#Mengembalikan dictionary yang berisi frequency count dari setiap nilai unik pada kolom col_name
def count(dataframe, col_name):
  #Mengakses data, nama kolom dan tipe data dari dataframe
  data = to_list(dataframe)
  nama_kolom = get_column_names(dataframe)
  tipe_data = get_column_types(dataframe)

  #Mengecek apakah nama kolom ada di dataframe
  if col_name not in nama_kolom:
    raise Exception(f"Kolom {col_name} tidak ditemukan.")
  
  #Mendapatkan indeks kolom
  index = nama_kolom.index(col_name)
  #Mengecek apakah tipe data kolom adalah string atau bukan
  if tipe_data[index] != "str":
    raise Exception(f"Kolom {col_name} harus bertipe string.")
  #Mengecek apakah tabel kosong
  if len(data) == 0:
    raise Exception("Tabel kosong.")
  
  #Dictionary untuk menyimpan frekuensi count
  frequency_count = {}
  for lists in data:
    #Mendapatkan data dari kolom yang dipilih
    data_in_list = lists[index]
    #Jika data sudah ada di frequency_count tambahkan 1 kalau tidak maka set ke 1
    if data_in_list in frequency_count:
      frequency_count[data_in_list] += 1
    else:
      frequency_count[data_in_list] = 1
  return frequency_count

#Mengembalikan rata-rata nilai pada kolom 'col_name' di dataframe
def mean_col(dataframe, col_name):
  #Mengakses data, nama kolom dan tipe data dari dataframe
  data = to_list(dataframe)
  nama_kolom = get_column_names(dataframe)
  tipe_data = get_column_types(dataframe)

  #Mengecek apakah nama kolom ada di dataframe
  if col_name not in nama_kolom:
    raise Exception(f"Kolom {col_name} tidak ditemukan.")
  
  #Mendapatkan indeks kolom
  index = nama_kolom.index(col_name)
  #Mengecek apakah tipe data kolom adalah numerik atau bukan
  if tipe_data[index] == "str":
    raise Exception(f"Kolom {col_name} bukan bertipe numerik.")
  #Mengecek apakah tabel kosong
  if len(data) == 0:
    raise Exception("Tabel kosong.")
  #Menyimpan total nilai
  total_nilai = 0
  #Loop untuk list di list data
  for lists in data:
    #Menambahkan nilai dari kolom yang dipilih ke total_nilai
    total_nilai += lists[index]
  #Menghitung rata-rata
  rata_rata = total_nilai / len(data)
  return rata_rata

#Fungsi ini akan menampilkan scatter plot dari nilai pada x dan y
def show_scatter_plot(x, y, x_label, y_label):
  plt.scatter(x, y)
  plt.xlabel(x_label)
  plt.ylabel(y_label)
  plt.show()

#Fungsi ini akan menampilkan scatter plot antara kolom col_name_x dan col_name_y pada dataframe
def scatter(dataframe, col_name_x, col_name_y):
  #Mengakses data, nama kolom dan tipe data dari dataframe
  data = to_list(dataframe)
  nama_kolom = get_column_names(dataframe)
  tipe_data = get_column_types(dataframe)
  
  #Mengecek apakah nama kolom ada di dataframe
  if col_name_x not in nama_kolom:
    raise Exception(f"Kolom {col_name_x} tidak ditemukan.")
  
  if col_name_y not in nama_kolom:
    raise Exception(f"Kolom {col_name_y} tidak ditemukan.")
  
  #Mendapatkan indeks kolom
  index_x = nama_kolom.index(col_name_x)
  index_y = nama_kolom.index(col_name_y)
  #Mengecek apakah tipe data kolom adalah numerik atau bukan
  if tipe_data[index_x] == "str":
    raise Exception(f"Kolom {col_name_x} bukan bertipe numerik.")
  
  if tipe_data[index_y] == "str":
    raise Exception(f"Kolom {col_name_y} bukan bertipe numerik.")
  
  #list untuk menyimpan data dari kolom yang dipilih
  list_x = []
  list_y = []
  #Looping melalui setiap list di data
  for lists in data:
    #Menambahkan nilai dari kolom yang dipilih ke list_x dan list_y
    list_x.append(lists[index_x])
    list_y.append(lists[index_y])
  
  #Menggunakan fungsi show_scatter_plot untuk menampilkan scatter plot
  scatter_plot = show_scatter_plot(list_x, list_y, col_name_x, col_name_y)
  return scatter_plot

#BONUS
#Mengembalikan nilai median pada kolom 'col_name' di dataframe
def median_col(dataframe, col_name):
  #Mengakses data, nama kolom dan tipe data dari dataframe
  data = to_list(dataframe)
  nama_kolom = get_column_names(dataframe)
  tipe_data = get_column_types(dataframe)
  
  #Mengecek apakah nama kolom ada di dataframe
  if col_name not in nama_kolom:
    raise Exception(f"Kolom {col_name} tidak ditemukan.")
  #Mendapatkan indeks kolom
  index = nama_kolom.index(col_name)
  #Mengecek apakah tipe data kolom adalah numerik atau bukan
  if tipe_data[index] == "str":
    raise Exception(f"Kolom {col_name} bukan bertipe numerik.")
  
  #list untuk menyimpan data dari kolom yang dipilih
  data_kolom = []
  #Looping melalui setiap list di data
  for lists in data:
    #Menambahkan nilai dari kolom yang dipilih ke list data_kolom
    data_kolom.append(lists[index])
  #Mengurutkan nilai dalam data_kolom
  data_urut = sorted(data_kolom)
  #Mencari panjang dari data
  panjang_data = len(data_urut)
  #Jika panjang data genap
  if panjang_data % 2 == 0:
    #Median adalah dua nilai yang ditengah-tengah kemudian di rata-ratakan
    median = (data_urut[panjang_data//2 - 1] + data_urut[panjang_data//2]) / 2
  #Jika panjang data ganjil
  else:
    #Median adalah nilai di tengah
    median = data_urut[panjang_data//2]
  return median

if __name__ == "__main__":
  #Memuat dataframe dari tabel pada file abalone.csv
  dataframe = read_csv("abalone.data")

  #Test Case
  #Cetak 10 baris pertama
  print(head(dataframe, top_n = 10))
  print()

  #Cetak informasi dataframe
  print(info(dataframe))
  print()

  #Kembalikan dataframe baru, dengan  kolom Length > 0.49
  new_dataframe = select_rows(dataframe, "Length", ">", 0.49)
  print(head(new_dataframe, top_n = 5))
  print()

  #Kembalikan dataframe baru, dimana Sex == "M" DAN Length > 0.49
  new_dataframe = select_rows(select_rows(dataframe, "Length", ">", 0.49), "Sex", "==", "M")
  print(head(new_dataframe, top_n = 5))
  print()

  #Kembalikan dataframe baru yang hanya terdiri dari kolom Sex, Length, Diameter, dan Rings
  new_dataframe = select_cols(dataframe, ["Sex", "Length", "Diameter", "Rings"])
  print(head(new_dataframe, top_n = 5))
  print()

  #Hitung mean pada kolom Length (pada dataframe original)
  print(f"Mean = {mean_col(dataframe, 'Length')}")
  print()

  #Bonus
  #Hitung median pada kolom Length
  print(f"Median = {median_col(dataframe, 'Length')}")
  print()

  #Melihat unique values pada kolom Sex, dan frekuensi kemunculannya (pada dataframe original)
  print(count(dataframe, "Sex"))
  print()

  #Tampilkan scatter plot antara kolom "Height" dan "Diameter"
  print(scatter(dataframe, "Height", "Diameter"))
  print()

 