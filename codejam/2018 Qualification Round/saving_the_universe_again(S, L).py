for t in xrange(input()):
	d, s = raw_input().split()
	d = int(d)
	A = [0] * 30
	num = n = 0
	for c in s:
		if c == "C":
			n += 1
		else:
			A[n] += 1
			num += (1 << n)
	
	cnt = 0
	for i in xrange(29, 0, -1):
		while A[i] and num > d:
			num += (1 << (i-1)) - (1 << i)
			A[i] -= 1
			A[i-1] += 1
			cnt += 1
	print "Case #%d: %s" % (t + 1, "IMPOSSIBLE") if num > d else "Case #%d: %s" % (t + 1, str(cnt))