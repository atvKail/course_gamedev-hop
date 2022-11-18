def main(variant):
    if variant == 1:
        Example1()
    elif variant == 2:
        Example2()
    input()


def Example2():
    try:
        xi = int(input("Введите в какую степень возводится (до 4 степени) = "))
        if xi > 4:
            print("степень > 4 ")
            exit(Example2())
        n = int(input("Введите сколько max чисел в последовательности = "))
        if xi == 1:
            sequence_sum = (n * (n + 1)) / 2
        elif xi == 2:
            sequence_sum = (n * (n + 1) * (2*n + 1)) / 6
        elif xi == 3:
            sequence_sum = ((n**2) * ((n + 1)**2)) / 4
        else:
            sequence_sum = (n * (n + 1) * (2 * n + 1)*(3 * (n**2) + 3 * n - 1)) / 30
        print(f"Сумма последовательности = {sequence_sum}")
    except ValueError:
        print("Такой степени нет")


def Example1():
    try:
        n = float(input("Введите n = "))
        k = float(input("Введите k = "))
        z = float(input("Введите z = "))
        if z == 0:
            print("Сдесь делить на ноль нельзя.\nВыход........")
            return ZeroDivisionError

        d = ((1 * k) / z - (n * k) / z) / (1 - n)
        print(f"d - разность арифметической прогрессии = {d}")
        sequence_sum = (((n * k) / z) * ((n + 1) * k) / z) / 2
        print(f"Сумма последовательности = {sequence_sum}")
    except ValueError:
        print("Введины символы, это не уравнение.")
    return 0


if __name__ == "__main__":
    print("Пример №1 арифметической последовательности")
    print("1*k + 2*k + 3*k + ... + n*k\n_______________________________\n             z")
    print()
    print("Пример №2 арифметической последовательности")
    print("1^s + 2^s + ... + n^s; s ∈ {1, 2, 3, 4}")
    try:
        main(int(input("Выберите какой пример рассмотрим.(1 или 2) ==> ")))
    except ValueError:
        print("Такого варианта нет!")
