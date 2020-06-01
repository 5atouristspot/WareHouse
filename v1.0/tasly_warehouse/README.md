echo '/data1/mycode/tasly_warehouse/' > /data1/mycode/tasly_warehouse/venv/local/lib/python2.7/site-packages/mypkpath.pth


接口执行用例：
```
curl -i -X GET http://127.0.0.1:3621/api/v1000/elevated/reloaddata

curl -i -X GET http://127.0.0.1:3621/api/v1000/elevated/storagebin?warehouse_type=1

curl -i -X GET http://127.0.0.1:3621/api/v1000/elevated/storagedetail?binum=06-02-20

curl -i -X GET http://127.0.0.1:3621/api/v1000/elevated/utilization_rate?warehouse_type=1


#新增两个模块　batch_type=1（API-原料），batch_type=2（API-成品）
curl -i -X GET http://127.0.0.1:3621/api/v1000/elevated/batchinfo?batch_type=1
返回格式：
[{"status": "Q",　"name": "API-\u539f\u6599", "batch": "19000231"}, {"status": "S","name": "API-\u539f\u6599", "batch": "19000230"}, {"status": "", "name": "API-\u539f\u6599", "batch": "19000219"}, {"status": "Q", "name": "API-\u539f\u6599", "batch": "19000139"}]
ps:每个模块点开后，显示带有　批号（batch）　的按钮

#批号按钮点开后显示具体物料信息，与之前显示具体信息的接口相同
curl -i -X GET http://127.0.0.1:3621/api/v1000/elevated/batchdetail?batch_type=1\&batchnum='19000231'
返回格式：[{"name": "0-material", "value": "10013"}, {"name": "1-storage_bin", "value": "API-\u539f\u6599"}, {"name": "2-status", "value": "Q"}, {"name": "3-batch", "value": "19000231"}, {"name": "4-avail_stock", "value": "20.0"}, {"name": "5-unit", "value": "KG"}, {"name": "6-material_desc", "value": "Zopiclone (Industry)"}, {"name": "7-last_goods_rec", "value": "2019-05-22"}, {"name": "8-date_of_manuf", "value": "2019-04-12"}, {"name": "9-sled_bbd", "value": "2021-03-11"}, {"name": "10-next_inspection", "value": "2020-05-21"}, {"name": "11-inventory_time", "value": "29"}]

#新增一个模块　batch_type=3(CF CABINET)
curl -i -X GET http://127.0.0.1:3621/api/v1000/elevated/batchinfo?batch_type=3

#新增加一个模块　warehouse_type = 9 (冰柜)ZFR-1127 ~ ZFR-1137
curl -i -X GET http://127.0.0.1:3621/api/v1000/elevated/storagebin?warehouse_type=9

#新增一个模块　batch_type=4(VENDOR)
curl -i -X GET http://127.0.0.1:3621/api/v1000/elevated/batchinfo?batch_type=4

#新增加一个模块　warehouse_type = 10 (普通货位2个)
curl -i -X GET http://127.0.0.1:3621/api/v1000/elevated/storagebin?warehouse_type=10

#新增加一个模块　warehouse_type = 11 (样品货位2个)
curl -i -X GET http://127.0.0.1:3621/api/v1000/elevated/storagebin?warehouse_type=11
```


>安装nginx
```
1.apt-get install nginx
```

```
2.修改配置文件，修改默认端口号为88
vim /etc/nginx/sites-available/default

server {
        listen 88 default_server;
        listen [::]:88 default_server;


```

```
3.把前端代码放到nginx www 目录下

cp -Rf ../warehouse /var/www/html/
```

```
4.访问前端代码
http://127.0.0.1:88/warehouse/index.html
```

```
5.开机启动脚本

vim /etc/init.d/bota.sh

#!/bin/bash

/usr/local/mysql5720/bin/mysqld_safe --defaults-file=/data1/mysql4999/my4999.cnf &

sleep 5

source /data1/mycode/tasly_warehouse/venv/bin/activate && nohup python /data1/mycode/tasly_warehouse/botasky/run.py &
exit 0
```
