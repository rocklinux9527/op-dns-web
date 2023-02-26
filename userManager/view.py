from flask import Blueprint
from flask import request, render_template, redirect, session, Response
from tools.sessions import sessionmsg
from userManager.user_db_play import _update_center, _query_user_id, _getCenterOne, _queryUserList, _insert_User, \
    _delete_user, _update_user, _query_user_id_and_password, _update_user_password
import json
import hashlib

salt = '98b85629951ad584feaf87e28c073088'

# 用户个人中心
userUrl = Blueprint('center', __name__)


@userUrl.route('/')
def userCenterMain():
    if 'username' not in session:
        return redirect('/login/')
    msg = sessionmsg()
    data = {'username': session['username']}
    print(data)
    data = {'username': session['username']}

    result = _getCenterOne(data)
    format_result = json.loads(result)
    print(format_result)
    if format_result.get("code") == 0:
        return render_template('center.html', msg=format_result.get("data")[0])
    else:
        return render_template('center.html', msg=format_result.get("data")[0])


# 修改个人密码
centerPasswordUrl = Blueprint('/user/chpwdoneself', __name__)


@centerPasswordUrl.route('/', methods=['GET', 'POST'])
def chpwdoneself():
    if 'username' not in session:
        return redirect('/login/')
    msg = sessionmsg()
    chpwd = {k: v for k, v in dict(request.form).items()}
    print("修改密码参数", chpwd)
    # password = 'my_password'
    # hashed_password = hash_password(password)
    # print(hashed_password)

    where = {'password': chpwd['oldpasswd']}
    # field = ['id', 'password']
    result = _query_user_id_and_password(where)
    print("返回数据", result)
    format_result = json.loads(result)
    if format_result['code'] == 0:
        data = {'id': chpwd['id'], 'password': chpwd['newpasswd']}
        result = _update_user_password(data)
    else:
        result = {'code': 1, 'msg': u"旧密码不正确请重新输入!"}
    return json.dumps(result)


def hash_password(password):
    hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
    return hashed_password


def verify_password(password, hashed_password):
    hashed_input_password = hashlib.sha256((password + salt).encode()).hexdigest()
    return hashed_input_password == hashed_password


# 修改个人资料
msgUrl = Blueprint('/user/chmessageoneself', __name__)


@msgUrl.route('/', methods=['GET', 'POST'])
def updateMsgSelf():
    if 'username' not in session:
        return redirect('/login/')
    msg = sessionmsg()
    if request.method == 'POST':
        user = {k: v for k, v in dict(request.form).items()}
        result = _update_center(user)
        if result['code'] == 0:
            result = {'code': 0, 'msg': result.get("msg")}
            return json.dumps(result)
        else:
            result = {'code': 1, 'msg': result.get("msg")}
            return json.dumps(result)


# 用户列表
userListUrl = Blueprint('/userlist', __name__)


@userListUrl.route('/', methods=['GET', 'POST'])
def userList():
    if 'username' not in session:
        return redirect('/login/')
    msg = sessionmsg()
    result = _queryUserList()
    print(result)
    return render_template('userlist.html', msg=msg, result=result.get("data"))


# 添加用户信息
addUserUrl = Blueprint('/add', __name__)


@addUserUrl.route('/', methods=['GET', 'POST'])
def userAdd():
    if 'username' not in session:
        return redirect('/login/')
    if request.method == 'POST':
        field = ["username", "name_cn", "password", "mobile", "email", "role", "status"]
        data = {k: v for k, v in dict(request.form).items()}
        print("注册信息", data)
        # data['password'] = hashlib.md5(data['password'] + salt).hexdigest()
        # print("md5", hashlib.md5(data['password'] + salt).hexdigest())
        if data.get("username") and data.get("name_cn") and data.get("password") and data.get("mobile") and data.get(
                "email") and data.get("role") and data.get("status"):
            result = _insert_User(data.get("username"), data.get("name_cn"),
                                  data.get("password"), data.get("mobile"), data.get(
                    "email"), data.get("role"), data.get("status"))
            if result['code'] == 0:
                result = {'code': 0, 'msg': "add user success"}
            return json.dumps(result)
        else:
            print("参数空了")
            return json.dumps({"code": 1, "msg": "parameter null "})


# 删除用户信息
deleteUserUrl = Blueprint('/delete', __name__)


@deleteUserUrl.route('/', methods=['GET', 'POST'])
def delete_user(format_result_delete=None):
    if 'username' not in session:
        return redirect('/login/')
    msg = sessionmsg()
    if request.method == 'GET':
        userid = request.args.get('id')
        print("删除用户id", userid)
        result_delete = _delete_user(userid)
        format_result_delete = json.loads(result_delete)
        if format_result_delete.get("code") == 0:
            result = {'code': 0, 'msg': "delete user success"}
        else:
            result = {'code': 1, 'msg': "delete user failed"}
        return json.dumps(result)


# 更新用户信息
updateUserUrl = Blueprint('/update', __name__)


@updateUserUrl.route('/', methods=['GET', 'POST'])
def update():
    if 'username' not in session:
        return redirect('/login/')
    msg = sessionmsg()
    if request.method == 'GET':
        userid = request.args.get('id')
        data = {'id': userid}
        if data:
            result = _query_user_id(data)
            format_result = json.loads(result)
            if format_result.get("code") == 0:
                return json.dumps(format_result.get("data")[0])
            else:
                return format_result
        else:
            result = {'code': 1, 'msg': "no user id not query data"}
            return json.dumps(result)

    else:
        data = {k: v for k, v in dict(request.form).items()}
        result = _update_user(data)
        return json.dumps(result)
