from tkinter import messagebox
from tkinter import *

#Kelas utama membuat display dari interface
class Display():
    def __init__(self, master):
        self.master = master
        #Mengatur judul dan ukuran jendela
        master.title("EAN-13 [by Bertrand Gwynfory Iskandar]")
        master.geometry("500x470")

        #Membuat label dan entry untuk nama file
        Label(master, text="Save barcode to PS file [eg: EAN13.eps]:").pack()
        self.__filename = StringVar()
        self.__filename.set(".eps")
        self.__entry_filename = Entry(master, textvariable=self.__filename, width=15) 
        self.__entry_filename.pack()

        #Membuat label dan entry untuk kode barcode
        Label(master, text="Enter code (first 12 decimal digits):").pack()
        self.__input_barcode = StringVar()
        self.__entry_barcode = Entry(master, textvariable=self.__input_barcode, width=15)
        self.__entry_barcode.pack()

        #Membuat kanvas untuk menampilkan barcode
        self.__display = Canvas(master, bg="white", height=350, width=400)
        self.__display.pack()

        #Mengikat event Return (Enter) pada entry kode barcode ke metode cek_barcode
        self.__entry_barcode.bind("<Return>", self.cek_barcode)
    
    def get_filename(self):
        return self.__filename.get()
    
    def get_barcode(self):
        return self.__input_barcode.get()

    def cek_filename(self, *args):
        #Memeriksa apakah file dalam format .eps
        if self.get_filename()[-4:] != ".eps":
            messagebox.showerror("Error!", "File harus berakhir dengan .eps!")
            self.__filename.set(".eps")
            self.__input_barcode.set("")
        else:
            #Jika file ada maka mengeluarkan pesan error
            try:
                open(self.get_filename(), "r")
                messagebox.showerror("Error!", "File .eps dengan nama ini sudah ada!")
            
            #Jika file tidak ada maka 
            except FileNotFoundError:
                #Jika file tidak ada maka akan menampilkan barcode
                barcode = Barcode(self.get_barcode())
                self.show_barcode(barcode.get_bits(), barcode.get_barcode())
                #Memperbarui canvas dan menyimpan barcode ke file PostScript
                self.__display.update()
                self.__display.postscript(file = self.get_filename(), colormode = "color")

    #Fungsi untuk memeriksa apakah kode barcode adalah integer dan 12 digit
    def cek_barcode(self, *args):
        try:
            #Memeriksa apakah entry barcode tidak kosong
            if self.get_barcode():
                #Memeriksa apakah kode adalah integer
                if int(self.get_barcode()):
                    pass
                #Memeriksa apalah panjang kode adalah 12
                if len(str(self.get_barcode())) != 12:
                    messagebox.showerror("Error!", "Jumlah angka kode barcode tidak 12!")
                    self.__filename.set(".eps")
                    self.__input_barcode.set("")
                #Memanggil fungsi cek_filename
                self.cek_filename()
        #Menunjukkan pesan error jika kode bukan integer
        except ValueError:
            messagebox.showerror("Error!", "Kode barcode harus berupa integer (tidak boleh string or float)!")

    #Fungsi untuk mencetak barcode pada canvas
    def show_barcode(self, bits, code):
        self.__display.delete("all")
        self.__display.create_text(200, 50,fill="black", font=("Calibri", 20, "bold"), text="EAN-13 Barcode:")

        #Mencetak barcode
        for i in range(95):
            if bits[i] == "1":
                #Cetak bar untuk sideguard ujung kiri 
                if i <= 2:
                    self.__display.create_rectangle((i * 3 + 65, 70, i * 3 + 68, 290), fill="blue", outline="blue", width=0)
                #Cetak bar untuk middleguard
                elif 45 <= i <= 49:
                    self.__display.create_rectangle((i * 3 + 65, 70, i * 3 + 68, 290), fill="blue", outline="blue", width=0)
                #Cetak guard untuk sideguard ujung kanan
                elif 92 <= i <= 94:
                    self.__display.create_rectangle((i * 3 + 65, 70, i * 3 + 68, 290), fill="blue", outline="blue", width=0)
                #Cetak bar untuk tiap digit
                else:
                    self.__display.create_rectangle((i * 3 + 65, 70, i * 3 + 68, 275), fill="black", width=0)

        #Mencetak digit code dan check digit
        self.__display.create_text(54, 300, font=("Calibri", 15, "bold"), text=code[0], fill= "black")
        for i in range(13):
            if 1 <= i <= 6:
                self.__display.create_text(i * 21 + 66, 300, font=("Calibri", 15, "bold"), text=f"{code[i]}", fill="black")
            elif 7 <= i <= 12:
                self.__display.create_text(i * 21 + 78, 300, font=("Calibri", 15, "bold"), text=f"{code[i]}", fill="black")

        self.__display.create_text(200, 330, fill="orange", font=("Calibri", 15, "bold"), text=f"Check Digit: {code[-1]}")
                
#Kelas untuk mendefinisikan spesifikasi EAN13
class EAN13:
    #Mendefinisikan pola guard untuk sisi dan tengah barcode
    side_guard = "101"
    middle_guard = "01010"

    #Mendefinisikan struktur dan kode untuk setiap digit
    __structure = {"0": "LLLLLLRRRRRR", "1": "LLGLGGRRRRRR", "2": "LLGGLGRRRRRR", "3": "LLGGGLRRRRRR", "4": "LGLLGGRRRRRR", 
                   "5": "LGGLLGRRRRRR", "6": "LGGGLLRRRRRR", "7": "LGLGLGRRRRRR", "8": "LGLGGLRRRRRR", "9": "LGGLGLRRRRRR"}

    __l_code = {"0": "0001101", "1": "0011001", "2": "0010011", "3": "0111101", "4": "0100011", 
               "5": "0110001", "6": "0101111", "7": "0111011", "8": "0110111", "9": "0001011"}

    __g_code = {"0": "0100111", "1": "0110011", "2": "0011011", "3": "0100001", "4": "0011101", 
               "5": "0111001", "6": "0000101", "7": "0010001", "8": "0001001", "9": "0010111"}

    #Mengambil struktur encoding mana yang digunakan berdasarkan digit pertama kode
    def get_encoding(self, first_digit):
        return self.__structure[first_digit]
    
    #Mengubah kode menjadi bit berdasarkan struktur encoding
    def convert_bits(self, char_code, digit):
        if char_code == "L":
            return self.__l_code[digit]
        elif char_code == "G":
            return self.__g_code[digit]
        elif char_code == "R":
            return self.__g_code[digit][::-1]
    
    #Fungsi untuk menghitung check digit
    def get_checkdigit(self, code):
        checksum = 0
        #Iterasi sebanyak panjang kode
        for i in range(len(code)):
            #Jika i sedang genap maka checksum ditambahkan digit (kebalik karena indeks python mulai dari 0)
            if i % 2 == 0:
                checksum += int(code[i])
            #Jika i ganjil maka checksum ditambahkan digit * 3
            else:
                checksum += int(code[i]) * 3
        #Kalkulasi hasil check digit
        x = checksum % 10
        if x != 0:
            return str(10 - x)
        else:
            return str(x)

#Kelas untuk menggabungkan 95 bit yang telah di encode 
class Barcode(EAN13):
    def __init__(self, code):
        #Concatenate checkdigit ke ujung kode
        self.__code = code + super().get_checkdigit(code)
        self.__bits = self.encode_barcode()

    def encode_barcode(self):
        #Mengambil struktur encoding yang akan digunakan
        encoding = super().get_encoding(self.__code[0])
        encoded_bits = super().side_guard

        #Iterasi sebanyak panjang kode
        for i in range(12):
            #Tambahkan middle guard setalah 6 digit pertama sudah di convert
            if i == 6:
                encoded_bits += super().middle_guard
            #Convert kode menjadi bit
            encoded_bits += super().convert_bits(encoding[i], self.__code[1:][i])
        
        #Return kode yang sudah di convert menjadi bit dan ditambahkan side guard dan middle guard
        return encoded_bits + super().side_guard

    def get_barcode(self):
        return self.__code
    
    def get_bits(self):
        return self.__bits

#Menjalankan program
if __name__ == "__main__":
    root = Tk()
    window = Display(root)
    root.mainloop()