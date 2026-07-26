class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
        candidate1 = nums[-3:]
        candidate2 = nums[:2] + nums[-1:]

        product1 = 1
        for num in candidate1:
            product1 *= num

        product2 = 1
        for num in candidate2:
            product2 *= num

        return max(product1, product2)

        