class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        # for num in range(x+1):
        #     if num * num > x:
        #         return num-1

        # Using Binary search
        left, right = 2, x // 2 # we start from 2 as we handled 1 and 0, and the right will be first guess which is int x/2

        while left <= right:
            mid = (left+right)//2
            num = mid * mid

            if num > x:
                right = mid-1
            elif num < x:
                left = mid + 1
            else:
                return mid

        return right                

        
