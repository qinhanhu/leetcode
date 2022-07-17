# 求最大公约数
# https://www.codenong.com/cs106205355/
def gcdV1(a, b):
	big, small = max(a, b), min(a, b)
	if big % small == 0:
		return small
	return gcdV1(big % small, small)

def gcdV2(a, b):
	if a == b:
		return a
	big, small = max(a, b), min(a, b)
	return gcdV2(big - small, small)

def gcdV3(a, b):
    if a==b:
        return a
    if (a&1)==0 and (b&1)==0:
        return gcdV3(a>>1,b>>1)<<1
    elif (a & 1) == 0 and (b & 1) != 0:
        return gcdV3(a>>1,b)
    elif (a & 1) != 0 and (b & 1) == 0:
        return gcdV3(a,b>>1)
    else:
        big=max(a,b)
        small=min(a,b)
        return gcdV3(big-small,small)

import math
def lcm(a, b):
	return a * b / math.gcd(a, b)
