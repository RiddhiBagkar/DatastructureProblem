class LinearSearch:


    def MINinArray(self, Array):
        current_min = Array[0]
        for i in range(1, len(Array)):  # Start from index 1
            if Array[i] < current_min:
                current_min = Array[i]
        return current_min


    def MAXinArray(self, Array):
        current_max = Array[0]
        for j in range(1, len(Array)):  # Start from index 1
            if Array[j] > current_max:
                current_max = Array[j]
        return current_max



arr=[4,5,3,2,1]
l1=LinearSearch()
print(l1.MINinArray(arr))
print(l1.MAXinArray(arr))