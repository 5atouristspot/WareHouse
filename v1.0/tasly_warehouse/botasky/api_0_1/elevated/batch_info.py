#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

"""
Created on 2017-8-29


@module: storagebin_info
@used: get storage bin info
"""

from . import api
from flask import request, jsonify, Response

import json

from botasky.utils.MyFILE import project_abdir, recursiveSearchFile
from botasky.utils.MyLOG import MyLog
logConfig = recursiveSearchFile(project_abdir, '*logConfig.ini')[0]
mylog = MyLog(logConfig, 'batch_info.py')
logger = mylog.outputLog()

from botasky.utils.MyCONN import MySQL

import ConfigParser
config = ConfigParser.ConfigParser()
colConfig = recursiveSearchFile(project_abdir, '*metaConfig.ini')[0]
config.read(colConfig)


__all__ = ['batch']
__author__ = 'zhihao'

@api.route('/batchinfo', methods=['GET', 'POST'])
def batch():
    '''
    :put in: batch_type 1(API-原料),2(API-成品),3(CF CABINET)
    :return:
    [{
        "name": "API-原料",
        "list": ["19000231", "19000230"]
    }
    ]

    [
    {
        "name": "API-成品",
        "list": ["19000231", "19000230"]
    }
    ]
    '''

    batch_type = request.args.get('batch_type', type=int, default=None)

    try:
        dbconfig = {'host': config.get('META', 'host'),
                    'port': int(config.get('META', 'port')),
                    'user': config.get('META', 'user'),
                    'passwd': config.get('META', 'pwd'),
                    'db': config.get('META', 'db'),
                    'charset': 'utf8'}

        if batch_type == 1:
            #sql = "select a.storage_bin,a.batch,b.status from tasly_warehouse_storage_info a left join tasly_warehouse_storage_info b on a.storage_bin = b.storage_bin where a.storage_bin = 'API-原料';"
            sql = "select storage_bin,batch,status from tasly_warehouse_storage_info where storage_bin = 'API-原料';"
            db = MySQL(dbconfig)
            db.query(sql)
            storagebin_info = db.fetchAllRows()
            #print storagebin_info
            db.close()
            bin_list = []
            for bin_number in storagebin_info:
                sub_keys = ['name', 'batch', 'status']
                #if bin_number[1] is None:
                #    sub_values = [bin_number[0], '']
                #else:
                #    sub_values = [bin_number[0], bin_number[1]]
                sub_values = [bin_number[0], bin_number[1], bin_number[2]]
                detail_info = dict(zip(sub_keys, sub_values))
                bin_list.append(detail_info)
            #return jsonify(bin_list)

            #print json.dumps(reload_info)
            resp = Response(json.dumps(bin_list))
            resp.headers['Access-Control-Allow-Origin'] = '*'
            resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
            return resp

        elif batch_type == 2:
            #sql = "select a.storage_bin,a.batch,b.status from tasly_warehouse_storage_info a left join tasly_warehouse_storage_info b on a.storage_bin = b.storage_bin where a.storage_bin = 'API-成品';"
            sql = "select storage_bin,batch,status from tasly_warehouse_storage_info where storage_bin = 'API-成品';"
            db = MySQL(dbconfig)
            db.query(sql)
            storagebin_info = db.fetchAllRows()
            # print storagebin_info
            db.close()
            bin_list = []
            for bin_number in storagebin_info:
                sub_keys = ['name', 'batch','status']
                # if bin_number[1] is None:
                #    sub_values = [bin_number[0], '']
                # else:
                #    sub_values = [bin_number[0], bin_number[1]]
                sub_values = [bin_number[0], bin_number[1], bin_number[2]]
                detail_info = dict(zip(sub_keys, sub_values))
                bin_list.append(detail_info)
            # return jsonify(bin_list)

            # print json.dumps(reload_info)
            resp = Response(json.dumps(bin_list))
            resp.headers['Access-Control-Allow-Origin'] = '*'
            resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
            return resp
        elif batch_type == 3:
            #sql = "select a.storage_bin,a.batch,b.status from tasly_warehouse_storage_info a left join tasly_warehouse_storage_info b on a.storage_bin = b.storage_bin where a.storage_bin = 'API-原料';"
            sql = "select storage_bin,batch,status from tasly_warehouse_storage_info where storage_bin = 'CF CABINET';"
            db = MySQL(dbconfig)
            db.query(sql)
            storagebin_info = db.fetchAllRows()
            #print storagebin_info
            db.close()
            bin_list = []
            for bin_number in storagebin_info:
                sub_keys = ['name', 'batch', 'status']
                #if bin_number[1] is None:
                #    sub_values = [bin_number[0], '']
                #else:
                #    sub_values = [bin_number[0], bin_number[1]]
                sub_values = [bin_number[0], bin_number[1], bin_number[2]]
                detail_info = dict(zip(sub_keys, sub_values))
                bin_list.append(detail_info)
            #return jsonify(bin_list)

            #print json.dumps(reload_info)
            resp = Response(json.dumps(bin_list))
            resp.headers['Access-Control-Allow-Origin'] = '*'
            resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
            return resp
        elif batch_type == 4:
            #sql = "select a.storage_bin,a.batch,b.status from tasly_warehouse_storage_info a left join tasly_warehouse_storage_info b on a.storage_bin = b.storage_bin where a.storage_bin = 'API-原料';"
            sql = "select storage_bin,batch,status from tasly_warehouse_storage_info where storage_bin = 'VENDOR';"
            db = MySQL(dbconfig)
            db.query(sql)
            storagebin_info = db.fetchAllRows()
            #print storagebin_info
            db.close()
            bin_list = []
            for bin_number in storagebin_info:
                sub_keys = ['name', 'batch', 'status']
                #if bin_number[1] is None:
                #    sub_values = [bin_number[0], '']
                #else:
                #    sub_values = [bin_number[0], bin_number[1]]
                sub_values = [bin_number[0], bin_number[1], bin_number[2]]
                detail_info = dict(zip(sub_keys, sub_values))
                bin_list.append(detail_info)
            #return jsonify(bin_list)

            #print json.dumps(reload_info)
            resp = Response(json.dumps(bin_list))
            resp.headers['Access-Control-Allow-Origin'] = '*'
            resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
            return resp



    except Exception, e:
        error_msg = "[action]:get batch info " \
                    "[status]:FAIL" \
                    "[host]:{host}" \
                    "[port]:{port}" \
                    "[Errorcode]:{e}".format(e=e, host=config.get('META', 'host'), port=int(config.get('META', 'port')))

        logger.error(error_msg)