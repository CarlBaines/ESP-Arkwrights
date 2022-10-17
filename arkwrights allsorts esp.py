from os import getcwd
from json import dump, load

global cwd
cwd = getcwd() #current directory

global productdetails

#for item in productdetails:
    #if item["product name"] == name:
        #product = item
        #break

with open(f"{cwd}/abc.json") as file:
    productdetails = load(file)

global departments
departments = ["Power tools","Power tool accessories","Hand tools","Tool storage","Measuring tools", "Testing equipment","Heating and plumbing","Electrical and lighting","Screws","Nails","Fixings"]
               

def write(productdetails):
    with open(f'{cwd}/abc.json', 'w') as file:
         dump(productdetails, file, indent = 1)


menu = input("Please enter a command:\n1) Search for a product\n2) Create a product\n3) Exit")

if menu == "1":
    productsearch = True
    while productsearch == True:
        menu2 = input("Please enter a command:\n1) Do you want to search a product by ID?\n2) Do you want to search a product by name?\n3) Quit.")
        if menu2 == '1':
            productID = str(input("What is the ID of the product? "))
            if productID in productdetails.keys():
                product = productdetails[productID]
            else:
                print("Product not found")

        elif menu2 == '2':
            productName = input("What is the name of the product? ")
            found = False
            for item in productdetails:
                if item["product name"] == name:
                    product = item
                    found = True
                    break
            if found is False:
                print("Item not found")
                continue
                  

        elif menu2 == '3':
            quit()

        print(product["product name"])

        print(product["department"])

        print(product["product location in warehouse"])

        print(product["product quantity"])

        print(product["product price with no vat"])

        print(product["product price with vat"])

        

        print("\n")

        
    
elif menu == "2":
    addproduct = True

    while addproduct == True:
        productID = int(input("What is the ID of the product? "))
        productName = input("What is the name of the product? ")
        department = input("What department is the product from? ")
        productLocationInWarehouse = str(input("Where is the product located in the warehouse? "))
        quantity = int(input("How much of the product is there? "))
        productPriceNoVat = float(input("What is the product price without vat? "))
        productPriceWithVat = float(input("What is the product price with vat? "))

        productdetails[productID] = {
            "product name": productName,
            "department": department,
            "product location in warehouse": productLocationInWarehouse,
            "product quantity": quantity,
            "product price with no vat": productPriceNoVat,
            "product price with vat": productPriceWithVat}
        write(productdetails)


        if len(str(productID)) != 7:
            print("Your product ID is not the correct length ")
            break
        

        def department_check(department):
            if department not in departments:
                print("Department doesnt exist")
                
        department_check(department)

        def warehouseLocationCheck(productLocationInWarehouse):
            if productLocationInWarehouse[0].isalpha() and productLocationInWarehouse[1].isdigit():
                return True
            else:
                return False
        warehouseLocationCheck(productLocationInWarehouse)

        def quantity_check(quantity):
            if not str(quantity).isdigit():
                print("That is not a valid quantity")
                return False
        quantity_check(quantity)

        def productPriceNoV(productPriceNoVat):
            try:
                float(productPriceNoVat)
            except:
                print("The price entered isn't a float")
                return False
            else:
                return True
        productPriceNoV(productPriceNoVat)

        def productPriceV(productPriceWithVat):
            try:
                float(productPriceNoVat)
            except:
                print("The price entered isn't a float")
                return False
            else:
                return True
        productPriceV(productPriceWithVat)

        def enterAnotherProduct():
            repeat = input("Do you want to enter another product? ")
            if repeat == "yes" or repeat == "y":
                pass
            else:
                quit()
        enterAnotherProduct()

        def append(productdetails):
            with open(f'{cwd}/abc.json', 'a') as file:
                 dump(productdetails, file, indent=3)

        
        
            
            
            

            
            
                 
        
        

      
                    
            
            
        
    
    
    
                                                
                                
    

                  
