puzzle=[[ 3, 8, 9, 0, 0, 0, 7, 0, 1 ],
	[ 0, 0, 0, 6, 0, 9, 0, 0, 0 ],
	[ 0, 0, 6, 7, 1, 0, 2, 0, 9 ],
	[ 0, 2, 0, 8, 0, 0, 0, 0, 4 ],
	[ 7, 0, 0, 2, 6, 5, 0, 0, 8 ],
	[ 8, 0, 0, 0, 0, 3, 0, 2, 0 ],
	[ 2, 0, 1, 0, 8, 4, 9, 0, 0 ],
	[ 0, 0, 0, 3, 0, 7, 0, 0, 0 ],
	[ 9, 0, 7, 0, 0, 0, 4, 8, 3 ]]

puzzlex=[[ 3, 1, 0, 0, 7, 0, 4, 0, 0 ],
	[ 0, 2, 0, 1, 0, 0, 0, 0, 0 ],
	[ 0, 8, 0, 0, 0, 0, 0, 3, 1 ],
	[ 2, 6, 3, 0, 1, 0, 9, 8, 7 ],
	[ 0, 0, 0, 8, 0, 0, 1, 2, 5 ],
	[ 8, 5, 1, 7, 9, 2, 6, 0, 0 ],
	[ 1, 3, 0, 0, 4, 7, 2, 0, 6 ],
	[ 6, 0, 2, 0, 0, 1, 0, 7, 0 ],
	[ 7, 0, 5, 0, 0, 0, 3, 1, 0 ]]


#while True:

    #puzzle = [[int(j) for j in input().split(" ")] for i in range(9)]

def subgrid(row,column):
    itemsInSubGrid = []
    if row < 3:
        if column < 3:
            for i in range(3):
                for j in range(3):
                    itemsInSubGrid.append(puzzle[i][j])
        elif column < 6:
            for i in range(3):
                for j in range(3,6):
                    itemsInSubGrid.append(puzzle[i][j])
        else:
            for i in range(3):
                for j in range(6,9):
                    itemsInSubGrid.append(puzzle[i][j])
    elif row < 6:
        if column < 3:
            for i in range(3,6):
                for j in range(3):
                    itemsInSubGrid.append(puzzle[i][j])
        elif column < 6:
            for i in range(3,6):
                for j in range(3,6):
                    itemsInSubGrid.append(puzzle[i][j])
        else:
            for i in range(3,6):
                for j in range(6,9):
                    itemsInSubGrid.append(puzzle[i][j])
    else:
        if column < 3:
            for i in range(6,9):
                for j in range(3):
                    itemsInSubGrid.append(puzzle[i][j])
        elif column < 6:
            for i in range(6,9):
                for j in range(3,6):
                    itemsInSubGrid.append(puzzle[i][j])
        else:
            for i in range(6,9):
                for j in range(6,9):
                    itemsInSubGrid.append(puzzle[i][j])
    return itemsInSubGrid

def printgrid():
    for i in range(9):
        if i%3 == 0 and i > 0:
            print("-----------------------")
        for j in range(9):
            if j%3 == 0:
                print('|',end=' ')
            if j < 8:
                print(puzzle[i][j],end=' ')
            else:
                print(puzzle[i][j])
        

def solve(row,column):
    
    if column > 8 or row > 8:
        return True
    elif puzzle[row][column] == 0: #identify spot to calculate value
        
        itemsInColumn = [ROW[column] for ROW in puzzle] #get values in column
        itemsInSubGrid = subgrid(row,column) #get the sub grid
        itemsInRow = puzzle[row] #find suitable value
        for i in range(1,10): 
            if i in itemsInColumn:
                if i == 9:
                    puzzle[row][column] = 0
                    return False
                continue
            elif i in itemsInSubGrid:
                if i == 9:
                    puzzle[row][column] = 0
                    return False
                continue
            elif i in itemsInRow:
                if i == 9:
                    puzzle[row][column] = 0
                    return False
                continue
            else:
                puzzle[row][column] = i
                if column < 8:                                 
                    if solve(row,column+1):
                        return True
                    else:
                        if puzzle[row][column] == 9:
                            puzzle[row][column] = 0
                        continue
                else:
                    if solve(row+1,0):
                        return True
                    else:
                        if puzzle[row][column] == 9:
                            puzzle[row][column] = 0
                        continue

    else:
        if column < 8:
            return solve(row,column+1)
        else:
            return solve(row+1,0)
#printgrid()
if solve(0,0):
    print("result exists")
printgrid()


    
    
        
        
