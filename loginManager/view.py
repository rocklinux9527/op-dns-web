from flask import Blueprint
from flask import request, render_template, redirect, Response, session
import json

loginUrl = Blueprint('login', __name__)


@loginUrl.route('/', methods=['GET', 'POST'])
def loginRun():
    import json
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        result = userCheck(username, password)
        data_format = json.loads(result)
        if data_format.get("code") == 0:
            if int(data_format.get("data")[0].get("status")) != 1:
                session['username'] = username
                session['role'] = data_format.get("data")[0].get("role")
                return json.dumps(data_format)
            else:
                result = {'code': 1, 'msg': u"用户已被锁定"}
                return json.dumps(result)
        else:
            result = {'code': 1, 'msg': u"用户名或者密码不正确"}
            return json.dumps(result)
    else:
        return render_template('login.html')


def userCheck(username, password, user_role='0', user_status='0'):
    import json
    from models import User
    query_data = User.query.filter(User.username == username, User.status == user_status, User.role == user_role,
                                   User.password == password).all()
    if query_data:
        return json.dumps({"code": 0, "total": len(query_data), "data": [i.to_dict() for i in query_data],
                           "messages": "query success"})
    else:
        return json.dumps(
            {"code": 1, "total": 0, "data": "", "messages": "User does not exist or  Password input error"})


loginoutUrl = Blueprint('logout', __name__)
@loginoutUrl.route('/', methods=['GET', 'POST'])
def loginout():
    if session.get('username'):
        session.pop('username', None)
        session.pop('role', None)
    return redirect('/login/')
