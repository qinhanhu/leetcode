https://www.geeksforgeeks.org/how-to-compute-mod-of-a-big-number/
def mod(self, num, a):

    # Initialize result
    res = 0

    # One by one process all digits
    # of 'num'
    for i in range(0, len(num)):
        res = (res * 10 + int(num[i])) % a

    return res