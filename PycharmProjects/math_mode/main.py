import re
import tree
import parsing
import  table

exc_name= 'wrong name of table, please try again'
exc_wrong='something went wrong, please try again'
exc_size='wrong size, please try again'
exc_name_taken='this name is already taken, please try again'
exc_parsing='something went wrong in parsing, please try again'
def beatiful_print(column_names, columns, indexes_of_right_col, right_rows):
    if not right_rows:
        print("selection is empty")
    else:
        size = len(column_names)
        size_col = len(columns[0])
        max = []
        for i in range(size):
            max.append(len(column_names[i]))

        # print('\n')
        for j in right_rows:
            for i in indexes_of_right_col:
                if len(columns[i][j]) > max[i]:
                    max[i] = len(columns[i][j])
        # print(max)

        for i in indexes_of_right_col:
            t = max[i] - len(column_names[i])
            if (t % 2 == 0):
                print("|", end='')
                k = 0
                while k < t / 2:
                    print(" ", end='')
                    k = k + 1
                print(column_names[i], end='')
                k = 0
                while k < t / 2:
                    print(" ", end='')
                    k = k + 1

            else:
                print("|", end='')
                k = 0
                while k < t / 2 - 1:
                    print(" ", end='')
                    k = k + 1
                print(column_names[i], end='')
                k = 0
                while k < t / 2:
                    print(" ", end='')
                    k = k + 1
        print("|", end='')
        print('\n')
        print("+", end='')
        for i in indexes_of_right_col:
            k = 0
            while k < max[i]:
                print("-", end='')
                k = k + 1
            print("+", end='')
        print('\n')
        for j in right_rows:
            for i in indexes_of_right_col:
                t = max[i] - len(columns[i][j])
                if (t % 2 == 0):
                    print("|", end='')
                    k = 0
                    while k < t / 2:
                        print(" ", end='')
                        k = k + 1
                    print(columns[i][j], end='')
                    k = 0
                    while k < t / 2:
                        print(" ", end='')
                        k = k + 1

                else:
                    print("|", end='')
                    k = 0
                    while k < t / 2 - 1:
                        print(" ", end='')
                        k = k + 1
                    print(columns[i][j], end='')
                    k = 0
                    while k < t / 2:
                        print(" ", end='')
                        k = k + 1
            print("|", end='')
            print('\n')
        print("+", end='')
        for i in indexes_of_right_col:
            k = 0
            while k < max[i]:
                print("-", end='')
                k = k + 1
            print("+", end='')
        print('\n')


def delete(column_names, columns, right_rows):
    size = len(column_names)
    size_col = len(columns[0])
    indexes_of_right_col = []
    for i in range(len(column_names)):
        indexes_of_right_col.append(i)
    for j in reversed(right_rows):
        for i in reversed(indexes_of_right_col):
            # columns[i][j]="*"
            if columns[i]:
                columns[i].pop(j)


def delete_dupes(arr):
    size = len(arr)
    for i in range(1, size):
        if i >= size:
            break
        if arr[i] == arr[i - 1]:
            arr.pop(i)
            size = len(arr)
    size = len(arr)
    if size > 2:
        if (arr[size - 1] == arr[size - 2]):
            arr.pop(size - 1)


def delete_dupes_rand_order(arr):
    arr1 = []
    for i in reversed(arr):
        if i not in arr1:
            arr1.append(i)
    arr1.sort()
    arr = []
    for elem in arr1:
        arr.append(elem)
    return arr


def edit_arr(arr):
    delete_dupes(arr)
    arr.sort()


def get_input():
    EmpInput = ""
    while ";" not in EmpInput:
        EmpInput += input()
        EmpInput += '  '
    return EmpInput


tables = []
print("Please create table to start ")
EmpInput1=''
while "exit" not in EmpInput1:
    EmpInput = get_input()
    EmpInput1 = EmpInput
    EmpInput1 = EmpInput1.casefold()
    first_command = EmpInput1.split()[0]
    if first_command == "create":
        result = []
        index = []
        number_of_index = []
        try:
            name_table = parsing.create_table(EmpInput, result, index, number_of_index)
            name_table1 = name_table
            check_if_name_is_right = -1
            if tables:
                for elem in tables:
                    if elem.get_name() == name_table:  # !!!!!!
                        check_if_name_is_right = 0

                if check_if_name_is_right == 0:
                    print("this name is already taken, please try again")
                    continue
            if check_if_name_is_right==-1:
                    try:
                        name_table = table.Table(name_table, result, index, number_of_index)
                        print(f"Table {name_table1} has been created")
                        tables.append(name_table)
                    except:
                        print(exc_wrong)
                        continue
            """        
            else:
                try:
                    name_table = table.Table(name_table, result, index, number_of_index)
                    print(f"Table {name_table1} has been created")
                    tables.append(name_table)
                except:
                    print("something went wrong")
                    continue
            """
        except:
            print(exc_wrong)
            continue
    elif (first_command == "insert"):
        column_values = []
        name_table = parsing.insert_table(EmpInput, column_values)
        check_if_name_is_right = -1
        for elem in tables:
            if elem.get_name() == name_table:
                name_of_insert = elem.get_name()
                check_if_name_is_right = 1
                break

        if check_if_name_is_right == -1:
            print("wrong name of table, please try again")
            continue
        else:
            col_numb = elem.get_numb_of_rows()

            if (elem.get_size() != len(column_values)):
                print("wrong size, please try again")
                continue
            else:
                try:
                    r1 = elem.add_row(col_numb, column_values)
                    print(f"Row has been added to table {name_of_insert}")
                except:
                    print(exc_wrong)
                    continue



    elif first_command == "select" or first_command == "select*":
        if ("*" in EmpInput1):
            if ("where" in EmpInput1):
                result1 = []
                try:
                    name_of_insert = parsing.command_all_where(EmpInput, result1)
                    check_if_name_is_right = -1
                    for elem in tables:
                        if elem.get_name() == name_of_insert:
                            check_if_name_is_right = 1
                            break
                    if check_if_name_is_right == -1:
                        print(exc_name)
                        continue
                    else:
                        col_names = []
                        elem.get_col_name(col_names)
                        size_col_names = len(col_names)
                        number = 0
                        size_res = len(result1)
                        if '"' in EmpInput1:
                            #for k in range(size_res - 2):
                                #for i in range(size_col_names):
                                    #if col_names[i]==result1[k]:
                                        #indexes.append(i)
                                    #if col_names[i] == result1[size_res - 3]:
                                        #number = i + 1
                            # result1.pop(size_res-3)
                            #try:
                                #if number == 0:
                                    #raise Exception("wrong column")
                           # delete_dupes(indexes)
                            #indexes = delete_dupes_rand_order(indexes)
                            #size_res = len(result1)
                            try:
                                column_names = []
                                indexes_of_right_col = []
                                right_rows = []
                                columns = elem.get_table()
                                elem.get_col_name(column_names)
                                all_columns=[]
                                elem.show_col_where(all_columns, result1[size_res - 3], result1[size_res - 2],
                                                    result1[size_res - 1], right_rows)
                                print(f"this is {elem.get_name()} table")
                                beatiful_print(column_names, columns, all_columns, right_rows)
                            except:
                                print(exc_wrong)
                                continue
                        else:
                            """
                            indexes=[]
                            for k in range(size_res - 2):
                                for i in range(size_col_names):
                                    # if col_names[i]==result1[k]:
                                    indexes.append(i)
                                   # if col_names[i] == result1[size_res - 3]:
                                       # number1 = i + 1
                                    #if col_names[i] == result1[size_res - 1]:
                                      # number2 = i + 1
                            #result1.pop(size_res - 3)
                            #try:
                                #if number1 == 0:
                                    #raise Exception("wrong column")
                                #if number2 == 0:
                                    #raise Exception("wrong column")

                            delete_dupes(indexes)
                            indexes = delete_dupes_rand_order(indexes)
                            """
                            size_res = len(result1)
                            try:
                                column_names = []
                                #indexes_of_right_col = []
                                right_rows = []
                                columns = elem.get_table()
                                elem.get_col_name(column_names)
                                all_columns = []
                                elem.show_col_where_two_col( all_columns, result1[size_res-3], result1[size_res-1],
                                                            result1[size_res - 2], right_rows)
                                print(f"this is {elem.get_name()} table")
                                beatiful_print(column_names, columns, all_columns, right_rows)
                            except:
                                print(exc_wrong)
                                continue

                except:
                    print(exc_wrong)
                    continue
                EmpInput = ""
                number = 0
            else:
                name_of_insert = parsing.command_all(EmpInput)
                check_if_name_is_right = -1
                for elem in tables:
                    if elem.get_name() == name_of_insert:
                        check_if_name_is_right = 1
                        break
                if check_if_name_is_right == -1:
                    print(exc_name)
                    continue
                else:
                    try:
                        column_names = []
                        columns = []
                        indexes_of_right_col = []
                        right_rows = []
                        columns = elem.get_table()
                        elem.get_col_name(column_names)
                        elem.show(indexes_of_right_col, right_rows)
                        print(f"this is {elem.get_name()} table")
                        beatiful_print(column_names, columns, indexes_of_right_col, right_rows)
                    except:
                        print(exc_wrong)
        elif ("where" in EmpInput1):
            result1 = []
            name_of_insert = parsing.select_columns_where(EmpInput, result1)
            check_if_name_is_right = -1
            for elem in tables:
                if elem.get_name() == name_of_insert:
                    check_if_name_is_right = 1
                    break
            if check_if_name_is_right == -1:
                print(exc_name)
                continue
            else:
                if '"' in EmpInput1:
                    col_names = []
                    #indexes = []
                    elem.get_col_name(col_names)
                    size_col_names = len(col_names)
                    size_res = len(result1)
                    number = 0
                    try:
                        column_names = []
                        indexes_of_right_col = []
                        right_rows = []
                        right_arr_rows = []
                        columns = elem.get_table()
                        elem.get_col_name(column_names)
                        names_of_right_col=[]
                        parsing.assign( result1,names_of_right_col)
                        for i in range (3):
                            size_col= len(names_of_right_col)
                            names_of_right_col.pop(size_col-1)
                        indexes=elem.show_col_where(names_of_right_col, result1[size_res - 3], result1[size_res - 2],
                                            result1[size_res - 1], right_arr_rows)
                        print(f"this is {elem.get_name()} table")
                        beatiful_print(column_names, columns, indexes, right_arr_rows)
                    except:
                        print(exc_wrong)
                        continue
                else:
                    col_names = []
                    #indexes = []
                    elem.get_col_name(col_names)
                    size_col_names = len(col_names)
                    """
                    number1 = 0
                    number2 = 0
                    for k in range(size_res - 2):
                        for i in range(size_col_names):
                            if col_names[i] == result1[k]:
                                indexes.append(i)
                            if col_names[i] == result1[size_res - 3]:
                                number1 = i + 1
                            if col_names[i] == result1[size_res - 1]:
                                number2 = i + 1
                    result1.pop(size_res - 1)
                    indexes.pop(len(indexes) - 1)
                    
                        for i in range(len(indexes) - 1):
                            if indexes[i + 1] < indexes[i]:
                                raise Exception("wrong order")
                        if len(indexes) < (len(result1) - 3):
                            raise Exception("wrong")
                        if number1 == 0:
                            raise Exception("wrong column")
                        if number2 == 0:
                            raise Exception("wrong column")
                        """
                    size_res = len(result1)
                    try:
                        column_names = []
                        indexes_of_right_col = []
                        right_rows = []
                        columns = elem.get_table()
                        elem.get_col_name(column_names)
                        columns_to_display=[]
                        parsing.assign(result1,columns_to_display)
                        for i in range (3):
                            size_col= len(columns_to_display)
                            columns_to_display.pop(size_col-1)
                        indexes=elem.show_col_where_two_col(columns_to_display, result1[size_res - 3],result1[size_res - 1], result1[size_res - 2], right_rows)
                        print(f"this is {elem.get_name()} table")
                        beatiful_print(column_names, columns, indexes, right_rows)
                    except:
                        print(exc_wrong)
                        continue


            #EmpInput = ""
        else:
            result1 = []
            name_of_insert = parsing.select_columns(EmpInput, result1)
            check_if_name_is_right = -1
            for elem in tables:
                if elem.get_name() == name_of_insert:
                    name_of_insert = elem.get_name()
                    check_if_name_is_right = 1
                    break
            if check_if_name_is_right == -1:
                print(exc_name)
                continue
            else:
                arr = []
                elem.get_col_name(arr)
                size_arr = len(arr)
                size_res = len(result1)
                result1.pop(size_res-1)
                size_res = len(result1)
                #for k in range(size_res):
                    #for i in range(size_arr):
                        #if arr[i] == result1[k]:
                            #indexes.append(i)
                    #for i in range(len(indexes) - 1):
                        #if indexes[i + 1] < indexes[i]:
                            #raise Exception("wrong order")
                    #if len(indexes) != (len(result1)):
                        #raise Exception("wrong")
                try:
                    column_names = []
                    right_rows = []
                    columns = elem.get_table()
                    elem.get_col_name(column_names)
                    indexes= elem.show_col(result1, right_rows)
                    print(f"this is {elem.get_name()} table")
                    beatiful_print(column_names, columns, indexes, right_rows)
                except:
                    print(exc_name)
                    continue
    elif (first_command == "delete"):
        if ("where" in EmpInput1):
            result1 = []
            try:
                name_of_insert = parsing.command_all_where(EmpInput, result1)
                check_if_name_is_right = -1
                for elem in tables:
                    if elem.get_name() == name_of_insert:
                        check_if_name_is_right = 1
                        break
                if check_if_name_is_right == -1:
                    print(exc_name)
                    continue
                if '"' in EmpInput1:
                    """
                    col_names = []
                    indexes = []
                    elem.get_col_name(col_names)
                    size_col_names = len(col_names)
                    size_res = len(result1)
                    number = 0
                    for k in range(size_res - 2):
                        for i in range(size_col_names):
                            if col_names[i] == result1[size_res - 3]:
                                number = i + 1
                    result1.pop(size_res - 3)
                    """
                    size_res = len(result1)
                    try:
                        number_of_del_col=elem.delete_col_where(result1[size_res - 3], result1[size_res - 2],result1[size_res - 1] )
                        print(f"we deleted {number_of_del_col} rows from '{elem.get_name()}' table")
                    except:
                        print(exc_wrong)
                        continue
                    """except:
                                        print("smth went wrong")
                            except Exception:
                                print('wrong column')
                    except Exception:
                        print('wrong name')
                        """
                else:
                    col_names = []
                    indexes = []
                    elem.get_col_name(col_names)
                    size_col_names = len(col_names)
                    size_res = len(result1)
                    """
                    number1 = 0
                    number2 = 0
                    for k in range(size_res - 2):
                        for i in range(size_col_names):
                            if col_names[i] == result1[size_res - 3]:
                                number1 = i + 1
                            if col_names[i] == result1[size_res - 1]:
                                number2 = i + 1
                    result1.pop(size_res - 3)
                    """

                    """
                        if number1 == 0:
                            raise Exception("wrong column")
                        if number2 == 0:
                            raise Exception("wrong column")
                            """
                    try:
                        size_res = len(result1)
                        number_of_del_col=elem.delete_col_where_two_col(result1[size_res-3], result1[size_res-1], result1[size_res - 2])
                        print(f"we deleted {number_of_del_col} rows from '{elem.get_name()}' table")
                    except:
                        print(exc_wrong)
                        continue
            except:
                print(exc_parsing)
                continue
        else:
            result1 = []
            name_of_insert = parsing.command_all(EmpInput)
            check_if_name_is_right = -1
            for elem in tables:
                if elem.get_name() == name_of_insert:
                    name_of_insert = elem.get_name()
                    check_if_name_is_right = 1
                    break

            if check_if_name_is_right == -1:
                print(exc_name)
                continue
            else:
                try:
                    elem.delete_all()
                    print(f"we deleted everything from {elem.get_name()} table")
                except:
                    print(exc_wrong)

    else:
        print('please insert supported function')
        continue


