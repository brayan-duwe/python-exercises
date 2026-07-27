class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
            
        value = []
        while x > 0:
            value.append(x % 10)
            x //= 10
        
        value_reversed = value[:]
        value_reversed.reverse()

        return value == value_reversed