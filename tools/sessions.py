from flask import session

def sessionmsg():
    msg = {'username': session['username'], 'role': session['role']}
    return msg
