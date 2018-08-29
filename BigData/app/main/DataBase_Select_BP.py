# coding=utf-8
import os
import sqlite3
import pandas as pd
import numpy as np
from flask import Flask,render_template,request,redirect,url_for,session
from werkzeug.utils import secure_filename
from flask import Blueprint
DB_Sel = Blueprint('DB_Sel', __name__)

@DB_Sel.route('/',methods=['get','post'])
def index():
    return render_template('DB_Select.html')

@DB_Sel.route('/excel',methods=['get','post'])
def excel():
    conn=sqlite3.connect('./app/upload_info')
    c=conn.cursor()
    sql_string='select * from upload_info where file_type="xlsx"'
    c.execute(sql_string)
    result=c.fetchall()
    c.close()
    conn.close()
    results = np.array(result)
    return render_template('DB_Select_Excel.html',results=results)

@DB_Sel.route('/csv',methods=['get','post'])
def csv():
    return render_template('DB_Select_Csv.html')

@DB_Sel.route('/txt',methods=['get','post'])
def txt():
    return render_template('DB_Select_Txt.html')