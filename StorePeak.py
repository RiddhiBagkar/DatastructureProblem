class BinarySearch:
        def Search_Peak(self, arr):
            low = 0
            high = len(arr) - 1

            while low <= high:
                mid = (low + high) // 2

                # Check if mid is a peak
                if (mid == 0 or arr[mid] >= arr[mid - 1]) and \
                        (mid == len(arr) - 1 or arr[mid] >= arr[mid + 1]):
                    return mid

                # If left neighbor is greater, move left
                elif mid > 0 and arr[mid - 1] > arr[mid]:
                    high = mid - 1

                # Else, move right
                else:
                    low = mid + 1

            return -1  # This line is never hit if array is non-empty


a=[1,6,2,1,1]
b1=BinarySearch()
print(b1.Search_Peak(a))
