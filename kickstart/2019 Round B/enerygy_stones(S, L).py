import sys
rl = lambda: sys.stdin.readline().split()
def compare(S1, S2):
	s1, _, l1 = S1
	s2, _, l2 = S2
	first = s1 * l2
	second = s2 * l1
	if first > second:
		return 1
	elif first == second:
		return 0
	return -1

def maxEnergy(time, i):
	if i == n:
		return 0
	
	s, e, l = A[i]
	if i == n-1:
		return max(0, e - l * time)
	if dp[time][i] != -1:
		return dp[time][i]
	
	dp[time][i] = max(maxEnergy(time + s, i + 1) + max(0, e - l * time), maxEnergy(time, i + 1))
	return dp[time][i]
	
	
for t in xrange(input()):
	n = input()
	A = [map(int, rl()) for _ in xrange(n)]
	A.sort(cmp=compare)
	dp = [[-1] * n for _ in xrange(10000)]
	ans = maxEnergy(0, 0)
	print "Case #%d: %d" % (t + 1, ans)