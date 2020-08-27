# -*- coding: utf-8 -*-

"""
Created on 2020-8-18


@module: build tree
@used: build material tree
"""

from utils.MyCONN import MySQL





def flush_batch_order_relation_batches(dbconfig):
    db = MySQL(dbconfig)
    sql = "update tasly_warehouse.batch_order_relation set batches = '';"
    db.insert(sql)
    db.close()


def insert_batch_order_relation_batches(dbconfig):
    try:
        db = MySQL(dbconfig)
        sql = "select id,order_num from batch_order_relation where movement_type in (101) and order_num != '';"
        db.query(sql)
        order_num_id_info = db.fetchAllRows()
        db.close()

        for batch_order_relation_id, order_num in order_num_id_info:
            #print(batch_order_relation_id, order_num)
            db_component_list = MySQL(dbconfig)
            sql_get_batches = "select id from component_list where order_num = '{order_num}' and batch != '';".format(order_num=order_num)
            db_component_list.query(sql_get_batches)
            batches_info = db_component_list.fetchAllRows()
            db_component_list.close()
            if batches_info != ():
                #print(batches_info)
                batches_list = []
                for batches in batches_info:
                    batches_list.append(str(batches[0]))

                batches_result = ','.join(batches_list)

                db_batch_order_relation = MySQL(dbconfig)
                sql_update_batches = "update batch_order_relation set batches = '{batches_result}' where id = {batch_order_relation_id};".\
                    format(batches_result=batches_result,batch_order_relation_id=batch_order_relation_id)
                #print(sql_update_batches)
                db_batch_order_relation.update(sql_update_batches)
                db_batch_order_relation.close()


    except Exception as e:
        print(e)


def flush_component_list_batches(dbconfig):
    db = MySQL(dbconfig)
    sql = "update tasly_warehouse.component_list set batches = '';"
    db.insert(sql)
    db.close()


def insert_component_list_batches(dbconfig):
    try:
        db = MySQL(dbconfig)
        sql = "select id,batch from component_list where order_num != '' and batch != '';"
        db.query(sql)
        batch_id_info = db.fetchAllRows()
        db.close()

        for component_list_id, batch in batch_id_info:
            #print(component_list_id, batch)
            db_batch_order_relation = MySQL(dbconfig)
            sql_get_batches = "select batches from batch_order_relation where batch = '{batch}' and movement_type in (101) and order_num != '' and batches != '' order by posting_date limit 1;".format(
                batch=batch)
            #print(sql_get_batches)
            db_batch_order_relation.query(sql_get_batches)
            batches_info = db_batch_order_relation.fetchAllRows()
            #print(batches_info)
            db_batch_order_relation.close()

            if batches_info != ():
                #print(batches_info[0])
                batches = batches_info[0][0]

                db_component_list = MySQL(dbconfig)
                sql_update_batches = "update component_list set batches = '{batches}' where id = {component_list_id};". \
                    format(batches=batches, component_list_id=component_list_id)
                #print(sql_update_batches)
                db_component_list.update(sql_update_batches)
                db_component_list.close()

    except Exception as e:
        print(e)


def flush_component_list_pid(dbconfig):
    db = MySQL(dbconfig)
    sql = "update tasly_warehouse.component_list set pid = '';"
    db.insert(sql)
    db.close()

def insert_component_list_pid(dbconfig):
    try:
        db = MySQL(dbconfig)
        sql = "select id from component_list where order_num != '' and batch != '';"
        db.query(sql)
        component_list_id_info = db.fetchAllRows()
        db.close()

        for component_list_id in component_list_id_info:
            #print(component_list_id[0])
            db_component_list = MySQL(dbconfig)
            sql_get_batches = "select id from component_list where batches like '%{component_list_id}%' and batch != '';".format(component_list_id=component_list_id[0])
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
                sql_update_batches = "update component_list set pid = '{component_list_pid_result}' where id = {component_list_id};". \
                    format(component_list_pid_result=component_list_pid_result, component_list_id=component_list_id[0])
                #print(sql_update_batches)
                db_component_list.update(sql_update_batches)
                db_component_list.close()





    except Exception as e:
        print(e)



if __name__ == '__main__':
    dbconfig = {'host': '127.0.0.1',
                'port': 4999,
                'user': 'root',
                'passwd': 'root',
                'db': 'tasly_warehouse',
                'charset': 'utf8'}

    flush_batch_order_relation_batches(dbconfig)

    insert_batch_order_relation_batches(dbconfig)

    flush_component_list_batches(dbconfig)

    insert_component_list_batches(dbconfig)

    flush_component_list_pid(dbconfig)

    insert_component_list_pid(dbconfig)