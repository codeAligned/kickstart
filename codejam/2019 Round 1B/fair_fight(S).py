import sys
from math import log
INT_MAX = 987654321

class segmentTree(object):
	def __init__(self, A):
		self.n = len(A)
		nn = 2**(int(log(self.n, 2))+2)
		self.rangeMax = [-INT_MAX] * nn
		self.init(A, 0, self.n-1, 1)
		
	def init(self, A, left, right, node):
		if left == right:
			self.rangeMax[node] = A[left]
			
		else:
			mid = (left + right) / 2
			leftMax = self.init(A, left, mid, node * 2)
			rightMax = self.init(A, mid + 1, right, node * 2 + 1)
			self.rangeMax[node] = max(leftMax, rightMax)
		return self.rangeMax[node]

	def query(self, left, right, node, nodeLeft, nodeRight):
		if right < nodeLeft or nodeRight < left:
			return -INT_MAX
		if left <= nodeLeft and nodeRight <= right:
			return self.rangeMax[node]
		
		mid = (nodeLeft + nodeRight) / 2
		leftMax = self.query(left, right, 2*node, nodeLeft, mid)
		rightMax = self.query(left, right, 2*node+1, mid+1, nodeRight)
		return max(leftMax, rightMax)
		
for t in xrange(input()):
	n, k = map(int, raw_input().split())
	A = map(int, raw_input().split())
	B = map(int, raw_input().split())
	ATree = segmentTree(A)
	BTree = segmentTree(B)
	ans = 0
	for i in xrange(n):
		for j in xrange(i, n):
			if abs(ATree.query(i, j, 1, 0, n-1) - BTree.query(i, j, 1, 0, n-1)) <= k:
				ans += 1
	
	print "Case #%d: %d" % (t + 1, ans)