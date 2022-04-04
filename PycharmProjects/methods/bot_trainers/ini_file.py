import configparser
import class_coach
from configparser import ConfigParser
def add_coach(tr, mark,sport,instagram):
    config = ConfigParser()
    config.read('example.ini')
    config[tr]={
        'mark':mark,
        'sport':sport,
        'instagram': instagram
    }
    with open('example.ini', 'w') as configfile:
        config.write(configfile)
def add_sport(sports):
    config = ConfigParser()
    config.read('example.ini')
    for sport in sports:
        config['sport'][sport]=str(sports.index(sport))
    with open('example.ini', 'w') as configfile:
        config.write(configfile)
def update_info(coaches, sports):
    for coach in coaches:
        add_coach(coach.name, str(coach.mark), coach.sport,coach.instagram)
    add_sport(sports)
def fill_arr():
    arr=[]
    config = ConfigParser()
    config.read('example.ini')
    for coach_name in config.sections():
        if coach_name!='sport':
            coach = class_coach.Coach(coach_name)
            coach.mark = config.get(coach_name, 'mark')
            coach.sport=config.get(coach_name, 'sport')
            #coach.instagram=config.get(coach_name, 'instagram')
            arr.append(coach)
    return arr
def get_sports():
    config = ConfigParser()
    config.read('example.ini')
    for section in config.sections():
        if section=='sport':
         return config.options(section)

