# Вывести последнюю букву в слове
word = 'Архангельск'
# ???
print(word[-1:])

# Вывести количество букв "а" в слове
word = 'Архангельск'
# ???
sum = 0
for my_char in word:
    if my_char.lower() == "а":
        sum += 1
print ("Букв А:", sum)

# Вывести количество гласных букв в слове
word = 'Архангельск'
# ???
sum = 0
glasnie = [ 'а' , 'у' , 'о' , 'ы' , 'и' , 'э' , 'я' , 'ю' , 'ё' , 'е' ,  ]
for my_char in word:
    if my_char.lower() in glasnie:
        sum += 1
print ("Гласных букв:", sum)
    

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
# ???
my_sentence = sentence.split()
print("Колчиество слов:", len(my_sentence))
# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
# ???
for my_word in sentence.split():
    print(my_word[0])

# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
# ???
split = sentence.split()
size = 0
for my_word in split:
    size += len(my_word)
size_avg = size/len(split)
print("Количество слов", len(split), "Средняя длина слова:", size_avg)