resource = "https://www.programiz.com/python-programming/methods/built-in/slice"
pyString = 'Python'

sObject = slice(3)
print(pyString[sObject])

dev = "haloo developer"


print(dev[1:6])

sObjectDev = slice(1, 5, 6)
print(dev[sObjectDev])

sObject = slice(-1, -4)
print(pyString[sObject])

pList = ['php', 'Python', 'rubi', 'go']
ptupple = ('Python', 'go')

sObject = slice(4)
print(pList[sObject])