import tkinter as tk
from tkinter import messagebox

class PacilokaApp:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Paciloka Hotel Booking")
        self.master.geometry("400x650")
        #Inisialisasi data atribut-atribut hotel
        self.dict_hotel = {'hotel1': [10, 250000, 'kode_hotel_1'], 'hotel2': [12, 500000, 'kode_hotel_2'], 'hotel3': [10, 7500000, 'kode_hotel_3'], 
                        'hotel4': [1, 1000000, 'kode_hotel_4'], 'hotel5': [10, 900000, 'kode_hotel_5'], 'hotel6': [10, 6000000, 'kode_hotel_6']}
        #Menampilkan halaman utama
        self.homepage()
        
    def homepage(self):
        #Hapus semua widget yang ada di jendela utama
        for widget in self.master.winfo_children():
            widget.destroy()
        #Daftar informasi dari setiap hotel
        list_hotel = "Hotels:\n"
        for name, atribut in self.dict_hotel.items():
            list_hotel += "Nama hotel: " + name + "\n"
            list_hotel += "Jumlah kamar: " + str(atribut[0]) + "\n"
            list_hotel += "Harga per kamar: " + str(atribut[1]) + "\n\n"
        #Menampilkan daftar hotel
        tk.Label(self.master, text=list_hotel).pack()
        #Buat entry untuk memasukkan nama pengguna, nama hotel, dan jumlah kamar
        self.nama_user = tk.StringVar()
        tk.Label(self.master, text="Nama Pengguna: \n").pack()
        tk.Entry(self.master, textvariable=self.nama_user).pack()

        self.nama_hotel = tk.StringVar()
        tk.Label(self.master, text="Nama Hotel: \n").pack()
        tk.Entry(self.master, textvariable=self.nama_hotel).pack()

        self.jumlah_kamar = tk.IntVar()
        tk.Label(self.master, text="Jumlah Kamar: \n").pack()
        tk.Entry(self.master, textvariable=self.jumlah_kamar).pack()
        #Buat tombol untuk memesan kamar dan keluar dari PacilokaApp
        tk.Button(self.master, text="Pesan Kamar", command=self.booking).pack()
        tk.Button(self.master, text="Exit", command=self.master.quit).pack()
    
    def booking(self):
        #Ambil data dari entry 
        nama_user = self.nama_user.get()
        nama_hotel = self.nama_hotel.get()
        jumlah_kamar = self.jumlah_kamar.get()

        #Mengecek error-error yang mungkin muncul
        #Mengecek apakah nama user lebih dari 3 karakter atau tidak
        if len(nama_user) < 3:
            messagebox.showerror("Error", "Nama minimal harus memiliki 3 karakter.")
            return
        #Mengecek apakah jumlah kamar yang dipesan minimal 1
        if jumlah_kamar <= 0:
            messagebox.showerror("Error", "Maaf, kamar yang dipesan harus lebih dari 0.")
            return
        #Mengcek apakah input pengguna untuk jumlah kamar adalah int dan bukan string atau float
        try:
            jumlah_kamar = int(self.jumlah_kamar.get())
        except ValueError:
            messagebox.showerror("Error", "Jumlah kamar harus berupa bilangan bulat.")
            return
        #Mengcek apakah nama hotel yang dimasukkan ada
        if nama_hotel not in self.dict_hotel:
            messagebox.showerror("Error", f"Maaf {nama_hotel} tidak tersedia di sistem.")
            return
        #Mengambil data hotel
        available_room, room_price, hotel_code = self.dict_hotel[nama_hotel]

        #Mengecek apakah jumlah kamar yang ingin dipesan tersedia
        if jumlah_kamar > available_room:
            messagebox.showerror("Error", f"Maaf, tidak bisa memesan kamar sebanyak {jumlah_kamar} di {nama_hotel}")
            return
        #Mengurangi jumlah kamar yang tersedia
        self.dict_hotel[nama_hotel][0] -= jumlah_kamar
        #Menghitung total harga dari kamar yang dipesan dan membuat nomor tiket
        total_harga = jumlah_kamar * room_price
        nomor_tiket = f"{hotel_code}/{self.dict_hotel[nama_hotel][0]}/{nama_user[:3]}"
        #Menampilkan pesan bahwa booking kamar berhasil
        messagebox.showinfo("Booking Berhasil!", f"Pesanan untuk {nama_user} di hotel {nama_hotel} sebanyak {jumlah_kamar} kamar berhasil! \nTotal Harga: {total_harga}\nNomor Ticket: {nomor_tiket}")
        
        self.homepage()
        self.nama_user.set("")
        self.nama_hotel.set("")
        self.jumlah_kamar.set(0)

if __name__ == "__main__":
    root = tk.Tk()
    app = PacilokaApp(master=root)
    root.mainloop()
