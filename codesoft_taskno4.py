contact={}

def display():
    print("\n\n")
    print('the all contacts')
    for key in contact:
        print(f"{key},{contact.get(key)}")
        

while True:
    print("1.add")
    print("2.del")
    print("3.update")
    print("4.view")
    print("5.search")
    print("6.exit")
    
    c=int(input("enter your choice:"))
    if c==1:
        name=input("enter the contact name:")
        ph=input("enter the phone number:")
        adress=input('enter the adress:')
        email=input('enter the email:')
        contact[name]=ph,adress
    elif c==2:
        dc=input('\nenter a contact to delete')
        contact.pop(dc)
    elif  c==3:
        edit=input('\nenter the contact to update:')
        ph=input('enter new phone number:')
        contact[edit]=ph
        print('updated sussecfully...\n')
        
    elif c==4:
        display()
        
    elif c==5:
        search_name=input('enter a name:')
        if search_name in contact:
            print(search_name,"the contact details..",contact[search_name])
        else:
            print('not found')
    elif c==6:
        break

    else:
        print('invalid input')
    
        
