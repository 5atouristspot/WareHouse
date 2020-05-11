# -*- coding:utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from Backend.utils.MyFILE import project_abdir, recursiveSearchFile
import configparser
config = configparser.ConfigParser()
colConfig = recursiveSearchFile(project_abdir, '*metaConfig.ini')[0]
config.read(colConfig)

app = Flask(__name__)
# flask的跨域解决
CORS(app)
# flask 安全配置
app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'jklklsadhfjkhwbii9/sdf\sdf'

#数据库链接，仅用于用户信息验证
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://{user}:{passwd}@{host}:{port}/{db}?charset=utf8mb4".format(user=config.get('META', 'user'),
                                                                                                            passwd=config.get('META', 'pwd'),
                                                                                                            host=config.get('META', 'host'),
                                                                                                            port=int(config.get('META', 'port')),
                                                                                                            db=config.get('META', 'db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

#使json显示正常中文
app.config['JSON_AS_ASCII'] = False

#仓库接口
from .api_0_1 import api as api_1_0_blueprint
app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1000')

from .api_0_1.elevated import api as api_1_0_elevated_blueprint
app.register_blueprint(api_1_0_elevated_blueprint, url_prefix='/api/v1000/elevated')


from . import models, views