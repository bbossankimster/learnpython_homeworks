def stringCompare (str1, str2):
    if str1 and str2:
        if str1==str2:
            return 1
        elif str2 == "learn":
            return 3
        elif len(str1) > len(str2) :
            return 2
    else:
        return 0


print (stringCompare("testString1", "testString1"))
print (stringCompare("testString11", "testString2"))
print (stringCompare("testString1", "learn"))
print (stringCompare("testString1", ""))
