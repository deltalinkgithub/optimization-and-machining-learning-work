# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 13:12:04 2022

@author: 211217
"""

## 開server接收

from flask import Flask
from flask import request
from flask_cors import CORS
from flask import make_response
from flask import render_template
import pymysql
import json
from pandas import DataFrame as df
app = Flask(__name__)
CORS(app)

# @app.route('/D10002', methods=['POST'])
# def getitD10002(): 
#     data = request.get_json()
#     print ('/D10002 get data '+str(data))
#     return data

@app.route('/login',methods=['POST','GET'])
def login():
    idpw=request.get_json()
    conn = pymysql.connect(host='10.11.50.35',port=8877, user='root', password='123456', database='spc')
    cur = conn.cursor()
    command="SELECT * FROM idlist WHERE id='{}'".format(idpw['first'])
    cur.execute(command) 
    results = cur.fetchall()
    results=df(results)
    if len(results)==0:
        print('不存在')
        return '不存在'
    elif idpw['second']!=results.iloc[0][2]:
        print('不符合')
        return '不符合'
    else:
        ip = request.remote_addr
        command="update idlist set ip='{}' where id='{}'".format(ip,idpw['first'])
        cur.execute(command)
        conn.commit()
        return '{} wlecome'.format(idpw['first'])
@app.route('/', methods=['POST','GET'])
def main():
    ip = request.remote_addr
    value='ip:{}'.format(ip)
    resp = make_response(render_template('page.html'))
    resp.set_cookie(key='framework', value=value, expires=None)
    return resp
@app.route('/set',methods=['POST','GET'])
def cookie():
    resp = make_response(render_template('page.html'))
    resp.set_cookie(key='framework', value='flask', expires=None)
    return resp
# @app.route('/api/content', methods=['POST'])
# def content_notebook():
#     data = request.get_json()
#     notebook_path = data['notebook_path']
#     base = data['base']
#     headers = data['headers']
# content = module.get_content_of_notebook(notebook_path, base, headers)
# return jsonify(content)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8003)
"""
# 給數值範例
import requests
data = {"value" : 586}
res = requests.post(url = r"http://127.0.0.1:8000//{}".format('D10002'),json = data)
res = requests.post(url = r"http://127.0.0.1:8000//{}".format('MLD'),json = data)
print (res)
"""