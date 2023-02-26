from flask import Flask
from tools.config import MysqlConfig
from app.view import mainUrl
from loginManager.view import loginUrl, loginoutUrl
from userManager.view import userUrl, centerPasswordUrl, msgUrl, userListUrl, addUserUrl, deleteUserUrl, updateUserUrl
from namedManage.view import namedUrl, namedAdddUrl, namedDeleteUrl,namedUpdateUrl
from flask_cors import CORS



def create_app():
    salt = '98b85629951ad584feaf87e28c073088'
    app = Flask(__name__,
                static_folder='static',
                template_folder='templates'
                )
    app.secret_key = salt
    app.config.from_object(MysqlConfig)
    CORS(app, supports_credentials=True)
    from models import db
    db.init_app(app)
    app.register_blueprint(mainUrl, url_prefix='/')
    app.register_blueprint(userUrl, url_prefix='/center')
    app.register_blueprint(addUserUrl, url_prefix='/add')
    app.register_blueprint(deleteUserUrl, url_prefix='/delete')
    app.register_blueprint(updateUserUrl, url_prefix='/update')
    app.register_blueprint(userListUrl, url_prefix='/userlist')
    app.register_blueprint(centerPasswordUrl, url_prefix='/user/chpwdoneself')
    app.register_blueprint(msgUrl, url_prefix='/user/chmessageoneself')
    app.register_blueprint(loginUrl, url_prefix='/login')
    app.register_blueprint(loginoutUrl, url_prefix='/logout')
    app.register_blueprint(namedUrl, url_prefix='/namedlist')
    app.register_blueprint(namedAdddUrl, url_prefix='/namedadd')
    app.register_blueprint(namedDeleteUrl, url_prefix='/nameddelete')
    app.register_blueprint(namedUpdateUrl, url_prefix='/namedupdate')
    return app


