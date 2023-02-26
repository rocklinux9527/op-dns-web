import json


def _insert_dns_records(zone, host, type, data, ttl):
    """
    1.新增记录
    :param zone:
    :param host:
    :param type:
    :param data:
    :param ttl:
    :return:
    """
    from models import db
    from models import Dnsrecords
    try:
        dns_records_insert = Dnsrecords(zone=zone, host=host, type=type, data=data, ttl=ttl)
        db.session.add(dns_records_insert)
        db.session.commit()
        return {"code": 0, "data": "", "msg": "insert ok"}
    except Exception as e:
        print(e)
        return {"code": 1, "data": "", "msg": "insert fail"}


def _query_named_id(data):
    """
    1.根据id查询数据
    """
    from models import Dnsrecords
    query_data = Dnsrecords.query.filter_by(id=int(data.get("id"))).all()
    if query_data:
        return json.dumps({"code": 0, "data": [i.to_dict() for i in query_data],
                           "msg": "Query Success"})
    else:
        return json.dumps(
            {"code": 1, "total": 0, "data": "", "msg": "data is null"})


def _query_named_List():
    """
    1.查询用户表信息总共有多少条数据
    :return:
    """
    from models import Dnsrecords
    query_data = Dnsrecords.query.all()
    if query_data:
        return {"code": 0, "total": len(query_data), "data": [i.to_dict() for i in query_data], "msg": "Query Success"}
    else:
        return {"code": 1, "total": 0, "data": "", "msg": "Query no data"}


def _delete_named_list(Id):
    """
    1.删除named信息
    :return:
    """
    from models import db
    from models import Dnsrecords
    import json
    try:
        delete_data = Dnsrecords.query.get(Id)
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


def _update_named(data):
    from models import db
    from models import Dnsrecords
    """
    1.id 更新named信息,修改数据
    """
    if data.get("id") and data.get("zone") and data.get("host") and data.get("type") and data.get(
            "data") and data.get("ttl"):
        try:
            Dnsrecords.query.filter_by(id=data.get("id")).update(
                {"zone": data.get("zone"), "host": data.get("host"), "type": data.get("type"),
                 "data": data.get("data"), "ttl": data.get("ttl")})
            msg = "Update  dns record data Success"
            db.session.commit()
            return {"code": 0, "data": True, "msg": msg}

        except Exception as e:
            print(e)
            return {"code": 1, "data": None, "msg": str(e)}
    else:
        return {"code": 1, "data": None, "msg": "Insufficient field parameter"}
