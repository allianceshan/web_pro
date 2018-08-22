# -*- coding: UTF-8 -*-
import os 
import sqlite3
import config
from flask import Flask,request,session,g,redirect,url_for,abort,render_template,flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@allianceshan.top:3306/xuhang'
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"]=True        #配置请求后自动提交
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'UserBase'                          #数据库中的表名
    UserID   = db.Column(db.Integer, primary_key=True)
    Phone    = db.Column(db.String(11), unique=True,nullable=False)
    QQNumber = db.Column(db.String(11))
    Sex      = db.Column(db.Integer,nullable=False)
    UserName = db.Column(db.String(18))
    UserEmal = db.Column(db.String(17),nullable=False)
    Password = db.Column(db.String(24),nullable=False)

    def __init__(self, Phone='',QQNumber='',Sex=1):
        self.Phone = Phone
        self.QQNumber = QQNumber
        self.Sex = Sex
        self.UserEmal = ''
        self.UserName = ''
        
    def __repr__(self):
        return '<User %r>' % self.username
    def insertUserData(self):
        check_user = User.query.filter_by(Phone = self.Phone).first()
        if check_user != None:
            return '手机号已被注册!'
        if len(self.Phone) != 11:
            return '手机号格式不对!'
        if self.Password == '' or self.Password ==' ' or len(self.Password) <6:
            return '密码为空或少于6位'
        if self.Sex != 1 and self.Sex != 0:
            return '性别错误!'
        if len(self.UserEmal) == 0:
            return '邮箱不能为空!'
        db.session.add(self)
        db.session.commit()    
        return '注册成功'
    def selectUserData(self):
        userdata = {}
        if len(self.Phone) !=11 and self.UserName == '' and len(self.UserEmal) == 0: 
            userdata['msg'] = '登录失败'
            userdata['error']='未填写手机号或邮箱信息'
        elif len(self.Password) < 6:
            userdata['msg'] = '登录失败'
            userdata['error']='密码格式错误'            
        elif len(self.Phone) == 11 and  len(self.Password) >=6:
            check_user = User.query.filter_by(Phone = self.Phone,Password = self.Password).first()
            if check_user != None:
                userdata['msg'] = '登录成功'
                userdata['userName'] = check_user.UserName
                print(userdata)   
            else:
                userdata['msg'] = '登录失败'
            return  userdata
        elif len(self.UserEmal) > 0 and len(self.Password) <6:
            check_user = User.query.filter_by(Phone = self.Phone,Password = self.Password).first()
            if check_user != None:
                userdata['msg'] = '登录成功'
                userdata['userName'] = check_user.UserName
            return userdata
#if __name__=='__main__':
    ##db.create_all()
    #users = User()
    #users.Phone='18435131883'
    #users.QQNumber='1564285868'
    #users.Sex=0
    #users.UserName='王珊'
    #users.UserEmal='1564285868@qq.com'
    #users.insertUserData()
    #user = User.query.filter_by(UserID=1).first()
    #id = user.UserID
    #phone = user.Phone
    #dd= 0