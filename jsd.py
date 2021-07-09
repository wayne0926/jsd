import requests
url = input('输入jsd的CDN链接：')
url = url.replace('cdn.jsdelivr.net', 'purge.jsdelivr.net')
print('正在请求链接：' + url)
for times in range(4):
    result = requests.get(url).json()['success']
    print('请求了第' + str(times+1) + '次')
    print(result)
print('完成')
