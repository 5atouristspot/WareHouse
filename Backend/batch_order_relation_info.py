#! /data1/mycode/WareHouse/Backend/venv/bin/python
# -*- coding: utf-8 -*-
from utils.MyCONN import MySQL

import time
import xlrd
from xlrd import open_workbook
import os

from utils.MyFILE import project_abdir, recursiveSearchFile
import configparser
config = configparser.ConfigParser()
colConfig = recursiveSearchFile(project_abdir, '*metaConfig.ini')[0]
config.read(colConfig)

# 所需读取文件数
files_num = 1

#material 物料号
material_col = 0

#Material Description 物料描述
material_description_col = 1

#User Name
user_name_col = 2

#Plant
plant_col = 3

#Storage Location
storage_location_col = 4

#Item
item_col = 5

#Movement Type
movement_type_col = 6

#Batch
batch_col = 7

#Order
order_num_col = 8

#Vendor
vendor_col = 9

#Posting Date
posting_date_col = 10

#Material Document
material_document_col = 11

#Purchase Order
purchase_order_col = 12

#Quantity
quantity_col = 13

#Qty in Un. of Entry
qty_u_e_col = 14

#Amount in LC
amount_col = 15

#Document Date
document_date_col = 16





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


def flush_batch_order_relation(dbconfig):
    db = MySQL(dbconfig)
    sql = "truncate table tasly_warehouse.batch_order_relation"
    db.insert(sql)
    db.close()

def insert_batch_order_relation(dbconfig, material, material_description, user_name, plant, storage_location, item, movement_type, batch, order_num, vendor, posting_date, material_document, purchase_order, quantity, qty_u_e, amount, document_date):
    db = MySQL(dbconfig)

    sql = "INSERT INTO tasly_warehouse.batch_order_relation (material, material_description, user_name, plant, storage_location, item, movement_type, batch, order_num, vendor, posting_date, material_document, purchase_order, quantity, qty_u_e, amount, document_date) " \
          "VALUES ('{material}','{material_description}','{user_name}','{plant}','{storage_location}','{item}','{movement_type}','{batch}','{order_num}','{vendor}',{posting_date},'{material_document}','{purchase_order}',{quantity},{qty_u_e},{amount},{document_date});".\
        format(material=material, material_description=material_description, user_name=user_name, plant=plant, storage_location=storage_location,item=item, movement_type=movement_type, batch=batch, order_num=order_num, vendor=vendor, posting_date=posting_date, material_document=material_document, purchase_order=purchase_order, quantity=quantity, qty_u_e=qty_u_e, amount=amount, document_date=document_date)
    print(sql)
    db.insert(sql)
    db.close()


for i in range(1, files_num + 1):
    try:
        print ('开始处理文件', i)
        address = file_address + 'batch_order_relation.xls'
        print ('文件路径', address)
        files = xlrd.open_workbook(address)
        table = files.sheet_by_index(0)
        rows = table.nrows
        #print rows

        dbconfig = {'host': config.get('META', 'host'),
                    'port': int(config.get('META', 'port')),
                    'user': config.get('META', 'user'),
                    'passwd': config.get('META', 'pwd'),
                    'db': config.get('META', 'db'),
                    'charset': 'utf8'}

        flush_batch_order_relation(dbconfig)

        for j in range(1, rows):
            print(str(table.cell(j, 0)))
            if "text" not in str(table.cell(j, 0)):
                continue

            material = Preservative_str(material_col)
            #print material

            material_description = Preservative_str(material_description_col)
            print (material_description)

            user_name = Preservative_str(user_name_col)
            #print user_name

            plant = Preservative_str(plant_col)
            #print plant

            storage_location = Preservative_str(storage_location_col)
            #print storage_location

            item = Preservative_str(item_col)
            #print item

            movement_type = Preservative_str(movement_type_col)
            #print movement_type

            batch = Preservative_str(batch_col)
            #print batch

            order_num = Preservative_str(order_num_col)
            #print order_num

            vendor = Preservative_str(vendor_col)
            #print vendor

            posting_date = Preservative_date(posting_date_col)
            #print posting_date

            material_document = Preservative_str(material_document_col)
            #print material_document

            purchase_order = Preservative_str(purchase_order_col)
            #print purchase_order

            quantity = Preservative_float(quantity_col)
            #print quantity

            qty_un_entry = Preservative_float(qty_u_e_col)
            #print qty_un_entry

            amount = Preservative_float(amount_col)
            #print amount

            document_date = Preservative_date(document_date_col)
            #print document_date

            insert_batch_order_relation(dbconfig, material, material_description, user_name, plant, storage_location, item, movement_type, batch, order_num, vendor, posting_date, material_document, purchase_order, quantity, qty_un_entry, amount, document_date)

    except Exception as e:
        print (e)
        continue

    print ('文件%d处理完成' % i)
