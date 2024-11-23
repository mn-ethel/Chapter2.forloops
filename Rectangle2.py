height=eval(input("Enter the height:"))
width=eval(input("Enter the width:"))
for i in range (height):
    for j in range(width):
        if i==0 or i==height-1 or j==0 or j==width-1 :
            print("*",end="")
        else:
            print (" ", end="")
    print()