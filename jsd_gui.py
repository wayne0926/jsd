import requests
import time
from guietta import _, Gui, Quit
gui = Gui(
	[ "链接","__url__",  "次数：", "__num__", ["提交"] ],
	[ "结果：", "result",_, _,   _ ],
	[  _,       _,      _,  _,   Quit('退出') ]
)
gui.result = ''
def a(gui, url):
    gui.提交.setEnabled(False)
    n = int(gui.num)
    for nb in range(n):
        t = requests.get(url).json()['success']
        gui.result += str('请求了第' + str(nb+1) + '次：')
        gui.result += str(t) + '\n'
        time.sleep(2)
    gui.提交.setEnabled(True)
def b(gui, *arg):
    gui.result = ''
    url = str(gui.url)
    url = url.replace('cdn.jsdelivr.net', 'purge.jsdelivr.net')
    gui.result = str('正在请求链接：' + url + '\n')
    a(gui, url)
    gui.result = gui.result + ('完成')
gui.events(
	[ _,_,_, _, b],
	[ _, _,_, _,_],
	[ _,_, _,_,_ ]
)
gui.run()