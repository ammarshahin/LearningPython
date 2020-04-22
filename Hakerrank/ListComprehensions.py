x = int(input("sdfsd"))
y = int(input())
z = int(input())
n = int(input())

list_of_coordinates = []
single_coordinate = []
i = 0
j = 0
k = 0

while i < x:
    while j < y:
        while k < z:
            if i+j+k < n:
                single_coordinate = [i, j, k]
                print(single_coordinate)
            k += 1
        j += 1
    i += 1 
