our_list = []
clean_list = []
marked_tasks = []

def print_task_list(our_list, marked_tasks):
    for task_no in range(len(our_list)):
        print(str(task_no + 1) + ". [", end = "")
        if task_no in marked_tasks:
            print("X", end="")
        else:
            print(" ", end="");
        print("]", our_list[task_no])

def add_item():
    new_task = input("Add an item: ")
    our_list.append(new_task)
    print("Item added")

def list_items():
    if not our_list:
       print("You dont have things to do")
    else:
        print("You saved the following to-do items: ")
        print_task_list(our_list, marked_tasks)

def mark_item():
    print("you saved the following to-do items: ")
    print_task_list(our_list, marked_tasks)
    d = int(input("Which one do you want to mark as completed? Press the number: ")) - 1
    marked_tasks.append(d)

def archive_item():
    for task_no in range(len(our_list)):
        if task_no not in marked_tasks:
            clean_list.append(our_list[task_no])

while True:

    c = input("Please specify a command [list, add, mark, archive, exit]: ")

    if c == "add":
        add_item()

    elif c == "list":
        list_items()

    elif c == "mark":
        mark_item()

    elif c == "archive":
        archive_item()
        our_list = clean_list
        clean_list = []
        marked_tasks = []
        print_task_list(our_list, marked_tasks)

    elif c == "exit":
        exit();
