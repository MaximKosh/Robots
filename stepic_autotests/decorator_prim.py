#       Декоратор — это функция, которая позволяет обернуть другую функцию для расширения
#       её функциональности без непосредственного изменения её кода.

# Пример

def decorator_function(func):
    def wrapper():
        print('Функция-обёртка!')
        print('Оборачиваемая функция: {}'.format(func))
        print('Выполняем обёрнутую функцию...')
        func()
        print('Выходим из обёртки')
    return wrapper

@decorator_function
def hello_world():
    print('Hello world!')

hello_world()