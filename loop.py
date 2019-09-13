data  = ["php", "rub", "go", "js"]

for dataList in data:
	print(dataList)

api = "developer envengles"
for dataApi in api:
	print(dataApi)
	print(dataApi * 2)
	print(dataApi * 3)

ab = range(20)

for i in ab:
	print(i * 2)

locations = ["ubud", "canggu"]
print(locations[1])

if locations[0] == 'canggu' :
	c = range(30)
	for d in c:
		print(d * 5)
elif locations[1] == 'canggu':
	categoriesApi = range(30)
	for x in categoriesApi:
		print(x * 2, "data oke")
else:
	print(len(locations))