for t in xrange(input()):
	n, k, p = map(int, raw_input().split())
	idx = []
	for _ in xrange(k):
		a, b, c = map(int, raw_input().split())
		idx.append((a, str(c)))
	idx.sort()
	ans = []
	if n != k:
		ans = list(("{0:0%db}" % (n - k)).format(p - 1))
	for a, c in idx:
		ans.insert(a - 1, c)
	print "Case #%d: %s" % (t + 1, "".join(ans))