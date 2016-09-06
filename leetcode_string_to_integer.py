#!/usr/bin/env python
#Thanks for 九章算法

class Solution(object):
	def myAtoi(self, str):
		str = str.strip()
		if str == "":
			return 0
		i = 0
		sign = 1
		ret = 0
		MaxInt = (1 << 31) - 1

		if str[i] == '+':
			i -= 1
		elif str[i] == '-':
			i -= 1
			sign = -1

		for i in (i, len(str)):
			if str[i] < '0' or str[i] > '9':
				break

			ret = ret * 10 + int(str[i])
			if ret > sys.maxint:
				break

		ret *= sign
		if ret >= MaxInt:
			return MaxInt
		if ret < MaxInt * -1:
			return MaxInt *-1 -1
	
		return ret

			
