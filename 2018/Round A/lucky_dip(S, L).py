for t in xrange (input()):
	n, k = map(int, raw_input().split())
	A = map(float, raw_input().split())
	E = sum(A) / n
	larger = [x for x in A if x >= E]
	
	for _ in xrange (k):
		larger = [x for x in larger if x >= E]
		E = (sum(larger) + E * (n - len(larger))) / n
	
	print "Case #%d: %f" % (t+1, E)