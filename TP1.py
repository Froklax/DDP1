import turtle
from tkinter import messagebox
#Judul turtle
turtle.title("Mini Super Mario Towers")
turtle.speed(0)
#Buat posisi turtle mulai di pojok kanan bawah biar lebih enak dilihat
turtle.penup()
turtle.goto(-600, -200)
turtle.pendown()
#Input berapa tower yang ingin dibuat dan pengecekan untuk integer only karena tidak boleh menerima floating point
while True:
    towers = turtle.numinput("Tower to Build", "Enter the number of towers you want to build (Min 1)", minval=1)
    if towers == int(towers):
        towers = int(towers)
        break
    else:
        messagebox.showwarning("Invalid Input", "Please enter a valid integer (Cannot be float).")
#Mengecek apakah tower berjumlah lebih dari 1
if towers > 1:
    while True:
        distance = turtle.numinput("Distance between Towers", "Enter the distance between towers (Min 2, Max 5)", minval=2, maxval=5)
        if distance == int(distance):
            distance = int(distance)
            break
        else:
            messagebox.showwarning("Invalid Input", "Please enter a valid integer (Cannot be float).")
    while True:
        layer_difference = turtle.numinput("Tower Layer Difference", "Enter the number of layer differences between each tower (Min 2, Max 5)", minval=2, maxval=5)
        if layer_difference == int(layer_difference):
            layer_difference = int(layer_difference)
            break
        else:
            messagebox.showwarning("Invalid Input", "Please enter a valid integer (Cannot be float).")
#Berbagai input untuk membuat tower dan pengecakan untuk integer only karena tidak boleh menerima floating point
while True:
    width = turtle.numinput("Brick Width - Tower", "Enter width of brick for tower (Min 1, Max 35)", minval=1, maxval=35)
    if width == int(width):
        width = int(width)
        break
    else:
        messagebox.showwarning("Invalid Input", "Please enter a valid integer (Cannot be float).")
while True:    
    height = turtle.numinput("Brick Length - Tower", "Enter height of brick for tower (Min 1, Max 25)", minval=1, maxval=25)
    if height == int(height):
        height = int(height)
        break
    else:
        messagebox.showwarning("Invalid Input", "Please enter a valid integer (Cannot be float).")
while True:
    num_layers = turtle.numinput("Layers - Tower", "Enter the number of layers for the first tower (Min 1, Max 25)", minval=1, maxval=25)
    if num_layers == int(num_layers):
        num_layers = int(num_layers)
        break
    else:
        messagebox.showwarning("Invalid Input", "Please enter a valid integer (Cannot be float).")
while True:
    layer_width = turtle.numinput("Layer Width - Tower", "Enter the width of a layer (Min 1, Max 10)", minval=1, maxval=10)
    if layer_width == int(layer_width):
        layer_width = int(layer_width)
        break
    else:
        messagebox.showwarning("Invalid Input", "Please enter a valid integer (Cannot be float).")
#Variabel yang digunakan di dalam loop
total_difference = 0
total_bricks = 0
tower_number = 0
#Loop untuk berapa tower yang dibuat
for tower in range(1, towers + 1):
    #Variabel untuk pengecekan kepala tower
    tower_head_check = 0
    #Variabel untuk perbedaan layer di setiap tower
    total_layers = num_layers + (layer_difference * tower_number)
    #Total brick untuk semua tower
    total_bricks += (total_layers * layer_width) + (layer_width + 1)
    #Membuat Tower
    for layer in range(total_layers):
        #Membuat Satuan Brick
        for brick in range(layer_width):
            turtle.fillcolor("#CA7F65")  
            turtle.begin_fill()
            turtle.forward(width)
            turtle.right(90)
            turtle.forward(height)
            turtle.right(90)
            turtle.forward(width)
            turtle.right(90)
            turtle.forward(height)
            turtle.end_fill()
            turtle.right(90)
            turtle.forward(width)
        #Kembali ke posisi awal panjang layer
        turtle.backward(width * (layer_width))  
        turtle.penup()
        turtle.left(90)
        turtle.forward(height)
        turtle.right(90)
        turtle.pendown()
        #Mengecek apakah landasan tower sudah selesai dibuat
        tower_head_check += 1
        if tower_head_check == total_layers:
            #Membuat kepala tower
            turtle.backward(width / 2)
            for brick in range(layer_width + 1):
                turtle.fillcolor("#693424")
                turtle.begin_fill()
                turtle.forward(width)
                turtle.right(90)
                turtle.forward(height)
                turtle.right(90)
                turtle.forward(width)
                turtle.right(90)
                turtle.forward(height)
                turtle.end_fill()
                turtle.right(90)
                turtle.forward(width)
    #Pergi ke posisi tower selanjutnya
    turtle.penup()
    turtle.backward(width / 2)
    turtle.right(90)
    turtle.forward(height * (total_layers))
    turtle.left(90)
    turtle.forward(distance * width)
    turtle.pendown()
    tower_number += 1
#Pergi ke posisi tepat dibawah tower-tower   
turtle.penup()
turtle.goto(-600, -300)
turtle.pendown()
#Mencetak total tower yang dibuat dan total semua brick dari tower-tower tersebut
turtle.write(f"{tower_number} Super Mario Towers have been built with a total of {total_bricks} bricks", font = ("Cooper Black", 20, "normal"))
#Keluar ketika menekan mouse
turtle.exitonclick()