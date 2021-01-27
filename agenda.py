from flask import Flask,request
import user_api
import todo_api

app=Flask(__name__)
@app.route("/")
def home():
    return "hello world"

@app.route('/user/query')
def on_query_user():
    return user_api.query_user()

@app.route('/user/add',methods=['POST'])
def on_add_user():
    username = request.args.get('username')
    password = request.args.get('password')
    if(user_api.add_user(username,password)):
        return  'success'
    else:
        return 'failed'
@app.route('/user/delete',methods=['POST'])
def on_delete_user():
    username=request.args.get('username')
    if user_api.delete_user(username):
        return  'success'
    else:
        return 'failed'
#todos api    
@app.route('/todos/query')
def on_todos_query():
    username=request.args.get('username')
    return todo_api.query_todos(username)
@app.route('/todos/delete',methods=['POST'])
def on_todos_delete():
    username=request.args.get('username')
    tid=request.args.get('tid')
    if todo_api.delete_todos(username,tid):
        return  'success'
    else:
        return 'failed'
@app.route('/todos/add',methods=['POST'])
def on_todos_add():
    username=request.args.get('username')
    title=request.args.get('title')
    date_time=request.args.get('date_time')
    todo=request.args.get('todo')
    if todo_api.add_todo(username,title,date_time,todo):
        return  'success'
    else:
        return 'failed'
@app.route('/todos/update',methods=['POST'])
def on_todos_update():
    username=request.args.get('username')
    tid=request.args.get('tid')
    title=request.args.get('title')
    date_time=request.args.get('date_time')
    todo=request.args.get('todo')
    if todo_api.update_todo(username,tid,title,date_time,todo):
        return  'success'
    else:
        return 'failed'
if __name__=='__main__':
    app.run(debug=True)