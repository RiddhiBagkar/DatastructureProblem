class LinearSearch:
    def elementclosest(self, Array,item):
        smallest_closest=-1
        largest_closest=-1
        for i in range (len(Array)):
            if Array[i] <= item:
                smallest_closest=Array[i]

            if item <= Array[i] <max(Array):
                largest_closest=Array[i]


        return (f"smallest than {item} :- {smallest_closest} \njust largest than {item}:- {largest_closest}")


arr=[3,7,12,13,15,18,19,21,25,26,27,32]
object1= LinearSearch()
print(object1.elementclosest(arr,item=20))