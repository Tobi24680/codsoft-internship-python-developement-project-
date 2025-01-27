tasks=[]

def add():
    task=input("ENTER A TASK TO  DONE:")
    tasks.append(task)
    print(f"{task} ADDED...")

def delete():
    list()
    tasktodel=int(input("ENTERA TASK TO DELETE:"))
    if tasktodel>len(tasks):
        print("CAN'T DELETE THIS TASK")
    else:
        tasks.pop(tasktodel)
        print("TASK DELETED SUCCEFULLY...")

def list():
    if not tasks:
        print("THERE IS NO TASK TO SHOW...")
    else:
        for i,task in enumerate(tasks):
            print(f"task {i} - {task}")

if __name__=="__main__":
    print("WELCOME TO THE TO-DO LIST....")
    while True:
        print("\n")
        print("1.Add a task")
        print("2.Del a  task")
        print("3.View")
        print("4.Exit")
        choice=int(input("ENTER A  NUMBER TO DONE FOR:"))
        if choice==1:
            add()

        elif choice==2:
            delete()

        elif choice==3:
            list()
            
        elif choice==4:
            break
            
        else:
           print("sorry")
print("THANK YOU VISIT AGAIN.....")        
