# -*- coding: utf-8 -*-
from utils.MyCONN import MySQL

import time
import xlrd
from xlrd import open_workbook
import os
from datetime import datetime

from utils.MyFILE import project_abdir, recursiveSearchFile
import configparser
config = configparser.ConfigParser()
colConfig = recursiveSearchFile(project_abdir, '*metaConfig.ini')[0]
config.read(colConfig)


# 所需读取文件数
files_num = 1

#material 物料号
material_col = 1

#storage_bin 点位
storage_bin_col = 2

#batch 批号
batch_col = 3

#material_desc 物料名称
material_desc_col = 4

#avail_stock 库存量
avail_stock_col = 5

#unit 单位
unit_col = 6

#last_goods_rec 收货时间
last_goods_rec_col = 7

#date_of_manuf 生产日期
date_of_manuf_col = 8

#sled_bbd 有效期
sled_bbd_col = 9

#next_inspection 复验期
next_inspection_col = 10

#status
status_col = 11


file_address = r'/data1/mycode/WareHouse/Backend/'


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
    print(table.cell(j, base_info))
    print(table.cell(j, base_info).value)
    if table.cell(j, base_info).value != '':
        res = table.cell(j, base_info).value
    else:
        res = ""
    return res

def Preservative_new_date(base_info):
    if table.cell(j, base_info).value != '':
        res = "'"+table.cell(j, base_info).value+"'"
    else:
        res = "''"
    return res

# 先判断是否为空；然后转换er二进制类型取出字符串型
def Preservative_bytes(base_info):
    print(table.cell(j, base_info))
    print(table.cell(j, base_info).value)
    res = table.cell(j, base_info).value
    if res != '':
        res_str = table.cell(j, base_info).value
        if type(table.cell(j, base_info).value) is bytes:
            res_str = res.decode()
    else:
        res_str = ""
    return res_str

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


def flush_tasly_warehouse_storage_info(dbconfig):
    db = MySQL(dbconfig)
    sql = "truncate table tasly_warehouse.tasly_warehouse_storage_info"
    db.insert(sql)
    db.close()

def insert_tasly_warehouse_storage_info(dbconfig, material, storage_bin, batch, material_desc, avail_stock, unit, last_goods_rec, date_of_manuf, sled_bbd, next_inspection, status):
    db = MySQL(dbconfig)

    sql = "INSERT INTO tasly_warehouse.tasly_warehouse_storage_info (material,storage_bin, batch, material_desc, avail_stock, unit, last_goods_rec, date_of_manuf, sled_bbd, next_inspection, status) " \
          "VALUES ('{material}','{storage_bin}','{batch}','{material_desc}',{avail_stock},'{unit}',{last_goods_rec},{date_of_manuf},{sled_bbd},{next_inspection},'{status}');".\
        format(material=material, storage_bin=storage_bin, batch=batch, material_desc=material_desc, avail_stock=avail_stock,unit=unit, last_goods_rec=last_goods_rec, date_of_manuf=date_of_manuf, sled_bbd=sled_bbd, next_inspection=next_inspection, status=status)
    #print (sql)
    db.insert(sql)
    db.close()


for i in range(1, files_num + 1):
    try:
        print ('开始处理文件', i)
        address = file_address + 'storage.xls'
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

        flush_tasly_warehouse_storage_info(dbconfig)

        for j in range(1, rows):
            print(str(table.cell(j, 0)))
            #if "number" not in str(table.cell(j, 0)):
            #    continue
            if "NUM" in str(table.cell(j, 0)):
                continue

            material = Preservative_str(material_col)
            print (material)

            storage_bin = Preservative_str(storage_bin_col)
            print (storage_bin)
            batch = Preservative_bytes(batch_col)
            material_desc = Preservative_str(material_desc_col)
            #print material_desc

            avail_stock = Preservative_float(avail_stock_col)
            #print avail_stock

            unit = Preservative_str(unit_col)
            #print unit

            last_goods_rec = Preservative_new_date(last_goods_rec_col)
            print (last_goods_rec)
            #last_goods_rec = datetime(last_goods_rec).strftime('yyyy/m/d')
            #print("XXXXXXXXX")
            #print(last_goods_rec)

            date_of_manuf = Preservative_new_date(date_of_manuf_col)
            #print date_of_manuf
            #date_of_manuf = datetime(date_of_manuf).strftime('yyyy/m/d')

            sled_bbd = Preservative_new_date(sled_bbd_col)
            #print sled_bbd
            #sled_bbd = datetime(sled_bbd).strftime('yyyy/m/d')

            next_inspection = Preservative_new_date(next_inspection_col)
            #print next_inspection
            #next_inspection = datetime(next_inspection).strftime('yyyy/m/d')

            status = Preservative_str(status_col)
            #print status
            '''
            if status == '待检':
                status = 'Q'
            elif status == '冻结':
                status = 'S'
            elif status == '待处理':
                status = 'D'
            '''
            insert_tasly_warehouse_storage_info(dbconfig, material, storage_bin,  batch, material_desc, avail_stock, unit,
                                                last_goods_rec, date_of_manuf, sled_bbd, next_inspection, status)

    except Exception as e:
        print (e)
        continue

    print ('文件%d处理完成' % i)
