# cp
获取cp互动通知

### TODO

STOP: 暂时找不到判断在线状态的方法(名人动态使用容器id访问)
STOP: 逐一读取评论列表数量过大(10分钟反复)

https://weibo.com/ajax/statuses/mymblog?uid=1750333295&page=2&feature=2

https://m.weibo.cn/p/index?extparam=%E6%9C%B1%E6%B4%81%E9%9D%99&containerid=10080819db7645a97752ca3604221911c638f6&luicode=10000011&lfid=100103type%3D98%26q%3D%E6%9C%B1%E6%B4%81%E9%9D%99%26t%3D

### setup

```bash
# 从requirements.txt安装依赖库(当提示权限不够时，前面加上sudo)
pip install -r requirements

# 使用 python 或 python3 运行
python3 main.py

```




### default

```bash

# 生成依赖文件
pip install pipreqs
pipreqs . --encoding=utf8 --force

```

