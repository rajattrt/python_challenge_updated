class Search:

    def search(self, recipe, workbench):
        recipe_rows = len(recipe)
        recipe_columns = len(recipe[0])
        workbench_rows = len(workbench)
        workbench_columns = len(workbench[0])

        workbench_m = [[0 for x in range(workbench_columns)] for y in range(workbench_rows)]
        recipe_m = [[0 for x in range(recipe_columns)] for y in range(recipe_rows)]
        
        #calculating the Unicode code of every position in recipe matrix and adding them
        for i in range(0, recipe_rows):
            for j in range(0, recipe_columns):
                if (recipe[i][j] != '_'):
                    recipe_m[i][j] = ord(recipe[i][j])
                if (i>0):
                    recipe_m[i][j] += recipe_m[i-1][j]
                if (j>0):
                    recipe_m[i][j] += recipe_m[i][j-1]
                if (i>0) and (j>0):
                    recipe_m[i][j] -= recipe_m[i-1][j-1]

        #calculating the Unicode code of every position in workbench matrix and adding them
        for i in range(0, workbench_rows):
            for j in range(0, workbench_columns):
                if (workbench[i][j] != '_'):
                    workbench_m[i][j] = ord(workbench[i][j])
                if (i>0):
                    workbench_m[i][j] += workbench_m[i-1][j]
                if (j>0):
                    workbench_m[i][j] += workbench_m[i][j-1]
                if (i>0) and (j>0):
                    workbench_m[i][j] -= workbench_m[i-1][j-1]

        #Returning false if the additions of the unicodes of both the matrixes do not match
        if (recipe_m[recipe_rows - 1][recipe_columns - 1] != workbench_m[workbench_rows - 1][workbench_columns - 1]):
            return False

        for i in range(recipe_rows - 1, workbench_rows):
            for j in range(recipe_columns - 1, workbench_columns):
                grid_most_left = 0
                grid_most_top = 0
                grid_most_diagonal = 0
                
                #Finding the Diagonal and exception cases and eliminating them
                try:
                    grid_most_top = workbench_m[(i-recipe_rows) if i-recipe_rows > 0 else (recipe_rows+10)][j] 
                except IndexError:
                    pass
                try:
                    grid_most_left = workbench_m[i][(j-recipe_columns) if j-recipe_columns > 0 else (recipe_rows+10)]
                except IndexError:
                    pass
                try:
                    grid_most_diagonal = workbench_m[(i-recipe_rows) if i-recipe_rows > 0 else 0][(j-recipe_columns) if j-recipe_columns > 0 else (recipe_rows+10)]
                except IndexError:
                    pass

                #finding the matching case
                if ( workbench_m[i][j] - grid_most_left - grid_most_top - grid_most_diagonal == recipe_m[recipe_rows - 1][recipe_columns - 1]):
                    for a in range(0, recipe_rows):
                        for b in range(0, recipe_columns):
                            if (workbench[i-(recipe_rows-1)+a][j - (recipe_columns -1) + b] != recipe[a][b]):
                                return False

                    return True

        return False