class Person:
    #Constructor
    def __init__(self, name, payment, stamina):
        self.__name = name
        self.__payment = payment
        self.__stamina = stamina
        self.__total_work = 0
        
    #Getter dan Setter
    def get_name(self):
        return self.__name

    def get_payment(self):
        return self.__payment

    def get_stamina(self):
        return self.__stamina

    def set_stamina(self, x):
        self.__stamina = x

    def get_total_work(self):
        return self.__total_work

    def set_total_work(self, x):
        self.__total_work = x

    #Methods
    #Memeriksa apakah orang memiliki stamina yang cukup untuk pekerjaan
    def is_available(self, cost_stamina):
        return self.__stamina >= cost_stamina

    #Menghitung total pembayaran berdasarkan jumlah pekerjaan yang dilakukan
    def pay_day(self):
        return self.__payment * self.__total_work

    #Mengurangi stamina berdasarkan stamina cost
    def work(self, cost_stamina):
        self.__stamina -= cost_stamina
        self.__total_work += 1
    
    def __str__(self):
        class_name = self.__class__.__name__
        name = self.__name
        total_work = self.__total_work
        stamina = self.__stamina
        payment = self.pay_day()
        return f"{class_name:20} | {name:20} | Total kerja: {total_work:20} | Stamina:{stamina:20} | Gaji:{payment:20}"


class Manager(Person):
    #Constructor
    def __init__(self, name, payment, stamina):
        super().__init__(name, payment, stamina)
        self.__list_worker = []
        
    #Getter dan Setter
    def get_list_worker(self):
        return self.__list_worker

    #Methods
    #Menghire worker baru 
    def hire_worker(self, name):
        for worker in self.__list_worker:
            #Jika worker sudah ada di list worker
            if name.lower() == worker.get_name().lower():
                print("Sudah ada!")
                break
        #Menambahkan worker baru ke list worker
        else:
            self.__list_worker.append(Worker(name))
            print("Berhasil mendapat pegawai baru")
            self.work(10)
    #Memecat worker    
    def fire_worker(self, name):
        for worker in self.__list_worker:
            if name.lower() == worker.get_name().lower():
                #Membuang worker dari list worker
                self.__list_worker.remove(worker)
                print(f"Berhasil memecat {name}")
                self.work(10)
                break
        #Jika nama worker tidak ada di list
        else:
            print("Nama tidak ditemukan")

    def give_work(self, name,bonus ,cost_stamina):
        for worker in self.__list_worker:
            if name.lower() == worker.get_name().lower():
                worker.work(bonus, cost_stamina)
                self.work(10)
                print(f"Berhasil memberi pekerjaan kepada {name}")
                break

class Worker(Person):
    #Constructor
    def __init__(self, name, payment = 5000, stamina = 100):
        super().__init__(name, payment, stamina)
        self.__bonus = 0

    #Methods    
    def work(self, bonus,cost_stamina):
        if self.is_available(cost_stamina):
            #Mengurangi stamina berdasarkan biaya stamina pekerjaan
            self.set_stamina(self.get_stamina() - cost_stamina)
            #Menambahkan bonus
            self.__bonus += bonus
            #Menambah jumlah total pekerjaan yang telah dilakukan
            self.set_total_work(self.get_total_work() + 1)
    
    #Metode untuk menghitung total pembayaran
    def pay_day(self):
        #Menghitung total pembayaran berdasarkan jumlah pekerjaan yang telah dilakukan dan bonus
        total_payment = super().pay_day() + self.__bonus
        #Reset bonus
        self.__bonus = 0
        return total_payment
    
    #Getter and Setter
    def get_bonus(self):
        return self.__bonus

    def set_bonus(self, new_bonus):
        self.__bonus = new_bonus    
    

def main():
    #Meminta nama, bayaran, dan stamina manager
    name =  input("Masukkan nama manajer: ")
    payment = int(input("Masukkan jumlah pembayaran: "))
    stamina = int(input("Masukkan stamina manajer: "))

    #Inisialisasi Manager
    manager = Manager(name, payment, stamina)

    #Loop utama program
    while manager.is_available(1):
        #Menu
        print("""
PACILOKA
-----------------------
1. Lihat status pegawai
2. Beri tugas
3. Cari pegawai baru
4. Pecat pegawai
5. Keluar
-----------------------
        """)
        #Meminta perintah yang ingin dilakukan
        action = int(input("Masukkan pilihan: "))
        
        if action == 1:
            #Mencetak informasi tentang setiap worker
            for worker in manager.get_list_worker():
                print(worker) 

            #Mencetak informasi tentang manager
            print(manager)   

        elif action == 2:
            #Memberikan tugas kepada worker
            #Meminta input nama, bonus, dan stamina cost
            nama_worker = input("Tugas akan diberikan kepada: ")
            bonus = int(input("Bonus pekerjaan: "))
            cost_stamina = int(input("Beban stamina: "))
            for worker in manager.get_list_worker():
                #Jika worker ada di list worket
                if nama_worker == worker.get_name():
                    #Jika stamina cukup
                    if worker.is_available(cost_stamina):
                        print("Hasil cek ketersediaan pegawai:")
                        print("Pegawai dapat menerima pekerjaan")
                        print("========================================")
                        #Manager memberikan pekerjaan ke worker
                        manager.give_work(nama_worker, bonus, cost_stamina)
                    #Jika stamina tidak cukup
                    else:
                        print("Hasil cek ketersediaan pegawai:")
                        print("Pegawai tidak dapat menerima pekerjaan. Stamina pegawai tidak cukup.")
        
        elif action == 3:
            #Menghire worker baru
            nama_worker = input("Nama pegawai baru: ")
            manager.hire_worker(nama_worker)

        elif action == 4:
            #Memecat worker
            nama_worker = input("Nama pegawai yang akan dipecat: ")
            manager.fire_worker(nama_worker)

        elif action == 5:
             #Exit program
            print("""
----------------------------------------
Berhenti mengawasi hotel, sampai jumpa !
----------------------------------------""")
            return
    print("""
----------------------------------------
Stamina manajer sudah habis, sampai jumpa !
----------------------------------------""")
if __name__ == "__main__":
    main()