# Задание 2.
# Напишите функцию принимающую на вход только ключевые параметры
# и возвращающую словарь, где ключ — значение переданного аргумента,
# а значение — имя аргумента. Если ключ не хешируем, используйте
# его строковое представление.


def key_arg_only(**kwarg):
    my_dict = {}
    for key, value in kwarg.items():
        if value.__hash__ is not None:
            my_dict[value] = key
        else:
            my_dict[str(value)] = key
    return my_dict


print(key_arg_only(key_1=123, key_2="Hello", key_3=[5, 6, 7]))
