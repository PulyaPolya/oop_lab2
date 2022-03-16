from settings import Settings
import collections


class Win_comb():
    def __init__(self):
        self.comb1 = [1,10, 11, 12, 13]
        self.comb2 =  [1, 1, 1, 1]
        self.comb3 = [1, 1, 1, 13, 13]
        self.comb_settings = Settings()
    def check_comb(self, array, diag = 0):
        list_4 = [item for item, count in collections.Counter(array).items() if count == 4]
        list_3 = [item for item, count in collections.Counter(array).items() if count == 3]
        list_2 = [item for item, count in collections.Counter(array).items() if count == 2]
        if len(list_2) == 2:
            if diag == 0:
                return 20 #'2+2'
            else:
                return 30
        elif  len(list_3) > 0:
            if len(list_2) > 0:
                if diag == 0:
                    return 80 #'3+2'
                else:
                    return 90
            else:
                if diag == 0:
                    return 40 #'3'
                else:
                    return 50
        elif len(list_2) == 1:
            if diag == 0:
                return 10 #'2'
            else:
                return 20
        elif len(list_4) > 0:
            if array[0] == 1 or array[1] ==1: # 1111
                if diag == 0:
                    return 200
                else:
                    return 210
            else:
                if diag == 0: # 4
                    return 160
                else:
                    return 170
        else:
            return 0
    def check_order(self, array, diag = 0):
        order = 0
        array.sort()
        for i in range(1, len(array)):
            if array[i] == array[i - 1] + 1:
                continue
            else:
                order = 1
                break
        if order == 0:
            if diag == 0:
                return 50
            else:
                return 60
        else:
            return 0

combination = Win_comb()

def check_arr_in_arr(comb, arr):
   arr.sort()
   copy = arr.copy()
   copy.pop(-1)
   if comb == copy:
       return 'yes'
   else:
       return 'no'

def count_row(row,  diag = 0):
    result = 0
    if diag == 1:
        row.sort()
        row_sorted = row.copy()
    else:
        row_sorted = row.copy()
    if row_sorted == combination.comb1:
        if diag == 0:
            result = 150
        else:
            result = 160
    elif check_arr_in_arr(combination.comb2, row_sorted) == 'yes':
        if diag == 0:
            result = 200
        else:
            result = 210
    elif row_sorted == combination.comb3:
        if diag == 0:
            result = 100
        else:
            result = 110

    else:
        result = 0
    return max(combination.check_comb(row),combination.check_order(row, diag), result)


