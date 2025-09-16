a = 0
b = 1
for i in range(21):
    if i % 2 == 0:
        a += i
    else:
        b *= i
print("Сума парних чисел від 0 до 20", a)
print("Добуток не парних чисел від 0 до 20", b)
