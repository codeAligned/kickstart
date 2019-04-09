for t in xrange(input()):
	n = input()
	A = map(int, raw_input().split())
	l1 = sorted(A[::2])
	l2 = sorted(A[1::2])
	if n % 2:
		l2.append(l2[-1])
		
	A = []
	for n1, n2 in zip(l1, l2):
		A += [n1, n2]
	
	idx = -1
	for i in xrange(n - 1):
		if A[i] > A[i+1]:
			idx = i
			break
	
	ans = "OK" if idx == -1 else str(idx)
	print "Case #%d: %s" % (t + 1, ans)