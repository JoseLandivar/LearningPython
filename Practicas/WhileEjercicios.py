# Sumar todos lo impares hasta el 100

num = 0
total = 0

for num in range(100):
    if num % 2 == 1:
        total += num

print(total)