height = int(input("Enter the height of the diamond: "))

for i in range(1, height+1, 2):
    print(" " * ((height - i) // 2) + "* " * i)

for i in range(height-2, 0, -2):
    print(" " * ((height - i) // 2) + "* " * i)
