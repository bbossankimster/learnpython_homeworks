with open('referat.txt', 'r', encoding='utf-8') as f:
    referat_string = f.read()
    print("Длина строки:", len(referat_string))
    words = referat_string.split()
    print(referat_string)
    print("Количество слов:", len(words))
    referat_string = referat_string.replace(".", "!")
    print(referat_string)

with open('referat2.txt', 'w', encoding='utf-8') as f:
    f.write(referat_string)
    print(referat_string)