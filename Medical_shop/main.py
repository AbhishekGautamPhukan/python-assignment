from inventory_package import *

while True:
    print("\nSelect Operation to perform:\n1. Add item\n2. Delete item\n3. Search an item\n4. List of expired drugs\n5. Exit")
    option=int(input("Enter your choice: "))

    if option==1:
        med_name=input("Enter medicine name: ").lower()
        price= float(input("Enter price: "))
        qnt= int(input("Enter quantity: "))
        exp_date= input("Enter the expiry date YY-MM-DD: ")
        
        add_item(med_name,price,qnt,exp_date)
    
    elif option==2:
        med_name=input("Enter medicine name to delete: ").lower()
        delete_item(med_name)
        
    elif option==3:
        med_name=input("Enter medicine name to search: ").lower()
        search_item(med_name)
    
    elif option==4:
        display_expired_drug()
    elif option==5:
        break
    else:
        print("Invalid choice")
