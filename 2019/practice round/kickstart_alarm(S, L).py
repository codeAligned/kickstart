def get_A(N, x, y, C, D, E1, E2, F):
	A = []
	A.append((x + y) % F)
	for _ in xrange(N-1):
		prev_x = x
		prev_y = y
		x = (C * prev_x + D * prev_y + E1) % F
		y = (D * prev_x + C * prev_y + E2) % F
		A.append((x + y) % F)
	return A

def get_power(A, N, k):
	ret = 0
	mod = 1000000007
	for i in xrange (N):
		for j in xrange(i+1):
			ret = (ret + A[i] * (N-i) * ((j+1)**k)) % mod
	return ret

for t in xrange (input()):
	N, K, x, y, C, D, E1, E2, F = map(int, raw_input().split())
	A = get_A(N, x, y, C, D, E1, E2, F)
	ret = 0
	for i in range (K):
		ret = (ret + get_power(A, N, i+1)) % 1000000007
	print "Case #%d: %d" % (t+1, ret)
