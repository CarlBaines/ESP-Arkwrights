from os import getcwd
from json import dump, load

global cwd
cwd = getcwd() #current directory

global productdetails
productdetails = {
    "productID": 0000000,
        "product name": "chainsaw",
        "department" : "Hand tools",
        "product location in warehouse" : "",
        "quantity" : 4,
        "price without vat" : 3.0,
        "price with vat" : 5.0
        }

global departments
departments = ["Power tools","Power tool accessories","Hand tools","Tool storage","Measuring tools", "Testing equipment","Heating and plumbing","Electrical and lighting","Screws","Nails","Fixings"]
               

def write(productdetails):
    with open(f'{cwd}/abc.json', 'w') as file:
         dump(productdetails, file, indent=3)
write(productdetails)

addproduct = True
while True:
    def inputs():
        productID = int(input("What is the ID of the product? "))
        productName = input("What is the name of the product? ")
        department = input("What department is the product from? ")
        productLocationInWarehouse = float(input("Where is the product located in the warehouse? "))
        quantity = int(input("How much of the product is there? "))
        productPriceNoVat = float(input("What is the product price without vat? "))
        productPriceWithVat = float(input("What is the product price with vat? "))

        productdetails[productID] = {
            "product name": productName,
            "department": department,
            "product location in warehouse": productLocationInWarehouse,
            "product quantity": quantity,
            "product price with no vat": productPriceNoVat,
            "product price with vat": productPriceWithVat,            }
        write(productdetails)
    inputs()

    if len(str(productID)) != 7:
        print("Your product ID is not the correct length ")
        continue

    def department_check(department):
        if department not in departments:
            print("Department doesnt exist")
    department_check(department)

    if str(productLocationInWarehouse
    

  
                
            
            
        
    
    
    
                                                
                                
    

                  
