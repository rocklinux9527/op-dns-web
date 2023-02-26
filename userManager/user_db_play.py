import json


def _getCenterOne(data, user_role='0', user_status='0'):
    """
    1.根据用户名称-查询用户信息
    :param data:
    :param user_role:
    :param user_status:
    :return:
    """
    from models import User
    query_data = User.query.filter(User.username == data['username'], User.status == user_status,
                                   User.role == user_role).all()
    if query_data:
        return json.dumps({"code": 0, "total": len(query_data), "data": [i.to_dict() for i in query_data],
                           "msg": data['username']})
    else:
        return json.dumps(
            {"code": 1, "total": 0, "data": "", "msg": "data is null"})


def _update_center(data):
    from models import db
    from models import User
    """
    1.id 更新用户个人信息,修改数据
    """
    if data.get("id") and data.get("username") and data.get("name_cn") and data.get("mobile") and data.get("email"):
        try:
            User.query.filter_by(id=data.get("id")).update(
                {"username": data.get("username"), "name_cn": data.get("name_cn"), "mobile": data.get("mobile"),
                 "email": data.get("email")})
            msg = "Update User data Success"
            db.session.commit()
            return {"code": 0, "data": True, "msg": msg, "username": data.get("username")}

        except Exception as e:
            print(e)
            return {"code": 1, "data": None, "msg": str(e)}
    else:
        return {"code": 1, "data": None, "msg": "Insufficient field parameter"}


def _queryUserList():
    """
    1.查询用户表信息总共有多少条数据
    :return:
    """
    from models import User
    query_data = User.query.all()
    if query_data:
        return {"code": 0, "total": len(query_data), "data": [i.to_dict() for i in query_data], "msg": "Query Success"}
    else:
        return {"code": 1, "total": 0, "data": "", "msg": "Query no data"}


def _insert_User(username, name_cn, password, mobile, email, role, status):
    """
    1.新增用户参数入库
    :param username:
    :param name_cn:
    :param password:
    :param mobile:
    :param email:
    :param role:
    :param status:
    :return:
    """
    from models import db
    from models import User
    try:
        user_insert = User(username=username, name_cn=name_cn, password=password, mobile=mobile, email=email, role=role,
                           status=status)
        db.session.add(user_insert)
        db.session.commit()
        return {"code": 0, "data": "", "msg": "insert ok"}
    except Exception as e:
        print(e)
        return {"code": 1, "data": "", "msg": "insert fail"}


def _delete_user(Id):
    """
    1.删除用户信息
    :return: 
    """
    from models import db
    from models import User
    import json
    try:
        delete_data = User.query.get(Id)
        if delete_data:
            db.session.delete(delete_data)
            db.session.commit()
            data = {"code": 0, "date": True, "msg": "delete success"}
        else:
            data = {"code": 1, "date": False, "msg": "match data failure "}
        return json.dumps(data)
    except Exception as e:
        data = {"code": 1, "data": "delete appname failed", "msg": str(e)}
        return json.dumps(data)


def _query_user_id(data):
    """
    1.根据id查询数据
    """
    print("id来了", data)
    from models import User
    query_data = User.query.filter_by(id=int(data.get("id"))).all()
    if query_data:
        return json.dumps({"code": 0, "data": [i.to_dict() for i in query_data],
                           "msg": "Query Success"})
    else:
        return json.dumps(
            {"code": 1, "total": 0, "data": "", "msg": "data is null"})


def _query_user_id_and_password(data):
    """
    1.根据id查询数据
    """
    print("密码", data)
    from models import User
    query_data = User.query.filter(User.password == data.get("password")).all()
    if query_data:
        return json.dumps({"code": 0, "data": [i.to_dict() for i in query_data],
                           "msg": "Query Success"})
    else:
        return json.dumps(
            {"code": 1, "total": 0, "data": "", "msg": "data is null"})


def _update_user(data):
    from models import db
    from models import User
    """
    1.id 更新用户个人信息,修改数据
    """
    if data.get("id") and data.get("username") and data.get("name_cn") and data.get("mobile") and data.get("email") and data.get(
            "role") and data.get("status"):
        try:
            User.query.filter_by(id=data.get("id")).update(
                {"username": data.get("username"), "name_cn": data.get("name_cn"), "mobile": data.get("mobile"),
                 "email": data.get("email"), "role": data.get("role"), "status": data.get("status")})
            msg = "Update User data Success"
            db.session.commit()
            return {"code": 0, "data": True, "msg": msg, "username": data.get("username")}

        except Exception as e:
            print(e)
            return {"code": 1, "data": None, "msg": str(e)}
    else:
        return {"code": 1, "data": None, "msg": "Insufficient field parameter"}


def _update_user_password(data):
    from models import db
    from models import User
    """
    1.id 更新用户个人信息,修改数据
    """
    if data.get("id") and data.get("password"):
        try:
            User.query.filter_by(id=data.get("id")).update(
                {"password": data.get("password")})
            msg = u"Update User data Passwrd Success!"
            db.session.commit()
            return {"code": 0, "data": True, "msg": msg}

        except Exception as e:
            print(e)
            return {"code": 1, "data": None, "msg": str(e)}
    else:
        return {"code": 1, "data": None, "msg": "Insufficient field parameter"}