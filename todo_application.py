name = "Todo Application: "
options = """1. Add todo 
2. List all todos 
3. Display single todo 
4. Mark todo as completed
5. Close the application"""

todos = [] # storage which stores all of users todos 

tid = 1

while True: # makes the program run forever until user want to close 
    # printing the title of the application
    print(name)
    # printing the available options 
    print(options)
    # ask user to choose the option 
    choice = int(input("Enter your choice ( 1 - 5 ): "))
    # perform action based on option 
    match choice: 
        case 1: 
            print("Adding Todo: ")
            title = input("Enter Title: ")
            description = input("Enter Description: ")
            todo = {"id":tid ,"title":title,"description":description,"is_completed":False}
            tid = tid + 1
            todos.append(todo)
        case 2:
            print("Listing Todos: ")
            for todo in todos: 
                print(f"ID: {todo["id"]}")
                print(f"Title: {todo["title"]}")
                print()
        case 3:
            t_id = int(input("Enter the ID of the Todo: "))
            target_todo = {}
            for todo in todos: 
                if todo["id"] == t_id: 
                    target_todo = todo 
                    break 
            if target_todo == {}: 
                print("Todo Not found")
            else:
                print("Todo Details: ")
                print(f"ID: {target_todo["id"]}")
                print(f"Title: {target_todo["title"]}")
                print(f"Description: {target_todo["description"]}")
                print(f"is_completed: {target_todo["is_completed"]}")
                
        case 4: 
            print("Marking Todo as Completed: ")
            t_id = int(input("Enter the ID of the Todo: "))
            target_todo = {}
            for todo in todos: 
                if todo["id"] == t_id: 
                    target_todo = todo 
                    break 
            if target_todo == {}: 
                print("Todo Not found")
            else:
                todo["is_completed"] = True 
        case 5:
            print("Closing the application....")
            break
        case _: 
            print("Invalid choice! Try again")
    print("-"*15)
    choice = input("Do you want to continue (y/n)?: ")
    if choice == "y":
        continue
    else:
        break 
