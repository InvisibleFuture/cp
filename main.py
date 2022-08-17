#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
import requests

# 初始化 client 对象
client   = requests.Session()

# cookies 字符串
cookies_str = 'XSRF-TOKEN=sP60RXs1v1pRYDA7EuzECr-z; SUB=_2AkMVqOWif8NxqwFRmP4dyWnlb41_zArEieKj9BR5JRMxHRl-yj9jqkkvtRB6PijLTA6mh3oOYPk5ecnTHoNjs9A_cIsE; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WFP4Ky4rDy0gYKnU7337YVc; WBPSESS=g2Va6ZLXRYSCdsm5QPfA3B-VCn9UI6TaXR4H76DcGXBsKfcPofJAATW42Fc3NHurNHt226eI3iw4N5nGnGi_Oa-Tdtx8_hsucuYTAC8wkeFh4AWH8vCvnDHtrjg2yrJh'

# 将 cookies 字符串转换为 cookie dict 格式 key: value 对
def get_cookies(cookies_str):
  cookies_dict = {}
  for cookie in cookies_str.split(';'):
    key, value = cookie.split('=', 1)
    cookies_dict[key] = value
  return cookies_dict

client.cookies.update(get_cookies(cookies_str))
print('------------------------------------------------------')

# 从文本文件 'author_urls.txt' 中读取作者主页链接
def get_author_urls():
  author_urls = []
  with open('author_urls.txt', 'r') as f:
    for line in f:
      author_urls.append(line.strip())
  return author_urls

# 输入作者主页链接, 正则获取 'https://weibo.com/' 与 '?' 之间的作者ID
def get_author_id(url):
  author_id = re.findall(r'(?<=https://weibo.com/)\w+', url)
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
  return weibo_data

# TODO: 最终将数据追加写入文件 'data.txt' 中

# 运行程序
if __name__ == '__main__':
  author_urls = get_author_urls()
  print(author_urls)
  author_ids  = get_author_ids(author_urls)
  print(author_ids)
  weibo_data  = get_weibo_data(author_ids)
  for list in weibo_data:
    #print(json.dumps(list, ensure_ascii=False, indent=2))
    for item in list:
      print('------------------------------------------------------')
      print(item['text_raw'])

# 预测指定主题在当前时间的热度指数
def predict_hot_index(topic):
  '''
  发布时间 * (转发数量 + 评论数量 + 点赞数量 + 收藏数量 + 分享数量 + 关注数量 + 粉丝数量 + 微博数量 + 关注数量)
  间隔时间 = (最后回复时间 - 发布时间) * 0.5
  (当前时间 - 浮动指数 - 最后发布时间) - 间隔时间
   * (转发数量 + 评论数量 + 点赞数量 + 收藏数量 + 分享数量 + 关注数量 + 粉丝数量 + 微博数量 + 关注数量)
  '''
  pass

# 获取指定 id 的在线状态 https://m.weibo.cn/api/container/getIndex?extparam=%E6%9C%B1%E6%B4%81%E9%9D%99&containerid=10080819db7645a97752ca3604221911c638f6_-_live&luicode=10000011&lfid=100103type%3D98%26q%3D%E6%9C%B1%E6%B4%81%E9%9D%99%26t%3D
def get_online_status(id):
  url = 'https://weibo.com/{}'.format(id)
  html = client.get(url).text
  soup = BeautifulSoup(html, 'lxml')
  # 判断是否在线
  if soup.find('div', {'class': 'WB_cardwrap S_bg2'}):
    return True
  else:
    return False



'''
定时采集(间隔15分钟), 将列表存储到DB sqlite3
采集完毕后将新数据加入已知索引

前端搜索功能 将全量展示列表 按照各种检索形式展示
(需设计一个交互界面)

抓取超话    > 先获取链接 https://weibo.com/ajax/profile/getSuperTopicInfo?owner_uid=1750333295
https://weibo.com/p/aj/v6/mblog/mbloglist
?ajwvr=6
&domain=100808&pagebar=0
&tab=super_index
&current_page=1
&since_id=4801418215819011
&pl_name=Pl_Core_MixedFeed__262
&id=1008089f1260fce8d1d56c76d01541995b2d5c
&script_uri=/p/1008089f1260fce8d1d56c76d01541995b2d5c/super_index&feed_type=1
&page=1&pre_page=1&domain_op=100808&__rnd=1660231012866

https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100808&pagebar=0&tab=super_index&current_page=1&since_id=4801418215819011&pl_name=Pl_Core_MixedFeed__262&id=1008089f1260fce8d1d56c76d01541995b2d5c&script_uri=/p/1008089f1260fce8d1d56c76d01541995b2d5c/super_index&feed_type=1&page=1&pre_page=1&domain_op=100808&__rnd=1660231012866


抓取交流回复 > 先获取链接
https://weibo.com/ajax/statuses/buildComments?is_reload=1&id=4801340033729292&is_show_bulletin=3&is_mix=0&count=10&uid=2606400364

互动事件 调起推送消息
'''

