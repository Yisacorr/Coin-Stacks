# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 14:44:57 2021

@author: Yisacor

"""

def solve(grid):
        n = len(grid)
        sumOld = 0
        sumNew = 0
        for i in range (0,len(grid)-1):
             for j in range (0,len(grid[1])-1): 
                 sumOld = sumOld + grid[i][j];
        copy_grid = grid;
        rowHill(copy_grid)
        grid_T=[]
        grid_T = [[copy_grid[j][i] for j in range(n)] for i in range(n)]
        for j in range (0,n):    
           
            for k in range((grid_T[j].index(max(grid_T[j])))+1, (n-1)): 
                while ((grid_T[j][k]) < (grid_T[j][k-1])):      
                    grid_T[j][k] = (grid_T[j][k] + 1)          
            for i in range(0,(grid_T[j].index(max(grid_T[j]))-1)):   
                    while ((grid_T[j][i]) > (grid_T[j][i+1])):
                              grid_T[j][i+1] = (grid_T[j][i+1] + 1)
        
        copy_grid = [[grid_T[j][i] for j in range(n)] for i in range(n)]
        
        for i in range (0, len(copy_grid)-1):
             for j in range (0, len(copy_grid[1])-1): 
                 sumNew = sumNew + grid[i][j]; 
        AddedCoin = sumNew-sumOld

        for l in range(n):
            grid[l] = copy_grid[l]    
            print(copy_grid[l])
        return AddedCoin

def rowHill(grid):
        n = len(grid)
        
        for j in range (0,n):    
            for k in range((grid[j].index(max(grid[j])))+1, (n-1)): 
  
                while ((grid[j][k]) < (grid[j][k-1])):      
                    grid[j][k] = (grid[j][k] + 1) 
                  
            for i in range(0,(grid[j].index(max(grid[j]))-1)):   
                    while ((grid[j][i]) > (grid[j][i+1])):
                              grid[j][i+1] = (grid[j][i+1] + 1)      
