class Hotel:
    def __init__(self, name, available_room, room_price):
        self.name = name
        self.available_room = available_room
        self.room_price = room_price
        self.profit = 0
        self.guest = []

    def booking(self, user, jumlah_kamar):
        if jumlah_kamar > self.available_room:
            return "Booking tidak berhasil!"
        elif user.money < jumlah_kamar * self.room_price:
            return "Booking tidak berhasil!"
        else:
            self.available_room -= jumlah_kamar
            self.profit += jumlah_kamar * self.room_price
            user.money -= jumlah_kamar * self.room_price
            if user.name not in self.guest:
                self.guest.append(user.name)
            if self.name not in user.hotel_list:
                user.hotel_list.append(self.name)
            return f"User dengan nama {user.name} berhasil melakukan booking di hotel {self.name} dengan jumlah {jumlah_kamar} kamar!"

    def __str__(self):
        return f"Hotel {self.name} memiliki {self.available_room} kamar tersedia dan telah mendapatkan keuntungan sebesar {self.profit}."

class User:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.hotel_list = []

    def topup(self, jumlah_topup):
        if jumlah_topup > 0:
            self.money += jumlah_topup
            return f"Berhasil menambahkan {jumlah_topup} ke user {self.name}. Saldo user menjadi {self.money}."
        else:
            return "Jumlah saldo yang akan ditambahkan ke user harus lebih dari 0!"

    def __str__(self):
        return f"User {self.name} memiliki saldo sebesar {self.money}."

if __name__ == '__main__':
    hotels = []
    users = []
    banyak_hotel = int(input("Masukan banyak hotel: "))
    banyak_user = int(input("Masukan banyak user: "))
    print()
    for i in range(banyak_hotel):
        name = input("Masukan nama hotel ke-" + str(i + 1) + " : ")
        available_room = int(input("Masukan banyak kamar hotel ke-" + str(i + 1) + " : "))
        room_price = int(input("Masukan harga satu kamar hotel ke-" + str(i + 1) + " : "))
        hotels.append(Hotel(name, available_room, room_price))
    print()
    for j in range(banyak_user):
        name = input("Masukan nama user ke-" + str(j + 1) + " : ")
        money = int(input("Masukan saldo user ke-" + str(j + 1) + " : "))
        users.append(User(name, money))
    print()
    while True:
        print("=============Welcome to Paciloka!=============\n")
        perintah = int(input("Masukkan perintah: "))
        if perintah == 1:
            print("Daftar Hotel")
            for i in range(len(hotels)):
                print(f"{i + 1}. {hotels[i].name}\n")
            print("Daftar User")
            for j in range(len(users)):
                print(f"{j + 1}. {users[j].name}\n")
        elif perintah == 2:
            nama_hotel = input("Masukkan nama hotel: ")
            found = False
            for hotel in hotels:
                if hotel.name == nama_hotel:
                    print(f"Hotel dengan nama {hotel.name} mempunyai profit sebesar {hotel.profit}\n")
                    found = True
                    break
            if not found:
                print("Nama hotel tidak ditemukan di sistem!\n")
        elif perintah == 3:
            nama_user = input("Masukkan nama user: ")
            found = False
            for user in users:
                if user.name == nama_user:
                    print(f"User dengan nama {user.name} mempunyai saldo sebesar {user.money}\n")
                    found = True
                    break
            if not found:
                print("Nama user tidak ditemukan di sistem!\n")
        elif perintah == 4:
            nama_user = input("Masukkan nama user: ")
            found = False
            for user in users:
                if user.name == nama_user:
                    saldo = int(input("Masukkan jumlah uang yang akan ditambahkan ke user: "))
                    print(user.topup(saldo) + "\n")
                    found = True
                    break
            if not found:
                print("Nama user tidak ditemukan di sistem!\n")
        elif perintah == 5:
            found_user = False
            found_hotel = False
            nama_user = input("Masukkan nama user: ")
            for user in users:
                if user.name != nama_user:
                    print("Nama user tidak ditemukan di sistem!\n")
                    continue
            nama_hotel = input("Masukkan nama hotel: ")
            for user in users:
                if user.name == nama_user:
                    found_user = True
                    for hotel in hotels:
                        if hotel.name == nama_hotel:
                            jumlah_kamar = int(input("Masukkan jumlah kamar yang akan dibooking: "))
                            if jumlah_kamar <= 0:
                                print("Jumlah kamar yang akan dipesan harus lebih dari 0!\n")
                                break
                            else:
                                print(hotel.booking(user, jumlah_kamar) + "\n")
                            found_hotel = True
                            break
                    if not found_hotel:
                        print("Nama hotel tidak ditemukan di sistem!\n")
                    break
        elif perintah == 6:
            nama_hotel = input("Masukkan nama hotel: ")
            found = False
            for hotel in hotels:
                if hotel.name == nama_hotel:
                    guest = ""
                    for nama in hotel.guest:
                        guest += nama + " "
                    if guest == "":
                        print(f"Hotel {hotel.name} tidak memiliki pelanggan!\n")
                    else:
                        print(f"{hotel.name} | {guest}\n")
                    found = True
                    break
            if not found:
                print("Nama hotel tidak ditemukan di sistem!\n")
        elif perintah == 7:
            nama_user = input("Masukkan nama user: ")
            found = False
            for user in users:
                if user.name == nama_user:
                    hotel_list = ""
                    for hotel in user.hotel_list:
                        hotel_list += hotel + " "
                    if hotel_list == "":
                        print(f"User {user.name} tidak pernah melakukan booking!\n")
                    else:
                        print(f"{user.name} | {hotel_list}\n")
                    found = True
                    break
            if not found:
                print("Nama user tidak ditemukan di sistem!\n")
        elif perintah == 8:
            print("Terima kasih sudah mengunjungi Paciloka!")
            break
        else:
            print("Perintah tidak diketahui! Masukkan perintah yang valid\n")
