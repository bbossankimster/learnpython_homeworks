

def whatIsYourAge (age):
    age = int(age)
    if 0 < age < 3:
        result = print("Привет, ребенок")
    elif 3 <= age <=6:
         result = print("Привет, ребенок. Ты ходишь в дет. сад")
    elif 6 < age <=17:
         result = print("Привет, школьник. Ты учишься в школе")
    elif 17 < age <=22:
         result = print("Привет, школьник. Ты учишься в ВУЗе")
    elif 22 < age:
         result = print("Привет. Ты вызрослый")
    else:
         result = print("Число меньше нуля. Выход")
    return result

whatIsYourAge (input("Введите возраст, целое число больше нуля: "))