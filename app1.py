from flask import Flask, render_template

import settings

app= Flask(__name__)
app.config.from_object(settings)

@app.route('/')
def hello_world():
    msg='hello everyone hello world'
    li = [1,2,3,4,5,6,7]
    return render_template('define_filter.html',msg=msg, li=li)

#过滤器本质也是函数
#1. 通过flask 模块中的add_template_filter
#2. 通过装饰器

def replace_hello(value):
    print('--------------------', value)
    value=value.replace('hello','')
    print('--------------------', value)
    return value.strip()
#第一种方式，
app.add_template_filter(replace_hello,'replace')
#第二种， 装饰器

@app.template_filter('lireverse')
def reverse_list(li):
    temp_li = list(li)
    temp_li.reverse()
    return temp_li


if __name__ == '__main__':
    app.run()