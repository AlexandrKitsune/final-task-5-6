field = [
    [''] * 3,
    [''] * 3,
    [''] * 3
]


def move(player):
    row = int(input('Выберите строку: '))
    col = int(input('Выберите колонку: '))
    if not 0 <= row <= 2 or not 0 <= col <= 2:
        print('Вы вышли за пределы поля')
        move(player)
    if field[row][col] != '':
        print('Место занято!')
        move(player)
    else:
        field[row][col] = player


def rules():
    print("""
    Правила данной игры:
    Поле имеет размеры 3*3
    Игроки по очереди ставят свои X и O
    Побеждает тот, кто раньше собирет
    три фигуры в ряд по вертикали,
    горизонтали или диагонали""")


def winner(player):
    print(f"{field[0]}\n{field[1]}\n{field[2]}")
    for row in field:
        if row == [player] * 3:
            print(f'Победили "{player}"!!!')
            return False
    if field[0][0] + field[1][1] + field[2][2] == player * 3:
        print(f'Победили "{player}"!!!')
        return False
    if field[0][2] + field[1][1] + field[2][0] == player * 3:
        print(f'Победили "{player}"!!!')
        return False
    if field[0][0] + field[1][0] + field[2][0] == player * 3:
        print(f'Победили "{player}"!!!')
        return False
    if field[0][1] + field[1][1] + field[2][1] == player * 3:
        print(f'Победили "{player}"!!!')
        return False
    if field[0][2] + field[1][2] + field[2][2] == player * 3:
        print(f'Победили "{player}"!!!')
        return False


def game():
    rules()
    print(f"{field[0]}\n{field[1]}\n{field[2]}")
    while True:
        print('Ходит "X"')
        move('X')
        if winner('X') == False:
            break
        print('Ходит"O"')
        move('O')
        if winner('O') == False:
            break

game()