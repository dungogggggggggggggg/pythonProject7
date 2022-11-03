import view as user
import model_div
import model_sub
import model_sum
import model_mult
import logger


def button_click():
    global value_a, value_b
    print('1-комплексные числа, 2- рациональные числа')
    value_item = int(input('Выберите значение: '))
    print()
    if value_item == 1:
        value_a = user.input_complex()
        value_b = user.input_complex()
    if value_item == 2:
        value_a = user.input_data()
        value_b = user.input_data()
    print('1-деление, 2-умножение, 3 - сложение, 4- вычитание')
    print('Выберите функцию: ')
    value_model = int(input('Выберите значение: '))
    print()

    if value_model == 1:
        model_div.init(value_a, value_b)
        result = model_div.do_it()
        user.view_data(result)
        logger.log_to_file(value_a, value_b, "//", result)

    if value_model == 2:
        model_mult.init(value_a, value_b)
        result = model_mult.do_it()
        user.view_data(result)
        logger.log_to_file(value_a, value_b, "*", result)

    if value_model == 3:
        model_sum.init(value_a, value_b)
        result = model_sum.do_it()
        user.view_data(result)
        logger.log_to_file(value_a, value_b, "+", result)

    if value_model == 4:
        model_sub.init(value_a, value_b)
        result = model_sub.do_it()
        user.view_data(result)
        logger.log_to_file(value_a, value_b, "-", result)
