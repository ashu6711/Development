def read():
    #opening Inventory1.txt fiile in read mode
    file=open('Inventory1.txt','r')

   #reading each line in Inventory1.txt and creating a list with each each line as an element
    a=file.readlines()    
    
    l=[]    
    final_list=[]

    #appending each line in the .txt file in l and replacing '\n' at the last with ''
    for i in range(len(a)):
        l.append(a[i].replace('\n',''))
        
    #creating a list in final_list for each element in l
    for each in l: 
        final_list.append(each.split(','))
            
    file.close()
    return final_list


