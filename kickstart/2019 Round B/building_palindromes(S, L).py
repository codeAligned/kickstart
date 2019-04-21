import sys
from collections import Counter
rl = lambda: sys.stdin.readline().split()
for t in xrange(input()):
	n, q = map(int, rl())
	S = raw_input().strip()
	A = [Counter("")]
	for c in S:
		C = A[-1].copy()
		C[c] += 1
		A.append(C)
	ans = 0
	for _ in xrange(q):
		i, j = map(int, rl())
		C = A[j] - A[i-1]
		if len([x for x in C if C[x] % 2]) <= 1:
			ans += 1
		
	print "Case #%d: %d" % (t + 1, ans)