from pymongo import MongoClient
import json
import uuid
import time
conn = MongoClient('localhost',27017)
db = conn["test"]
agendas = db['agenda']

def query_todos(username):
    return json.dumps(agendas.find_one({'username':username})['todolist'])

def delete_todos(username,tid=None):
    if(agendas.count_documents({'username':username})==0):
        return False
    if tid==None:
        agendas.update_one({'username':username},{'$set':{'todolist':None}})
        return True
    #delete specified todo
    todolist=agendas.find_one({'username':username})['todolist']
    for todo in todolist:
        if(todo['tid']==tid):
            todolist.remove(todo)
            agendas.update_one({'username':username},{'$set':{'todolist':todolist}})
            return True
    return False
    # if (agendas.count_documents({'$and':[{'username':username},]}))
def add_todo(username,title=None,date_time=None,todo=None):
    print('todo')
    if agendas.count_documents({'username':username})==0:#没有用户
        return False
    record=agendas.find_one({'username':username})
    print("record:\t%s"%record)
    todolist=record['todolist']
    if todolist==None:
        todolist=[]
    uid = str(uuid.uuid1())
    todo_to_add={
        'tid':uid,
        'title':title,
        'date_time':date_time,
        'todo':todo
    }
    
    todolist.append(todo_to_add)
    agendas.update_one({'username':username},{'$set':{'todolist':todolist}})
    return True
def update_todo(username,tid,title=None,date_time=None,todo=None):
    #username doesnot match
    if agendas.count_documents({'username':username})==0:
        return False
    record = agendas.find_one({'username':username})
    todolist=record['todolist']
    for tdi in todolist:
        if tdi['tid']==tid:
            tdi['title']=title
            tdi['date_time']=date_time
            tdi['todo']=todo
            agendas.update_one({'username':username},{'$set':{'todolist':todolist}})
            return True
    return False

if __name__=="__main__":
    date_time=time.asctime(time.localtime(time.time()))
    update_todo(username='username0',tid='15096ae1-6086-11eb-958a-347df614dfba',title='modified_tile',date_time=date_time,todo='today i want to do something different')

    # for i in range(10):
    #     for j in range(3):
    #         username="username%d"%i
    #         title="username%d"%j
    #         date_time=time.asctime(time.localtime(time.time()))
    #         todo="something to do %d"%j
    #         add_todo(username=username,title=title,date_time=date_time,todo=todo)