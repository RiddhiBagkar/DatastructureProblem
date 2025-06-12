class LinearSearch:
    def FirstOcurr(self,Array,item):
        for i in range(len(Array)):
           if Array[i] == item:
                return f"First occurence is at {i}"
        return "Not found"
Array=[34,34,34,34,34]
item=3
L1=LinearSearch()
print(L1.FirstOcurr(Array,item))