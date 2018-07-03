prime_nums = []

for i in range(1000):    #changed 100 to 1000
	count=0
	for n in range(1,i):
		if i % n == 0:
			count += 1
	if count == 1:
		prime_nums.append(i)


		
print(prime_nums)
