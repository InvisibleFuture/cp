import re
import requests
import time
import store

# 将 cookies 字符串转换为 cookie dict 格式 key: value 对
def get_cookies(cookies_str):
  cookies_dict = {}
  for cookie in cookies_str.split(';'):
    key, value = cookie.split('=', 1)
    cookies_dict[key] = value
  return cookies_dict


# 从文本文件 'author_urls.txt' 中读取作者主页链接
def get_author_urls():
  author_urls = []
  with open('author_urls.txt', 'r') as f:
    for line in f:
      author_urls.append(line.strip())
  return author_urls


# 输入作者主页链接, 正则获取 'https://weibo.com/' 与 '?' 之间的作者ID
def get_author_id(url):
  author_id = re.findall(r'(?<=https://weibo.com/u/)\w+', url)
  if author_id:
    author_id = author_id[0]
  else:
    author_id = ''
  return author_id


# 将作者链接全部转换为作者ID, 排除掉空字符串和去除重复项
def get_author_ids(author_urls):
  author_ids = []
  for url in author_urls:
    author_id = get_author_id(url)
    if author_id:
      author_ids.append(author_id)
  author_ids = list(set(author_ids))
  return author_ids


# 读取所有作者的微博数据
def get_weibo_data(author_ids):
  weibo_data = []
  for author_id in author_ids:
    '''
    循环读取每页
    如果list长度为0, 则终止循环
    如果读取页数超过1000, 则终止循环
    如果检测到储存的最大id, 则终止循环
    '''
    page = 1
    while True:
      if page > 10:
        break
      url = 'https://weibo.com/ajax/statuses/mymblog?uid={}&page={}&feature=0'.format(author_id, page)
      list = client.get(url).json()['data']['list']
      if len(list) == 0:
        break
      #if weibo_data[-1]['max_id'] == 0:
      #  break
      print(len(list))
      weibo_data.append(list)
      page += 1

      # 顺便更新作者数据
      if page == 2 and len(list) > 0:
        user = list[0]['user']
        up = store.user.update({'id': user['id']}, store.where('id') == user['id'])
        if len(up) == 0: store.user.insert({'id': user['id']})
        print(len(up), user['id'], '更新作者数据', user['screen_name'])
  return weibo_data

def get_weibo_count():
  return store.weibo.count(store.where('id') > 0)

def get_user_count():
  return store.user.count(store.where('id') > 0)

# 获取博主数据存入数据库
def update_weibo():
  author_urls = get_author_urls()
  author_ids  = get_author_ids(author_urls)
  weibo_data  = get_weibo_data(author_ids)
  for list in weibo_data:
    for item in list:
      up = store.weibo.update(item, store.where('id') == item['id'])
      if len(up) == 0: store.weibo.insert(item)
      print(len(up), item['id'], item['text_raw'][:20].replace('\n', ''))

# 每 10 分钟检查一次
def updateWeibo():
  while True:
    time.sleep(600)
    update_weibo()


client   = requests.Session()
cookies_str = 'XSRF-TOKEN=sP60RXs1v1pRYDA7EuzECr-z; SUB=_2AkMVqOWif8NxqwFRmP4dyWnlb41_zArEieKj9BR5JRMxHRl-yj9jqkkvtRB6PijLTA6mh3oOYPk5ecnTHoNjs9A_cIsE; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WFP4Ky4rDy0gYKnU7337YVc; WBPSESS=g2Va6ZLXRYSCdsm5QPfA3B-VCn9UI6TaXR4H76DcGXBsKfcPofJAATW42Fc3NHurNHt226eI3iw4N5nGnGi_Oa-Tdtx8_hsucuYTAC8wkeFh4AWH8vCvnDHtrjg2yrJh'
client.cookies.update(get_cookies(cookies_str))

# 获取博主数据存入数据库
#author_urls = weibo.get_author_urls()
#author_ids  = weibo.get_author_ids(author_urls)
#weibo_data  = weibo.get_weibo_data(author_ids)
#for list in weibo_data:
#  #print(json.dumps(list, ensure_ascii=False, indent=2))
#  for item in list:
#    up = store.weibo.update(item, store.where('id') == item['id'])
#    if len(up) == 0: store.weibo.insert(item)
#    print(len(up), item['id'], item['text_raw'][:20].replace('\n', ''))
#all = store.weibo.all()
#print(json.dumps(all, ensure_ascii=False, indent=2))
