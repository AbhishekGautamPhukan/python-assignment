from datetime import datetime
items={}

def add_item(med_name,price,qnt,exp_date):
    items[med_name]={
        'price': price,
        'quantity': qnt,
        'expiry_date':exp_date}
    
    print(f"Item {med_name} added successfully!")

def delete_item(name):
    if name in items:
        del items[name]
        print(f"{name} item has been deleted succesfully!")
    else:
        print(f"{name} item not found!")
    
def search_item(name):
    if name in items:
        print("Item found!")
    else:
        print("Item not found!")
    
def display_expired_drug():
    today=datetime.today().date()
    exp_items=[]
    
    for name, details in items.items():
        exp_date= datetime.strptime(details['expiry_date'],'%Y-%m-%d').date()
        if exp_date < today:
            exp_items.append(name)
            
    if exp_items:
        print("Expired items: ")
        for i in exp_items:
            print(i)
        
        
    else:
        print("No expired items.")
    
