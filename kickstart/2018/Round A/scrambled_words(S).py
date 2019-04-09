def makeString(s1, s2, n, a, b, c, d):
	x = [ord(s1), ord(s2)]
	for i in xrange (2, n):
		x.append((a * x[i-1] + b * x[i-2] + c) % d)
	s = [s1, s2] + [chr(97 + (i % 26)) for i in x[2:]]
	return "".join(s)

def findWord(word):
	m = len(word)
	for i in xrange(n - m + 1):
		if word[0] == S[i] and word[m-1] == S[i+m-1]:
			s1 = list(word[1:m-1]); s2 = list(S[i+1:i+m-1])
			s1.sort(); s2.sort()
			if s1 == s2:
				return True
	return False

for t in xrange(input()):
	l = input()
	dict = raw_input().split()
	line = raw_input().split()
	s1, s2 = line[:2]
	n, a, b, c, d = map(int, line[2:])
	S = makeString(s1, s2, n, a, b, c, d)
	
	ans = 0
	for word in dict:
		ans += findWord(word)
	
	print "Case #%d: %d" % (t + 1, ans)