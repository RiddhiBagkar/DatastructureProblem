class BinarySearch:
    def LastIndex(self, A, item):
        B = 0
        E = len(A) - 1
        result = -1

        while B <= E:
            MID = (B + E) // 2
            if A[MID] <= item:
                result = MID
                B = MID + 1  # Keep searching left
            else:
                E = MID - 1
        return result


arr=[1,2,3,3,4,4]
item=3

b1=BinarySearch()
print(b1.LastIndex(arr,item))