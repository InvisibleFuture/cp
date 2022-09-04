import requests


base_path = 'https://api.telegram.org/bot5719456826:AAGZNimEYjY-1wOkL0u1Ao5enqjxbfENpFA/'

def sendResponse(uid, text, parse_mode, reply_markup, disable_web_page_preview, photo, disable_notification, callback):
  '''
  向telegram发送响应
  '''
  url = base_path + 'sendMessage'
  data = {
    'chat_id': uid,
    'text': text,
    'parse_mode': parse_mode,
    'reply_markup': reply_markup,
    'disable_web_page_preview': disable_web_page_preview,
    'photo': photo,
    'disable_notification': disable_notification,
    'callback': callback
  }
  return requests.post(url, data=data).json()
