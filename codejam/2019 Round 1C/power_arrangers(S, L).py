import sys
from collections import defaultdict

t, f = map(int, raw_input().split())
for _ in xrange(t):
	ans = ""
	d = defaultdict(list)
	for i in xrange(1, 120):
		guess = 1 + 5 * (i-1)
		print guess
		sys.stdout.flush()
		d[raw_input().strip()].append(i)
		
	for x in d:
		if len(d[x]) == 23:
			ans += x
			break
	
	nextd = defaultdict(list)
	for i in d[x]:
		guess = 2 + 5 * (i-1)
		print guess
		sys.stdout.flush()
		nextd[raw_input().strip()].append(i)
	
	for x in nextd:
		if len(nextd[x]) == 5:
			ans += x
			break
	
	d = nextd
	nextd = defaultdict(list)
	for i in d[x]:
		guess = 3 + 5 * (i-1)
		print guess
		sys.stdout.flush()
		nextd[raw_input().strip()].append(i)
	
	for x in nextd:
		if len(nextd[x]) == 1:
			ans += x
			break
	
	d = nextd
	for i in d[x]:
		guess = 4 + 5 * (i-1)
		print guess
		sys.stdout.flush()
		last = raw_input().strip()
	
	ans += list(set("ABCDE") - set(ans) - set(last))[0]
	ans += last
	
	print ans
	sys.stdout.flush()
	verdict = raw_input().strip()
	if verdict == "N":
		sys.exit()