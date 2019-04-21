from collections import Counter
for t in xrange(input()):
	n, s = map(int, raw_input().split())
	A = map(int, raw_input().split())
	ans = 1
	P = [Counter([])]
	for num in A:
		C = P[-1].copy()
		C[num] += 1
		P.append(C)
	
	for i in xrange(1, n+1):
		for j in xrange(i+1, n+1):
			C = P[j] - P[i-1]
			ans = max(ans, sum([C[x] for x in C if C[x] <= s]))
	print "Case #%d: %d" % (t + 1, ans)