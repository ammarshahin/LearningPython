x = int(input())
y = int(input())
z = int(input())
n = int(input())

list_of_coordinates = []
single_coordinate = []
i = 0

while i <= x:
    j = 0
    while j <= y:
        k = 0
        while k <= z:
            if i+j+k <= n:
                single_coordinate = [i, j, k]
                print(single_coordinate)
            k += 1
        j += 1
    i += 1
