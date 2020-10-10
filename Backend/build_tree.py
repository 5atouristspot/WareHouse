# -*- coding: utf-8 -*-

"""
Created on 2020-8-18


@module: build tree
@used: build material tree
"""

from utils.MyCONN import MySQL

from utils.MyFILE import project_abdir, recursiveSearchFile
import configparser
config = configparser.ConfigParser()
colConfig = recursiveSearchFile(project_abdir, '*metaConfig.ini')[0]
config.read(colConfig)

def flush_batch_order_relation_relationbatches(dbconfig):
    db = MySQL(dbconfig)
    sql = "update tasly_warehouse.batch_order_relation set relation_batches = '';"
    db.insert(sql)
    db.close()

def insert_batch_order_relation_relationbatches(dbconfig):
    try:
        db = MySQL(dbconfig)
        #sql = "select material,material_description,max(id),max(order_num) from batch_order_relation where movement_type in (101) and order_num != '' and batch = '000203007T' group by material,material_description;"
        sql = "select material,material_description,batch,max(id),max(order_num) from batch_order_relation where movement_type in (101) and order_num != '' group by material,material_description,batch;"
        db.query(sql)
        order_num_id_info = db.fetchAllRows()
        db.close()

        for material,material_description,batch,batch_order_relation_id, order_num in order_num_id_info:
            #print(batch_order_relation_id, order_num)
            db_component_list = MySQL(dbconfig)
            sql_get_batches = "select batch,max(id) from batch_order_relation where order_num = '{order_num}' and movement_type in (261) group by batch ;".format(order_num=order_num)
            db_component_list.query(sql_get_batches)
            relationbatches_info = db_component_list.fetchAllRows()
            db_component_list.close()
            if relationbatches_info != ():
                #print(batches_info)
                relationbatches_list = []
                for relationbatches in relationbatches_info:
                    relationbatches_list.append(str(relationbatches[1]))

                relationbatches_result = ','.join(relationbatches_list)

                db_batch_order_relation = MySQL(dbconfig)
                sql_update_batches = "update batch_order_relation set relation_batches = '{relationbatches_result}' where id = {batch_order_relation_id};".\
                    format(relationbatches_result=relationbatches_result, batch_order_relation_id=batch_order_relation_id)
                #print(sql_update_batches)
                db_batch_order_relation.update(sql_update_batches)
                db_batch_order_relation.close()


    except Exception as e:
        print(e)


def flush_batch_order_relation_pid(dbconfig):
    db = MySQL(dbconfig)
    sql = "update tasly_warehouse.batch_order_relation set pid = '';"
    db.insert(sql)
    db.close()

'''
def insert_batch_order_relation_pid(dbconfig):
    try:
        db = MySQL(dbconfig)
        sql = "select id from batch_order_relation where order_num != '' and batch != '' and movement_type in (261);"
        db.query(sql)
        component_list_id_info = db.fetchAllRows()
        db.close()

        for component_list_id in component_list_id_info:
            #print(component_list_id[0])
            db_component_list = MySQL(dbconfig)
            sql_get_batches = "select id from batch_order_relation where (relation_batches like '%,{component_list_id},%' or relation_batches like '{component_list_id},%' or relation_batches like '%,{component_list_id}') and batch != '' and movement_type in (101);".format(component_list_id=component_list_id[0])
            db_component_list.query(sql_get_batches)
            component_list_pid_info = db_component_list.fetchAllRows()
            db_component_list.close()

            if component_list_pid_info != ():
                #print('XXXXX')
                #print(component_list_pid_info)
                #print('XXXXX')
                batches_list = []
                for component_list_pid in component_list_pid_info:
                    batches_list.append(str(component_list_pid[0]))

                component_list_pid_result = ','.join(batches_list)
                #print('YYYYY')
                #print(component_list_pid_result)
                #print('YYYYY')

                db_component_list = MySQL(dbconfig)
                sql_update_batches = "update batch_order_relation set pid = '{component_list_pid_result}' where id = {component_list_id};". \
                    format(component_list_pid_result=component_list_pid_result, component_list_id=component_list_id[0])
                #print(sql_update_batches)
                db_component_list.update(sql_update_batches)
                db_component_list.close()

    except Exception as e:
        print(e)
'''

def insert_batch_order_relation_pid(dbconfig):
    try:
        db = MySQL(dbconfig)
        sql = "select id from batch_order_relation where order_num != '' and batch != '' and movement_type in (261);"
        db.query(sql)
        component_list_id_info = db.fetchAllRows()
        db.close()

        for component_list_id in component_list_id_info:
            #print(component_list_id[0])
            db_component_list = MySQL(dbconfig)
            sql_get_batch_101 = "select batch from batch_order_relation where (relation_batches like '%,{component_list_id},%' or relation_batches like '{component_list_id},%' or relation_batches like '%,{component_list_id}') and batch != '' and movement_type in (101);".format(component_list_id=component_list_id[0])
            db_component_list.query(sql_get_batch_101)
            component_list_batch_info_101 = db_component_list.fetchAllRows()
            db_component_list.close()

            if component_list_batch_info_101 != ():

                #print('XXXXX')
                #print(component_list_pid_info)
                #print('XXXXX')
                batches_list = []
                for component_list_batch_101 in component_list_batch_info_101:
                    db_component_list = MySQL(dbconfig)
                    sql_get_batch_261 = "select id from batch_order_relation where batch = '{component_list_batch_101}' and movement_type in (261) order by posting_date desc;".format(
                        component_list_batch_101=component_list_batch_101[0])
                    db_component_list.query(sql_get_batch_261)
                    component_list_batch_id_info_261 = db_component_list.fetchOneRow()
                    #print('XXXXXX')
                    #print(component_list_batch_id_info_261)
                    #print('XXXXXXX')
                    db_component_list.close()
                    if component_list_batch_id_info_261 is not None:
                        for component_list_batch_id_261 in component_list_batch_id_info_261:
                            print('component_list_batch_id_info_261')
                            print(component_list_batch_id_info_261)
                            print('component_list_batch_id_info_261')
                            batches_list.append(str(component_list_batch_id_261))

                component_list_pid_result = ','.join(batches_list)
                #print('YYYYY')
                #print(component_list_pid_result)
                #print('YYYYY')

                db_component_list = MySQL(dbconfig)
                sql_update_batches = "update batch_order_relation set pid = '{component_list_pid_result}' where id = {component_list_id};". \
                    format(component_list_pid_result=component_list_pid_result, component_list_id=component_list_id[0])
                #print(sql_update_batches)
                db_component_list.update(sql_update_batches)
                db_component_list.close()

    except Exception as e:
        print(e)


if __name__ == '__main__':
    dbconfig = {'host': config.get('META', 'host'),
                'port': int(config.get('META', 'port')),
                'user': config.get('META', 'user'),
                'passwd': config.get('META', 'pwd'),
                'db': config.get('META', 'db'),
                'charset': 'utf8'}

    flush_batch_order_relation_relationbatches(dbconfig)

    insert_batch_order_relation_relationbatches(dbconfig)

    flush_batch_order_relation_pid(dbconfig)

    insert_batch_order_relation_pid(dbconfig)