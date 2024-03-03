number = input("Enter starting number ")
sinnum = int(number)
iterator = 0
numlenplac = 0
while(True):
	number = str(sinnum)
	number = list(number)
	number = list(map(int, number))
	lownum = []
	highnum = []
	revsin = ""
	try:
		number[1]
	except:
		print(f"Not a Lychrel number after 0 iterations: {number}")
	numlen = len(number)
	if numlen % 2 == 0:
		oddflag = 0
		numlen = numlen / 2 
		numlen = int(numlen)
		numlenplac = numlen
		numlen -= 1
		while(numlen > -1):
			lownum.append(number[numlen])
			numlen -= 1
		while(numlenplac < len(number)):
			highnum.append(number[numlenplac])
			numlenplac += 1
	else:
		oddflag = 1
	if oddflag == 1:
		numlen = numlen / 2 - 0.5
		numlen = int(numlen)
		numlenplac = numlen + 1
		numlen -= 1
		while(numlen > -1):
			lownum.append(number[numlen])
			numlen -= 1
		while(numlenplac < len(number)):
			highnum.append(number[numlenplac])
			numlenplac += 1
	lownum.sort()
	highnum.sort()
	iterator += 1
	if highnum == lownum:
		break
	number.reverse()
	number = list(map(str, number))
	for num in number:
		revsin += num
	revsin = int(revsin)
	sinnum = sinnum + revsin
	if iterator == 10:
		break
iterator = iterator - 1
if iterator >= 9:
	print(f"Still a Lychrel number after 10 iterations: {sinnum}")
else:
	print(f"Not a Lychrel number after {iterator} iterations: {sinnum}")