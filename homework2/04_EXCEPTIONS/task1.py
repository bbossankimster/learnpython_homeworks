def hello_user():
    while True:
        try:
            answer = input("Как дела?\n")
        except KeyboardInterrupt:
            print("Пока! Произошел KeyboardInterrupt")
            break
        if answer == "Хорошо":
            print("Пока!")
            break


hello_user()