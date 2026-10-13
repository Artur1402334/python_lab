import time
import os


RED = '\u001b[41m'
WHITE = '\u001b[47m'
YELLOW = '\u001b[43m'
GREEN = '\u001b[42m'
RESET = '\u001b[0m'


def flag():
    pixel = '    '
    lenght = 10
    height = lenght

    for i in range(height):
        if i < height // 2:
            print(WHITE + pixel * lenght + RESET)
        else:
            print(RED + pixel * lenght + RESET)


def pattern():
    line1 = "#########"
    line2 = "    #    "
    line3 = "#########"
    line4 = "  #   #  "
    line5 = "#########"

    for i in range(3):
        print(line1 * 3)
        print(line2 * 3)
        print(line3 * 3)
        print(line4 * 3)
        print(line5 * 3)


def animation():
    colors=[RED, YELLOW, GREEN]
    commands = ['READY', 'SET', 'GO!']
    for i in range(3):
        os.system("cls")
        print(f'{colors[i]} {commands[i]}  {RESET}')
        time.sleep(1)


def sequence():
    file = open('sequence.txt', 'r')
 
    first_sum = 0
    second_sum = 0
    counter = 0
 
    for line in file:
        val = abs(float(line))
        if counter < 125:
            first_sum += val
        else:
            second_sum += val
        counter += 1
 
    file.close()
 
    first_avg = first_sum / 125
    second_avg = second_sum / 125
 
    total = first_avg + second_avg
    print(f'{RED}{" " * int(first_avg / total * 100)}{RESET} {first_avg / total * 100:.2f}%')
    print(f'{WHITE}{" " * int(second_avg / total * 100)}{RESET} {second_avg / total * 100:.2f}%')


def graph():
    plot_list = [[0 for i in range(10)] for i in range(10)]
    result = [0 for i in range(10)]

    for i in range(10):
        result[i] = i ** 0.5

# шаг по оси Y (без округления, чтобы график не "уезжал")
    step = abs(result[9] - result[0]) / 9
    print(round(step, 2))

# первый столбец каждой строки: значение Y для этой строки
    for i in range(10):
        for j in range(10):
            if j == 0:
                plot_list[i][j] = step * (8 - i) + step

# ставим точки: в столбец x, если f(x) попадает в "полосу" этой строки
    for i in range(9):
        for j in range(10):
            if abs(plot_list[i][0] - result[9 - j]) < step /2 :
                for k in range(9):
                    if 8 - k == j:
                        plot_list[i][k + 1] = 1

    for i in range(9):
        line = ''
        for j in range(10):
            if j == 0:
                line += '\t' + str(round(plot_list[i][j], 1)) + '\t'
            elif plot_list[i][j] == 0:
                line += '--'
            elif plot_list[i][j] == 1:
                line += '!!'
        print(line)
    print('\t0\t1 2 3 4 5 6 7 8 9')


# flag()
# animation()
# pattern()
# sequence()
# graph()