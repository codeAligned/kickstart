from fractions import gcd

def LCM(a, b):
	return abs(a * b) / gcd(a, b)
	
for t in xrange(input()):
	n = input()
	A = list(set([raw_input().strip() for _ in xrange(n)]))
	lcm = 1
	for x in A:
		lcm = LCM(lcm, len(x))
	
	ans = ""
	for idx in range(n + 1):
		n = len(A)
		S = set()
		for i in xrange(n):
			S.add(A[i][idx%len(A[i])])
		
		S = "".join(sorted(list(S)))
		ok = 0
		newA = []
		if len(S) == 3:
			ans = "IMPOSSIBLE"
			ok = -1
			break
		elif len(S) == 2:
			if S == "RS": 
				ans += "R"
				for i in xrange(len(A)):
					if A[i][idx%len(A[i])] != "S":
						newA += [A[i]]
						
			elif S == "PR": 
				ans += "P"
				for i in xrange(len(A)):
					if A[i][idx%len(A[i])] != "R":
						newA += [A[i]]
				
			else: 
				ans += "S"
				for i in xrange(len(A)):
					if A[i][idx%len(A[i])] != "P":
						newA += [A[i]]
			A = newA
		else:
			if S == "P": ans += "S"
			elif S == "S": ans += "R"
			else: ans += "P"
			ok = 1
			A = []
			
		if ok or not A:
			break
	
	if A:
		ans = "IMPOSSIBLE"
		
	print "Case #%d: %s" % (t+1, ans)