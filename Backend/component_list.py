#! /data1/mycode/WareHouse/Backend/venv/bin/python
# -*- coding: utf-8 -*-
from utils.MyCONN import MySQL

import time
import xlrd
from xlrd import open_workbook
import os


# 所需读取文件数
files_num = 1

#order_num
order_num_col = 0

#material
material_col = 1

#item_component_list
item_component_list_col = 2

#requirement_date
requirement_date_col = 3

#requantity
requantity_col = 4

#quantity_wi
quantity_wi_col = 5

#unit
unit_col = 6

#material_description
material_description_col = 7

#batch
batch_col = 8

#operation_act
operation_act_col = 9

#reitem
reitem_col = 10

#plant
plant_col = 11

#stroage_location
stroage_location_col = 12

#message_type
message_type_col = 13

#system_status
system_status_col = 14




file_address = r'/data1/mycode/WareHouse/Backend/'


# 先判断是否为空；然后判断是否为字符串型
def Preservative(base_info):
    if table.cell(j, base_info).value != '':
        sex_old = str(table.cell(j, base_info).value)
        if '.' in str(sex_old):
            res = sex_old.split('.')[0]
        else:
            res = table.cell(j, base_info).value.encode('utf-8')
    else:
        res = ""
    return res


# 先判断是否为空；然后取出浮点型
def Preservative_float(base_info):
    if table.cell(j, base_info).value != '':
        res = table.cell(j, base_info).value
    else:
        res = 0
    return res

# 先判断是否为空；然后取出字符串型
def Preservative_str(base_info):
    if table.cell(j, base_info).value != '':
        res = table.cell(j, base_info).value
    else:
        res = "'" + '' + "'"
    return res

# 先判断是否为空；然后取出字符串型
def Preservative_batch(base_info):
    if table.cell(j, base_info).value != '':
        res = table.cell(j, base_info).value
    else:
        res = ""
    return res

def Preservative_date(datestr_col):
    if table.cell(j, datestr_col).value != '':
        datestr = xlrd.xldate.xldate_as_datetime(table.cell(j, datestr_col).value, 0)
        print (datestr)
        datestr = str(datestr).split(' ')[0]
        datestr = "'" + datestr + "'"
        # print datestr
    else:
        #datestr = "'" + '1970-12-01' + "'"
        datestr = "0"
    # print datestr
    return datestr


def flush_component_list(dbconfig):
    db = MySQL(dbconfig)
    sql = "delete from tasly_warehouse.component_list"
    db.insert(sql)
    db.close()

def insert_component_list(dbconfig, order_num,material,item_component_list,requirement_date,requantity,quantity_wi,unit,material_description,batch,operation_act,reitem,plant,stroage_location,message_type,system_status):
    db = MySQL(dbconfig)

    sql = "INSERT INTO tasly_warehouse.component_list (order_num,material,item_component_list,requirement_date,requantity,quantity_wi,unit,material_description,batch,operation_act,reitem,plant,stroage_location,message_type,system_status) " \
          "VALUES ('{order_num}','{material}','{item_component_list}',{requirement_date},{requantity},{quantity_wi},'{unit}','{material_description}','{batch}','{operation_act}','{reitem}','{plant}','{stroage_location}','{message_type}','{system_status}');".\
        format(order_num=order_num, material=material, item_component_list=item_component_list, requirement_date=requirement_date, requantity=requantity, quantity_wi=quantity_wi, unit=unit, material_description=material_description, batch=str(batch),
               operation_act=operation_act, reitem=reitem, plant=plant, stroage_location=stroage_location, message_type=message_type, system_status=system_status)
    print(sql)
    db.insert(sql)
    db.close()


for i in range(1, files_num + 1):
    try:
        print ('开始处理文件', i)
        address = file_address + 'component_list.xls'
        print ('文件路径', address)
        files = xlrd.open_workbook(address)
        table = files.sheet_by_index(0)
        rows = table.nrows
        #print rows

        dbconfig = {'host': '127.0.0.1',
                    'port': 4999,
                    'user': 'root',
                    'passwd': 'root',
                    'db': 'tasly_warehouse',
                    'charset': 'utf8'}

        flush_component_list(dbconfig)

        for j in range(1, rows):
            print(str(table.cell(j, 0)))
            if "text" not in str(table.cell(j, 0)):
                continue

            order_num = Preservative_str(order_num_col)
            #print order_num

            material = Preservative_str(material_col)
            print (material)

            item_component_list = Preservative_str(item_component_list_col)
            #print item_component_list

            requirement_date = Preservative_date(requirement_date_col)
            #print requirement_date

            requantity = Preservative_float(requantity_col)
            #print requantity

            quantity_wi = Preservative_float(quantity_wi_col)
            #print quantity_wi

            unit = Preservative_str(unit_col)
            #print unit

            material_description = Preservative_str(material_description_col)
            #print material_description

            batch = Preservative_batch(batch_col)
            #print batch

            operation_act = Preservative_str(operation_act_col)
            #print operation_act

            reitem = Preservative_str(reitem_col)
            #print reitem

            plant = Preservative_str(plant_col)
            #print plant

            stroage_location = Preservative_str(stroage_location_col)
            #print stroage_location

            message_type = Preservative(message_type_col)
            #print message_type

            system_status = Preservative_str(system_status_col)
            #print system_status


            insert_component_list(dbconfig, order_num,material,item_component_list,requirement_date,requantity,quantity_wi,unit,material_description,batch,operation_act,reitem,plant,stroage_location,message_type,system_status)

    except Exception as e:
        print (e)
        continue

    print ('文件%d处理完成' % i)
