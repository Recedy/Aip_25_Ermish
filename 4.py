def f():
    if input("Пароль - ") == input("Повторите пароль - "):
        return "Пароль принят"
    return "Пароль не принят"

def f2(n: int):
    s = "kype"
    if n in range(37, 54):
        s = "bok"
    if n % 2 == 0 and n in range(1, 54):
        return "Верх " + s
    elif n % 2 != 0 and n in range(1, 54):
        return "Низ " + s
    return "Ошиб"

def f3(n: int):
    if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
        return f"Год {n} - високосный"
    return "Это год не високосный"

def f4(calor_one: str, calor_tow: str):
    match {calor_one.lower():1, calor_tow.lower():1}:
        case {"красный":1, "синий":1}: return "фиолетовый"
        case {"красный":1, "желтый":1}: return "оранжевый"
        case {"синий":1, "желтый":1}: return "зеленый"
    return "erro"

while True:
    match input():
        case '1':
            print(f())
        case '2':
            print(f2(int(input("Место? "))))
        case '3':
            print(f3(int(input("Год? "))))
        case '4':
            print(f4(input("Цвет 1 "), input("Цвет 2 ")))
        case "e": break
