for t in xrange(input()):
	n, p = map(int, raw_input().split())
	A = map(int, raw_input().split())
	A.sort()
	ret = cur = A[p-1] * p - sum(A[:p])
	for i in xrange(p, n):
		cur += (A[i] - A[i-1]) * (p - 1) - (A[i-1] - A[i-p])
		ret = min(ret, cur)
		
	print "Case #%d: %d" % (t+1, ret)