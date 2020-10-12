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

@api.route('/materialtrace', methods=['GET', 'POST'])
@auth.login_required
def materialtrace():
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

        sql = "select batch,order_num,max(id),max(relation_batches) from batch_order_relation where movement_type in (101) and batch = '{batch}' group by batch,order_num ;". \
            format(batch=batch)
        db.query(sql)
        batch_order_num_id_info = db.fetchAllRows()
        db.close()

        for batch_order_num_id in batch_order_num_id_info:
            box = []

            batch = batch_order_num_id[0]
            order_num = batch_order_num_id[1]
            relation_id = batch_order_num_id[2]
            relation_batches = batch_order_num_id[3]

            if is_finish_product(dbconfig, batch, relation_batches):
                #成品信息
                finish_product_info = get_finish_product_info(dbconfig, order_num, batch, relation_id)
            else:
                finish_product_info = dict(id='', material='', material_description='', order_num='',
                         batch='', quantity_wi='', unit='', creating_date='',
                         consuming_date='', gaining_date='', pasting_date='')
            # 组成物料的信息
            tree_node_info = get_tree_first_level_node_info(dbconfig, batch, relation_batches, box)
            #logger.info(tree_node_info)
            #TODO:确实是这有问题　着重测这个函数
            tree_info = list_to_tree(tree_node_info)
            #logger.info(tree_info)

            res = {}
            res.setdefault("order_num", "{order_num}".format(order_num=order_num))
            res.setdefault("finish_product_info", finish_product_info)
            res.setdefault("list", tree_info)
            boxes.append(res)
        #print(boxes)
        #logger.info(boxes)


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


def is_finish_product(dbconfig, batch, relation_batches):
    db = MySQL(dbconfig)
    # 如果101的信息　同时又　包含261的信息　那么它就不是成品信息;除非它的下级中的batch有和它相同的，那么它就是半成品　，要显示成品信息
    sql_is_finish_product = "select batch,order_num,id,relation_batches from batch_order_relation where movement_type in (261) and batch = '{batch}' ;". \
        format(batch=batch)
    logger.info(sql_is_finish_product)
    db.query(sql_is_finish_product)
    finish_product_261_info = db.fetchAllRows()
    logger.info(finish_product_261_info)
    db.close()

    #半成品
    db = MySQL(dbconfig)
    sql_sub_batch = "select batch from batch_order_relation where id in ({relation_batches}) ;". \
        format(relation_batches=relation_batches)
    #logger.info(sql_sub_batch)
    db.query(sql_sub_batch)
    sub_batch_info = db.fetchAllRows()
    #logger.info(sub_batch_info)
    db.close()
    sub_batch_list = []
    for sub_batch in sub_batch_info:
        sub_batch_item = sub_batch[0]
        sub_batch_list.append(sub_batch_item)

    if finish_product_261_info == ():
        return True
    else:
        if batch in sub_batch_list:
            return True
        else:
            return False


def get_finish_product_info(dbconfig, order_num, batch, relation_id):
    try:
        #组成物料的信息

        db = MySQL(dbconfig)
        #用relation_id找的，不返回pid（同一返回pid=0）,用batches找的返回pid(以区分是第一层节点还是第二层节点)(第一层返回的是成品信息)(时间相关的值和单位在另外的逻辑里)
        sql_detail = "select id,material,material_description,order_num,batch,quantity,relation_batches,0 from batch_order_relation where id = {relation_id} ;".\
            format(relation_id=relation_id)
        #logger.info(sql_detail)
        db.query(sql_detail)
        detail_info = db.fetchAllRows()

        #如果能取到成品信息
        if detail_info != ():

            #单位unit
            material = detail_info[0][1]
            material_description = detail_info[0][2]

            sql_unit = "select unit from unit_info where material = '{material}' and material_description = '{material_description}';".format(material=material, material_description=material_description)
            #logger.info(sql_unit)
            db.query(sql_unit)
            unit_info = db.fetchAllRows()
            if unit_info != ():
                unit = unit_info[0][0]
            else:
                unit = ''
            #logger.info('unit')
            #logger.info(unit)

            #生成时间 101的posting_date
            sql_creating_date = "select order_num,max(posting_date) from batch_order_relation where batch = '{batch}' and order_num = '{order_num}' and movement_type in (101) group by order_num;".format(batch=batch,order_num=order_num)
            #logger.info(sql_creating_date)
            db.query(sql_creating_date)
            creating_date_info = db.fetchAllRows()
            if creating_date_info != ():
                creating_date = creating_date_info[0][1]
            else:
                creating_date = ''
            #logger.info('creating_date')
            #logger.info(creating_date)

            #消耗时间为空	consuming_date
            consuming_date = ''
            #物料收获时间为空 gaining_date
            gaining_date = ''


            #放行时间 321的posting_date
            sql_pasting_date = "select order_num,max(posting_date) from batch_order_relation where batch = '{batch}' and order_num = '{order_num}' and movement_type in (321) group by order_num;".format(batch=batch,order_num=order_num)
            #logger.info(sql_pasting_date)
            db.query(sql_pasting_date)
            pasting_date_info = db.fetchAllRows()
            logger.info('pasting_date_info')
            logger.info(pasting_date_info)
            if pasting_date_info != ():
                pasting_date = pasting_date_info[0][1]
            else:
                pasting_date = ''
            logger.info('pasting_date')
            logger.info(pasting_date)

            db.close()

            finish_product_info = dict(id=detail_info[0][0], material=detail_info[0][1], material_description=detail_info[0][2], order_num=detail_info[0][3],
                         batch=detail_info[0][4], quantity_wi=abs(int(detail_info[0][5])), unit=unit, creating_date=creating_date,
                         consuming_date=consuming_date, gaining_date=gaining_date, pasting_date=pasting_date)

            logger.info('finish_product_info')
            logger.info(finish_product_info)
        else:
                finish_product_info = ()

        #logger.info(finish_product_info)

        return finish_product_info

    except Exception as e:
        print(e)


def get_tree_first_level_node_info(dbconfig, batch, relation_batches, box):
    try:
        #组成物料的信息
        db = MySQL(dbconfig)
        #用relation_id找的，不返回pid（同一返回pid=0）,用batches找的返回pid(以区分是第一层节点还是第二层节点)(第一层返回的是成品信息)(时间相关的值和单位在另外的逻辑里)
        sql_detail = "select id,material,material_description,order_num,batch,quantity,relation_batches,0 from batch_order_relation where id in ({relation_batches});".\
            format(relation_batches=relation_batches)
        #logger.info(sql_detail)
        db.query(sql_detail)
        detail_info = db.fetchAllRows()
        db.close()

        for detail in detail_info:
            db = MySQL(dbconfig)
            #单位unit
            material = detail[1]
            material_description = detail[2]
            sql_unit = "select unit from unit_info where material = '{material}' and material_description = '{material_description}';".format(material=material, material_description=material_description)
            #logger.info(sql_unit)
            db.query(sql_unit)
            unit_info = db.fetchOneRow()
            #logger.info(unit_info)
            if unit_info != ():
                unit = unit_info[0]
            else:
                unit = ''
            #logger.info(unit)

            #如果不再包含下级组件　则展示　　生成时间='',　消耗时间,物料收货时间,放行时间; 若包含下级组件则展示　生成时间,消耗时间,物料收货时间='', 放行时间

            batch_sub = detail[4]
            #logger.info(batch_sub)
            order_num = detail[3]
            #logger.info(order_num)

            #TODO:这个地方找的不对用１０１重新找！！！！！！
            #sql_relation_batches = "select relation_batches from batch_order_relation where batch = '{batch_sub}' and order_num = '{order_num}' and movement_type in (101) order by posting_date desc limit 1;". \
            #    format(batch_sub=batch_sub, order_num=order_num)
            sql_relation_batches = "select relation_batches from batch_order_relation where batch = '{batch_sub}' and movement_type in (101) order by posting_date desc limit 1;". \
                format(batch_sub=batch_sub)
            #logger.info(sql_relation_batches)
            db.query(sql_relation_batches)
            relation_batches_info = db.fetchAllRows()

            if relation_batches_info == ():
                relation_batches = ''
            else:
                relation_batches = relation_batches_info[0][0]

            #logger.info(relation_batches)
            #不再包含下级组件
            if relation_batches == '':
                #生成时间 为空
                creating_date = ''

                #消耗时间261	consuming_date
                sql_consuming_date = "select order_num,max(posting_date) from batch_order_relation where batch = '{batch}' and order_num = '{order_num}' and movement_type in (261) group by order_num;".format(
                    batch=batch_sub, order_num=order_num)
                #logger.info(sql_consuming_date)
                db.query(sql_consuming_date)
                consuming_date_info = db.fetchAllRows()

                if consuming_date_info != ():
                    consuming_date = consuming_date_info[0][1]
                else:
                    consuming_date = ''

                #物料收获时间101 gaining_date
                sql_gaining_date = "select order_num,max(posting_date) from batch_order_relation where batch = '{batch}' and order_num = '{order_num}' and movement_type in (101) group by order_num;".format(
                    batch=batch_sub, order_num=order_num)
                #logger.info(sql_gaining_date)
                db.query(sql_gaining_date)
                gaining_date_info = db.fetchAllRows()

                if gaining_date_info != ():
                    gaining_date = gaining_date_info[0][1]
                else:
                    gaining_date = ''


                #放行时间 321的posting_date
                sql_pasting_date = "select order_num,max(posting_date) from batch_order_relation where batch = '{batch}' and order_num = '{order_num}' and movement_type in (321) group by order_num;".format(
                    batch=batch_sub,order_num=order_num)
                #logger.info(sql_pasting_date)
                db.query(sql_pasting_date)
                pasting_date_info = db.fetchAllRows()

                if pasting_date_info != ():
                    pasting_date = pasting_date_info[0][1]
                else:
                    pasting_date = ''

            #包含下级组件
            else:
                #生成时间 101的posting_date
                sql_creating_date = "select order_num,max(posting_date) from batch_order_relation where batch = '{batch}' and order_num = '{order_num}' and movement_type in (101) group by order_num;".format(
                    batch=batch_sub,order_num=order_num)
                #logger.info(sql_creating_date)
                db.query(sql_creating_date)
                creating_date_info = db.fetchAllRows()

                if creating_date_info != ():
                    creating_date = creating_date_info[0][1]
                else:
                    creating_date = ''

                #消耗时间为空	consuming_date
                sql_consuming_date = "select order_num,max(posting_date) from batch_order_relation where batch = '{batch}' and order_num = '{order_num}' and movement_type in (261) group by order_num;".format(
                    batch=batch_sub, order_num=order_num)
                #logger.info(sql_consuming_date)
                db.query(sql_consuming_date)
                consuming_date_info = db.fetchAllRows()

                if consuming_date_info != ():
                    consuming_date = consuming_date_info[0][1]
                else:
                    consuming_date = ''

                #物料收获时间为空 gaining_date
                gaining_date = ''


                #放行时间 321的posting_date
                sql_pasting_date = "select order_num,max(posting_date) from batch_order_relation where batch = '{batch}' and order_num = '{order_num}' and movement_type in (321) group by order_num;".format(
                    batch=batch_sub, order_num=order_num)
                #logger.info(sql_pasting_date)
                db.query(sql_pasting_date)
                pasting_date_info = db.fetchAllRows()

                if pasting_date_info != ():
                    pasting_date = pasting_date_info[0][1]
                else:
                    pasting_date = ''

            db.close()

            #整合信息
            line_info = dict(id=detail[0], material=detail[1], material_description=detail[2], order_num=detail[3], batch=detail[4], quantity_wi=abs(int(detail[5])), unit=unit, pid=int(detail[7]),
                             creating_date=creating_date,
                             consuming_date=consuming_date, gaining_date=gaining_date, pasting_date=pasting_date)

            #logger.info(line_info)
            box.append(line_info)


            #当前batch等于　上级batch 就继续
            if batch == batch_sub:
                continue
            #还有下级组件
            elif relation_batches != '':
                #logger.info(relation_batches)
                #logger.info(batch_sub)
                get_tree_other_level_node_info(dbconfig, batch_sub, relation_batches, box)

        #logger.info(box)
        return box
    except Exception as e:
        print(e)

def get_tree_other_level_node_info(dbconfig, batch, relation_batches, box):
    try:
        #组成物料的信息
        db = MySQL(dbconfig)
        #用relation_id找的，不返回pid（同一返回pid=0）,用batches找的返回pid(以区分是第一层节点还是第二层节点)(第一层返回的是成品信息)(时间相关的值和单位在另外的逻辑里)
        sql_detail = "select id,material,material_description,order_num,batch,quantity,relation_batches,pid from batch_order_relation where id in ({relation_batches});".\
            format(relation_batches=relation_batches)
        #logger.info(sql_detail)
        db.query(sql_detail)
        detail_info = db.fetchAllRows()
        db.close()

        for detail in detail_info:
            db = MySQL(dbconfig)
            #单位unit
            material = detail[1]
            material_description = detail[2]
            sql_unit = "select unit from unit_info where material = '{material}' and material_description = '{material_description}';".format(material=material, material_description=material_description)
            #logger.info(sql_unit)
            db.query(sql_unit)
            unit_info = db.fetchOneRow()
            #logger.info(unit_info)
            if unit_info != ():
                unit = unit_info[0]
            else:
                unit = ''
            #logger.info(unit)

            #如果不再包含下级组件　则展示　　生成时间='',　消耗时间,物料收货时间,放行时间; 若包含下级组件则展示　生成时间,消耗时间,物料收货时间='', 放行时间

            batch_sub = detail[4]
            #logger.info(batch_sub)
            order_num = detail[3]
            #logger.info(order_num)

            #TODO:这个地方找的不对用１０１重新找！！！！！！
            #sql_relation_batches = "select relation_batches from batch_order_relation where batch = '{batch_sub}' and order_num = '{order_num}' and movement_type in (101) order by posting_date desc limit 1;". \
            #    format(batch_sub=batch_sub, order_num=order_num)
            sql_relation_batches = "select relation_batches from batch_order_relation where batch = '{batch_sub}' and movement_type in (101) order by posting_date desc limit 1;". \
                format(batch_sub=batch_sub)
            #logger.info(sql_relation_batches)
            db.query(sql_relation_batches)
            relation_batches_info = db.fetchAllRows()

            if relation_batches_info == ():
                relation_batches = ''
            else:
                relation_batches = relation_batches_info[0][0]

            #logger.info(relation_batches)
            #不再包含下级组件
            if relation_batches == '':
                #生成时间 为空
                creating_date = ''

                #消耗时间261	consuming_date
                sql_consuming_date = "select order_num,max(posting_date) from batch_order_relation where batch = '{batch}' and order_num = '{order_num}' and movement_type in (261) group by order_num;".format(
                    batch=batch_sub, order_num=order_num)
                #logger.info(sql_consuming_date)
                db.query(sql_consuming_date)
                consuming_date_info = db.fetchAllRows()

                if consuming_date_info != ():
                    consuming_date = consuming_date_info[0][1]
                else:
                    consuming_date = ''

                #物料收获时间101 gaining_date
                sql_gaining_date = "select order_num,max(posting_date) from batch_order_relation where batch = '{batch}' and order_num = '{order_num}' and movement_type in (101) group by order_num;".format(
                    batch=batch_sub, order_num=order_num)
                #logger.info(sql_gaining_date)
                db.query(sql_gaining_date)
                gaining_date_info = db.fetchAllRows()

                if gaining_date_info != ():
                    gaining_date = gaining_date_info[0][1]
                else:
                    gaining_date = ''


                #放行时间 321的posting_date
                sql_pasting_date = "select order_num,max(posting_date) from batch_order_relation where batch = '{batch}' and order_num = '{order_num}' and movement_type in (321) group by order_num;".format(
                    batch=batch_sub,order_num=order_num)
                #logger.info(sql_pasting_date)
                db.query(sql_pasting_date)
                pasting_date_info = db.fetchAllRows()

                if pasting_date_info != ():
                    pasting_date = pasting_date_info[0][1]
                else:
                    pasting_date = ''

            #包含下级组件
            else:
                #生成时间 101的posting_date
                sql_creating_date = "select order_num,max(posting_date) from batch_order_relation where batch = '{batch}' and order_num = '{order_num}' and movement_type in (101) group by order_num;".format(
                    batch=batch_sub,order_num=order_num)
                #logger.info(sql_creating_date)
                db.query(sql_creating_date)
                creating_date_info = db.fetchAllRows()

                if creating_date_info != ():
                    creating_date = creating_date_info[0][1]
                else:
                    creating_date = ''

                #消耗时间为空	consuming_date
                sql_consuming_date = "select order_num,max(posting_date) from batch_order_relation where batch = '{batch}' and order_num = '{order_num}' and movement_type in (261) group by order_num;".format(
                    batch=batch_sub, order_num=order_num)
                #logger.info(sql_consuming_date)
                db.query(sql_consuming_date)
                consuming_date_info = db.fetchAllRows()

                if consuming_date_info != ():
                    consuming_date = consuming_date_info[0][1]
                else:
                    consuming_date = ''

                #物料收获时间为空 gaining_date
                gaining_date = ''


                #放行时间 321的posting_date
                sql_pasting_date = "select order_num,max(posting_date) from batch_order_relation where batch = '{batch}' and order_num = '{order_num}' and movement_type in (321) group by order_num;".format(
                    batch=batch_sub, order_num=order_num)
                #logger.info(sql_pasting_date)
                db.query(sql_pasting_date)
                pasting_date_info = db.fetchAllRows()

                if pasting_date_info != ():
                    pasting_date = pasting_date_info[0][1]
                else:
                    pasting_date = ''

            db.close()

            #整合信息
            line_info = dict(id=detail[0], material=detail[1], material_description=detail[2], order_num=detail[3], batch=detail[4], quantity_wi=abs(int(detail[5])), unit=unit, pid=int(detail[7]),
                             creating_date=creating_date,
                             consuming_date=consuming_date, gaining_date=gaining_date, pasting_date=pasting_date)

            #logger.info(line_info)
            box.append(line_info)


            #当前batch等于　上级batch 就继续
            if batch == batch_sub:
                continue
            #还有下级组件
            elif relation_batches != '':
                #logger.info(relation_batches)
                #logger.info(batch_sub)
                get_tree_first_level_node_info(dbconfig, batch_sub, relation_batches, box)

        #logger.info(box)
        return box
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
