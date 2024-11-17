#Script to solve Sudoku puzzles
#Created by Donald Maruta 08 Nov 24

#Import modules
import pandas as pd
import numpy as np
import os

os.chdir(r'c:\temp')

#Read CSV file with Sudoku puzzle in it
sudoku = pd.read_csv('sudoku.csv', header=None)

print(sudoku)

#Count number of empty cells
idx, idy = np.where(pd.isnull(sudoku))
total_len = len(idx)

i = 0 #Counter number

#Start calculating values for each cell
while i < total_len:
    tempCol = sudoku[idy[i]].tolist() #Values of same column
    tempRow = sudoku.loc[idx[i]].values.tolist() #Values of same row
    tempX = int(idx[i] / 3)
    tempY = int(idy[i] / 3)
    tempSudoku = sudoku.iloc[(tempX * 3): (tempX * 3) + 3, (tempY * 3): (tempY * 3) + 3]
    tempLst = tempSudoku.values.tolist() #values of 3x3 grid
    tempLst = sum(tempLst, [])

    #Checks current cell for existing number - if not, then assigns it to 0
    tempNum = sudoku.iloc[idx[i], idy[i]] if not pd.isna(sudoku.iloc[idx[i], idy[i]]) else 0

    found = False #Sets found to false
    while tempNum < 9:
        tempNum = tempNum + 1
        if ((tempNum not in tempCol) and (tempNum not in tempRow) and (tempNum not in tempLst)):
            sudoku.iloc[idx[i], idy[i]] = tempNum
            found = True
            break
        
    if found:
        i = i + 1 #Goes to the next cell
    else: #Resets current cell and go to previous cell
        sudoku.iloc[idx[i], idy[i]] = np.nan
        i = i - 1

print(sudoku)
