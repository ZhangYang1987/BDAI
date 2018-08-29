# coding=utf-8
import os
import uuid
import filetype
import sqlite3
from flask import Flask,render_template,request,redirect,url_for
from werkzeug.utils import secure_filename

from flask import Blueprint
upload = Blueprint('upload', __name__)


def save_info(id,file_name,file_size,file_type):

    conn=sqlite3.connect('./app/upload_info')
    c=conn.cursor()
    save_string='insert into upload_info (ID,file_name,file_size,file_type)' \
                ' values ('+"'"+str(id)+"'"+','+"'"+str(file_name)+"'"+','\
                +"'"+str(file_size)+"'"+','+"'"+str(file_type)+"'"+')'
    print(save_string)
    c.execute(save_string)
    c.close()
    conn.commit()
    conn.close()


@upload.route('/',methods=['get','post'])
def uploads():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)  # 当前文件所在路径
        upload_path = os.path.join(basepath, os.path.pardir,'static/uploads', secure_filename(f.filename))  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
        f.save(upload_path)
        file = str(f.filename).split('.')
        filename = file[0]
        type = file[1]
        size = '0B'
        file_size = os.path.getsize(upload_path)
        if file_size>1024 and file_size<1048576:
            size=str(int(file_size/1024))+'KB'
        elif file_size>1048576:
            size = str(int(file_size / 1048576)) + 'MB'
        elif file_size<1024:
            size=str(int(file_size))+'B'
        save_info(uuid.uuid1(),filename,size,type)
        return redirect(url_for('upload.uploads')) #注意此处，如果只用uploads会报错
    return render_template('upload.html')