pogoda = {"city": "Москва", "temperature": "20"}
print(pogoda.get("city"))
pogoda["temperature"] = str(int(pogoda["temperature"]) - 5)
print(pogoda)

