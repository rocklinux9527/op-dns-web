from flask import Blueprint
from flask import request, render_template, redirect, session, Response
from tools.sessions import sessionmsg
from namedManage.named_db_play import _insert_dns_records,_query_named_id,_query_named_List,_delete_named_list,_update_named
import json
import hashlib

field = ["id", "zone", "host", "type", "data", "ttl"]
fields = ["zone", "host", "type", "data", "ttl"]

# 域名列表
namedUrl = Blueprint('/namedlist', __name__)


@namedUrl.route('/')
def namedListMain():
    if 'username' not in session:
        return redirect('/login/')
    msg = sessionmsg()
    result = _query_named_List()
    print(result)
    return render_template('named.html', msg=msg, result=result['data'])


namedAdddUrl = Blueprint('/namedadd', __name__)


@namedAdddUrl.route('/', methods=['GET', 'POST'])
def namedAddMain():
    if 'username' not in session:
        return redirect('/login/')
    msg = sessionmsg()
    if request.method == 'POST':
        data = {k: v for k, v in dict(request.form).items()}
        if data.get("zone") and data.get("host") and data.get("type") and data.get("data") and data.get("ttl"):
            result = _insert_dns_records(data.get("zone"), data.get("host"), data.get("type"), data.get("data"),
                                         data.get("ttl"))
            if result['code'] == 0:
                result = {'code': 0, 'msg': "Add Zone Successful"}
                return json.dumps(result)
            else:
                result = {'code': 1, 'msg': "Add Zone Failure"}
                return json.dumps(result)

# 更新域名信息
namedUpdateUrl = Blueprint('/namedupdate', __name__)

@namedUpdateUrl.route('/', methods=['GET', 'POST'])
def namedupdate():
    if 'username' not in session:
        return redirect('/login/')
    msg = sessionmsg()
    if request.method == 'GET':
        named_id = request.args.get('id')
        data = {'id': named_id}
        result = _query_named_id(data)
        format_result = json.loads(result)
        if format_result.get("code") == 0:
            return json.dumps(format_result.get("data")[0])
    if request.method == 'POST':
        data = {k: v for k, v in dict(request.form).items()}
        print("入参数", data)
        result = _update_named(data)
        print("返回参数", result)
        return json.dumps(result)


# 删除域名信息
namedDeleteUrl = Blueprint('/nameddelete', __name__)


@namedDeleteUrl.route('/', methods=['GET', 'POST'])
def nameddelete():
    if 'username' not in session:
        return redirect('/login/')
    msg = sessionmsg()
    if request.method == 'GET':
        dataid = request.args.get('id')
        if _delete_named_list(dataid):
            result = {'code': 0, 'msg': "delete user success"}
        return json.dumps(result)
