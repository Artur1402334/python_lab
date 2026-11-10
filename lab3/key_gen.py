import random
import tkinter as tk
from pathlib import Path
from string import ascii_uppercase, digits

import pygame

# Пути к файлам считаем от папки, где лежит сам скрипт
BASE_DIR = Path(__file__).resolve().parent
BG_FILE = str(BASE_DIR / 'background.png')
MUSIC_FILE = str(BASE_DIR / 'music.mp3')

BLOCKS_COUNT = 3
BLOCK_LENGTH = 4
MIN_SUM = 30
MAX_SUM = 35

# Параметры анимации: сколько кадров и пауза между ними (в миллисекундах)
ANIMATION_STEPS = 15
ANIMATION_DELAY = 60

SYMBOLS = ascii_uppercase + digits

# Веса символов: A=1 ... Z=26, цифра весит своё значение
WEIGHTS = {}
for number, letter in enumerate(ascii_uppercase, start=1):
    WEIGHTS[letter] = number
for digit in digits:
    WEIGHTS[digit] = int(digit)


def generate_key():
    blocks = []
    while len(blocks) < BLOCKS_COUNT:
        block = random.choices(SYMBOLS, k=BLOCK_LENGTH)
        block_sum = 0
        for symbol in block:
            block_sum += WEIGHTS[symbol]
        if MIN_SUM <= block_sum <= MAX_SUM:
            blocks.append(''.join(block))
    return '-'.join(blocks)


def animate(step, final_key):
    if step < ANIMATION_STEPS:
        # Пока кадры не закончились, показываем случайный «мусор»
        blocks = []
        for _ in range(BLOCKS_COUNT):
            blocks.append(''.join(random.choices(SYMBOLS, k=BLOCK_LENGTH)))
        key_var.set('-'.join(blocks))
        # Через паузу вызываем эту же функцию со следующим кадром
        window.after(ANIMATION_DELAY, animate, step + 1, final_key)
    else:
        # Кадры закончились: показываем ключ и включаем кнопку обратно
        key_var.set(final_key)
        btn_generate.configure(state='normal')


def start_generation():
    # Выключаем кнопку, чтобы анимацию нельзя было запустить дважды
    btn_generate.configure(state='disabled')
    animate(0, generate_key())


# Окно: размер берём по размеру картинки
window = tk.Tk()
window.title('Terraria Keygen')
window.resizable(False, False)

bg_img = tk.PhotoImage(file=BG_FILE)
window.geometry(f'{bg_img.width()}x{bg_img.height()}')

# Картинка на весь фон окна
bg_label = tk.Label(window, image=bg_img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Переменная, связанная с полем ключа
key_var = tk.StringVar()

# Тёмная рамка по центру внизу, чтобы поле и кнопка хорошо читались
frame = tk.Frame(window, bg='#1e3a34', padx=20, pady=15)
frame.place(relx=0.5, rely=0.85, anchor='center')

# Поле для ключа: текст можно копировать, но нельзя набирать руками
key_entry = tk.Entry(frame,
                     textvariable=key_var,
                     state='readonly',
                     readonlybackground='white',
                     justify='center',
                     font=('Consolas', 24),
                     width=14)
key_entry.grid(row=0, column=0, pady=(0, 10))

# Кнопка запуска генерации (скобки у функции не ставим)
btn_generate = tk.Button(frame,
                         text='Сгенерировать',
                         font=('Verdana', 14),
                         command=start_generation)
btn_generate.grid(row=1, column=0)

# Фоновая музыка по кругу; если не вышло, программа всё равно работает
try:
    pygame.mixer.init()
    pygame.mixer.music.load(MUSIC_FILE)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(loops=-1)
except (pygame.error, FileNotFoundError):
    print('Музыка не запустилась: проверь файл music.mp3')

window.mainloop()