list1 = [4, 5, 6]
list2 = [10, 20, 30]

for i in list1:
	for a in list2:
		if a == 10:
			break
			print(i * a)
		print("oke excute")


for val in "string":
	if val == "i":
		continue
	print(val)
print("the end")

for val in "hallo bos":
	if val == "bos":
		break
	print(val)
print("stop bos")
#list
vowels = "abcdefgh"
while True:
	v = input("enter a vowels")

	if v in vowels:
		break
	print("hallo vowels")
print("beres")

dataTuple = (100, 200, 300)
print(dataTuple)
	