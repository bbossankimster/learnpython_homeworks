pogoda = {"city": "Москва", "temperature": "20"}
print(pogoda.get("city"))
pogoda["temperature"] = str(int(pogoda["temperature"]) - 5)
print(pogoda)
print(pogoda.get("country", "Россия"))
print("Before adding Date len =",len(pogoda))
pogoda["date"] = "27.05.2019"
print("After adding Date len =", len(pogoda))