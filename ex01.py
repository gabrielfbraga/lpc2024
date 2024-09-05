import random

numero1 = numero2 = numero3 = numero4 = numero5 = numero6 = 0

resultados = [random.randint(1,6) for _ in range(100)]

for c in resultados:
    if c == 1:
        numero1 += 1
    elif c == 2:
        numero2 += 1
    elif c == 3:
        numero3 += 1
    elif c == 4:
        numero4 += 1
    elif c == 5:
        numero5 += 1
    elif c == 6:
        numero6 += 1

print(f"O número 1 foi conseguido {numero1} vezes")
print(f"O número 2 foi conseguido {numero2} vezes")
print(f"O número 3 foi conseguido {numero3} vezes")
print(f"O número 4 foi conseguido {numero4} vezes")
print(f"O número 5 foi conseguido {numero5} vezes")
print(f"O número 6 foi conseguido {numero6} vezes")



