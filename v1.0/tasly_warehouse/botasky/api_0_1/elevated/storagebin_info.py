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
mylog = MyLog(logConfig, 'storagebin_info.py')
logger = mylog.outputLog()

from botasky.utils.MyCONN import MySQL

import ConfigParser
config = ConfigParser.ConfigParser()
colConfig = recursiveSearchFile(project_abdir, '*metaConfig.ini')[0]
config.read(colConfig)


__all__ = ['storagebin']
__author__ = 'zhihao'


@api.route('/storagebin', methods=['GET', 'POST'])
def storagebin():
    '''
    :put in: warehouse_type 1~9
    :return:
    [{
		"name": "Rack货架         1#",
		"list": ["01-06-02", "01-06-03"]
	},
	{
		"name": "Rack货架         2#",
		"list": ["01-06-02", "01-06-03"]
	}
    ]
    '''

    warehouse_type = request.args.get('warehouse_type', type=int, default=None)
    try:
        dbconfig = {'host': config.get('META', 'host'),
                    'port': int(config.get('META', 'port')),
                    'user': config.get('META', 'user'),
                    'passwd': config.get('META', 'pwd'),
                    'db': config.get('META', 'db'),
                    'charset': 'utf8'}



        if warehouse_type == 1:
            dict1_l = []
            rack_type_l = ['一号货架', '二号货架', '三号货架', '四号货架', '五号货架', '六号货架']
            for rack_type in rack_type_l:
                #sql = "select a.rack_type,a.storage_bin,b.status from tasly_warehouse_storage_bin a left join tasly_warehouse_storage_info b on a.storage_bin = b.storage_bin where a.warehouse_type = 1 and a.rack_type = '{rack_type}' order by a.storage_bin;".format(rack_type=rack_type)
                sql = "select distinct(a.storage_bin),b.status,a.rack_type from tasly_warehouse_storage_bin a left join tasly_warehouse_storage_info b on a.storage_bin = b.storage_bin where a.warehouse_type = 1 and a.rack_type = '{rack_type}' order by a.storage_bin;".format(
                    rack_type=rack_type)
                db = MySQL(dbconfig)
                db.query(sql)
                Rack_info = db.fetchAllRows()
                db.close()

                #按照点位号　排序
                #sorted(Rack_info, key=lambda x: x[1])
                print Rack_info

                name = Rack_info[0][2]

                bin_list = []
                sub_keys = ['name', 'status']
                for bin_number in Rack_info:
                    #sub_values = [bin_number[1], bin_number[2]]
                    #print sub_values
                    #if bin_number[2] is None:
                    #    sub_values = [bin_number[1], '']
                    #else:
                    #    sub_values = [bin_number[1], bin_number[2]]
                    sub_values = [bin_number[0], bin_number[1]]
                    detail_info = dict(zip(sub_keys, sub_values))

                    bin_list.append(detail_info)

                keys = ['name', 'list']
                values = [name, bin_list]
                dict1_rack = dict(zip(keys, values))
                dict1_l.append(dict1_rack)

            #return jsonify(dict1_l)
            #return json.dumps(dict1_l,encoding = 'utf8', ensure_ascii=False)
            resp = Response(json.dumps(dict1_l))
            resp.headers['Access-Control-Allow-Origin'] = '*'
            resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
            return resp

        else:
            sql = "select a.storage_bin,b.status from tasly_warehouse_storage_bin a left join tasly_warehouse_storage_info b on a.storage_bin = b.storage_bin where warehouse_type = {warehouse_type};".format(warehouse_type=warehouse_type)
            db = MySQL(dbconfig)
            db.query(sql)
            storagebin_info = db.fetchAllRows()
            #print storagebin_info
            db.close()
            bin_list = []
            for bin_number in storagebin_info:
                sub_keys = ['name', 'status']
                #if bin_number[1] is None:
                #    sub_values = [bin_number[0], '']
                #else:
                #    sub_values = [bin_number[0], bin_number[1]]
                sub_values = [bin_number[0], bin_number[1]]
                detail_info = dict(zip(sub_keys, sub_values))
                bin_list.append(detail_info)
            #return jsonify(bin_list)

            #print json.dumps(reload_info)
            resp = Response(json.dumps(bin_list))
            resp.headers['Access-Control-Allow-Origin'] = '*'
            resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
            return resp

    except Exception, e:
        error_msg = "[action]:get storage bin info " \
                    "[status]:FAIL" \
                    "[host]:{host}" \
                    "[port]:{port}" \
                    "[Errorcode]:{e}".format(e=e, host=config.get('META', 'host'), port=int(config.get('META', 'port')))

        logger.error(error_msg)



