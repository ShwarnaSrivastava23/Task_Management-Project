def task():
    tasks = {}
    print("----Welcome To The Task Management App----")

    total_task = int(input("Enter how many task you want to add = ")) #5
    for i in range(1,total_task+1):
        task_name = input(input("Enter task{i} = "))
        tasks.append(task_name)

    print(" Todays tasks are\n{tasks}")
    while True:
        operation = int(input("Enter 1-ADD\n2-Update\n3-Delete\n4-View\n5-Exit/Stop"))
        if operation == 1:
            add = input("ENter task you want to add = ")
            tasks.append(add)
            print(f"Task{add} has been successfully added...")

        elif operation == 2:
            updated_val = input("Enter the task name you want to update = ")
            if updated_val in tasks:
                up = input("Enter new task = ")
                ind = tasks.index(updated-val)
                tasks[ind] = up
                print("updated_task {up}")

        elif operation == 3:
            del_val = int(input("Enter the task you want to delete = "))
            if del_val in tasks:
                ind = tasks.index(del_val)
                del_tasks[ind]
                print("Task{del_val} has been deleted...")   
        elif opertion == 4:
            print(f"Total task = {tasks}")
        
        elif opertion == 5:
            print("Closing the program....")
            break

        else:
            print("Invalid Input")

