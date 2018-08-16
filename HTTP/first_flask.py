# -*- coding: UTF-8 -*-
from flask import Flask,url_for,redirect,render_template,request
from flask_wtf import Form
import requests
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
import wtforms.validators
import config
app = Flask(__name__)
app.config.from_object(config)
index = 0
    
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/loginsdf/')
def login():
    return '这是登录页面'

#设置请求参数 参数放在尖括号中
@app.route('/artcle/<id>')
def artcle(id):
    return '您请求的参数是' + id

@app.route('/login_form',methods=['GET','POST'])
def GetUserData():
    print("用户名： " + request.form['recipient-name'])
    print("密码：   " + request.form['message-text'])
    return '用户名：' + request.form['recipient-name'] + '  密码： ' + request.form['message-text'] 
if __name__=='__main__':
    app.run()