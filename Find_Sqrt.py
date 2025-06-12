class BinarySearch:
    def sqrt_binary_search(self,n, precision=0.0001):
        low = 0
        high = n
        mid = 0

        while (high - low) > precision:
            mid = (low + high) / 2
            if mid * mid < n:
                low = mid
            else:
                high = mid

        return round(mid,2)


arr=[2,3,4,5,6,7,8,9,10]    
b1=BinarySearch()
print(b1.sqrt_binary_search(10))