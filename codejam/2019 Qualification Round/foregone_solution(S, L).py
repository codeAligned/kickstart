for t in xrange(input()):
	n = input()
	a = b = 0
	mul = 1
	while n > 0:
		if n % 10 == 4:
			a += 2 * mul
			b += 2 * mul
		else:
			a += (n % 10) * mul
		mul *= 10
		n /= 10	
	
	print "Case #%d: %d %d" % (t + 1, a, b)