import re
numbers = input("Enter numbers: ")
numbers = re.split(" ", numbers)
numbers = list(map(int, numbers))
pivotnumber = numbers [0]
numbers.pop(0)
firstnum = []
bignum = []
for num in numbers:
	if num < pivotnumber:
		firstnum.append(num)
	else:
		bignum.append(num)
masterarry = firstnum
masterarry.append(pivotnumber)
for num in bignum:
	masterarry.append(num)
print (masterarry)