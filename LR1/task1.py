
﻿def obchislyty_x(a, b):
    if not (1 <= a <= 100 and 1 <= b <= 100):
        raise ValueError("a та b повинні бути цілими числами в діапазоні від 1 до 100")

    if a > b:
        return a * a - b
    elif a == b:
        return -a
    else:
        return (a * b - 1) // b

try:
    a = int(input("Введіть a (від 1 до 100): "))
    b = int(input("Введіть b (від 1 до 100): "))
    
    x = obchislyty_x(a, b)
    print(f"Значення X: {x}")
except ValueError as e:
    print(e)
