# main_program.py
import mod

def main():
    m = float(input("Введіть значення m: "))
    n = float(input("Введіть значення n: "))

    if m <= 0 or n <= 0:
        print("m та n мають бути додатніми числами.")
    else:
        result = mod.expression(m, n)
        print("Значення виразу z = ", result)

if __name__ == "__main__":
    main()
