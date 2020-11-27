school_results = [
    {'school_class': '1a', 'scores': [3,5,5,5,3,3,5,3,4,5,5,4,3,3,3,4,4,5,2]},
    {'school_class': '1b', 'scores': [3,5,5,5,2,2,3,5,5,4,3,3,3,4,4,5,2]},
    {'school_class': '1v', 'scores': [3,5,5,5,2,3,4,4,3,2,2,3,5,5,4,3,3,3,4,4,5,2]},
    {'school_class': '1g', 'scores': [3,5,5,5,2,2,3,5,5,3,2,3,4,3,2,2,4,3,3,3,4,4,5]},
]

school_average = 0
for i in range(len(school_results)):
    scores = school_results[i]['scores']
    class_average = 0
    for j in range(len(scores)):
        class_average = class_average + scores[j]
    class_average = class_average/len(scores)
    school_average = school_average + class_average
    print("Средний балл в классе", school_results[i]['school_class'],class_average)
print("Средний балл в школе", school_average/len(school_results))
