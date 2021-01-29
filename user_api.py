from pymongo import MongoClient,CursorType
import json
import string
conn = MongoClient('localhost',27017)
db = conn["test"]
agendas = db['agenda']

def query_user():
    cursor=agendas.find({},{'username':1})
    
    res=[]
    for a in cursor:
        res.append(a['username'])
    return json.dumps(res)

def add_user(username,password):
    cursor=agendas.find({'username':username})
    count=agendas.count_documents({'username':username})
    if count > 0 or username==None or password== None\
                or len(username.strip())==0 or len(password.strip())==0:
        return False
    res=agendas.insert_one({'username':username,'password':password,'todolist':[]})
    return True
def delete_user(username):
    count=agendas.count_documents({'username':username})
    if count == 0:
        return False
    agendas.delete_one({'username':username})
    return True

if __name__=='__main__':
    for i in range(10):
        username="username%d"%i
        password="password%d"%i
        add_user(username,password)