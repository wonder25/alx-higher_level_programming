age = input("Enter age: ")

age = int(age)
if age == 5:
	print("Go to Kindergaten")
elif age > 5 and age <=17:
	print("Go to grades 1 through 12")
elif age > 17:
	print("Go to college")
else:
	print("stay home")
