class LinearSearch:
    def CountOcurr(self,Array,key):
        count=0
        for i in range(len(Array)):
            if Array[i]==key:
                count+=1
        return count

Array=[2,3,4,5,3,4,2,3]
key=3
L1=LinearSearch()

print(L1.CountOcurr(Array,key))