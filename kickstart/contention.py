import sys
rl = lambda: sys.stdin.readline().split()

def count(n):
	return bin(n).count("1")
	
for t in xrange(input()):
	n, q = map(int, rl())
	booking = [list(map(int, rl())) for _ in xrange(q)]
	booking.sort(key=lambda x: x[1]-x[0])
	B = 0
	ret = n
	for x, y in booking:
		cur = ((1<<(y+1))-1) & ~((1<<(x-1))-1)
		ret = min(ret, count(cur) - count(B & cur))
		B |= cur
	
	print "Case #%d: %d" % (t+1, ret)