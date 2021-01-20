# -*- coding: utf-8 -*-

"""
Created on 2017-8-29


@module: material trace
@used: get material component
"""


from . import api
from flask import request, jsonify, Response

import json

from Backend.utils.MyFILE import project_abdir, recursiveSearchFile
from Backend.utils.MyLOG import MyLog
logConfig = recursiveSearchFile(project_abdir, '*logConfig.ini')[0]
mylog = MyLog(logConfig, 'material_trace_old.py')
logger = mylog.outputLog()

from Backend.utils.MyCONN import MySQL

import configparser
config = configparser.ConfigParser()
colConfig = recursiveSearchFile(project_abdir, '*metaConfig.ini')[0]
config.read(colConfig)

from Backend.app.views import auth

__all__ = ['materialtrace']
__author__ = 'zhihao'

@api.route('/materialtrace_old', methods=['GET', 'POST'])
@auth.login_required
def materialtrace_old():
    batch = request.args.get('batch', type=str, default="")

    try:
        dbconfig = {'host': config.get('META', 'host'),
                    'port': int(config.get('META', 'port')),
                    'user': config.get('META', 'user'),
                    'passwd': config.get('META', 'pwd'),
                    'db': config.get('META', 'db'),
                    'charset': 'utf8'}
        boxes = []
        db = MySQL(dbconfig)
        #sql = "select batch,order_num from batch_order_relation where movement_type in (101) and batch = '{batch}' order by posting_date desc ;". \
        #    format(batch=batch)

        sql = "select batch,order_num from batch_order_relation where movement_type in (101) and batch = '{batch}' group by batch,order_num ;". \
            format(batch=batch)
        db.query(sql)
        batch_order_num_info = db.fetchAllRows()
        db.close()

        for batch_order_num in batch_order_num_info:
            box = []

            batch = batch_order_num[0]
            order_num = batch_order_num[1]

            tree_node_info = get_tree_first_level_node_info(dbconfig, order_num, batch, box)
            tree_info = list_to_tree(tree_node_info)
            #logger.error(tree_info)

            res = {}
            res.setdefault("order_num", "{order_num}".format(order_num=order_num))
            res.setdefault("list", tree_info)
            boxes.append(res)
            #boxes.append({"order_num": "{order_num}".format(order_num=order_num), res.setdefault("list", []).append(tree_info)} )
            #boxes.append(tree_info)

        #print(boxes)

        resp = Response(json.dumps(boxes))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
        return resp

    except Exception as e:
        error_msg = "[action]:get material component " \
                    "[status]:FAIL" \
                    "[host]:{host}" \
                    "[port]:{port}" \
                    "[Errorcode]:{e}".format(e=e, host=config.get('META', 'host'), port=int(config.get('META', 'port')))

        logger.error(error_msg)


def get_tree_first_level_node_info(dbconfig, order_num, batch, box):
    try:
        db = MySQL(dbconfig)
        #用order_num找的，不返回pid（同一返回pid=0）,用batches找的返回pid(以区分是第一层节点还是第二层节点)
        sql_detail = "select id,material,material_description,order_num,batch,quantity_wi,unit,batches,0 from component_list where order_num in ({order_num}) and batch != '';".\
            format(order_num=order_num)
        db.query(sql_detail)
        detail_info = db.fetchAllRows()
        sql_posting_date = "select posting_date from batch_order_relation where batch = '{batch}' order by posting_date desc limit 1;".format(batch=batch)
        db.query(sql_posting_date)
        posting_date_info = db.fetchAllRows()

        if posting_date_info != ():
            posting_date = posting_date_info[0][0]
        else:
            posting_date = ''

        db.close()

        for detail in detail_info:
            line_info = dict(id=detail[0],material=detail[1],material_description=detail[2],order_num=detail[3],batch=detail[4],quantity_wi=detail[5],unit=detail[6],pid=int(detail[8]),posting_date=posting_date)
            box.append(line_info)

            batches = detail[7]
            batch = detail[4]
            if batches != '':
                get_tree_other_level_node_info(dbconfig, batches, batch, box)

        #list_to_tree(box)
        return box
    except Exception as e:
        print(e)


def get_tree_other_level_node_info(dbconfig, batches, batch, box):
    try:
        db = MySQL(dbconfig)
        #用order_num找的，不返回pid（同一返回pid=0）,用batches找的返回pid(以区分是第一层节点还是第二层节点)
        sql_detail = "select id,material,material_description,order_num,batch,quantity_wi,unit,batches,pid from component_list where id in ({batches}) and batch != '';".\
            format(batches=batches)
        db.query(sql_detail)
        detail_info = db.fetchAllRows()

        sql_posting_date = "select posting_date from batch_order_relation where batch = '{batch}' order by posting_date desc limit 1;".format(batch=batch)
        db.query(sql_posting_date)
        posting_date_info = db.fetchAllRows()

        if posting_date_info != ():
            posting_date = posting_date_info[0][0]
        else:
            posting_date = ''

        db.close()

        for detail in detail_info:
            #如果子节点的batches存在，递归调用get_tree_other_level_node_info
            batches = detail[7]
            batch = detail[4]

            line_info = dict(id=detail[0],material=detail[1],material_description=detail[2],order_num=detail[3],batch=detail[4],quantity_wi=detail[5],unit=detail[6],pid=int(detail[8]),posting_date=posting_date)

            box.append(line_info)

            if detail[7] != '':
                get_tree_other_level_node_info(dbconfig, batches, batch, box)
            else:
                continue

    except Exception as e:
        print(e)


def list_to_tree(data):
    res = {}
    for v in data:
        # 以id为key，存储当前元素数据
        res.setdefault(v["id"], v)
    for v in data:
        res.setdefault(v["pid"], {}).setdefault("children", []).append(v)
        # 这里默认的关联关系，v的内存地址是一致的，所以后续修改只后，关联的结构也会变化。
    #print(res[0]["children"])
    #logger.error(res[0]["children"])
    return res[0]["children"]
