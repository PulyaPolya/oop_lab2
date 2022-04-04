from enum import Enum
import class_coach
import ini_file
class State(Enum):
    wait_for_tr=1
    wait_for_mark=2
    nothing=0
    wait_for_change=3
    wait_for_sport=4
class Messanger:
    def __init__(self):
        self.state=State.nothing
        self.coaches=ini_file.fill_arr()
        self.current_coach_name = ''
        self.list_of_sports=ini_file.get_sports()
        self.command=''
    def get_trainers(self):
        arr=[]
        for coach in self.coaches:
            arr.append(coach.name)
        return arr
    def get_coach(self,name):
        i=0
        for tr in self.coaches:
            if tr.name==name:
                #self.coaches.append(tr)
                return tr
            else:
                i+=1
        if i==len(self.coaches):
            tr=class_coach.Coach(name)
            self.coaches.append(tr)
            return tr
    def get_coaches_name(self):
        arr=[]
        for coach in self.coaches:
            arr.append(coach.name)
        return arr