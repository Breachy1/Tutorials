def primes(num):
	prime_nums = []

	for i in range(num):    #changed to num
		count=0
		for n in range(1,i):
			if i % n == 0:
				count += 1
		if count == 1:
			prime_nums.append(i)

	return prime_nums


