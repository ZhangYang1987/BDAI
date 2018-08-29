import pandas as pd
import os
from flask import Flask,render_template,request,redirect,url_for
from werkzeug.utils import secure_filename

class DataIn():

    #读取csv文件
    def read_csv(self):
        pd.read_csv(csv_file_path,header=1)
        pd.read_excel(excel_file_path,header=1)

# class flask_web():
#     app=Flask(__name__)
#
#     @app.route('/upload',methods=['get','post'])
#     def upload():
#         if request.method == 'POST':
#             f = request.files['file']
#             basepath = os.path.dirname(__file__)  # 当前文件所在路径
#             upload_path = os.path.join(basepath, 'static/uploads', secure_filename(f.filename))  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
#             f.save(upload_path)
#             return redirect(url_for('upload'))
#         return render_template('upload.html')
#
#     if __name__=='__main__':
#         app.run(host='0.0.0.0',port=6000)