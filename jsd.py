import requests
url = input('输入jsd的CDN链接：')
url = url.replace('cdn.jsdelivr.net', 'purge.jsdelivr.net')
print('正在请求链接：' + url)
num = 1
while num <= 4:
    t = requests.get(url).json()
    print('请求了第' + str(num) + '次')
    num = num + 1
print('完成')