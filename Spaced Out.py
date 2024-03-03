nums = []
nums.append(input("Enter number 1: "))
nums.append(input("Enter number 2: "))
nums.append(input("Enter number 3: "))
nums = list(map(int, nums))
nums.sort()
nums.reverse()
diff = nums[0] - nums[1]
if nums[1] == nums[0] - diff and nums[2] == nums[1] - diff:
	print("Spaced Out")
else:
	print("Not Spaced Out")