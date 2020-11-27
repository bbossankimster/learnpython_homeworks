import random
numbers1 = []
numbers2 = []
for i in range(10):
    numbers1.append(random.randint(1,100))
    numbers2.append(numbers1[i] + 1)
print("Исходный список", numbers1)
print("Измененный список", numbers2)
