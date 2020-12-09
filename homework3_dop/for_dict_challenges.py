from collections import Counter
# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
# ???
#cnt = Counter(students)
print("\n### Задание 1 ###")
my_list = []
for n in students:
      my_list.append(n['first_name'])
my_counter = Counter(my_list)
for i in my_counter :
      print(i, ":", my_counter[i])
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.

students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
# ???
def most_freq (students_list, comment):
      my_list2 = []
      for n in students_list:
            my_list2.append(n['first_name'])
      my_counter2 = Counter(my_list2)
      most_name = my_counter2.most_common(1)
      print(comment, most_name[0][0])
print("\n### Задание 2 ###")
most_freq(students, "Cамое частое имя среди учеников:")
# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
# ???
print("\n### Задание 3 ###")
most_freq(school_students[0], "Самое частое имя в классе 1:")
most_freq(school_students[1], "Самое частое имя в классе 2:")
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
# ???

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.
def sex_stat (students_list, is_male_dic, comment = '', subtask = False):
      woman = 0
      man = 0
      my_list2 = []
      stat = {}
      for n in students_list:
            my_list2.append(n['first_name'])
      for my_str2 in my_list2:
            #for name in my_str2:
            if is_male_dic.get(my_str2) == False:
                  woman += 1
            else:
                  man += 1
      if subtask:
            stat['мальчиков'] = man
            stat['девочек'] = woman
            return stat
      else:  
          print(comment, woman, "девочки/ек и", man, "мальчика/ов")   

print("\n### Задание 4 ###")
sex_stat(school[0]['students'], is_male, "В классе 2a")
sex_stat(school[1]['students'], is_male, "В классе 3c")
# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
# ???
print("\n### Задание 5 ###")
my_stat = []
my_stat.append(sex_stat(school[0]['students'], is_male, "В классе 2a", True))
my_stat.append(sex_stat(school[1]['students'], is_male, "В классе 2a", True))
if my_stat[0]['мальчиков'] > my_stat[1]['мальчиков']:
      print('Больше всего мальчиков в классе 2a')
else:
      print('Больше всего мальчиков в классе 3c')
if my_stat[0]['девочек'] > my_stat[1]['девочек']:
      print('Больше всего девочек в классе 2a')
else:
      print('Больше всего девочек в классе 3c')
#sex_stat(school[1]['students'], is_male, "В классе 3c")
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a