def invoice1():

    #two list to store the name and quantity of the product bought by the customer
    CART=[]
    CART_QUANTITY=[]

    #importing read_file having function read which returns the 2D list where the data of the inventory is stored and storing it in 'List'
    import read_file
    List=read_file.read()

    #using While loop to take input of the user for buying the products and storing its data in CART and CART_QUANTITY
    buy = "y"
    while buy == "y":
        sucess=False
        while sucess==False:
            prod=input("Enter the product you want to buy: ")
            prod_=prod.lower()            
            for i in range(len(List)):
                if prod_==List[i][0].lower():
                    sucess=True               
            if sucess == False:
                print("we don't have this product")
                sucess=False
        CART.append(prod_)
        suc=False
        while suc==False:            
            try:
                num=int(input("Number of %s you want to buy: "%prod_))
                for i in range(len(List)):
                    if List[i][0]==prod_:
                        if num<int(List[i][2]):
                            CART_QUANTITY.append(num)
                            suc = True
                        elif num>int(List[i][2]):
                            print("we have " +List[i][2]+ " number of "+List[i][0])   
            except:                
                print("Invalid input")
                suc=False             
        success=False
        while success==False:            
            buy1=input("continue to buy (y/n): ")
            buy=buy1.lower()
            if buy=='y':
                 success=True 
            elif buy=='n':
                success=True

    #Returning the value of CART,CART_QUANTITY,List
    return CART,CART_QUANTITY,List
def invoice2():
    #importing date time library
    import datetime
    
    name=input("Enter your name: ")
    #storing the value of CART,CART_QUANTITY,List returned by invoice1 fuction and storing it in Cart,Cart_quantity,List1
    Cart,Cart_quantity,List1=invoice1()

    #Creating a list to store the taotal amount of each product
    amt=[]
    amount=0.00
    for i in range(len(Cart_quantity)):
        for k in range(len(List1)):
            if Cart[i]==List1[k][0]:
                amount=int(Cart_quantity[i])*int(List1[k][1])
                amt.append(amount)
    
    #importing random numbers form random library
    from random import randint
    ss=randint(1,10000)

    #Creating invoice by using the data input by the user
    f=open("%s%d.txt"%(name,ss),"w")
    f.write("invoice no. ")
    f.write(str(ss))
    f.write("\n")
    f.write("Date of purchase: ")
    f.write(str(datetime.datetime.now().year)+"/"+str(datetime.datetime.now().month)+"/"+str(datetime.datetime.now().day))
    f.write("\n")
    f.write("=============================================================================================")
    f.write("\n")
    f.write("                                 Ashutosh Electronics")
    f.write("\n")
    f.write("                                 Bhainsepati,Lalitpur")
    f.write("\n")
    f.write("                                    565656,555556")
    f.write("\n")
    f.write("==============================================================================================")
    f.write("\n")
    f.write("Customer's Name: "+str(name))
    f.write('\n')
    for i in range(len(Cart)):
        f.write("Name of the product: "+str(Cart[i]))
        f.write('\n')
        f.write("No. of %s= "%str(Cart[i]))
        f.write(str(Cart_quantity[i]))
        f.write('\n')    
    for i in range(len(Cart)):        
        f.write("Total amount for %s= "%str(Cart[i])+str(amt[i]))
        f.write("\n")
    amount_t=0.00
    for i in range(len(amt)):
        amount_t=amount_t+amt[i]
    f.write("Total cost of the products= "+str(amount_t))
    f.write("\n")
    ab=False
    while ab==False:
        try:
            discount=int(input("Enter discount percentage: "))
            ab=True
        except:
            print("Invalid Input")
    f.write("Discount= "+str(discount)+"%")
    f.write("\n")
    f_c=amount_t*(discount/100)
    f_cost=amount_t-f_c
    f.write("The Final cost of the products after discount= "+str(f_cost))
    f.write("\n")
    f.write("==============================================================================================")
    f.write("\n")
    f.write("              Thanks for purchasing our product. Hope to see you soon :)")
    f.close()

    #printing the invoice number for convinience
    print("File number for the invoice: %s%d"%(name,ss))
    return f,Cart,Cart_quantity


       


        
        


