#!/usr/bin/python3
# -*- coding: utf-8 -*-

import weibo
import store
import json

print('weibo.get_weibo_count', weibo.get_weibo_count())

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
all = store.weibo.all()
print(json.dumps(all, ensure_ascii=False, indent=2))
