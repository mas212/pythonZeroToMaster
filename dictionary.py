disc = {}

print(type(disc))

work = {
	"staff" : "10 orang",
	"frelance" : 50
}
print(len(work))

my_dict = {'name':'Jack', 'age': 26}
print(my_dict['name'])

list1 = []
for x in range(10):
	result =  x ** 2
	list1.append(result)
print(list1)

data = []
for a in range(7):
	if a > 2:
		result1 = a ** 3
		data.append(result1)
print(data)

squere = {
	1 : 1,
	2 : 2,
	3 : 3
}

for i in squere:
	print(squere[i])

def dataPeople():
	people  = {
		1:{'name': 'John', 'age': '27', 'sex': 'Male'},
		2:{'name': 'Marie', 'age': '22', 'sex': 'Female'}
	}
	#print(people)
	for a in people:
		print(a) 
		if a > 1 :
			print(people)
dataPeople()

people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Luna', 'age': '24', 'sex': 'Female', 'married': 'No'}}
people[4] = {'name': 'Hari', 'age': '27', 'sex': 'Male'}
print(people[4])