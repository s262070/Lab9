print "Enter a temperature in celsius"
celsius = int(raw_input())
fahrenheit = celsius * 9 / 5 + 32
print fahrenheit

myList = [102,98,96,101,100,99,103,97,98,105]
newList = []
for x in myList:
    if x >=100:
        newList.append(x)
print newList
