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

@app.post('/webhook')
def webhook(request: fastapi.Request):
  data = request.json()
  print(data)
  return 'ok'

uvicorn.run(app=app, host='0.0.0.0', port=2336)
