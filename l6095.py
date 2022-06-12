class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        special = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']
        digit = ['0','1','2','3','4','5','6','7','8','9']
        strong = [0] * 6
        pre = 0
        adjacent = False
        if len(password) >= 8:
            strong[0] = 1
        else:
            return False
        for i in range(len(password)):
            if password[i].islower():
                strong[1] = 1
            if password[i].isupper():
                strong[2] = 1
            if password[i] in digit:
                strong[3] = 1
            if password[i] in special:
                strong[4] = 1
            if i > 0 and password[i] == password[i-1]:
                adjacent = True
                return False
        if not adjacent:
            strong[5] = 1
        return sum(strong) == 6