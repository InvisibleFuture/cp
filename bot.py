from pyclbr import Function
from xmlrpc.client import boolean
import requests


base_path = 'https://api.telegram.org/bot5719456826:AAGZNimEYjY-1wOkL0u1Ao5enqjxbfENpFA/'

def sendResponse(uid, text, parse_mode:str='', reply_markup:dict={}, disable_web_page_preview:bool=False, photo:str='', disable_notification:bool=False, callback:Function=None):
  '''
  向telegram发送响应
  '''
  method = 'sendMessage'
  data = {
    'chat_id': uid,
    'parse_mode': parse_mode,
    'reply_markup': reply_markup,
    'disable_web_page_preview': disable_web_page_preview,
    'disable_notification': disable_notification,
  }
  if photo:
    data['photo'] = photo
    data['caption'] = text
    method = 'sendPhoto'
  else:
    data['text'] = text

  return requests.post(base_path+method, data=data).json()
