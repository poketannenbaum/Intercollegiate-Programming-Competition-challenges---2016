number = input("Number")
number = list(number)
number = list(map(int, number))
onum = number.copy()
oonum = number.copy()
ans = []
for num in oonum:
	try:
		placeholder = number[0]
		counter = 0
		try:
			number[0]
		except:
			break
		for num in onum:
			try:
				if num == placeholder:
					counter += 1
					number.remove(num)
					try:
						if onum[counter] != num:
							ans.append(counter)
							ans.append(placeholder)
							onum.pop(0)
					except:
						ans.append(counter)
						ans.append(placeholder)
						onum.pop(0)
				if num != placeholder:
					break
			except:
				break
		try:
			revcounter = 0
			while(revcounter < counter - 1):
				onum.pop(0)
				revcounter += 1
		except:
			break
	except:
		break
ans = list(map(str,ans))
answer = ""
for num in ans:
	answer += num
print(answer)