import os
import tinydb

# 检查 data 目录是否存在, 不存在则创建
if not os.path.exists('data'):
  os.mkdir('data')


# 初始化数据库
cp      = tinydb.TinyDB('./data/cp.json')
user    = tinydb.TinyDB('./data/user.json')
weibo   = tinydb.TinyDB('./data/weibo.json')
chaohua = tinydb.TinyDB('./data/chaohua.json')
comment = tinydb.TinyDB('./data/comment.json')
where   = tinydb.where

#db.insert({'name': '张三', 'age': 18})
#db.insert({'name': '李四', 'age': 19})
#db.all()
#db.search(tinydb.where('age') == 25)
#db.search(tinydb.where('age') > 25)
#db.update({'age': 29}, tinydb.where('age') == 25)
#db.all()
#db.remove(tinydb.where('age') == 25)
#db.all()
#db.close()
#一次增加多条的方法：
#table.insert_multiple([{'name': 'n1', 'age': 1},{'name': 'n2', 'age': 2},{'name': 'n3', 'age': 4}])
#6. 看一个表当中的key 是否存在
#from tinydb.queries import Query, where
#table.contains(where('name'))
#True


# 查询指定 cp 组的成员



# 查询指定两个用户之间的所有互动
def get_interaction(user1, user2):
  comment_list = comment.search(tinydb.where('user_id') == user1)
