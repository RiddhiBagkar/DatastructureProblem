class BinarySearch:
    def SearchElement(self,A,item):
        B=0
        E=len(A)-1
        while B <= E:
            mid = (B + E) // 2
            if item == A[mid]:
                return mid
            elif item > A[mid]:
                B = mid+1
            else:
                E = mid-1
        return -1

A=[23,45,56,78,90]
item=90
b1=BinarySearch()
print(b1.SearchElement(A,item))