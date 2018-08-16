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

@app.route('/regest/')
def regest():
    return render_template('regest.html')

#设置请求参数 参数放在尖括号中
@app.route('/artcle/<id>')
def artcle(id):
    return '您请求的参数是' + id

@app.route('/login_form',methods=['POST'])
def GetUserData():
    print("用户名： " + request.form['recipient-name'])
    print("密码：   " + request.form['message-text'])
    return '用户名：' + request.form['recipient-name'] + '  密码： ' + request.form['message-text'] 

@app.route('/regest',methods=['POST'])
def RegestUserData():
    print("用户名：" + request.form['exampleInputUser'])
    print('密码： ' + request.form['exampleInputPassword1'])
    print("邮箱 "+ request.form['exampleInputEmail1'])
    print("QQ号" + request.form["exampleInputQQ"])
    return "注册成功"
    
if __name__=='__main__':
    app.run()