import re
numbers = input("Input the list of numbers: ")
numbers = re.split(" ", numbers)
numbers = list(map(int, numbers))
numbers.sort()
numbers.reverse()
numtally = 0
for num in numbers:
	if num == numbers[0]:
		numtally += 1
print(f"The largest number is {numbers[0]} and it occurs {numtally} time(s)")