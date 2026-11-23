ROWS = 3
COLS = 3
START_SCORE = 15


class Item:
    def __init__(self, symbol, weight, value):
        self.symbol = symbol
        self.weight = weight
        self.value = value


def knapsack(items, capacity):
    """Возвращает максимальную сумму очков и список взятых предметов."""

    def node_bound_count(i, weight, value):
        """Оптимистичная оценка: сколько очков можно получить в лучшем
        случае, если продолжить с предмета номер i."""
        if weight > capacity:
            return 0
        node_value = value
        j = i
        total_weight = weight

        while j < len(items) and total_weight + items[j].weight <= capacity:
            node_value += items[j].value
            total_weight += items[j].weight
            j += 1
        if j < len(items):
            ratio = items[j].value / items[j].weight
            node_value += (capacity - total_weight) * ratio

        return node_value

    def branch_bound(i, weight, value, taken):
        """Рекурсивно решает: брать предмет номер i или не брать."""
        nonlocal max_value, best_items
        if weight <= capacity and value > max_value:
            max_value = value
            best_items = taken
        if i == len(items):
            return

        # Ветка 1: предмет i не берём
        if node_bound_count(i, weight, value) > max_value:
            branch_bound(i + 1, weight, value, taken)

        # Ветка 2: предмет i берём (только если он помещается)
        ratio = items[i].value / items[i].weight
        fits = weight + items[i].weight <= capacity
        if fits and value + (capacity - weight) * ratio > max_value:
            branch_bound(i + 1,
                         weight + items[i].weight,
                         value + items[i].value,
                         taken + [items[i]])

    items = sorted(items, key=lambda x: x.value / x.weight, reverse=True)
    max_value = 0
    best_items = []
    branch_bound(0, 0, 0, [])
    return max_value, best_items


def print_inventory(taken, rows, cols):
    """Печатает инвентарь в виде таблицы rows x cols."""
    cells = []
    for item in taken:
        # предмет занимает weight ячеек подряд
        for _ in range(item.weight):
            cells.append('[' + item.symbol + ']')
    while len(cells) < rows * cols:
        cells.append('[ ]')

    for row in range(rows):
        line = cells[row * cols:(row + 1) * cols]
        print(','.join(line))


if __name__ == '__main__':
    items = [Item('r', 3, 25), Item('p', 2, 15), Item('a', 2, 15),
             Item('m', 2, 20), Item('i', 1, 5), Item('k', 1, 15),
             Item('x', 3, 20), Item('t', 1, 25), Item('f', 1, 15),
             Item('d', 1, 10), Item('s', 2, 20), Item('c', 2, 20)]
    capacity = ROWS * COLS

    total_value = 0
    for item in items:
        total_value += item.value

    max_value, taken = knapsack(items, capacity)

    # Взятые предметы прибавляют очки, оставленные - вычитают
    score = START_SCORE + max_value - (total_value - max_value)

    if score > 0:
        print_inventory(taken, ROWS, COLS)
        print()
        print('Итоговые очки выживания:', score)
    else:
        print('Решения нет: итоговый счёт не положительный.')
