x = int(input())
y = int(input())
z = int(input())
n = int(input())

list_of_coordinates = []

i = 0
while i <= x:
    j = 0
    while j <= y:
        k = 0
        while k <= z:
            if i+j+k != n:
                single_coordinate = [i, j, k]
                list_of_coordinates.append(single_coordinate)
            k += 1
        j += 1
    i += 1

print(list_of_coordinates)