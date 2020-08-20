# -*- coding: utf-8 -*-

"""
Created on 2017-8-29


@module: search_info
@used: get search info info
"""

from . import api
from flask import request, jsonify, Response

import json

from Backend.utils.MyFILE import project_abdir, recursiveSearchFile
from Backend.utils.MyLOG import MyLog
logConfig = recursiveSearchFile(project_abdir, '*logConfig.ini')[0]
mylog = MyLog(logConfig, 'search_info.py')
logger = mylog.outputLog()

from Backend.utils.MyCONN import MySQL

import configparser
config = configparser.ConfigParser()
colConfig = recursiveSearchFile(project_abdir, '*metaConfig.ini')[0]
config.read(colConfig)

from Backend.app.views import auth

__all__ = ['searchinfo']
__author__ = 'zhihao'

@api.route('/searchinfo', methods=['GET', 'POST'])
@auth.login_required
def searchinfo():
    '''
    :put in:
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
    search_type = request.args.get('search_type', type=str, default="")
    search_keys = request.args.get('search_keys', type=str, default="")

    '''
    if search_type == "storage_bin":
        # 通过storage_bin字段搜索
        sql = build_sql(search_type, search_keys)
    elif search_type == "material":
        # 通过material字段搜索
        sql = build_sql(search_type, search_keys)
    elif search_type == "batch":
        # 通过batch字段搜索
        sql = build_sql(search_type, search_keys)
    elif search_type == "material_desc":
        # 通过material_desc字段搜索
        sql = build_sql(search_type, search_keys)
    else:
        sql = "select id, material, storage_bin, batch, material_desc, avail_stock, unit, last_goods_rec, date_of_manuf, sled_bbd, next_inspection, status from tasly_warehouse_storage_info order by id;"
    '''
    if search_type in ["storage_bin", "material", "batch", "material_desc"]:
        #logger.error(search_type)
        #logger.error(search_keys)
        sql = build_sql(search_type, search_keys)
    else:
        sql = "select id, material, storage_bin, batch, material_desc, avail_stock, unit, last_goods_rec, date_of_manuf, sled_bbd, next_inspection, status from tasly_warehouse_storage_info order by id;"

    try:
        dbconfig = {'host': config.get('META', 'host'),
                    'port': int(config.get('META', 'port')),
                    'user': config.get('META', 'user'),
                    'passwd': config.get('META', 'pwd'),
                    'db': config.get('META', 'db'),
                    'charset': 'utf8'}

        #sql = "select a.storage_bin,a.batch,b.status from tasly_warehouse_storage_info a left join tasly_warehouse_storage_info b on a.storage_bin = b.storage_bin where a.storage_bin = 'API-原料';"
        #sql = "select id, material, storage_bin, batch, material_desc, avail_stock, unit, last_goods_rec, date_of_manuf, sled_bbd, next_inspection, status from tasly_warehouse_storage_info order by id;"
        db = MySQL(dbconfig)
        db.query(sql)
        storagebin_info = db.fetchAllRows()
        #print storagebin_info
        db.close()
        bin_list = []
        for bin_number in storagebin_info:
            sub_keys = ['id', 'material', 'storage_bin', 'batch', 'material_desc', 'avail_stock', 'unit', 'last_goods_rec', 'date_of_manuf', 'sled_bbd', 'next_inspection', 'status']
            #if bin_number[1] is None:
            #    sub_values = [bin_number[0], '']
            #else:
            #    sub_values = [bin_number[0], bin_number[1]]
            sub_values = [bin_number[0], bin_number[1], bin_number[2], bin_number[3], bin_number[4], bin_number[5], bin_number[6], bin_number[7], bin_number[8], bin_number[9], bin_number[10]]
            detail_info = dict(zip(sub_keys, sub_values))
            bin_list.append(detail_info)
            #return jsonify(bin_list)

            #print json.dumps(reload_info)
        resp = Response(json.dumps(bin_list))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
        return resp

    except Exception as e:
        error_msg = "[action]:get search info " \
                    "[status]:FAIL" \
                    "[host]:{host}" \
                    "[port]:{port}" \
                    "[Errorcode]:{e}".format(e=e, host=config.get('META', 'host'), port=int(config.get('META', 'port')))

        logger.error(error_msg)


def build_sql(search_type,search_keys):
    if len(search_keys.split(' ')) <= 1:
        sql = "select id, material, storage_bin, batch, material_desc, avail_stock, unit, last_goods_rec, date_of_manuf, sled_bbd, next_inspection, status from tasly_warehouse_storage_info where {search_type} like '%{search_key}%' order by id;".format(
            search_key=search_keys, search_type=search_type)
    else:
        sql = "select id, material, storage_bin, batch, material_desc, avail_stock, unit, last_goods_rec, date_of_manuf, sled_bbd, next_inspection, status from tasly_warehouse_storage_info where {search_type} like '%{search_key}%'".format(
            search_key=search_keys.split(' ')[0],search_type=search_type)
        for search_key in search_keys.split(' ')[1:]:
            sql_extra = " or {search_type} like '%{search_key}%'".format(search_key=search_key,search_type=search_type)
            sql = sql + sql_extra
        sql = sql + " order by id;"

    return sql