import csv
import re

# 从 cp.csv 载入cp/group 到数组
def load_cp():
  cp = []
  with open('cp.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
      cp.append(row)
  return cp

# 输入作者主页链接, 正则获取 'https://weibo.com/' 与 '?' 之间的作者ID
def get_author_id(url):
  author_id = re.findall(r'(?<=https://weibo.com/)\w+', url)
  if author_id:
    author_id = author_id[0]
  else:
    author_id = ''
  return author_id

# 从 csv 文件中获取所有cp组的信息
def load_group():
  group = {}
  with open('cp.csv', 'r') as f:
    reader = csv.reader(f)
    reader.__next__()
    for row in reader:
      data = list(set(list(filter(None, row[2].split(',')))))
      for group_name in data:
        if group_name not in group:
          group[group_name] = {'name': group_name, 'list': []}
        if row[0] not in group[group_name]['list']:
          group[group_name]['list'].append(row[0])
  return group

# 从 csv 文件中获取所有成员的信息
def load_user():
  user = {}
  with open('cp.csv', 'r') as f:
    reader = csv.reader(f)
    reader.__next__()
    for row in reader:
      user[row[0]] = {'url': row[1], 'group': row[2].split(',')}
  return user


#print(load_group())
#print(load_user())

# https://m.weibo.cn/api/container/getIndex?extparam=%E6%9C%B1%E6%B4%81%E9%9D%99&containerid=10080819db7645a97752ca3604221911c638f6_-_live&luicode=10000011&lfid=100103type%3D98%26q%3D%E6%9C%B1%E6%B4%81%E9%9D%99%26t%3D


# 检查所有成员是否在线
def check_online(user):
  online = {}
  for name in user:
    url = user[name]['url']
    author_id = get_author_id(url)
    if author_id:
      online[name] = {'url': url, 'group': user[name]['group'], 'author_id': author_id}
  return online

print(check_online(load_user()))

