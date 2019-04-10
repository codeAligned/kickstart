for t in xrange(input()):
	n, p = map(int, raw_input().split())
	for _ in xrange(n):
		w, h = map(int, raw_input().split())
	
	P = p - 2 * (w + h) * n
	L = 2 * min(w, h)
	R = 2 * ((w ** 2 + h ** 2) ** 0.5)
	K = min(P / L, n)
	ans = p - (P - R * K) if R * K < P else p
	
	print "Case #%d: %f" % (t + 1, ans)