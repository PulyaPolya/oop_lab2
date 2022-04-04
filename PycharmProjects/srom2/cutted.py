if first_command == "select" or first_command == "select*":
    # if name_select_all:
    if ("*" in EmpInput1):
        if ("where" in EmpInput1):

            try:
                # name_of_insert = parsing.command_all_where(EmpInput, result1)
                check_if_name_is_right = -1
                for elem in tables:
                    if elem.get_name() == name_all:
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
                    """
                    if '"' in EmpInput1:
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
                    """

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
                        # indexes_of_right_col = []
                        right_rows = []
                        columns = elem.get_table()
                        elem.get_col_name(column_names)
                        all_columns = []
                        elem.show_col_where_two_col(all_columns, result1[size_res - 3], result1[size_res - 1],
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
            # else:
            """
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
            """
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
                # indexes = []
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
                    names_of_right_col = []
                    parsing.assign(result1, names_of_right_col)
                    for i in range(3):
                        size_col = len(names_of_right_col)
                        names_of_right_col.pop(size_col - 1)
                    indexes = elem.show_col_where(names_of_right_col, result1[size_res - 3], result1[size_res - 2],
                                                  result1[size_res - 1], right_arr_rows)
                    print(f"this is {elem.get_name()} table")
                    beatiful_print(column_names, columns, indexes, right_arr_rows)
                except:
                    print(exc_wrong)
                    continue
            else:
                col_names = []
                # indexes = []
                elem.get_col_name(col_names)
                size_col_names = len(col_names)
                size_res = len(result1)
                try:
                    column_names = []
                    indexes_of_right_col = []
                    right_rows = []
                    columns = elem.get_table()
                    elem.get_col_name(column_names)
                    columns_to_display = []
                    parsing.assign(result1, columns_to_display)
                    for i in range(3):
                        size_col = len(columns_to_display)
                        columns_to_display.pop(size_col - 1)
                    indexes = elem.show_col_where_two_col(columns_to_display, result1[size_res - 3],
                                                          result1[size_res - 1], result1[size_res - 2], right_rows)
                    print(f"this is {elem.get_name()} table")
                    beatiful_print(column_names, columns, indexes, right_rows)
                except:
                    print(exc_wrong)
                    continue

        # EmpInput = ""

if (first_command == "delete"):
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
            """
            if '"' in EmpInput1:
                size_res = len(result1)
                try:
                    number_of_del_col=elem.delete_col_where(result1[size_res - 3], result1[size_res - 2],result1[size_res - 1] )
                    print(f"we deleted {number_of_del_col} rows from '{elem.get_name()}' table")
                except:
                    print(exc_wrong)
                    continue
            """

            col_names = []
            indexes = []
            elem.get_col_name(col_names)
            size_col_names = len(col_names)
            size_res = len(result1)

            try:
                size_res = len(result1)
                number_of_del_col = elem.delete_col_where_two_col(result1[size_res - 3], result1[size_res - 1],
                                                                  result1[size_res - 2])
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