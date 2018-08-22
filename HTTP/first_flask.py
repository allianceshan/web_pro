# -*- coding: UTF-8 -*-
import re
from flask import Flask,url_for,redirect,render_template,request
from flask_wtf import Form
import requests
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
import wtforms.validators
import people 
from people import app
index = 0
admin_data = {'大航':"这是服务器上大航的数据",'大珊':'这是服务器上大珊的数据','大珊深处':'这个是我们合照的数据'}
@app.route('/')
def hello_world():
    return render_template('index.html')
@app.route('/somedata')
def somedata():
    if request.method=="GET":
        ar = request.args.to_dict()

        values = admin_data[ar['name']]
        print(values)
        return "数据" + values
    #return send_from_directory('static',filename='123.txt',as_attachment=True)

@app.route('/regest/')
def regest():
    return render_template('regest.html',result='')

#设置请求参数 参数放在尖括号中
@app.route('/artcle/<id>')
def artcle(id):
    return '您请求的参数是' + id

@app.route('/login_form',methods=['POST'])
def GetUserData():
    print("用户名： " + request.form['recipient-name'])
    print("密码：   " + request.form['message-text'])
    user = people.User()
    datas = request.form['recipient-name']
    user.Password = request.form['message-text']
    if len(user.Password) < 6:
        return '密码小于6位'
    if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", datas) != None:
        user.UserEmal = datas
    if len(datas) == 11:
        user.Phone = datas
    return user.selectUserData()

    #return '用户名：' + request.form['recipient-name'] + '  密码： ' + request.form['message-text'] 
@app.route('/regest',methods=['POST'])
def RegestUserData():
    print("用户名：" + request.form['exampleInputUser'])
    print('密码： ' + request.form['exampleInputPassword1'])
    print("邮箱 "+ request.form['exampleInputEmail1'])
    print("QQ号" + request.form["exampleInputQQ"])
    print("性别：" + request.form['inlineRadioOptions'])
    user = people.User()
    user.Phone    = request.form['exampleInputPhone']
    user.UserName = request.form['exampleInputUser']
    user.Password = request.form['exampleInputPassword1']
    user.UserEmal = request.form['exampleInputEmail1']
    user.QQNumber = request.form['exampleInputQQ']
    user.Sex      = int(request.form['inlineRadioOptions'])
    result =  user.insertUserData()
    print("注册返回值：" + result);
    if result != '注册成功':
        return render_template('regest.html',result=result)
    return render_template('index.html')
    
if __name__=='__main__':
    app.run(port=80)