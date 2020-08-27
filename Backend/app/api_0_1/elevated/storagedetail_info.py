# -*- coding: utf-8 -*-

"""
Created on 2017-8-29


@module: storagedetail_info
@used: get storage detail info
"""

from . import api
from flask import request, jsonify,Response

import json

from Backend.utils.MyFILE import project_abdir, recursiveSearchFile
from Backend.utils.MyLOG import MyLog
logConfig = recursiveSearchFile(project_abdir, '*logConfig.ini')[0]
mylog = MyLog(logConfig, 'storagedetail_info.py')
logger = mylog.outputLog()

from Backend.utils.MyCONN import MySQL

import datetime
import time

import configparser
config = configparser.ConfigParser()
colConfig = recursiveSearchFile(project_abdir, '*metaConfig.ini')[0]
config.read(colConfig)

from Backend.app.views import auth

__all__ = ['storagedetail']
__author__ = 'zhihao'

#计算库存时间
def Caltime(last_goods_rec):
    #%Y-%m-%d为日期格式，其中的-可以用其他代替或者不写，但是要统一，同理后面的时分秒也一样；可以只计算日期，不计算时间。
    #date1=time.strptime(date1,"%Y-%m-%d %H:%M:%S")
    #date2=time.strptime(date2,"%Y-%m-%d %H:%M:%S")
    date_now = time.strftime("%Y-%m-%d")
    date1=time.strptime(date_now, "%Y-%m-%d")
    date2=time.strptime(last_goods_rec, "%Y-%m-%d")
    #根据上面需要计算日期还是日期时间，来确定需要几个数组段。下标0表示年，小标1表示月，依次类推...
    #date1=datetime.datetime(date1[0],date1[1],date1[2],date1[3],date1[4],date1[5])
    #date2=datetime.datetime(date2[0],date2[1],date2[2],date2[3],date2[4],date2[5])
    date1=datetime.datetime(date1[0],date1[1],date1[2])
    date2=datetime.datetime(date2[0],date2[1],date2[2])
    #返回两个变量相差的值，就是相差天数
    timedelta = str(date1-date2).split(' ')[0]
    return timedelta

@api.route('/storagedetail', methods=['POST','GET'])
@auth.login_required
def storagedetail():
    '''

    :return:
    '''
    binum = request.args.get('binum', type=str, default=None)
    try:
        dbconfig = {'host': config.get('META', 'host'),
                    'port': int(config.get('META', 'port')),
                    'user': config.get('META', 'user'),
                    'passwd': config.get('META', 'pwd'),
                    'db': config.get('META', 'db'),
                    'charset': 'utf8'}

        sql = "select material,storage_bin,status,batch,avail_stock,unit,material_desc,last_goods_rec,date_of_manuf,sled_bbd,next_inspection from tasly_warehouse_storage_info where storage_bin = '{binum}';".format(binum=binum)
        db = MySQL(dbconfig)
        db.query(sql)
        storagedetail_result = db.fetchAllRows()
        db.close()
        #print storagedetail_result
        #dict_l = []
        sub_dict_l = []
        if storagedetail_result is not ():
            for storagedetail in storagedetail_result:
                material = storagedetail[0]
                storage_bin = storagedetail[1]
                status = storagedetail[2]
                batch = storagedetail[3]
                avail_stock = storagedetail[4]
                unit = storagedetail[5]
                material_desc = storagedetail[6]
                last_goods_rec = storagedetail[7]
                date_of_manuf = storagedetail[8]
                sled_bbd = storagedetail[9]
                next_inspection = storagedetail[10]
                inventory_time = Caltime(last_goods_rec)
                keys = ['material','storage_bin','status','batch','avail_stock','unit','material_desc','last_goods_rec',
                        'date_of_manuf', 'sled_bbd','next_inspection', 'inventory_time']
                #print keys
                values = [material, storage_bin, status, batch, avail_stock, unit, material_desc, last_goods_rec, date_of_manuf,
                          sled_bbd, next_inspection, inventory_time]
                #print values
                #sub_dict_l = []
                for i in range(0,12):
                    #print values[i],keys[i]
                    sub_keys = ['name', 'value']
                    sub_values = [keys[i],values[i]]
                    detail_info = dict(zip(sub_keys, sub_values))
                    #print detail_info
                    sub_dict_l.append(detail_info)
                #dict_l.append(sub_dict_l)
                #print dict_l
        else:
                keys = ['material','storage_bin','status','batch','avail_stock','unit','material_desc','last_goods_rec',
                        'date_of_manuf', 'sled_bbd','next_inspection', 'inventory_time']
                #print keys
                values = ["", "", "", "", "", "", "", "", "", "", "", ""]
                #print values
                #sub_dict_l = []
                for i in range(0,12):
                    #print values[i],keys[i]
                    sub_keys = ['name', 'value']
                    sub_values = [keys[i],values[i]]
                    detail_info = dict(zip(sub_keys, sub_values))
                    #print detail_info
                    sub_dict_l.append(detail_info)
                #dict_l.append(sub_dict_l)
                #print dict_l

        #return jsonify(sub_dict_l)
        resp = Response(json.dumps(sub_dict_l))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
        return resp

    except Exception as e:
        error_msg = "[action]:get storage detail info " \
                    "[status]:FAIL" \
                    "[host]:{host}" \
                    "[port]:{port}" \
                    "[Errorcode]:{e}".format(e=e, host=config.get('META', 'host'), port=int(config.get('META', 'port')))

        logger.error(error_msg)
