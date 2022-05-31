def get_array():
    array = []
    length = int(input("Input array len: "))

    for i in range(length):
        array.append(int(input("Number: ")))

    return array

def merge(a, b):
    x = 0
    y = 0
    z = []
    while x < len(a) and y < len(b):
        if a[x] < b[y]:
            z.append(a[x])
            x += 1
        else:
            z.append(b[y])
            y += 1

    while x < len(a):
        z.append(a[x])
        x += 1

   while y < len(b):
        z.append(b[y])
        y += 1
    return z

def sort(array):
    if len(array) == 1:
        return array

    a = array[0:(len(array)//2)]
    b = array[(len(array)//2):len(array)]
    return merge(sort(a), sort(b))

array = get_array()
print("Here is your array: " + str(array))
array = sort(array)
print("\nHere is your array sorted: " + str(array))
