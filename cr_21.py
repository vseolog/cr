x = [4,5,8,9,12,16,18]
s = 16

def two_sum(x, s):
	pairs = []
	for i in range(len(x)):
		for j in range(i+1, len(x)):
			if x[i] + x[j] == s:
				pairs.append((i, j))

	return pairs

s = two_sum(x, s)