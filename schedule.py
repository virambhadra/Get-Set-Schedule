from os import scandir as sdir
import time



class scheduler:
    cards = []
    def __init__(self):
        name = input('Enter your username: ')
        with open('users/users.csv','r') as users:
            data = users.readlines()
            print(data)
        if name in data:
            scheduler.show_card(name)
        else:
            scheduler.start(name)
    

    def start(name):
        prof = 'Student' if input('Select one : 1.Student 2.Professor : ')=='1' else 'Professor'
        stream = 'Engineering' if input('Stream: 1.Engineering 2.Medical : ')=='1' else 'Medical'
        prof_card = prof+stream
        print(prof_card)
        if prof_card+'.csv' in scheduler.dir_items():
            scheduler.show_prof_card(prof_card, name)
        else:
            data = scheduler.add_card(prof_card, name)
            scheduler.add_prof_card(prof_card, data)


    def show_prof_card(prof_card, name):    
        with open(prof_card+'.csv','r') as case:
            case = case.readlines()
            for line in case:
                line_sep = line.split(';')
                print(*line_sep)
            scheduler.write_card(name, case)


    def add_prof_card(prof_card, data):
        with open(prof_card+'.csv','w') as case:
            case.writelines(data)

    def dir_items():
        return [_.name for _ in list(sdir()) if _.name.endswith('.csv')]


    def add_card(prof_card, name):
        start = int(input('Enter Start-time of Schedule: '))
        end = int(input('Enter End-time of Schedule: '))
        interval = int(input('interval in number of hrs '))
        base = []
        for i in range(start,end,interval):
            instance = scheduler.time_formatter(str(i)+':00')
            print(instance)
            temp = input("what would tou like to do at"+instance+'? ')
            base.append(''.join([instance,';',temp])+'\n')
            print(base)
        scheduler.write_card(name, base)
        scheduler.show_card(name)
        scheduler.add_user(name)
        return base
        


    def time_formatter(timevalue_24hour):
        t = time.strptime(timevalue_24hour, "%H:%M")
        timevalue_12hour = time.strftime( "%I:%M %p", t )
        return timevalue_12hour
    
    
    def show_card(name):
        for line in scheduler.read_card(name):
            line_sep = line.split(';')
            print(*line_sep)
       # print(*scheduler.read_card(name))


    def read_card(name):
        with open('users/'+name+'.csv','r') as temp:
             return [line for line in temp.readlines()]
    

    def write_card(name, data):
        with open('users/'+name+'.csv','w') as newfile:
            newfile.writelines(data)
        scheduler.add_user(name)
    

    def add_user(name):
        with open('users/users.csv','a') as users:
            users.writelines(name+'\n')
    

    def modify():
        name = input('Enter username: ')
        card = scheduler.read_card(name)
        print(*enumerate(card,1))
        ind = int(input('Enter index you want to edit: '))
        data = input('What do you want to replace instead? ')
        card[ind-1] = card[ind-1].split(';')[0]+';'+data+'\n'
        scheduler.write_card(name, card)
        scheduler.show_card(name)
