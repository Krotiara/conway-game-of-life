import class_Field
import sys


class InputErrorField(Exception):
    def __str__(self):
        return "Вы ввели поле неправильно,пожаулйста,попробуйте еще раз"


def prepare_field(field):
    for i in range(len(field)):
        for j in range(len(field[i])):
            field[i][j] = int(field[i][j])
            if field[i][j] == 1:
                field[i][j] = [1, 1]
            else:
                field[i][j] = [0, 0]
    return field


def live():
    for step in range(count):
        step_game = field_game.relive()
        for i in range(field_game.field_wgt):
            for j in range(field_game.field_hgt):
                if step_game[i][j]:
                    field_game.m_field[i][j] = [1, 1]
                else:
                    field_game.m_field[i][j] = [0, 0]
    return field_game.m_field


def print_result(result):
    for i in range(field_game.field_wgt):
        for j in range(field_game.field_hgt):
            if result[i][j] == [1, 1]:
                result[i][j] = '1'
            else:
                result[i][j] = '0'
    for i in result:
        print(''.join(i))


def inspection_correct(console_field):
    for i in range(len(console_field)):
        for j in range(len(console_field[i])):
            if console_field[i][j] not in '01':
                raise InputErrorField


if __name__ == '__main__':
    buffer = []
    run = True
    count = int(input("Введите количество циклов жизни"))
    print("Введите ниже поле в формате ReadMe")
    console_field = [list(line.strip()) for line in sys.stdin]
    try:
        inspection_correct(console_field)
    except InputErrorField:
        print("Вы неправильно ввели поле")
        print(sys.stderr)
        sys.exit()
    wight = len(console_field[0])
    height = len(console_field)
    field = prepare_field(console_field)
    field_game = class_Field.Field(wight, height, field)
    field_game.flag_field = False
    result = live()
    print_result(result)
