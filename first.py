a = int(input ("Введіть а: "))
while (a<=0):
    a = int(input ("Введіть ще раз а: "))
b = int(input ("Введіть b: "))
while (b<=0):
    b = int(input ("Введіть ще раз b: "))
if a>b:
    x = b*a-1
elif a==b:
    x=-10
else:
    x=(a-5)/b
print("X=",x)
