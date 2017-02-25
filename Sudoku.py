from math import ceil
#Parse True/False values of initial Grid
def parseInit():
    for i in range(9):
        for j in range(9):
            if Grid[i][j]!=0 :
                boolGrid[i][j]=[False for k in range(9)]
                boolGrid[i][j][Grid[i][j]-1]=True
#Sum up the truth values for all elements
def checkCompletion():
    return int(sum(sum(sum(j) for j in i) for i in boolGrid))
#Filter out non-zero elements and call unTrueRest()
def filterPresent():
    for i in range(9):
        for j in range(9):
            if Grid[i][j]!=0:
                    unTrueRest(i,j,Grid[i][j])
#Same column,row,3x3 box gets current value position set to False
def unTrueRest(i,j,n):
    for k in range(9):
		if k!=j:
			boolGrid[i][k][n-1]=False
		if k!=i:
			boolGrid[k][j][n-1]=False
		for l in range(9):		
			if(ceil((k+1)/3.0)==ceil((i+1)/3.0) and i!=k and ceil((l+1)/3.0)==ceil((j+1)/3.0) and l!=j):
				boolGrid[k][l][n-1]=False
#If we are certain of a number, fill it in Grid
def eval():
	for i in range(9):
		for j in range(9):
			if sum(boolGrid[i][j])==1:
				for k in range(9):
					if boolGrid[i][j][k]==True:
						Grid[i][j]=k+1
#Print the 9x9 Grid
def printSudoku():
	for i in range(9):
		for j in range(9):
			print Grid[i][j]," ",
		print("\n")
Grid=[[0 for i in range(9)] for j in range(9)]
boolGrid=[[[True for i in range(9)] for j in range(9)] for k in range(9)]
n=input("Enter the number of known elements")
for i in range(n):
	x,y,a=input("Enter the x,y position and value")
	Grid[x][y]=a
parseInit()
while(checkCompletion()>81):
	filterPresent()
	eval()
	if checkCompletion()==temp :
		backupBool=boolGrid
		for i in range(9):
			for j in range(9):
				t=sum(x for x in boolGrid[i][j])
				if t!=1 :
					for k in range(9):
						flag=0
						if boolGrid[i][j][k]==True:
							Grid[i][j]=k+1
							while(checkCompletion()>81):
								filterPresent()
								eval()
								if t1==checkCompletion():
									flag=1
									break
								t1=checkCompletion()
							if flag==1 :
								boolGrid=backupBool
						if checkCompletion()==81 :
							break
				if checkCompletion()==81:
					break
			if checkCompletion()==81:
				break
	temp=checkCompletion()
printSudoku()