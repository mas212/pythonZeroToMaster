def product():
	my_list = [10, 20, 30, 40, 50, 60]
	new_list = list(map(lambda x: x * 3, my_list))
	print(new_list)
product()