def max_beauty_score(garden):
    rows, cols = len(garden), len(garden[0])
    for i in range(1, rows):
        garden[i][0] += garden[i-1][0]
    for j in range(1, cols):
        garden[0][j] += garden[0][j-1]
  
    for i in range(1, rows):
        for j in range(1, cols):
            garden[i][j] += max(garden[i-1][j], garden[i][j-1])
    
    return garden[-1][-1]

garden = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Maximum Beauty Score:", max_beauty_score(garden))


