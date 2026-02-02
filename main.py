tasks = []

def addtask():
    print("----------------------------------------------------------")
    newtask = input("Add a new task: ").strip()
    if newtask:
        tasks.append(newtask)
    else:
        print("Empty task not added.")

def showlist():
    print("----------------------------------------------------------")
    print("Current Tasks: ")
    if not tasks:
        print("No tasks.")
        return
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

while True:
    print("----------------------------------------------------------")
    print("1: Add a new Task")
    print("2: Show current Tasks")
    print("3: Exit")
    choice = input("What do you want to do: ").strip()
    try:
        option = int(choice)
    except ValueError:
        print("Enter a valid numeric option!")
        continue

    if option == 1:
        addtask()
    elif option == 2:
        showlist()
    elif option == 3:
        print("Goodbye!")
        break
    else:
        print("Enter a valid option!")
