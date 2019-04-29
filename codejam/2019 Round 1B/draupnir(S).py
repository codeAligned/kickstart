import sys
t, w = map(int, raw_input().split())
for _ in xrange(t):
	Q = [1, 63, 2*63, 3*63, 4*63, 5*63]
	A = []
	for q in Q:
		print q
		sys.stdout.flush()
		A.append(input())
	
	ans = [0] * 6
	ans[5] = A[5] / (1<<52)
	ans[4] = (A[4] - ans[5] * (1<<42)) / (1<<50)
	ans[3] = (A[3] - ans[4] * (1<<37) - ans[5] * (1<<31)) / (1<<47)
	ans[2] = (A[2] - ans[3] * (1<<31) - ans[4] * (1<<25) - ans[5] * (1<<21)) / (1<<42)
	ans[1] = (A[1] - ans[2] * (1<<21) - ans[3] * (1<<15) - ans[4] * (1<<12) - ans[5] * (1<<10)) / (1<<31)
	ans[0] = (A[0] - ans[1] - ans[2] - ans[3] - ans[4] - ans[5]) / (1<<1)
	
	print " ".join(map(str, ans))
	sys.stdout.flush()
	verdict = input()
	if verdict == -1:
		sys.exit()