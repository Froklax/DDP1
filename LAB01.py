#Meminta input untuk pesan kelompok zog
pesan_zog = input("Pesan Kelompok Zog: ")

#Ubah hex string menjadi byte string dan kemudian karakter ASCII
bytes_string = bytes.fromhex(pesan_zog)
ascii_string = bytes_string.decode("ASCII")

#Meminta input untuk Angka ke-1 dan ke-2
angka_satu = int(input("Angka 1: "))
angka_dua = int(input("Angka 2: "))

#Mengubah clue menjadi password dan kemudian dalam bentuk biner
password_zog = angka_satu * angka_dua * 13
string_biner = bin(password_zog)

#Output pesan dan password
print(f"Hasil terjemahan pesan: {ascii_string}")
print(f"Password: {string_biner}\n")
print(f'Pesan "{ascii_string}" telah diterima dengan password "{string_biner}".')