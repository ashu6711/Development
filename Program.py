#main file of the program from where the program is executed.

#Using 'while' loop to make the program run untill the user runs it continuesly
run_program='yes'
while run_program=='yes':
    
    #importing read_file.py which returns the 2D list stored in final_list and storing it in 'z'
    import read_file    
    z=(read_file.read())    

    print("product              Quantity               Rate")

    #printing the number of products availabe in the inventory with their name
    for  i in range(len(z)):
        print("%s    "%z[i][0]+"             %s"%str(z[i][2])+"                 %s"%str(z[i][1]))


    '''importing file_up() fucntion from the file file_update
    which returns file in which invoice is printed;f1 and updated Inventory1.txt;f ''' 
    from file_update import file_up
    a=file_up()
    
    #using try:,except: for fault tolerance while asking the user to continue running the program
    success=False
    while success==False:
        run_program=input("Continue running the program(yes/no): " )
        try:
            if run_program=="yes" or run_program=="no":           
                success=True
        except:
            print("Invalid Input")
            






