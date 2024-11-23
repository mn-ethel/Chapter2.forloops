F=eval(input("Enter number of fibonacci numbers:"))
a=1
b=1
print(a,b,end=" ")
for i in range (2,F):
   c=a+b
   a=b
   b=c
   print(c,end=" ")


