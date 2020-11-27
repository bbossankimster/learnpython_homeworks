def ask_user():
    my_quest = {"Как жизнь": "Замечательно!", "Что делаешь?": "Работаю", "Кто ты?": "РОБОТ", "Что купить?": "Хлеб"}
    while True:
        my_string = input("User: ")
        if my_quest.get(my_string):
            print("Ответ", my_quest.get(my_string))
        else:
            print("Такого вопроса нет в словаре")

ask_user()