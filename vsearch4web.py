# -*- coding: utf-8 -*-  
from flask import Flask, render_template, request, escape
import os

app = Flask(__name__)
os.getcwd()

dict_class_name = dict()
dict_class_time = dict()
file_names = [x for x in os.listdir('class_name')]
for f in file_names:
    with open('class_name/{fn}'.format(fn = f),'r',encoding='utf8') as file_object:
        dict_class_name[f.strip('.txt')] = file_object.read().splitlines()
for f in file_names:
    with open('class_time/{fn}'.format(fn = f),'r',encoding='utf8') as file_object:
        dict_class_time[f.strip('.txt')] = file_object.read().splitlines()

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    name = request.form['name']
    return render_template('results.html',
                           the_name = name,
                           the_classname = dict_class_name['{sn}'.format(sn = name)],
                           the_classtime = dict_class_time['{sn}'.format(sn = name)],
                           )

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='欢迎来到网上，查找文学与传媒系老师课程表')

@app.route('/viewlog')
def view_the_log() -> 'html':
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('表单内容', '访问者IP', '浏览器', '运行结果')
    return render_template('viewlog.html',
                           the_title='查看日志',
                           the_row_titles=titles,
                           the_data=contents,)

if __name__ == '__main__':
    app.run(debug=True)





