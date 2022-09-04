#!/usr/bin/python3
# -*- coding: utf-8 -*-

import fastapi
import uvicorn
import threading
import weibo
import bot

#bot.sendResponse()

# 每 10 分钟检查一次
thread = threading.Thread(target=weibo.updateWeibo, args=(), kwargs={}, daemon=True)
thread.start()


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

  if data['message']:
    chat = data['message']['chat']
    text = data['message']['text']

    if text == '你好':
      bot.sendResponse(chat['id'], '你好呀~')
    
    if text == '你是谁':
      bot.sendResponse(chat['id'], '我是你的机器人哦~')
    
    if text == 'count':
      bot.sendResponse(chat['id'], '存档微博数量: '+str(weibo.get_weibo_count())+' \n关注博主数量: '+str(weibo.get_user_count())+' \n')

  return 'ok'

uvicorn.run(app=app, host='0.0.0.0', port=2336)
