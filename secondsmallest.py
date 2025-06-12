arr = [1, 3, 4, 65]
smallest = float('inf')
second_smallest = float('inf')

for num in arr:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif smallest < num < second_smallest:
        second_smallest = num

if second_smallest == float('inf'):
    print("No second smallest element found")
else:
    print("Second smallest element is:", second_smallest)
