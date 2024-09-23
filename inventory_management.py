inventory={
    "Gainer": (3000,100),
    "Peanut Butter": (500,150),
    "Honey": (49,150),
    "Glutamine":(799,100),
    "Creatine": (499,70)}

def update_inv(item,qnt_sold):
    if item not in inventory:
        print(f"Error:{item} does not exist in the store.")
        return
    
    price,cur_qnt=inventory[item]
    
    if qnt_sold >cur_qnt:
        print(f"Error: not enough in stock, only {cur_qnt} of {item} is available.")
        return
    
    new_qnt=cur_qnt-quantity
    inventory[item]=(price,new_qnt)
    print(f"Updated Current quantity of {item}")
    
item=input("Which item is sold: ")
quantity=int(input("Enter the quantity sold: "))
    
update_inv(item,quantity)
print("Inventory Updated: ")

for item,(x, y) in inventory.items():
    print(f"{item}: Price=Rs{x}, Quantity={y}")
