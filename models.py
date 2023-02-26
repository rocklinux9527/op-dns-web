"""
@author:lijx
@contact: 360595252@qq.com
@site: http://blog.51cto.com/breaklinux
@version: 1.0
"""
# -*- coding: utf-8 -*-
import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Dnsrecords(db.Model):
    __tablename__ = 'dns_records'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主键自增长
    zone = db.Column(db.String(255), nullable=False)
    host = db.Column(db.String(255), nullable=False)
    type = db.Column(db.Enum('A', 'MX', 'CNAME', 'NS', 'SOA', 'PTR', 'TXT', 'AAAA', 'SVR', 'URL'), default='A',
                     nullable=False)
    data = db.Column(db.String(255), nullable=True)
    ttl = db.Column(db.Integer, server_default="3600", nullable=True)
    mx_priority = db.Column(db.Integer)
    view = db.Column(db.Enum('any', 'Telecom', 'Unicom', 'CMCC', 'ours'), default="any", nullable=False)
    priority = db.Column(db.Integer, server_default="255", nullable=False)
    refresh = db.Column(db.Integer, server_default="28800", nullable=False)
    retry = db.Column(db.Integer, server_default="14400", nullable=False)
    expire = db.Column(db.Integer, server_default="86400", nullable=False)
    minimum = db.Column(db.Integer, server_default="86400", nullable=False)
    serial = db.Column(db.Integer, server_default="2015050917", nullable=False)
    resp_person = db.Column(db.String(64), server_default="ddns.net")
    primary_ns = db.Column(db.String(64), server_default="ns.ddns.net.',")

    def to_dict(self):
        return {"id": self.id, "zone": self.zone, "host": self.host, "type": self.type,
                "data": self.data, "ttl": int(self.ttl), "mx_priority": self.mx_priority, "view": self.view,
                "priority": self.priority, "refresh": self.refresh,
                "expire": self.expire, "minimum": self.minimum,
                "serial": self.serial, "resp_person": self.resp_person, "primary_ns": self.primary_ns}


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主键自增长
    username = db.Column(db.String(255), unique=True, nullable=False)
    name_cn = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    mobile = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {"id": self.id, "username": self.username, "name_cn": self.name_cn,
                "password": self.password,
                "mobile": self.mobile, "email": self.email, "role": int(self.role),
                "status": int(self.status)}
