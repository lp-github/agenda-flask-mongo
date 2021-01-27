# 设计部署后端api
# 需求
1. 用户日程信息的增删改查
2. 存储结构
{
    username:'***'
    password:'***'
    todolist:[
        {
            tid:'***'
            title:'***'
            date_time:date,
            todo:''
        },
        ...
    ]
} ,
        ...  

# API设计
## 用户相关
1. "/"  [GET]
   无参数
   返回hello world
2. "/user/query" [GET]
   无参数
   返回所有用户的username
3. "/user/add" [POST]
   参数：username，password
   返回success或者failed
4. "/user/delete" [POST]
   参数 username
   返回成功失败
## 议程相关
1. "/todos/query" [GET]
   参数username
   返回指定用户名字的todolist
2. "/todos/delete" [POST]
   参数username(，tid)
   删除指定用户指定tid的todo，不传title则删除todolist数组所有todo
   返回success或者failed
3. "/todos/add" [POST]
   参数username(，title,date_time,todo)
   添加todo到数组
   返回success或者failed
4. "/todos/update" [POST]
   参数username,tid(,title,date_time,todo)
   修改指定tid的todo项