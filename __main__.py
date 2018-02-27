from search import Search

if __name__ == '__main__':
   
    with open('recipeW') as f:
        recipe = f.readlines()
    
    recipe = [x.strip() for x in recipe]

    with open('workbenchW') as f:
        workbench = f.readlines()
    
    workbench = [x.strip() for x in workbench]

    s_ins = Search()

    b = s_ins.search(recipe,workbench)
    print ("The given recipe is part of the Workbench : " + str(b))