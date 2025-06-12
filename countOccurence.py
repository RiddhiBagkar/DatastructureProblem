class BinarySearch:
    def first_occurrence(self,arr, x):
        low, high = 0, len(arr) - 1
        first = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == x:
                first = mid
                high = mid - 1  # look on left side
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        return first

    def last_occurrence(self,arr, x):
        low, high = 0, len(arr) - 1
        last = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == x:
                last = mid
                low = mid + 1  # look on right side
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        return last

    def count_occurrences(self,arr, x):
        first =self.first_occurrence(arr, x)
        if first == -1:
            return 0
        last = self.last_occurrence(arr, x)
        return last - first + 1


arr=[1,2,3,3,4]
x=3
b1=BinarySearch()
print(b1.count_occurrences(arr,x))