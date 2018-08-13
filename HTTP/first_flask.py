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
    #if index == 1:
        #login_url = url_for('login')
        #return redirect(login_url)
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
    print("用户名： " + request.form['userName'])
    print("密码：   " + request.form['passWord'])
    return '用户名：' + request.form['userName'] + '  密码： ' + request.form['passWord'] 
if __name__=='__main__':
    app.run()