import os
def save_to_file(trainer, mark):
    with open('list.txt', 'a') as the_file:
        the_file.write(trainer+' '+str(mark)+'\n')
    the_file.close()
def add_to_dict(trainer,mark,dict):
    dict[trainer]=mark
    return dict
def get_dict():
    dict={}
    f=open('list.txt', 'r')
    if os.path.getsize('list.txt')>0:
        for x in f:
            x = x.replace('\n', '')
            line=x.split()
            dict[line[0]]=line[1]
    return dict

