'''
1. create
    1. add new single dataset (via console)
2. read
    1. show all datasets
    2. show single dataset
3. update
    1. update single dataset
4. delete
    1. delete all
    2. delete single row
5. save/export
6. end program
'''

def show_main_menu():
    print("What would you like to do: ")
    print("1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    print("5. End")

def ask_for_integer_input(min, max):
    while True:
        print("Plese enter a number bewteen",min, "and",max,"!")
        answer = input("Input: ")
        if answer.isdecimal():
            if min > int(answer):
                print("The entered value is too low.")
            elif max < int(answer):
                print("The entered value is too high.")
            else:
                return int(answer)
        else:
            print("The entered value is no integer.")

def peek_single_dataset(lines):
    option3 = ask_for_integer_input(1, len(lines))
    print(lines[int(option3)-1])

def show_all_datasets(lines):
    max_sizes = []
    for line in lines:
        for i, token in enumerate(line.split(';')):
            if len(max_sizes) <= i:
                max_sizes.append(len(token.strip()))
            elif len(token.strip()) > max_sizes[i]:
                max_sizes[i] = len(token.strip())
    for linenumber, line in enumerate(lines):
        first = str(linenumber) if linenumber else " "
        print(first.ljust(3),end=' ')
        for i, token in enumerate(line.split(';')):
            print(fr"{token.strip()}".ljust(max_sizes[i]+1,'.'), end='')
        print()

def delete_single_dateset(lines):
    pass

def delete_all_datasets(lines):
    pass

def update_single_dataset(lines):
    pass

def add_via_console(lines):
    pass

def create_menu(create_lines):
    pass

def read_menu(read_lines):
    print("1. Show all")
    print("2. Show single line")
    option2 = ask_for_integer_input(1, 2)
    if option2 == 1:
        show_all_datasets(read_lines)
    else:
        peek_single_dataset(read_lines)

def update_menu(update_lines):
    pass

def delete_menu(delete_lines):
    pass


import pathlib  # loads the library for object-oriented filesystem paths
current_folder = pathlib.Path(__file__).parent.absolute().__str__()
import_file_name = "export.csv"
path_source = current_folder + "/" + import_file_name
print("Importing: " + path_source)

with open(path_source) as file:
    cur_lines = file.readlines()
    while True:
        show_main_menu()
        option = ask_for_integer_input(1, 6)
        if option == 1: # hier wird importiert oder hinzugefügt
            create_menu(cur_lines)
        elif option == 2: # hier wird gefiltert und angezeigt
            read_menu(cur_lines)
        elif option == 3: # hier werden vorhandene werte geändert
            update_menu(cur_lines)
        elif option == 4: # hier werden vorhanden werte gelöscht
            delete_menu(cur_lines)
        elif option == 6: # hier wird das programm beendet
            #cleanUnicode(path_source)
            print("good bye")
            break
