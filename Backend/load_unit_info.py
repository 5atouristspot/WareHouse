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

#material
material_col = 0

#material_description
material_description_col = 1

#unit
unit_col = 2


file_address = r'/data1/mycode/WareHouse/Backend/'

# 先判断是否为空；然后取出字符串型
def Preservative_str(base_info):
    if table.cell(j, base_info).value != '':
        res = table.cell(j, base_info).value
    else:
        res = "'" + '' + "'"
    return res

def flush_unit_info(dbconfig):
    db = MySQL(dbconfig)
    sql = "delete from tasly_warehouse.unit_info"
    db.insert(sql)
    db.close()

def insert_unit_info(dbconfig, material, material_description, unit):
    db = MySQL(dbconfig)

    sql = "INSERT INTO tasly_warehouse.unit_info (material, material_description, unit) " \
          "VALUES ('{material}','{material_description}','{unit}');".\
        format(material=material, material_description=material_description, unit=unit)
    print(sql)
    db.insert(sql)
    db.close()

for i in range(1, files_num + 1):
    try:
        print ('开始处理文件', i)
        address = file_address + 'unit_info.xls'
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

        flush_unit_info(dbconfig)

        for j in range(1, rows):
            print(str(table.cell(j, 0)))
            if "text" not in str(table.cell(j, 0)):
                continue

            material = Preservative_str(material_col)
            print (material)

            material_description = Preservative_str(material_description_col)
            print (material_description)

            unit = Preservative_str(unit_col)
            print (unit)

            insert_unit_info(dbconfig, material, material_description, unit)

    except Exception as e:
        print (e)
        continue

    print ('文件%d处理完成' % i)