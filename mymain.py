import time

#введение констант для удобной работы
CSI = "\x1b["
RESET = f"{CSI}0m"

#рисуем флаг Польши


def draw_flag():
    print("Флаг Польши")
    line = 10 * " "
    print(f"{CSI}107m{line}{RESET}")
    time.sleep(0.01)
    print(f"{CSI}41m{line}{RESET}")
    time.sleep(0.01)
    print()


#рисуем повторяющийся узор


def draw_art():
    t = int(input("Сколько раз повторить узор? "))
    for i in range(5):
        if i % 2 == 0:
            line = f"{CSI}100m               {RESET}"
            print(line * t)
            time.sleep(0.01)
        else:
            if i == 1:
                line = f"{CSI}107m       {CSI}100m {CSI}107m       {RESET}"
                print(line * t)
                time.sleep(0.01)
            else:
                line = f"{CSI}107m   {CSI}100m {CSI}107m       {CSI}100m {CSI}107m   {RESET}"
                print(line * t)
                time.sleep(0.01)
    print()


#выводим диаграмму


def draw_graphic():
    f = open("sequence.txt")
    lines = f.readlines()
    f.close()
    lines = list(map(float, lines))
    lines = list(map(abs, lines))
    sum1 = sum(lines[:125]) / 125
    sum2 = sum(lines[125:]) / 125
    main_sum = sum1 + sum2
    percent1 = round((sum1 / main_sum) * 50)
    percent2 = round((sum2 / main_sum) * 50)
    print(f"{CSI}30;105m[{' ' * (percent1-4)}{percent1/50*100}% {CSI}107m{'-' * (50 - percent1)}]{RESET}")
    time.sleep(0.01)
    print(f"{CSI}30;106m[{' ' * (percent2-4)}{percent2/50*100}% {CSI}107m{'-' * (50 - percent2)}]{RESET}")
    time.sleep(0.01)
    print()


#выводим функцию


def draw_function():
    x_list = []
    for i in range(81, 0, -1):
        num_y = i ** 0.5
        if i == 0:
            print(f"\t{int(num_y)}\t{'--' * int(num_y - 1)}!!{'--' * 9}")
        elif num_y % 1 == 0:
            x_list.append(i)
            row = f"{'--' * int(num_y - 1)}!!{'--' * int(10 - num_y)}"
            line = f"\t{int(i ** 0.5)}\t{row}"
            print(line)
    x_list = reversed(x_list)
    print(f"\t0\t", *x_list)


if __name__ == '__main__':   
    draw_flag()
    draw_art()
    draw_graphic() 
    draw_function()