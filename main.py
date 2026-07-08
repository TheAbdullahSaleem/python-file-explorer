import os
def current_dir():
    print(os.getcwd())
def list_files():
    for item in os.listdir():
        if os.path.isfile(item):
            print(f"[FILE] {item}")
        elif os.path.isdir(item):
          print(f"[FOLDER] {item}")
def check_exists():
    path = input("Enter The Path You want to check if exists or not:     ")
    if os.path.exists(path):
        print("The path exists")
    else:
        print("The path does not exist")
def create_folder():
    try:
        folder_name = input("Enter the name of folder you want to create:       ")
        os.mkdir(folder_name)
    except FileExistsError:
        print(f"A fodler with {folder_name} Already exists")
def delete_folder():
    try:
        folder_name = input("Enter the name of folder you want to delete:      ")
        os.rmdir(folder_name)
    except OSError:
        print(f"{OSError}")
    except FileNotFoundError:
        print(f"There is no folder named {folder_name}")
    except PermissionError:
        print(f"You dont have permission to edit {folder_name}")
def rename():
    try:
        old_name = input("Enter the name of file or folder you want to rename:       ")
        new_name = input("Enter the new name:        ")
        os.rename(old_name,new_name)
    except FileNotFoundError:
        print("This file cannot be found")
    except PermissionError:
        print("You dont have permission to do it")
    except OSError:
        print("Something went wrong")
def create_file():
    try:
        name = input("Enter the name of file you want to create")
        with open(name , 'w') as file:
            pass
    except PermissionError:
        print("You dont have permission to perform this action")
def delete_file():
    try:
        name = input("Enter the name of file you want to delete")
        os.remove(name)
    except OSError:
        print(f"{OSError}")
    except FileNotFoundError:
        print(f"There is no file named {name}")
    except PermissionError:
        print(f"You dont have permission to edit {name}")
def option_selection():
    while True:
        while True:
            try:
                user_choice = int(input("""
========== FILE EXPLORER ==========

1. Show Current Directory
2. List Files & Folders
3. Check if File/Folder Exists
4. Create Folder
5. Delete Empty Folder
6. Rename File/Folder
7. Create File
8. Delete File
9. Exit
            """))
            except ValueError:
                print("Please only enter a number not any other thing")
            else:
                break
        if user_choice < 1 or user_choice > 9:
            print("Please enter a valid choice")
            continue
        else:
            break
    return user_choice
def file_explorer():
    while True:
        user_choice=option_selection()
        if user_choice == 1:
            current_dir()
        elif user_choice == 2:
            list_files()
        elif user_choice == 3:
            check_exists()
        elif user_choice == 4:
            create_folder()
        elif user_choice == 5:
            delete_folder()
        elif user_choice == 6:
            rename()
        elif user_choice == 7:
            create_file()
        elif user_choice == 8:
            delete_file()
        elif user_choice == 9:
            print("Goodbye!")
            break
file_explorer()
