
import webview
from flask import Flask,render_template
from fucs import read_settings
import os.path as path
from sys import argv

server=Flask(__name__,static_folder='./web/static',template_folder='./web/templates')


@server.route('/')
def home():
    return render_template('base.html')

@server.route('/settings/')
def settings():
    dirname=path.dirname(path.realpath(argv[0]))
    filepath=path.join(dirname,'config.txt')
    import subprocess, os, platform
    if platform.system() == 'Darwin':       # macOS
        subprocess.call(('open', filepath))
    elif platform.system() == 'Windows':    # Windows
        os.startfile(filepath)
    else:                                   # linux variants
        subprocess.call(('xdg-open', filepath))
    return render_template('settings.html')

@server.route('/start/')
def start():
    job,needed,seat,exception=read_settings()
    total_len=len(job)
    print("---=-=-==")
    print(seat)
    print(needed)
    print(exception)
    print(job)
    return render_template('main_start.html',job=job,needed=needed,seat=seat,exception=exception,total_len=total_len,pointer_=0,total_seats=len(seat))

if __name__ == '__main__':
    window = webview.create_window(
        title='111-打掃分配',
        url=server,		# 这里直接将实例化后的flask对象传给url参数就可以自动启动web服务了
        confirm_close=False,	# 退出时提示
    )
    # 自定义退出提示的中文内容
    webview.start(debug=False)