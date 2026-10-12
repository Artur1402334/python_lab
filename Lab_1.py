import time
import os


RED = '\u001b[41m'
WHITE = '\u001b[47m'
YELLOW = '\u001b[43m'
GREEN = '\u001b[42m'
RESET = '\u001b[0m'
ERASE = '\x1B[2K'
BEGIN = '\x1B[1G'


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


flag()
animation()
pattern()
sequence()