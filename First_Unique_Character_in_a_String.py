def firstUniqChar(s):
	length = len(s)
	if length == 0:
		return -1
	if length == 1:
		return 0

	string = {}
	for i in s:
		string[i] = string.get(i, 0) + 1

	for i in s:
		if string[i] == 1:
			return s.index(i)

	return -1

