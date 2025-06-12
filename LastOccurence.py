class LinearSearch:
    def LastOcurr(self,Array,key):
        last_index=-1
        i=0
        while i < len(Array):
            if Array[i] == key:
                last_index=i
            i+=1
        return last_index
Array=[34,24,45,34,67]
item=34
L1=LinearSearch()
print(L1.LastOcurr(Array,item))