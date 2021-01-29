### mongo的基本增删改查
https://docs.mongodb.com/manual/tutorial/getting-started/
1. #### 查
```python
mycoll = db['test']['coll_name']
#query
record = mycoll.find_one(query,field)
#find_one 返回一个文档记录
cursor = mycoll.find(query,field)
#find()返回游标Cursor对象
```
*  field用来决定把哪些字段投影(projection)到结果中
mongo projection投影的使用，除了_id字段，不可以混合includsion和
exclusion，比如对于collection包含下面的文档
```python
{
   "_id": ObjectId("53d1fd30bdcf7d52c0d217de"),
   "name": "bill",
   "birthdate": ISODate("2014-07-80T00:00:00.000Z"),
   "created": ISODate("2014-07-25T06:44:38.641Z")
}
```

尝试在结果中把name和birthdate显示出来
```python
db.collection.find({},{'name':1,'birthdate':1,'_id':0})
#work same as
db.collection.find({},{'created':0,'_id':0})
#the following is wrong usage example,the fixed use of inclusion and exclusion
db.collection.find({},{'name':1,'created':0,'_id':0})
```
第三种方法会抛出异常
* 注意Cursor对象可以用下标来获得具体文档
```
for ele in cursor:
   #do
```
```python
cursor.next()获取下一个文档
list(cursor)#转换为列表
cursor.sort([('name',1),('age',-1)])
```
2. #### 增
```python
mycoll.insert_one()
insert_many()
insert()
```
3. #### 改
```python
update_one(query,op)
update_many(query,op)
```
4. #### 删
```python
delete_one(query)
delete_many(query)
remove(query)
```
5. #### 复合
```python
find_one_and_update(query，op)
find_one_and_delete(query)
```
### mongo一些其他操作
1. 查询
   除了精准匹配文档外，还有一些函数的使用，子字段的判断，数组的索引，数组元素的判断,字段的正则匹配
```python
find({'user.name','username0'})
find({'username':{'$exists':True}})
find({'price':{'$gt':12.0}})
#$gt,$gte,$e,$ne,$lt,$lte
find({'scores':{'$size':5}})#数组大小为5
find({'scores.1':100})#
#$in,$nin,$all
```
2. 数组元素
* ##### 数组中对象的匹配和更改
```python
    '$elemMatch'#query
  'todolist.$.title'#只修改第一个匹配
```
* 添加一个或多个
```python
db.studentscore.update({},{'$push':{score:{'physics':100}}})
db.studentscore.update({},{'$push':{score:{'$each':[{'physics':100},{'math':100}]}}})
```

```python
{
   "_id" : 5,
   "quizzes" : [
      { "wk": 1, "score" : 10 },
      { "wk": 2, "score" : 8 },
      { "wk": 3, "score" : 5 },
      { "wk": 4, "score" : 6 }
   ]
}
db.students.update(
   { _id: 5 },
   {
     '$push': {
       quizzes: {
          '$each': [ { wk: 5, score: 8 }, { wk: 6, score: 7 }, { wk: 7, score: 6 } ],
          '$sort': { score: -1 },
          '$slice': 3
       }
     }
   }
)
```
pop
```python
update({},{'$pop':{'score':1}})#last
update({},{'$pop':{'score':-1}})#first
```
pull
```python
update({},{'$pull':{'fruits:',{'$in':['apples','oranges']}}})
#$gt,$gte,$e,$ne,$lt,$lte
# ↓数组内嵌文档
update({},{'$pull':{'todolist':{'tid':123456,'title':'hello'}}})
#↑删除文档数组中符合要求的数组项
#↓数组内嵌数组
{
   _id: 1,
   results: [
      { item: "A", score: 5, answers: [ { q: 1, a: 4 }, { q: 2, a: 6 } ] },
      { item: "B", score: 8, answers: [ { q: 1, a: 8 }, { q: 2, a: 9 } ] }
   ]
}
{
   _id: 2,
   results: [
      { item: "C", score: 8, answers: [ { q: 1, a: 8 }, { q: 2, a: 7 } ] },
      { item: "B", score: 4, answers: [ { q: 1, a: 0 }, { q: 2, a: 8 } ] }
   ]
}
db.survey.update(
  { },
  { '$pull': { 'results': { 'answers': { '$elemMatch': { 'q': 2, 'a': { '$gte': 8 } } } } } },
  { 'multi': True }
)
```
addToSet
和push不同在于，添加数组内不存在的值
```python
update({},
{ '$addToSet': { 'tags': { '$each': [ "camera", "electronics", "accessories" ] } } }
)
```
