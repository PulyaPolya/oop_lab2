def get_full_name(name, last, second = ''):
    if second:
        full = name + ' ' + second + ' ' + last
    else:
        full = name + ' ' + last
    return full.title()