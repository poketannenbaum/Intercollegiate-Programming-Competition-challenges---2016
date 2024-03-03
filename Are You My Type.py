num = input("Number ")
counter = 1
crosscounter = 1
num = int(num)
factorlist = []
while counter < num:
	if counter * crosscounter == num:
		factorlist.append(counter)
		factorlist.append(crosscounter)
	crosscounter += 1
	if crosscounter > num:
		crosscounter = 0
		counter += 1
factorlist = set(factorlist)
sum = 0
factorlist.remove(num)
for numf in factorlist:
	sum += numf
if sum > num:
	print(f"Abundant Factors are: {factorlist}")
if sum < num:
	print(f"Deficient Factors are: {factorlist}")
if sum == num:
	print(f"Perfect Factors are: {factorlist}")
print(f"Sum is: {sum}")
