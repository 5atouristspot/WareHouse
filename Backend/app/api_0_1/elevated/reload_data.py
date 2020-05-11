# -*- coding: utf-8 -*-

"""
Created on 2017-8-29


@module: reload_data
@used: reload data from excel
"""

from . import api
from flask import request, jsonify, Response
import json

import subprocess

from Backend.utils.MyFILE import project_abdir, recursiveSearchFile
from Backend.utils.MyLOG import MyLog
logConfig = recursiveSearchFile(project_abdir, '*logConfig.ini')[0]
mylog = MyLog(logConfig, 'reload_data.py')
logger = mylog.outputLog()

from Backend.app.views import auth

__all__ = ['reload_data']
__author__ = 'zhihao'


@api.route('/reloaddata', methods=['GET', 'POST'])
@auth.login_required
def reload_data():
    try:
        (status, output) = subprocess.getstatusoutput('cd /data1/mycode/tasly_warehouse/ && /data1/mycode/tasly_warehouse/venv/bin/python ./load_storage_info.py')

        keys = ['status', 'output']
        values = [status, output]
        reload_info = dict(zip(keys, values))
        #print json.dumps(reload_info)
        resp = Response(json.dumps(reload_info))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
        return resp



    except Exception as e:
        error_msg = "[action]:reload data from excel " \
                    "[status]:FAIL" \
                    "[Errorcode]:{e}".format(e=e)

        logger.error(error_msg)