class LinearSearch:
    def ExistanceElement(self,Array,item):
        N = len(Array)
# LOC:- LOCATION AT WHICH THE ELEMENT WILL BE FOUND
        i = 0
# loop through array until N is less than i and until item is not found
        while i < N:
            if Array[i] == item:
                return  True
            else:
                return False


arrayy = [12, 34, 56, 67, 78, 89]
item = 98
L1 = LinearSearch()
print(L1.ExistanceElement(arrayy, item))