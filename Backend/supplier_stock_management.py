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

#供货类型
supply_type_col = 0

#material 物料号
material_col = 1

#Material Description 物料描述
material_description_col = 2

#单位
unit_col = 3

#供应商
supplier_col = 4

#圣特物料需求
sante_material_requirements_col = 5

#供应商库存（已备货）
supplier_inventory_col = 6

#供应商在产数量
supplier_production_quantity_col = 7

#预计完成时间
estimate_completion_time_col = 8

#圣特采购订单数量
sante_purchase_order_quantity_col = 9

#圣特到货时间
sante_arrival_time_col = 10

#供应商发货时间
supplier_delivery_time_col = 11

file_address = r'/data1/mycode/WareHouse/Backend/'


def Preservative(base_info):
    if table.cell(j, base_info).value != '':
        str_info = str(table.cell(j, base_info).value)
        if '.' in str(str_info):
            res = str_info.split('.')[0]
        else:
            res = table.cell(j, base_info).value.encode('utf-8')
    else:
        res = ""
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
        #print (datestr)
        datestr = str(datestr).split(' ')[0]
        datestr = "'" + datestr + "'"
        # print datestr
    else:
        #datestr = "'" + '1970-12-01' + "'"
        datestr = "0"
    # print datestr
    return datestr

# 先判断是否为空；然后取出浮点型
def Preservative_float(base_info):
    if table.cell(j, base_info).value != '':
        res = table.cell(j, base_info).value
    else:
        res = 0
    return res


def flush_batch_order_relation(dbconfig):
    db = MySQL(dbconfig)
    sql = "truncate table tasly_warehouse.supplier_stock_management"
    db.insert(sql)
    db.close()



def insert_batch_order_relation(dbconfig, supply_type,material,material_description,unit,supplier,sante_material_requirements,supplier_inventory,supplier_production_quantity,estimate_completion_time,sante_purchase_order_quantity,sante_arrival_time,supplier_delivery_time):
    db = MySQL(dbconfig)

    sql = "INSERT INTO tasly_warehouse.supplier_stock_management (supply_type,material,material_description,unit,supplier,sante_material_requirements,supplier_inventory,supplier_production_quantity,estimate_completion_time,sante_purchase_order_quantity,sante_arrival_time,supplier_delivery_time) " \
          "VALUES ('{supply_type}','{material}','{material_description}','{unit}','{supplier}','{sante_material_requirements}','{supplier_inventory}','{supplier_production_quantity}',{estimate_completion_time},'{sante_purchase_order_quantity}',{sante_arrival_time},{supplier_delivery_time});".\
        format(supply_type=supply_type, material=material, material_description=material_description, unit=unit, supplier=supplier, sante_material_requirements=sante_material_requirements, supplier_inventory=supplier_inventory,
               supplier_production_quantity=supplier_production_quantity, estimate_completion_time=estimate_completion_time, sante_purchase_order_quantity=sante_purchase_order_quantity, sante_arrival_time=sante_arrival_time, supplier_delivery_time=supplier_delivery_time)
    print(sql)
    db.insert(sql)
    db.close()


for i in range(1, files_num + 1):
    try:
        print ('开始处理文件', i)
        address = file_address + 'supplier_stock_management.xls'
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

            supply_type = Preservative_str(supply_type_col)
            #print (supply_type)

            material = Preservative(material_col)
            # print (material)

            material_description = Preservative_str(material_description_col)
            # print (material_description)

            unit = Preservative_str(unit_col)
            # print (unit)

            supplier = Preservative_str(supplier_col)
            # print (supplier)

            sante_material_requirements = Preservative_str(sante_material_requirements_col)
            # print (sante_material_requirements)

            supplier_inventory = Preservative_str(supplier_inventory_col)
            # print (supplier_inventory)

            supplier_production_quantity = Preservative_str(supplier_production_quantity_col)
            # print (supplier_production_quantity)

            estimate_completion_time = Preservative_date(estimate_completion_time_col)
            # print (estimate_completion_time)

            sante_purchase_order_quantity = Preservative_str(sante_purchase_order_quantity_col)
            # print (sante_purchase_order_quantity)

            sante_arrival_time = Preservative_date(sante_arrival_time_col)
            # print (sante_arrival_time)

            supplier_delivery_time = Preservative_date(supplier_delivery_time_col)
            # print (supplier_delivery_time)

            insert_batch_order_relation(dbconfig, supply_type, material, material_description, unit, supplier,
                                        sante_material_requirements, supplier_inventory, supplier_production_quantity,
                                        estimate_completion_time, sante_purchase_order_quantity, sante_arrival_time,
                                        supplier_delivery_time)


    except Exception as e:
        print (e)
        continue

    print ('文件%d处理完成' % i)