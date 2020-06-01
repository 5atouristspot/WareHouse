#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

"""
Created on 2017-7-04
Modify on 2017-12-01


@module: run
@used: main of botasky
"""

import os
from flask import Flask

#from gevent import monkey
#from gevent.pywsgi import WSGIServer

#monkey.patch_all()

#from botasky.utils.MyDAEMON import daemonize

__all__ = ['create_app', 'main']
__author__ = 'zhihao'


#used of running gunicorn

#apt-get install figlet
#os.system('figlet botasky')

app = Flask(__name__)

'''使json显示正常中文'''
app.config['JSON_AS_ASCII'] = False

from api_0_1 import api as api_1_0_blueprint
app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1000')



#from api_0_1.moosefs import api as api_1_0_moosefs_blueprint
#app.register_blueprint(api_1_0_moosefs_blueprint, url_prefix='/api/v1000/moosefs')

#from api_0_1.keepalived import api as api_1_0_keepalived_blueprint
#app.register_blueprint(api_1_0_keepalived_blueprint, url_prefix='/api/v1000/keepalived')

from api_0_1.elevated import api as api_1_0_elevated_blueprint
app.register_blueprint(api_1_0_elevated_blueprint, url_prefix='/api/v1000/elevated')


def create_app():
    app = Flask(__name__)

    from api_0_1 import api as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1000')

    from api_0_1.moosefs import api as api_1_0_moosefs_blueprint
    app.register_blueprint(api_1_0_moosefs_blueprint, url_prefix='/api/v1000/moosefs')

    from api_0_1.keepalived import api as api_1_0_keepalived_blueprint
    app.register_blueprint(api_1_0_keepalived_blueprint, url_prefix='/api/v1000/keepalived')

    return app


def main():
    #apt-get install figlet
    os.system('figlet botasky')

    daemonize('/dev/null', '/tmp/botasky_stdout.log', '/tmp/botasky_stdout.log')

    app = create_app()

    server = WSGIServer(('127.0.0.1', 3621), app)
    server.serve_forever()



if __name__ == '__main__':

    #curl -u da:xinxin -i -X GET http://192.168.41.12:3621/api/v1000/
    app.run(debug=True, host='192.168.58.1', port=3621)


