#CLI todo app 

#imports
import pickle
import os

#globals
Done = True
path = ''
n_todo = '\\todo.bin'
n_done = '\\done.bin'

#functions
def task():
    f = open(path+'\\todo.bin', 'ab+')
    t_name = input('Enter task name: ')
    t_des = input('Enter task details: ')
    t = {'name' : t_name, 'des': t_des}
    pickle.dump(t , f)
    f.close()
    f = open(path+n_done, 'wb+')
    f.close()

def show(filename):
    f = open(path+filename, 'rb+')
    while True:
        try:
            o = pickle.load(f)
            tname = o['name']
            tdes = o['des']
            print(tname,'   ',  tdes)
        except EOFError:
            break
    f.close()

def clearf():
    os.remove(path+n_todo)
    os.remove(path+n_done)
    o = open(path+n_todo, 'w+')
    o.close()
    o = open(path+n_done, 'w+')
    o.close()

def done(tname):
    f1 = open(path+n_todo, 'rb+')
    f2 = open(path+'\\todo1.bin', 'wb+')
    f3 = open(path+n_done, 'ab+')
    while True:
        try:
            o = pickle.load(f1)
            if o['name'] != tname:
                pickle.dump(o, f2)
            elif o['name'] == tname:
                pickle.dump(o, f3)
        except EOFError:
            break
    f1.close()
    f2.close()
    f3.close()
    os.remove(path+n_todo)
    os.rename(path+'\\todo1.bin', path+n_todo)

def helper():
    print('''
    Type:
    1) task to create new task
    2) show to show previous tasks
    3) done to mark as done
    4) clear to clear all tasks
    5) bye to exit
    ''')

'''def sort(o):
    o = str(o)
    o = o.split()
    
    ban = "'}"
    tname = ''
    tdes = ''
    for i in o[1]:
        if i not in ban:
            tname += i
    for i in o[3]:
        if i not in ban:
            tdes += i
    print('Name: '+ tname + '  Description: '+ tdes)
''' 

def check():
    if larg[0] == 'task':
        task()

    elif larg[0] == 'show':
        show(n_todo)
        print('Done tasks:')
        show(n_done)
    
    elif larg[0] == 'bye':
        print('Bye!')
        global Done
        Done = False

    elif larg[0] == 'clear':
        clearf()
    
    elif larg[0] == 'help':
        helper()

    elif larg[0] == 'done':
        tn = input('Enter task to be marked as done: ')
        done(tn)

    else:
        print('type help')



#__main__
if path == '':
    path = input('Enter path to save todo file: ')

while Done:
    arg = input('$ ')
    arg = arg.lower()
    larg = arg.split()
    check()
