class LinearSearch:
    def AllIndices(self,A,item):
        indices_list=[i for i in range(len(A)) if A[i]==item]
        return indices_list

l1=LinearSearch()
print(l1.AllIndices(A=[1,2,3,4,2,3,2],item=2))
