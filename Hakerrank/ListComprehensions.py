if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

list_of_coordinates = []
sigle_coordinate = []
i = 0
j = 0
k = 0

while i < x:
    while j < y:
        while k < Z:
            if i+j+k < n:
                sigle_coordinate = [i,j,k]
                print(sigle_coordinate)