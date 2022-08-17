import tinydb

'''
cp      中存储了 cp 的 id, 和 list(多个 user 的 id), 结构是 {'id': 'xxx', list: [id1, id2, id3]}
user    中存储了用户 id 和 头像链接, 结构是 {'id': 'xxx', 'avatar': 'xxx'}
weibo   中存储了发布用户 id 和 微博内容, 结构是 {'id': 'xxx', 'content': 'xxx'}
chaohua 中存储了发布用户 id 和 超话内容, 结构是 {'id': 'xxx', 'content': 'xxx'}
comment 中存储了发布用户 id 和 评论内容 和 目标微博 id, 结构是 {'id': 'xxx', 'content': 'xxx', 'weibo_id': 'xxx'}
'''

cp      = tinydb.TinyDB('cp.json')
user    = tinydb.TinyDB('user.json')
weibo   = tinydb.TinyDB('weibo.json')
chaohua = tinydb.TinyDB('chaohua.json')
comment = tinydb.TinyDB('comment.json')



#db.insert({'name': '张三', 'age': 18})
#db.insert({'name': '李四', 'age': 19})
#
#db.all()
#db.search(tinydb.where('age') == 25)
#db.search(tinydb.where('age') > 25)
#
#db.update({'age': 29}, tinydb.where('age') == 25)
#db.all()
#
#db.remove(tinydb.where('age') == 25)
#
#db.all()
#db.close()


# 查询指定 cp 组的成员



# 查询指定两个用户之间的所有互动
def get_interaction(user1, user2):
  comment_list = comment.search(tinydb.where('user_id') == user1)



'''
只存储目标展示数据:
1. 两个或多个用户之间的互动记录到指定组
2. 因此先存储指定 cp 组
3. 当采集到对话数据时, 取对话者两方 id
4. 所有包含对话者两方 id 的 cp 组, 都记录这次会话事件的微博或超话id(两个comment是否相同? 记录上级id?)
5. 因此

在跑 comment 时, 由于随时可能增加新的, 因而每次只从微博检查回复数量
如果每10分钟跑一次, 扫描范围可能近万数
因此, 只对热度话题进行高频率检查(动态频率)
'''
