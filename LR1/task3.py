
﻿N = int(input("Введіть ціле число N (від 1 до 9): "))

if not 1 <= N <= 9:
    raise ValueError("N має бути цілим числом від 1 до 9")

k = 0

for i in range(1, N + 1):
    if i <= 5:
        print(''.join(str(x) for x in range(1, i + 1)))
    else:
        print('     ' + ''.join(str(x) for x in range(1, 12 - i)))

