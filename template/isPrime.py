# 判断质数
import math
def isPrime(n):
    if n <= 3:
        return n > 1

    if n % 6 != 1 and n % 6 != 5:
        return False

    sqrt = int(math.sqrt(n))
    for i in range(5, sqrt+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True
    

        
                    
                
    