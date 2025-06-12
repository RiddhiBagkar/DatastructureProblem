class LinearSearch:
    def SearchElement(self,Array,item):
        #N stores lenght of array
        N=len(Array)
        #LOC:- LOCATION AT WHICH THE ELEMENT WILL BE FOUND
        loc=-1

        i=0

        #loop through array until N is less than i and until item is not found
        while i < N :
            if Array[i] == item:
                loc=i
                return loc
            i += 1
        return loc



arrayy=[12,34,56,67,78,89]
item=98
L1=LinearSearch()
print(L1.SearchElement(arrayy,item))



