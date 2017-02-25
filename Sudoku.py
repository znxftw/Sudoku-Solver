#Start Date : 23-02-2017
#Completion Date : 25-02-2017

from math import ceil
from copy import deepcopy

# Parse True/False values of initial Grid
def parseInit():
    for i in range(9):
        for j in range(9):
            if Grid[i][j] != 0:
                boolGrid[i][j] = [False for k in range(9)]
                boolGrid[i][j][Grid[i][j] - 1] = True
# Sum up the truth values for all elements
def checkCompletion():
    return int(sum(sum(sum(j) for j in i) for i in boolGrid))
# Filter out non-zero elements and call unTrueRest()
def filterPresent():
    for i in range(9):
        for j in range(9):
            if Grid[i][j] != 0:
                unTrueRest(i, j, Grid[i][j])
# Same column,row,3x3 box gets current value position set to False
def unTrueRest(i, j, n):
    for k in range(9):
        if k != j:
            boolGrid[i][k][n - 1] = False
        if k != i:
            boolGrid[k][j][n - 1] = False
        for l in range(9):
            if (ceil((k + 1) / 3.0) == ceil((i + 1) / 3.0) and i != k and ceil((l + 1) / 3.0) == ceil(
                        (j + 1) / 3.0) and l != j):
                boolGrid[k][l][n - 1] = False
# If we are certain of a number, fill it in Grid
def eval():
    for i in range(9):
        for j in range(9):
            if sum(boolGrid[i][j]) == 1:
                for k in range(9):
                    if boolGrid[i][j][k] == True:
                        Grid[i][j] = k + 1
# Print the 9x9 Grid
def printSudoku():
    for i in range(9):
        for j in range(9):
            print Grid[i][j], " ",
        print("\n")
# Escape condition in case eval() fucks up somewhere to restart
def checkZero():
    for i in range(9):
        for j in range(9):
            if sum(boolGrid[i][j])==0:
                return 1
    return 0
Grid = [[0 for i in range(9)] for j in range(9)]
boolGrid = [[[True for i in range(9)] for j in range(9)] for k in range(9)]
n = input("Enter the number of known elements (<81)")
print("Enter x,y,value in given format for all ",n, " values")
for i in range(n):
    x, y, a = input("")
    Grid[x][y] = a
parseInit()
temp=t1=0
#Loop through, eliminate possibilities using boolGrid, fill-in single valued-rows of boolGrid to Grid
while (checkCompletion() > 81):
    filterPresent()
    eval()
    # If it ends up going in an infinite loop, attempt assuming value of any one square till it is solved.
    if checkCompletion() == temp:
        backupBool = deepcopy(boolGrid)
        backupGrid = deepcopy(Grid)
        for i in range(9):
            for j in range(9):
                if sum(boolGrid[i][j]) > 1:
                    for k in range(9):
                        flag = 0
                        if boolGrid[i][j][k] == True:
                            Grid[i][j] = k + 1
                            while (checkCompletion() > 81):
                                filterPresent()
                                eval()
                                if t1 == checkCompletion() or checkCompletion()<81 or checkZero():
                                    flag = 1
                                    break
                                t1 = checkCompletion()
                            if flag == 1:
                                boolGrid = deepcopy(backupBool)
                                Grid = deepcopy(backupGrid)
                        if checkCompletion() == 81:
                            break
                if checkCompletion() == 81:
                    break
            if checkCompletion() == 81:
                break
    temp = checkCompletion()
printSudoku()
