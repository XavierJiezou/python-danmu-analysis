'''依赖模块
pip install requests
'''
import re
import requests

url = input('请输入B站视频链接: ')
res = requests.get(url)
cid = re.findall(r'"cid":(.*?),', res.text)[-1]
url = f'https://comment.bilibili.com/{cid}.xml'
res = requests.get(url)
with open(f'{cid}.xml', 'wb') as f:
    f.write(res.content)