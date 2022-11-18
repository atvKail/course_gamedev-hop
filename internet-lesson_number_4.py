def main():
    import random

    try:
        variant = int(input("Выбирите 1 или 2. 1: Робот отгадывает ваше число и выводит все шаги;"
                            " 2: Вы отгадываете число робота ==> "))
        if variant == 1:
            a, b = map(int, input("Задайте диапозон, пример:'start end' ").split())
            if a > b:
                a, b = b, a
            n = abs(a - b)
            xv = [i for i in range(a, b + 1)]
            say = False
            mid = (xv[n // 2], n // 2)
            while not say:
                print(f"n = {n + 1}; Computer selected number = {mid[0]}; diapason = {a} to {b}")
                otv = input(f"Это ваше число {mid[0]}? (Введите Yes или No) == > ")
                if otv.lower() != "yes" and otv.lower() != "no":
                    print("Не понимаю")
                    continue
                elif otv.lower() == "yes":
                    say = True
                else:
                    sim = input(f"Ваше число больше или меньше {mid[0]}. Введите > or <  ==> ")
                    if sim != ">" and sim != "<":
                        print("Не понятно, заново :)")
                        continue
                    elif sim == ">":
                        a, b = mid[0], b
                        xv = xv[mid[1]:]
                        n = len(xv)
                        mid = (xv[n // 2], n // 2)
                    else:
                        a, b = a, mid[0]
                        xv = xv[:mid[1] + 1]
                        n = len(xv)
                        mid = (xv[n // 2], n // 2)
        if variant == 2:
            a, b = map(int, input("Задайте диапозон, пример:'start end' ").split())
            n = abs(a - b)
            say = None
            if a > b:
                a, b = b, a
            number = random.randint(a, b)
            while say != number:
                try:
                    say = int(input("Ваше число: "))
                except ValueError:
                    print("Не понятно")
                    continue
                if say < number:
                    print("больше")
                elif say > number:
                    print("меньше")
            print("Угадали!")
            input()
    except Exception:
        print("Error, возможно у вас неправильный ввод.")


if __name__ == "__main__":
    main()
