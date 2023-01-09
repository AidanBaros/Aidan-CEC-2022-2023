audience = [[1, 2, 3, 2, 1, 1],
            [2, 4, 4, 3, 2, 2],
            [5, 5, 5, 5, 4, 4],
            [6, 6, 7, 6, 5, 5]]

audience = [[1, 2, 3, 2, 1, 1],
            [2, 4, 4, 3, 2, 2],
            [5, 5, 5, 10, 4, 4],
            [6, 6, 7, 6, 5, 5]]

def canISee(arrangment):
    for i in range(len(arrangment)):
        for j in range(len(arrangment)):
            if i-1 >= 0:
                if arrangment[i][j] < arrangment[i-1][j]:
                    return False
    return True

print(canISee(audience))