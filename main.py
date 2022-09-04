#!/usr/bin/python3
# -*- coding: utf-8 -*-

import fastapi
import uvicorn
import threading
import weibo
import bot

# 每 10 分钟检查一次
thread = threading.Thread(target=weibo.updateWeibo, args=(), kwargs={}, daemon=True)
thread.start()

# 估值一个亿的人工智能核心代码
def ai(text:str, callback):
  data = text\
    .replace('不同', '相同')\
    .replace('?', '!')\
    .replace('不', '')\
    .replace('吗', '')\
    .replace('吧', '')\
    .replace('有', '没有')\
    .replace('是不是', '是')\
    .replace('能不能', '能')\
    .replace('行不行', '行')\
    .replace('怎么样', '挺好的')\
    .replace('因为', '其实')\
    .replace('吧', '')\
    .replace('好', '好呀')\
    .replace('我', '我也')\
    .replace('你', '我')\
    .replace('啊', '呀')\
    .replace('嘿', '嘻')\
    .replace('喵', '汪')\
    .replace('？', '！')
  if data != text: callback(data)

# 创建服务器
app = fastapi.FastAPI()

@app.get('/')
def index():
  return 'Hello World'

@app.get('/update')
def update():
  weibo.update_weibo()
  return 'OK'

@app.post('/webhook')
async def webhook(request: fastapi.Request):
  data = await request.json()
  print(data)

  if data['message'] and ('text' in data['message']):
    chat = data['message']['chat']
    text = data['message']['text']

    if text == 'hello':
      bot.send_message(chat['id'], 'world!')
      return 'ok'

    if text == '你好':
      bot.sendResponse(chat['id'], '你好呀~')
      return 'ok'
    
    if text == '你是谁':
      bot.sendResponse(chat['id'], '我是你的机器人哦~')
      return 'ok'
    
    if text == 'count':
      bot.sendResponse(chat['id'], '存档微博数量: '+str(weibo.get_weibo_count())+' \n关注博主数量: '+str(weibo.get_user_count())+' \n')
      return 'ok'

    ai(text, lambda data: bot.sendResponse(chat['id'], data))

  return 'ok'

uvicorn.run(app=app, host='0.0.0.0', port=2336)
