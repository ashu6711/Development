def file_up():
    """importing invoice2() function from Invoice_record which returns invoice file;f,'Cart','Cart_quantity'
    and is stored in f1,cart,cart_n respectively"""
    from Invoice_record import invoice2
    f1, cart, cart_n = invoice2()

    # importing read_file.py which returns the 2D list stored in final_list and storing it in 'product'
    from read_file import read
    product = read()

    '''updating the inventory1.txt with the purchase of the product by reducing the quantity
    of the product bought from the quantity of product available in 'product' where the data is stored '''
    for i in range(len(cart)):
        for k in range(len(product)):
            if cart[i] == product[k][0]:
                product[k][2] = int(product[k][2]) - int(cart_n[i])

    '''writng the data of the 2D list 'product' in the file Inventory1.txt due
    to which theinventory is updated after the purchase'''
    f = open("Inventory1.txt", "w")
    for i in range(len(product)):
        for j in range(len(product[i])):
            f.write(str(product[i][j]))
            if j != 2:
                f.write(',')
            else:
                f.write("\n")
    f.close()

    # returning 'f1' which the invoice file and 'f' which is the updated inventory file
    return f1, f
