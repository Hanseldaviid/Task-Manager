# Task in python 


def create_task():
    title = input("Title of the task:").strip()
    priority = input("Priority? (high | medium | low): ").strip()
    
    task = {
        "title": title,
        "priority": priority,
        "complete": False
    }
    return task

def complete_task(task):
    found = False
    tasks = input("Task done?: ")
    for t in task:
        if t['title'].lower() == tasks.lower():
            t['complete'] = True
            found = True
            print("✅ Task completed it \n")
            break
    if not found:
        print("Task not found")        
    
    return task            
    
def filter(task, search):
    filtrer = []
    for t in task:
        if t['priority'] == search:
            filtrer.append(t)
            
    return filtrer 

print()

task = [] 

while True:
    print("\n = = Menu = = \n")
    print("1) Add task ")
    print("2) Show all tasks")
    print("3) Task done")
    print("4) Filtrer taks")
    print("5) Exit ")
    try:
        choice = int(input("Select an option: (1-5) "))
        match choice:
            case 1:
                print("==================================")
                add = create_task()
                task.append(add)
                print("✅ Task completed successfully \n ")
                print("==================================")
            case 2:
                if not task:
                    print("Nothing to see ")
                else:
                    for t in task:
                        state = "[ X ]" if t['complete'] else "[ ]"
                        print(f"{state} {t['title']} | Priority:{t['priority']}")
            case 3:
                if not task:
                    print("Nothing to see")
                else:
                    print("Completed taks")
                    complete_task(task) 
            case 4:
                if not task:
                    print("There's not taks")
                else:
                    p = input("What priority do you want to see? (high | medium | low): ").strip()
                    result = filter(task,p)
                    if not result:
                            print("Not task with that level of priority")
                    else:
                        for r in result:
                            state = "[ X ]" if t['complete'] else "[ ]"
                            print(f"{state} {t['title']} | Priority:{t['priority']}")                   
            case 5:
                print("Exiting . . . ") 
                break
            case _: 
                print("Invalid option")
    except ValueError:
        print("Enter valid options ")               
                         
                          
                            
                             
                
                    
                
                