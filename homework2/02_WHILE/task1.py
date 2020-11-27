def hello_user():
    while True:
        answer = input("Как дела?\n")
        if answer == "Хорошо":
            print("Пока!")
            break

hello_user()