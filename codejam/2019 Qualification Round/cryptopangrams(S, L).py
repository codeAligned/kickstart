from fractions import gcd

for t in xrange(input()):
	n, l = map(int, raw_input().split())
	A = map(int, raw_input().split())
	
	Llist = [0] * (l + 1)
	
	for i in xrange(l-1):
		if A[i] != A[i+1]:
			Llist[i] = A[i] / gcd(A[i], A[i+1])
			break
	
	for j in xrange(i, 0, -1):
		Llist[j-1] = (A[j-1] / Llist[j])
	
	for j in xrange(i, l):
		Llist[j+1] = (A[j] / Llist[j])
	
	primes = sorted(list(set(Llist)))
	s = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
	d = {}
	for p, c in zip(primes, s):
		d[p] = c
	
	ans = ""
	for num in Llist:
		ans += d[num]
	print "Case #%d: %s" % (t + 1, ans)