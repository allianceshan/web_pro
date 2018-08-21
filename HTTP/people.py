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

    def __init__(self, Phone='',QQNumber='',Sex=1):
        self.Phone = Phone
        self.QQNumber = QQNumber
        self.Sex = Sex
        
    def __repr__(self):
        return '<User %r>' % self.username
    def insertUserData(self):
        check_user = User.query.filter_by(Phone = self.Phone).first()
        if check_user != None:
            return 'Have Regist!'
        if len(self.Phone) != 11:
            return 'Phone is too small!'
        if self.Sex != 1 and self.Sex != 0:
            return 'Sex Error!'
        if len(self.UserEmal) == 0:
            return 'Emal is null!'
        db.session.add(self)
        db.session.commit()        
    
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