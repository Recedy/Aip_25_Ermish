import random
def f1():
    s = ""
    for _ in range(0, int(input("N повторений "))):
        s = s + " " + str(input("Слово "))
    return s
def f2():
    s = ""
    p = ""
    while p != "stop":
        p = str(input())
        s = input() + " " + s
    return s
def f3():
    s = ""
    while s != "stop":
        s = str(input("Слово "))
        if 'ф' in s:
            print("Ого! Это редкое слово!")
        else:
            print("Эх, это не очень редкое слово...")
    return
def f4():
    c = 0
    n = 0
    while n != 3:
        x1 = random.randint(-200, 200)
        x2 = random.randint(-200, 200)
        if x1 + x2 == int(input(f"{x1} + {x2} = ")):
            c += 1
        else:
            n += 1
    return f"Игра окончена. Правильных ответов: {c}"

while True:
    user_input = input("Выберите опцию (1-4) или 'e' для выхода: ")
    match user_input:
        case '1':
            print(f1())
        case '2':
            print(f2())
        case '3':
            print(f3())
        case '4':
            print(f4())
        case "e":
            break
        case _:
            print("Неверный ввод, попробуйте снова.")