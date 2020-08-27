# -*- coding: utf-8 -*-

"""
Created on 2019-05-22


@module: utilization_rate
@used: 每个货仓，货架的　总位点数　, 未使用位点数,　占用率
以warehouse_type为标识，区别货仓
１：　高架库区１
２：　高架库区预留区（没有）
３：　地面库区１
４：　地面库区２
５：　生产供料区
６：　冷库区
７：　恒温库区　
８：　ＰＶＤＣ　

以rack_type　为标识，区别　高架库区１　中的货架号
Rack货架１#　：　货架１
Rack货架２#　：　货架２
Rack货架３#　：　货架３
Rack货架４#　：　货架４
Rack货架５#　：　货架５
Rack货架６#　：　货架６
"""

#如果想在python中让这两种有一个明确的分工。即"/"可以用于float除法，"//"用于整除法，我们可以在程序开始的时候做以下声明
from __future__ import division

import collections

from . import api
from flask import request, jsonify, Response

import json

from Backend.utils.MyFILE import project_abdir, recursiveSearchFile
from Backend.utils.MyLOG import MyLog
logConfig = recursiveSearchFile(project_abdir, '*logConfig.ini')[0]
mylog = MyLog(logConfig, 'storeage_utilization_rate.py')
logger = mylog.outputLog()

from Backend.utils.MyCONN import MySQL

import configparser
config = configparser.ConfigParser()
colConfig = recursiveSearchFile(project_abdir, '*metaConfig.ini')[0]
config.read(colConfig)

from Backend.app.views import auth

__all__ = ['utilization_rate']
__author__ = 'zhihao'


@api.route('/utilization_rate', methods=['GET', 'POST'])
@auth.login_required
def utilization_rate():
    warehouse_type = request.args.get('warehouse_type', type=int, default=None)
    '''
    #高架库区１　每个货架　货架总货位数
    select count(1) from tasly_warehouse_storage_bin a left join tasly_warehouse_storage_info b on a.storage_bin = b.storage_bin where a.warehouse_type = 1 and a.rack_type = 'Rack 货架1#' ;
    
    #高架库区１　每个货架　货架未使用位数
    select count(1) from tasly_warehouse_storage_bin a left join tasly_warehouse_storage_info b on a.storage_bin = b.storage_bin where a.warehouse_type = 1 and a.rack_type = 'Rack 货架1#' and b.status is NULL;
    
    #高架库区１　每个货架　货架　占用率
    '''
    try:
        dbconfig = {'host': config.get('META', 'host'),
                    'port': int(config.get('META', 'port')),
                    'user': config.get('META', 'user'),
                    'passwd': config.get('META', 'pwd'),
                    'db': config.get('META', 'db'),
                    'charset': 'utf8'}

        dict1_l = []
        if warehouse_type == 1:
            rack_type_l = ['一号货架', '二号货架', '三号货架', '四号货架', '五号货架', '六号货架']
            for rack_type in rack_type_l:
                #sql_total = "select count(1) from tasly_warehouse_storage_bin a left join tasly_warehouse_storage_info b on a.storage_bin = b.storage_bin where a.warehouse_type = 1 and a.rack_type = '{rack_type}' ;".format(rack_type=rack_type)
                sql_total = "select count(1) from tasly_warehouse_storage_bin where warehouse_type = 1 and rack_type = '{rack_type}' ;".format(rack_type=rack_type)
                db = MySQL(dbconfig)
                db.query(sql_total)
                Rack_total_info = db.fetchAllRows()
                total_num = Rack_total_info[0][0]

                sql_vacancy = "select count(1) from tasly_warehouse_storage_bin a left join tasly_warehouse_storage_info b on a.storage_bin = b.storage_bin where a.warehouse_type = 1 and a.rack_type = '{rack_type}' and b.status is NULL;".format(rack_type=rack_type)
                db = MySQL(dbconfig)
                db.query(sql_vacancy)
                Rack_vacancy_info = db.fetchAllRows()
                vacancy_num = Rack_vacancy_info[0][0]

                db.close()
                if int(total_num) != 0:
                    util_rate = (int(total_num)-int(vacancy_num))/int(total_num)
                else:
                    util_rate = 0

                #sub_keys = ['total_num', 'vacancy_num', 'util_rate']
                sub_keys = [rack_type, '未使用', '使用率']
                sub_values = [total_num, vacancy_num, util_rate]
                detail_info = dict(zip(sub_keys, sub_values))

                keys = ['name', 'list']
                values = [rack_type, detail_info]
                dict1_rack = dict(zip(keys, values))
                dict1_l.append(dict1_rack)


            #高架库区１　总使用率，库位总量，总未使用
            #sql_all_total = "select count(1) from tasly_warehouse_storage_bin a left join tasly_warehouse_storage_info b on a.storage_bin = b.storage_bin where a.warehouse_type = 1 ;"
            sql_all_total = "select count(1) from tasly_warehouse_storage_bin where warehouse_type = 1 ;"
            db = MySQL(dbconfig)
            db.query(sql_all_total)
            Rack_all_total_info = db.fetchAllRows()
            all_total_num = Rack_all_total_info[0][0]

            sql_all_vacancy = "select count(1) from tasly_warehouse_storage_bin a left join tasly_warehouse_storage_info b on a.storage_bin = b.storage_bin where a.warehouse_type = 1 and b.status is NULL;"
            db = MySQL(dbconfig)
            db.query(sql_all_vacancy)
            Rack_all_vacancy_info = db.fetchAllRows()
            all_vacancy_num = Rack_all_vacancy_info[0][0]

            db.close()

            if int(all_total_num) != 0:
                all_util_rate = (int(all_total_num) - int(all_vacancy_num)) / int(all_total_num)
            else:
                all_util_rate = 0

            sub_keys = ['高架库区1', '未使用', '使用率']
            sub_values = [all_total_num, all_vacancy_num, all_util_rate]
            detail_info = dict(zip(sub_keys, sub_values))

            keys = ['name', 'list']
            values = ['total', detail_info]
            dict1_rack = dict(zip(keys, values))
            dict1_l.append(dict1_rack)


            #return jsonify(dict1_l)
            resp = Response(json.dumps(dict1_l))
            resp.headers['Access-Control-Allow-Origin'] = '*'
            resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
            return resp
        else:

            sql_total = "select count(distinct(a.storage_bin)) from tasly_warehouse_storage_bin a left join tasly_warehouse_storage_info b on a.storage_bin = b.storage_bin where a.warehouse_type = {warehouse_type} ;".format(warehouse_type=warehouse_type)
            db = MySQL(dbconfig)
            db.query(sql_total)
            Rack_total_info = db.fetchAllRows()
            total_num = Rack_total_info[0][0]

            sql_vacancy = "select count(1) from tasly_warehouse_storage_bin a left join tasly_warehouse_storage_info b on a.storage_bin = b.storage_bin where a.warehouse_type = {warehouse_type} and b.status is NULL;".format(warehouse_type=warehouse_type)
            db = MySQL(dbconfig)
            db.query(sql_vacancy)
            Rack_vacancy_info = db.fetchAllRows()
            vacancy_num = Rack_vacancy_info[0][0]

            db.close()
            if int(total_num) != 0:
                util_rate = (int(total_num)-int(vacancy_num))/int(total_num)
            else:
                util_rate = 0

            #sub_keys = ['total_num', 'vacancy_num', 'util_rate']
            sub_keys = ['库位总量', '未使用', '使用率']
            sub_values = [total_num, vacancy_num, util_rate]
            detail_info = dict(zip(sub_keys, sub_values))

            keys = ['name', 'list']
            values = [warehouse_type, detail_info]
            dict1_rack = dict(zip(keys, values))
            dict1_l.append(dict1_rack)

            #return jsonify(dict1_l)
            resp = Response(json.dumps(dict1_l))
            resp.headers['Access-Control-Allow-Origin'] = '*'
            resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
            return resp




    except Exception as e:
        error_msg = "[action]:get storage utilization rate " \
                    "[status]:FAIL" \
                    "[host]:{host}" \
                    "[port]:{port}" \
                    "[Errorcode]:{e}".format(e=e, host=config.get('META', 'host'), port=int(config.get('META', 'port')))

        logger.error(error_msg)

