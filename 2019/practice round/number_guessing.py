import sys

T = input()
for _ in range(T):
	A, B = map(int, raw_input().split())
	N = input()
	for i in range (N):
		guess = (A + B + 1) / 2
		print guess
		sys.stdout.flush()
		reply = raw_input()
		if reply == "CORRECT":
			break
		elif reply == "TOO_SMALL":
			A = guess
		elif reply == "TOO_BIG":
			B = guess - 1
		else:
		    sys.exit(-1)
			