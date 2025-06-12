class BinarySearch:

    def LowerBound(self,arr,Target):
        low=0
        high=len(arr)-1
        ans=-1

        while low <= high:
            mid = (low+high)//2

            if arr[mid] >= Target:
                ans= mid
                high = mid - 1
            else:
                low= mid+1
        return (f'lower bound of {target} is :{ans}')

    def upperbound(self,arr,target):
        low = 0
        high = len(arr) - 1
        ans = -1
        while low <= high:
            mid = (low + high) // 2

            if arr[mid] > target:
                ans =arr[mid]
                high = mid - 1
            else:
                low = mid + 1
        return ans





arr=[1,2,3,4,6,8]
target=5
s1=BinarySearch()
print(s1.LowerBound(arr,target))
print(s1.upperbound(arr,target))

