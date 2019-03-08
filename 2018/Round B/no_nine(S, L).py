def is_legal(n):
	return "9" not in str(n) and (n % 9 != 0) 

def solve(n):
	x = map(int, list(str(n)))
	x.reverse()
	ret = 0
	for i in xrange(1, len(x)):
		ret += x[i] * (9 ** i)
	ret = 8 * ret / 9
	
	for i in xrange (n - (n % 10), n + 1):
		if is_legal(i):
			ret += 1
	return ret
	
for t in xrange(input()):
	f, l = map(int, raw_input().split())
	ans = solve(l) - solve(f) + 1
	print "Case #%d: %d" % (t + 1, ans)