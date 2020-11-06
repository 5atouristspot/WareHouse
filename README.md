# WareHouse
This is a warehouse management system
>Frontend
```
```
>Backend
```
pip install mysqlclient

```
```
测试注册用户接口
curl -i -X POST -H "Content-Type: application/json" -d '{"username":"kkkk","password":"123456"}' http://127.0.0.1:3621/api/users

登陆时获取token
curl -i -u fffff:123456  -X GET -H "Content-Type: application/json"  http://127.0.0.1:3621/api/login

使用token 访问
curl -i -u eyJhbGciOiJIUzUxMiIsImlhdCI6MTU2ODI1Mzc5NiwiZXhwIjoxNTY4MjU0Mzk2fQ.eyJpZCI6M30.V6QaL5VTXM_7oXNN5997R08N3gF3LZcO_iyyOe0Exs9WpLANEc7DhlC2HZltooy72Qoqs6GrfqwjTCnISeIvsw:unused -X GET -H "Content-Type: application/json"  http://127.0.0.1:3621/

业务接口token认证
    curl -i -u eyJhbGciOiJIUzUxMiIsImlhdCI6MTU2ODYwMjI5MywiZXhwIjoxNTY4NjAyODkzfQ.eyJpZCI6M30.2ne7-y1qUM1RyioKqTsthwL2Ik2FNRbed3rbQ8foav9JZ6KNy6PZjhvAl0EH1SS6Af17-GyZRySOKQFFdhT2KQ:unused -X GET -H "Content-Type: application/json"  http://127.0.0.1:3621/api/v1000/elevated/batchdetail?batch_type=1\&batchnum='19000231'
```

```
storagedetail接口
curl -i -u eyJhbGciOiJIUzUxMiIsImlhdCI6MTYwMjQxMjIxNywiZXhwIjoxNjAyNDEyODE3fQ.eyJpZCI6M30.EWv3SviySVVuBBXpjN4wm001CEzTwH5eKc_8LWqQ7U4c_J5w89a0jfnpcP1amqVLKARQeAk8h26vDAzU6R9PSQ:unused -X GET -H "Content-Type: application/json"  http://127.0.0.1:3622/api/v1000/elevated/storagedetail?binum='低温库-研发'\&status='S'

返回的json:

[{"name": "material", "value": "\u8bd5\u5236"}, {"name": "storage_bin", "value": "\u4f4e\u6e29\u5e93-\u7814\u53d1"}, {"name": "status", "value": "S"}, {"name": "batch", "value": "T201901001(800912310)"}, {"name": "avail_stock", "value": "10.5"}, {"name": "unit", "value": "KG"}, {"name": "material_desc", "value": "\u6c34\u98de\u84df\u5bbe\u80f6\u56ca35mg\u88c5\u56ca\u6df7\u5408\u7269"}, {"name": "last_goods_rec", "value": "2019-04-25"}, {"name": "date_of_manuf", "value": "0"}, {"name": "sled_bbd", "value": "0"}, {"name": "next_inspection", "value": "0"}, {"name": "inventory_time", "value": "561"}, {"name": "material", "value": "\u8bd5\u5236"}, {"name": "storage_bin", "value": "\u4f4e\u6e29\u5e93-\u7814\u53d1"}, {"name": "status", "value": "S"}, {"name": "batch", "value": "G120051P177"}, {"name": "avail_stock", "value": "78000.0"}, {"name": "unit", "value": "EA"}, {"name": "material_desc", "value": "\u6c34\u6797\u4f73\u5370\u5b571#\u7a7a\u5fc3\u80f6\u56ca\u58f3"}, {"name": "last_goods_rec", "value": "2002-06-10"}, {"name": "date_of_manuf", "value": "2020-05-30"}, {"name": "sled_bbd", "value": "2020-04-30"}, {"name": "next_inspection", "value": "0"}, {"name": "inventory_time", "value": "6724"}, {"name": "material", "value": "\u8bd5\u5236"}, {"name": "storage_bin", "value": "\u4f4e\u6e29\u5e93-\u7814\u53d1"}, {"name": "status", "value": "S"}, {"name": "batch", "value": "851707001"}, {"name": "avail_stock", "value": "52790.0"}, {"name": "unit", "value": "EA"}, {"name": "material_desc", "value": "\u975e\u6d1b\u5730\u5e73\u7f13\u91ca\u5305\u8863\u72472.5mg*1*10\u7247"}, {"name": "last_goods_rec", "value": "2018-07-20"}, {"name": "date_of_manuf", "value": "2018-07-01"}, {"name": "sled_bbd", "value": "0"}, {"name": "next_inspection", "value": "0"}, {"name": "inventory_time", "value": "840"}, {"name": "material", "value": "\u8bd5\u5236"}, {"name": "storage_bin", "value": "\u4f4e\u6e29\u5e93-\u7814\u53d1"}, {"name": "status", "value": "S"}, {"name": "batch", "value": "851707002"}, {"name": "avail_stock", "value": "32550.0"}, {"name": "unit", "value": "EA"}, {"name": "material_desc", "value": "\u975e\u6d1b\u5730\u5e73\u7f13\u91ca\u5305\u8863\u72472.5mg*1*10\u7247"}, {"name": "last_goods_rec", "value": "2018-07-20"}, {"name": "date_of_manuf", "value": "2018-07-01"}, {"name": "sled_bbd", "value": "0"}, {"name": "next_inspection", "value": "0"}, {"name": "inventory_time", "value": "840"}, {"name": "material", "value": "\u8bd5\u5236"}, {"name": "storage_bin", "value": "\u4f4e\u6e29\u5e93-\u7814\u53d1"}, {"name": "status", "value": "S"}, {"name": "batch", "value": "851707003"}, {"name": "avail_stock", "value": "31510.0"}, {"name": "unit", "value": "EA"}, {"name": "material_desc", "value": "\u975e\u6d1b\u5730\u5e73\u7f13\u91ca\u5305\u8863\u72472.5mg*1*10\u7247"}, {"name": "last_goods_rec", "value": "2018-07-20"}, {"name": "date_of_manuf", "value": "2018-07-01"}, {"name": "sled_bbd", "value": "0"}, {"name": "next_inspection", "value": "0"}, {"name": "inventory_time", "value": "840"}, {"name": "material", "value": "\u8bd5\u5236"}, {"name": "storage_bin", "value": "\u4f4e\u6e29\u5e93-\u7814\u53d1"}, {"name": "status", "value": "S"}, {"name": "batch", "value": "851807001"}, {"name": "avail_stock", "value": "31310.0"}, {"name": "unit", "value": "EA"}, {"name": "material_desc", "value": "\u975e\u6d1b\u5730\u5e73\u7f13\u91ca\u5305\u8863\u72475mg*1*10\u7247"}, {"name": "last_goods_rec", "value": "2018-07-20"}, {"name": "date_of_manuf", "value": "2018-07-01"}, {"name": "sled_bbd", "value": "0"}, {"name": "next_inspection", "value": "0"}, {"name": "inventory_time", "value": "840"}, {"name": "material", "value": "\u8bd5\u5236"}, {"name": "storage_bin", "value": "\u4f4e\u6e29\u5e93-\u7814\u53d1"}, {"name": "status", "value": "S"}, {"name": "batch", "value": "851807002"}, {"name": "avail_stock", "value": "31370.0"}, {"name": "unit", "value": "EA"}, {"name": "material_desc", "value": "\u975e\u6d1b\u5730\u5e73\u7f13\u91ca\u5305\u8863\u72475mg*1*10\u7247"}, {"name": "last_goods_rec", "value": "2018-07-20"}, {"name": "date_of_manuf", "value": "2018-07-01"}, {"name": "sled_bbd", "value": "0"}, {"name": "next_inspection", "value": "0"}, {"name": "inventory_time", "value": "840"}, {"name": "material", "value": "\u8bd5\u5236"}, {"name": "storage_bin", "value": "\u4f4e\u6e29\u5e93-\u7814\u53d1"}, {"name": "status", "value": "S"}, {"name": "batch", "value": "851807003"}, {"name": "avail_stock", "value": "32100.0"}, {"name": "unit", "value": "EA"}, {"name": "material_desc", "value": "\u975e\u6d1b\u5730\u5e73\u7f13\u91ca\u5305\u8863\u72475mg*1*10\u7247"}, {"name": "last_goods_rec", "value": "2018-07-20"}, {"name": "date_of_manuf", "value": "2018-07-01"}, {"name": "sled_bbd", "value": "0"}, {"name": "next_inspection", "value": "0"}, {"name": "inventory_time", "value": "840"}, {"name": "material", "value": "\u8bd5\u5236"}, {"name": "storage_bin", "value": "\u4f4e\u6e29\u5e93-\u7814\u53d1"}, {"name": "status", "value": "S"}, {"name": "batch", "value": "801807001V"}, {"name": "avail_stock", "value": "35.49"}, {"name": "unit", "value": "KG"}, {"name": "material_desc", "value": "\u975e\u6d1b\u5730\u5e73\u7f13\u91ca\u72472.5mg"}, {"name": "last_goods_rec", "value": "2018-08-16"}, {"name": "date_of_manuf", "value": "2018-07-01"}, {"name": "sled_bbd", "value": "0"}, {"name": "next_inspection", "value": "0"}, {"name": "inventory_time", "value": "813"}, {"name": "material", "value": "\u8bd5\u5236"}, {"name": "storage_bin", "value": "\u4f4e\u6e29\u5e93-\u7814\u53d1"}, {"name": "status", "value": "S"}, {"name": "batch", "value": "801807002V"}, {"name": "avail_stock", "value": "39.26"}, {"name": "unit", "value": "KG"}, {"name": "material_desc", "value": "\u975e\u6d1b\u5730\u5e73\u7f13\u91ca\u72472.5mg"}, {"name": "last_goods_rec", "value": "2018-07-16"}, {"name": "date_of_manuf", "value": "2018-07-01"}, {"name": "sled_bbd", "value": "0"}, {"name": "next_inspection", "value": "0"}, {"name": "inventory_time", "value": "844"}, {"name": "material", "value": "\u8bd5\u5236"}, {"name": "storage_bin", "value": "\u4f4e\u6e29\u5e93-\u7814\u53d1"}, {"name": "status", "value": "S"}, {"name": "batch", "value": "801807003V"}, {"name": "avail_stock", "value": "45.34"}, {"name": "unit", "value": "KG"}, {"name": "material_desc", "value": "\u975e\u6d1b\u5730\u5e73\u7f13\u91ca\u72472.5mg"}, {"name": "last_goods_rec", "value": "2018-07-16"}, {"name": "date_of_manuf", "value": "2018-07-01"}, {"name": "sled_bbd", "value": "0"}, {"name": "next_inspection", "value": "0"}, {"name": "inventory_time", "value": "844"}, {"name": "material", "value": "\u8bd5\u5236"}, {"name": "storage_bin", "value": "\u4f4e\u6e29\u5e93-\u7814\u53d1"}, {"name": "status", "value": "S"}, {"name": "batch", "value": "801907001V"}, {"name": "avail_stock", "value": "41.06"}, {"name": "unit", "value": "KG "}, {"name": "material_desc", "value": "\u975e\u6d1b\u5730\u5e73\u7f13\u91ca\u72475mg"}, {"name": "last_goods_rec", "value": "2018-08-16"}, {"name": "date_of_manuf", "value": "2018-07-01"}, {"name": "sled_bbd", "value": "0"}, {"name": "next_inspection", "value": "0"}, {"name": "inventory_time", "value": "813"}, {"name": "material", "value": "\u8bd5\u5236"}, {"name": "storage_bin", "value": "\u4f4e\u6e29\u5e93-\u7814\u53d1"}, {"name": "status", "value": "S"}, {"name": "batch", "value": "801907002V"}, {"name": "avail_stock", "value": "48.56"}, {"name": "unit", "value": "KG "}, {"name": "material_desc", "value": "\u975e\u6d1b\u5730\u5e73\u7f13\u91ca\u72475mg"}, {"name": "last_goods_rec", "value": "2018-08-16"}, {"name": "date_of_manuf", "value": "2018-07-01"}, {"name": "sled_bbd", "value": "0"}, {"name": "next_inspection", "value": "0"}, {"name": "inventory_time", "value": "813"}, {"name": "material", "value": "\u8bd5\u5236"}, {"name": "storage_bin", "value": "\u4f4e\u6e29\u5e93-\u7814\u53d1"}, {"name": "status", "value": "S"}, {"name": "batch", "value": "801907003V"}, {"name": "avail_stock", "value": "46.8"}, {"name": "unit", "value": "KG "}, {"name": "material_desc", "value": "\u975e\u6d1b\u5730\u5e73\u7f13\u91ca\u72475mg"}, {"name": "last_goods_rec", "value": "2018-08-16"}, {"name": "date_of_manuf", "value": "2018-07-01"}, {"name": "sled_bbd", "value": "0"}, {"name": "next_inspection", "value": "0"}, {"name": "inventory_time", "value": "813"}]

```

```
搜索接口
curl -i -u eyJhbGciOiJIUzUxMiIsImlhdCI6MTU5NjQ0NjEzNywiZXhwIjoxNTk2NDQ2NzM3fQ.eyJpZCI6M30.4BHm99cMmKkl-nBCTVt0_rOGCXZIJ2s_I0CZCt8SN25HZQ_mPkdOaJ-yn-VDgAB3IPrDz78tBNAHl8nVSV2nzA:unused -X GET -H "Content-Type: application/json" http://127.0.0.1:3622/api/v1000/elevated/searchinfo?search_type=storage_bin\&search_keys="04-01-18+04-01-17"

curl -i -u eyJhbGciOiJIUzUxMiIsImlhdCI6MTU5NjQ0NjEzNywiZXhwIjoxNTk2NDQ2NzM3fQ.eyJpZCI6M30.4BHm99cMmKkl-nBCTVt0_rOGCXZIJ2s_I0CZCt8SN25HZQ_mPkdOaJ-yn-VDgAB3IPrDz78tBNAHl8nVSV2nzA:unused -X GET -H "Content-Type: application/json" http://127.0.0.1:3622/api/v1000/elevated/searchinfo?search_type=material_desc\&search_keys='100ml+ml'

curl -i -u eyJhbGciOiJIUzUxMiIsImlhdCI6MTU5NjQ0NjEzNywiZXhwIjoxNTk2NDQ2NzM3fQ.eyJpZCI6M30.4BHm99cMmKkl-nBCTVt0_rOGCXZIJ2s_I0CZCt8SN25HZQ_mPkdOaJ-yn-VDgAB3IPrDz78tBNAHl8nVSV2nzA:unused -X GET -H "Content-Type: application/json" http://127.0.0.1:3622/api/v1000/elevated/searchinfo?search_type=batch\&search_keys='1702001+17011'

curl -i -u eyJhbGciOiJIUzUxMiIsImlhdCI6MTU5NjQ0NjEzNywiZXhwIjoxNTk2NDQ2NzM3fQ.eyJpZCI6M30.4BHm99cMmKkl-nBCTVt0_rOGCXZIJ2s_I0CZCt8SN25HZQ_mPkdOaJ-yn-VDgAB3IPrDz78tBNAHl8nVSV2nzA:unused -X GET -H "Content-Type: application/json" http://127.0.0.1:3622/api/v1000/elevated/searchinfo?search_type=material\&search_keys='NA+0.0'


返回json格式

[
    {
        "id":26386,
        "material":"试制",
        "storage_bin":"04-01-17",
        "batch":"80ml",
        "material_desc":"80ml瓶体",
        "avail_stock":"2750.0",
        "unit":"EA",
        "last_goods_rec":"2017-09-30",
        "date_of_manuf":"0",
        "sled_bbd":"0",
        "next_inspection":"0",
        "inventory_time":"1067",
        "status":"S"
    },
    {
        "id":26387,
        "material":"试制",
        "storage_bin":"04-01-18",
        "batch":"80ml",
        "material_desc":"80ml瓶盖",
        "avail_stock":"2750.0",
        "unit":"EA",
        "last_goods_rec":"2017-09-30",
        "date_of_manuf":"0",
        "sled_bbd":"0",
        "next_inspection":"0",
        "inventory_time":"1067",
        "status":"S"
    },
    {
        "id":26404,
        "material":"试制",
        "storage_bin":"04-01-24",
        "batch":"1702001",
        "material_desc":"100ml瓶盖",
        "avail_stock":"1657.0",
        "unit":"EA",
        "last_goods_rec":"2019-04-15",
        "date_of_manuf":"2017-01-12",
        "sled_bbd":"0",
        "next_inspection":"0",
        "inventory_time":"505",
        "status":"S"
    },
    {
        "id":26405,
        "material":"试制",
        "storage_bin":"04-01-24",
        "batch":"1802001",
        "material_desc":"100ml新品瓶体",
        "avail_stock":"683.0",
        "unit":"EA",
        "last_goods_rec":"2019-04-15",
        "date_of_manuf":"2018-01-25",
        "sled_bbd":"0",
        "next_inspection":"0",
        "inventory_time":"505",
        "status":"S"
    }
]

```
```
物料追溯接口：

curl -i -u eyJhbGciOiJIUzUxMiIsImlhdCI6MTU5NzkxMDcxMiwiZXhwIjoxNTk3OTExMzEyfQ.eyJpZCI6M30.6i9LSfKcNSAvQJKkaEmIt1AmOOxlRGTUwUSFLwMuiyPAnn3TT_pQWKyeSuAtOhCm5sBUXzhrp5QunnA7WvFO3A:unused -X GET -H "Content-Type: application/json" http://127.0.0.1:3622/api/v1000/elevated/materialtrace?batch='650605018'

返回json格式

[{
	"order_num": "101563",
	"list": "[{'id': 158825, 'material': '60010', 'material_description': 'Silibinin Capsules 35mg', 'order_num': '101563', 'batch': '600903050', 'quantity_wi': 975181.0, 'unit': 'EA', 'pid': 0, 'posting_date': '2016-08-22', 'children': [{'id': 157823, 'material': '10001', 'material_description': 'silibinin', 'order_num': '101503', 'batch': '15000383', 'quantity_wi': 35.0, 'unit': 'KG', 'pid': 158825, 'posting_date': '2016-05-09'}, {'id': 157825, 'material': '20028', 'material_description': 'Soya Lecithin', 'order_num': '101503', 'batch': '15000354', 'quantity_wi': 0.39, 'unit': 'KG', 'pid': 158825, 'posting_date': '2016-05-09'}, {'id': 157826, 'material': '20028', 'material_description': 'Soya Lecithin', 'order_num': '101503', 'batch': '16000033', 'quantity_wi': 64.61, 'unit': 'KG', 'pid': 158825, 'posting_date': '2016-05-09'}, {'id': 157828, 'material': '20035', 'material_description': 'Anhydrous Ethanol', 'order_num': '101503', 'batch': '16000029', 'quantity_wi': 480.0, 'unit': 'KG', 'pid': 158825, 'posting_date': '2016-05-09'}, {'id': 157830, 'material': '20035', 'material_description': 'Anhydrous Ethanol', 'order_num': '101503', 'batch': '16000029', 'quantity_wi': 20.0, 'unit': 'KG', 'pid': 158825, 'posting_date': '2016-05-09'}, {'id': 157832, 'material': '20033', 'material_description': 'Lactose (SpheroLac 100)', 'order_num': '101503', 'batch': '15000369', 'quantity_wi': 106.0, 'unit': 'KG', 'pid': 158825, 'posting_date': '2016-05-09'}, {'id': 157834, 'material': '20034', 'material_description': 'Talc Powder', 'order_num': '101503', 'batch': '16000036', 'quantity_wi': 31.46, 'unit': 'KG', 'pid': 158825, 'posting_date': '2016-05-09'}, {'id': 157836, 'material': '20029', 'material_description': 'Glycolys STD', 'order_num': '101503', 'batch': '16000006', 'quantity_wi': 20.6, 'unit': 'KG', 'pid': 158825, 'posting_date': '2016-05-09'}, {'id': 157838, 'material': '20036', 'material_description': 'Silibinin printing 1#vacant capsules', 'order_num': '101503', 'batch': '15000366', 'quantity_wi': 975395.0, 'unit': 'EA', 'pid': 158825, 'posting_date': '2016-05-09'}]}, {'id': 158827, 'material': '30010', 'material_description': 'PVC/PVDC Colorless 231mm', 'order_num': '101563', 'batch': '16000038', 'quantity_wi': 175.2, 'unit': 'KG', 'pid': 0, 'posting_date': '2016-08-22'}, {'id': 158829, 'material': '30011', 'material_description': 'AluminumFoil231mm SilibininCapsules 35mg', 'order_num': '101563', 'batch': '16000026', 'quantity_wi': 29.65, 'unit': 'KG', 'pid': 0, 'posting_date': '2016-08-22'}, {'id': 158831, 'material': '30012', 'material_description': 'Tropical Type Blister AluminumFoil 231mm', 'order_num': '101563', 'batch': '16000027', 'quantity_wi': 96.91, 'unit': 'KG', 'pid': 0, 'posting_date': '2016-08-22'}, {'id': 158833, 'material': '40018', 'material_description': 'Silibinin Capsules Leaflet', 'order_num': '101563', 'batch': '16000025', 'quantity_wi': 3244.0, 'unit': 'EA', 'pid': 0, 'posting_date': '2016-08-22'}, {'id': 158834, 'material': '40018', 'material_description': 'Silibinin Capsules Leaflet', 'order_num': '101563', 'batch': '16000044', 'quantity_wi': 45495.0, 'unit': 'EA', 'pid': 0, 'posting_date': '2016-08-22'}, {'id': 158836, 'material': '40019', 'material_description': 'Silibinin Capsules 35mg*2*10EA Carton', 'order_num': '101563', 'batch': '16000068', 'quantity_wi': 30509.0, 'unit': 'EA', 'pid': 0, 'posting_date': '2016-08-22'}, {'id': 158837, 'material': '40019', 'material_description': 'Silibinin Capsules 35mg*2*10EA Carton', 'order_num': '101563', 'batch': '16000085', 'quantity_wi': 18226.0, 'unit': 'EA', 'pid': 0, 'posting_date': '2016-08-22'}, {'id': 158839, 'material': '40010', 'material_description': 'BOPP Film 178mm', 'order_num': '101563', 'batch': '16000013', 'quantity_wi': 7.33, 'unit': 'KG', 'pid': 0, 'posting_date': '2016-08-22'}, {'id': 158840, 'material': '40010', 'material_description': 'BOPP Film 178mm', 'order_num': '101563', 'batch': '16000018', 'quantity_wi': 8.36, 'unit': 'KG', 'pid': 0, 'posting_date': '2016-08-22'}, {'id': 158842, 'material': '40020', 'material_description': 'Silibinin Capsules 35mg*2*10EA Shipper', 'order_num': '101563', 'batch': '16000060', 'quantity_wi': 8.0, 'unit': 'EA', 'pid': 0, 'posting_date': '2016-08-22'}, {'id': 158843, 'material': '40020', 'material_description': 'Silibinin Capsules 35mg*2*10EA Shipper', 'order_num': '101563', 'batch': '16000069', 'quantity_wi': 157.0, 'unit': 'EA', 'pid': 0, 'posting_date': '2016-08-22'}, {'id': 158845, 'material': '40021', 'material_description': 'Silibinin Capsules35mg*2*10EA Paperboard', 'order_num': '101563', 'batch': '16000061', 'quantity_wi': 336.0, 'unit': 'EA', 'pid': 0, 'posting_date': '2016-08-22'}]"
}, {
	"order_num": "101632",
	"list": "[{'id': 159935, 'material': '40018', 'material_description': 'Silibinin Capsules Leaflet', 'order_num': '101632', 'batch': '16000106', 'quantity_wi': 32900.0, 'unit': 'EA', 'pid': 0, 'posting_date': '2016-08-22'}, {'id': 159937, 'material': '40022', 'material_description': 'Silibinin Capsules35mg*3*10EA Carton', 'order_num': '101632', 'batch': '16000110', 'quantity_wi': 32655.0, 'unit': 'EA', 'pid': 0, 'posting_date': '2016-08-22'}, {'id': 159939, 'material': '40010', 'material_description': 'BOPP Film 178mm', 'order_num': '101632', 'batch': '16000075', 'quantity_wi': 13.09, 'unit': 'KG', 'pid': 0, 'posting_date': '2016-08-22'}, {'id': 159941, 'material': '40023', 'material_description': 'Silibinin Capsules 35mg*3*10EA Shipper', 'order_num': '101632', 'batch': '16000093', 'quantity_wi': 114.0, 'unit': 'EA', 'pid': 0, 'posting_date': '2016-08-22'}, {'id': 159942, 'material': '40023', 'material_description': 'Silibinin Capsules 35mg*3*10EA Shipper', 'order_num': '101632', 'batch': '16000119', 'quantity_wi': 50.0, 'unit': 'EA', 'pid': 0, 'posting_date': '2016-08-22'}, {'id': 159944, 'material': '40024', 'material_description': 'Silibinin Capsules35mg*3*10EA Paperboard', 'order_num': '101632', 'batch': '16000094', 'quantity_wi': 330.0, 'unit': 'EA', 'pid': 0, 'posting_date': '2016-08-22'}, {'id': 159945, 'material': '70008', 'material_description': 'Silibinin Capsules 35mg*2*10EA', 'order_num': '101632', 'batch': '650605018', 'quantity_wi': 972700.0, 'unit': 'EA', 'pid': 0, 'posting_date': '2016-08-22', 'children': [{'id': 158825, 'material': '60010', 'material_description': 'Silibinin Capsules 35mg', 'order_num': '101563', 'batch': '600903050', 'quantity_wi': 975181.0, 'unit': 'EA', 'pid': 159945, 'posting_date': '2016-08-22', 'children': [{'id': 157823, 'material': '10001', 'material_description': 'silibinin', 'order_num': '101503', 'batch': '15000383', 'quantity_wi': 35.0, 'unit': 'KG', 'pid': 158825, 'posting_date': '2016-05-09'}, {'id': 157825, 'material': '20028', 'material_description': 'Soya Lecithin', 'order_num': '101503', 'batch': '15000354', 'quantity_wi': 0.39, 'unit': 'KG', 'pid': 158825, 'posting_date': '2016-05-09'}, {'id': 157826, 'material': '20028', 'material_description': 'Soya Lecithin', 'order_num': '101503', 'batch': '16000033', 'quantity_wi': 64.61, 'unit': 'KG', 'pid': 158825, 'posting_date': '2016-05-09'}, {'id': 157828, 'material': '20035', 'material_description': 'Anhydrous Ethanol', 'order_num': '101503', 'batch': '16000029', 'quantity_wi': 480.0, 'unit': 'KG', 'pid': 158825, 'posting_date': '2016-05-09'}, {'id': 157830, 'material': '20035', 'material_description': 'Anhydrous Ethanol', 'order_num': '101503', 'batch': '16000029', 'quantity_wi': 20.0, 'unit': 'KG', 'pid': 158825, 'posting_date': '2016-05-09'}, {'id': 157832, 'material': '20033', 'material_description': 'Lactose (SpheroLac 100)', 'order_num': '101503', 'batch': '15000369', 'quantity_wi': 106.0, 'unit': 'KG', 'pid': 158825, 'posting_date': '2016-05-09'}, {'id': 157834, 'material': '20034', 'material_description': 'Talc Powder', 'order_num': '101503', 'batch': '16000036', 'quantity_wi': 31.46, 'unit': 'KG', 'pid': 158825, 'posting_date': '2016-05-09'}, {'id': 157836, 'material': '20029', 'material_description': 'Glycolys STD', 'order_num': '101503', 'batch': '16000006', 'quantity_wi': 20.6, 'unit': 'KG', 'pid': 158825, 'posting_date': '2016-05-09'}, {'id': 157838, 'material': '20036', 'material_description': 'Silibinin printing 1#vacant capsules', 'order_num': '101503', 'batch': '15000366', 'quantity_wi': 975395.0, 'unit': 'EA', 'pid': 158825, 'posting_date': '2016-05-09'}]}, {'id': 158827, 'material': '30010', 'material_description': 'PVC/PVDC Colorless 231mm', 'order_num': '101563', 'batch': '16000038', 'quantity_wi': 175.2, 'unit': 'KG', 'pid': 159945, 'posting_date': '2016-08-22'}, {'id': 158829, 'material': '30011', 'material_description': 'AluminumFoil231mm SilibininCapsules 35mg', 'order_num': '101563', 'batch': '16000026', 'quantity_wi': 29.65, 'unit': 'KG', 'pid': 159945, 'posting_date': '2016-08-22'}, {'id': 158831, 'material': '30012', 'material_description': 'Tropical Type Blister AluminumFoil 231mm', 'order_num': '101563', 'batch': '16000027', 'quantity_wi': 96.91, 'unit': 'KG', 'pid': 159945, 'posting_date': '2016-08-22'}, {'id': 158833, 'material': '40018', 'material_description': 'Silibinin Capsules Leaflet', 'order_num': '101563', 'batch': '16000025', 'quantity_wi': 3244.0, 'unit': 'EA', 'pid': 159945, 'posting_date': '2016-08-22'}, {'id': 158834, 'material': '40018', 'material_description': 'Silibinin Capsules Leaflet', 'order_num': '101563', 'batch': '16000044', 'quantity_wi': 45495.0, 'unit': 'EA', 'pid': 159945, 'posting_date': '2016-08-22'}, {'id': 158836, 'material': '40019', 'material_description': 'Silibinin Capsules 35mg*2*10EA Carton', 'order_num': '101563', 'batch': '16000068', 'quantity_wi': 30509.0, 'unit': 'EA', 'pid': 159945, 'posting_date': '2016-08-22'}, {'id': 158837, 'material': '40019', 'material_description': 'Silibinin Capsules 35mg*2*10EA Carton', 'order_num': '101563', 'batch': '16000085', 'quantity_wi': 18226.0, 'unit': 'EA', 'pid': 159945, 'posting_date': '2016-08-22'}, {'id': 158839, 'material': '40010', 'material_description': 'BOPP Film 178mm', 'order_num': '101563', 'batch': '16000013', 'quantity_wi': 7.33, 'unit': 'KG', 'pid': 159945, 'posting_date': '2016-08-22'}, {'id': 158840, 'material': '40010', 'material_description': 'BOPP Film 178mm', 'order_num': '101563', 'batch': '16000018', 'quantity_wi': 8.36, 'unit': 'KG', 'pid': 159945, 'posting_date': '2016-08-22'}, {'id': 158842, 'material': '40020', 'material_description': 'Silibinin Capsules 35mg*2*10EA Shipper', 'order_num': '101563', 'batch': '16000060', 'quantity_wi': 8.0, 'unit': 'EA', 'pid': 159945, 'posting_date': '2016-08-22'}, {'id': 158843, 'material': '40020', 'material_description': 'Silibinin Capsules 35mg*2*10EA Shipper', 'order_num': '101563', 'batch': '16000069', 'quantity_wi': 157.0, 'unit': 'EA', 'pid': 159945, 'posting_date': '2016-08-22'}, {'id': 158845, 'material': '40021', 'material_description': 'Silibinin Capsules35mg*2*10EA Paperboard', 'order_num': '101563', 'batch': '16000061', 'quantity_wi': 336.0, 'unit': 'EA', 'pid': 159945, 'posting_date': '2016-08-22'}]}]"
}]

```


#启动项目
##导入数据库

>1.起mysql实例　并　登录
>2.赋予权限
```
CREATE USER root@'%' IDENTIFIED BY 'root';
GRANT ALL PRIVILEGES ON *.* TO root@'%' WITH GRANT OPTION;
```
3.导入数据
```
source /WareHouse/Backend/tasly_warehouse.sql
```
##后端启动
>1.进入虚拟化环境
```
cd /WareHouse/Backend && source ./venv/bin/activate
```
>2.起服务
```
cd /WareHouse/Backend && ./backend.sh --start
```
##前端启动
```
cd /WareHouse/Frontend/warehouse && npm run dev
```


##调整高架库槽位的语句
```
update tasly_warehouse_storage_bin set storage_bin = '01-02-06' where id = 1196;
update tasly_warehouse_storage_bin set storage_bin = '01-03-06' where id = 1197;
update tasly_warehouse_storage_bin set storage_bin = '01-04-06' where id = 1198;
update tasly_warehouse_storage_bin set storage_bin = '01-05-06' where id = 1199;
update tasly_warehouse_storage_bin set storage_bin = '01-06-06' where id = 1200;
update tasly_warehouse_storage_bin set storage_bin = '01-07-06' where id = 1201;
update tasly_warehouse_storage_bin set storage_bin = '01-08-06' where id = 1202;
update tasly_warehouse_storage_bin set storage_bin = '01-09-06' where id = 1203;
update tasly_warehouse_storage_bin set storage_bin = '01-10-06' where id = 1204;
update tasly_warehouse_storage_bin set storage_bin = '01-11-06' where id = 1205;
update tasly_warehouse_storage_bin set storage_bin = '01-12-06' where id = 1206;
update tasly_warehouse_storage_bin set storage_bin = '01-13-06' where id = 1207;
update tasly_warehouse_storage_bin set storage_bin = '01-14-06' where id = 1208;
update tasly_warehouse_storage_bin set storage_bin = '01-15-06' where id = 1209;
update tasly_warehouse_storage_bin set storage_bin = '01-16-06' where id = 1210;
update tasly_warehouse_storage_bin set storage_bin = '01-17-06' where id = 1211;
update tasly_warehouse_storage_bin set storage_bin = '01-18-06' where id = 1212;
update tasly_warehouse_storage_bin set storage_bin = '01-19-06' where id = 1213;
update tasly_warehouse_storage_bin set storage_bin = '01-20-06' where id = 1214;
update tasly_warehouse_storage_bin set storage_bin = '01-21-06' where id = 1215;
update tasly_warehouse_storage_bin set storage_bin = '01-22-06' where id = 1216;
update tasly_warehouse_storage_bin set storage_bin = '01-23-06' where id = 1217;
update tasly_warehouse_storage_bin set storage_bin = '01-24-06' where id = 1218;
update tasly_warehouse_storage_bin set storage_bin = '01-25-06' where id = 1219;
update tasly_warehouse_storage_bin set storage_bin = '01-26-06' where id = 1220;
update tasly_warehouse_storage_bin set storage_bin = '01-27-06' where id = 1221;
update tasly_warehouse_storage_bin set storage_bin = '01-28-06' where id = 1222;
update tasly_warehouse_storage_bin set storage_bin = '01-29-06' where id = 1223;
update tasly_warehouse_storage_bin set storage_bin = '01-30-06' where id = 1224;
update tasly_warehouse_storage_bin set storage_bin = '01-31-06' where id = 1225;
update tasly_warehouse_storage_bin set storage_bin = '01-32-06' where id = 1226;
update tasly_warehouse_storage_bin set storage_bin = '01-02-05' where id = 1227;
update tasly_warehouse_storage_bin set storage_bin = '01-03-05' where id = 1228;
update tasly_warehouse_storage_bin set storage_bin = '01-04-05' where id = 1229;
update tasly_warehouse_storage_bin set storage_bin = '01-05-05' where id = 1230;
update tasly_warehouse_storage_bin set storage_bin = '01-06-05' where id = 1231;
update tasly_warehouse_storage_bin set storage_bin = '01-07-05' where id = 1232;
update tasly_warehouse_storage_bin set storage_bin = '01-08-05' where id = 1233;
update tasly_warehouse_storage_bin set storage_bin = '01-09-05' where id = 1234;
update tasly_warehouse_storage_bin set storage_bin = '01-10-05' where id = 1235;
update tasly_warehouse_storage_bin set storage_bin = '01-11-05' where id = 1236;
update tasly_warehouse_storage_bin set storage_bin = '01-12-05' where id = 1237;
update tasly_warehouse_storage_bin set storage_bin = '01-13-05' where id = 1238;
update tasly_warehouse_storage_bin set storage_bin = '01-14-05' where id = 1239;
update tasly_warehouse_storage_bin set storage_bin = '01-15-05' where id = 1240;
update tasly_warehouse_storage_bin set storage_bin = '01-16-05' where id = 1241;
update tasly_warehouse_storage_bin set storage_bin = '01-17-05' where id = 1242;
update tasly_warehouse_storage_bin set storage_bin = '01-18-05' where id = 1243;
update tasly_warehouse_storage_bin set storage_bin = '01-19-05' where id = 1244;
update tasly_warehouse_storage_bin set storage_bin = '01-20-05' where id = 1245;
update tasly_warehouse_storage_bin set storage_bin = '01-21-05' where id = 1246;
update tasly_warehouse_storage_bin set storage_bin = '01-22-05' where id = 1247;
update tasly_warehouse_storage_bin set storage_bin = '01-23-05' where id = 1248;
update tasly_warehouse_storage_bin set storage_bin = '01-24-05' where id = 1249;
update tasly_warehouse_storage_bin set storage_bin = '01-25-05' where id = 1250;
update tasly_warehouse_storage_bin set storage_bin = '01-26-05' where id = 1251;
update tasly_warehouse_storage_bin set storage_bin = '01-27-05' where id = 1252;
update tasly_warehouse_storage_bin set storage_bin = '01-28-05' where id = 1253;
update tasly_warehouse_storage_bin set storage_bin = '01-29-05' where id = 1254;
update tasly_warehouse_storage_bin set storage_bin = '01-30-05' where id = 1255;
update tasly_warehouse_storage_bin set storage_bin = '01-31-05' where id = 1256;
update tasly_warehouse_storage_bin set storage_bin = '01-32-05' where id = 1257;
update tasly_warehouse_storage_bin set storage_bin = '01-02-04' where id = 1258;
update tasly_warehouse_storage_bin set storage_bin = '01-03-04' where id = 1259;
update tasly_warehouse_storage_bin set storage_bin = '01-04-04' where id = 1260;
update tasly_warehouse_storage_bin set storage_bin = '01-05-04' where id = 1261;
update tasly_warehouse_storage_bin set storage_bin = '01-06-04' where id = 1262;
update tasly_warehouse_storage_bin set storage_bin = '01-07-04' where id = 1263;
update tasly_warehouse_storage_bin set storage_bin = '01-08-04' where id = 1264;
update tasly_warehouse_storage_bin set storage_bin = '01-09-04' where id = 1265;
update tasly_warehouse_storage_bin set storage_bin = '01-10-04' where id = 1266;
update tasly_warehouse_storage_bin set storage_bin = '01-11-04' where id = 1267;
update tasly_warehouse_storage_bin set storage_bin = '01-12-04' where id = 1268;
update tasly_warehouse_storage_bin set storage_bin = '01-13-04' where id = 1269;
update tasly_warehouse_storage_bin set storage_bin = '01-14-04' where id = 1270;
update tasly_warehouse_storage_bin set storage_bin = '01-15-04' where id = 1271;
update tasly_warehouse_storage_bin set storage_bin = '01-16-04' where id = 1272;
update tasly_warehouse_storage_bin set storage_bin = '01-17-04' where id = 1273;
update tasly_warehouse_storage_bin set storage_bin = '01-18-04' where id = 1274;
update tasly_warehouse_storage_bin set storage_bin = '01-19-04' where id = 1275;
update tasly_warehouse_storage_bin set storage_bin = '01-20-04' where id = 1276;
update tasly_warehouse_storage_bin set storage_bin = '01-21-04' where id = 1277;
update tasly_warehouse_storage_bin set storage_bin = '01-22-04' where id = 1278;
update tasly_warehouse_storage_bin set storage_bin = '01-23-04' where id = 1279;
update tasly_warehouse_storage_bin set storage_bin = '01-24-04' where id = 1280;
update tasly_warehouse_storage_bin set storage_bin = '01-25-04' where id = 1281;
update tasly_warehouse_storage_bin set storage_bin = '01-26-04' where id = 1282;
update tasly_warehouse_storage_bin set storage_bin = '01-27-04' where id = 1283;
update tasly_warehouse_storage_bin set storage_bin = '01-28-04' where id = 1284;
update tasly_warehouse_storage_bin set storage_bin = '01-29-04' where id = 1285;
update tasly_warehouse_storage_bin set storage_bin = '01-30-04' where id = 1286;
update tasly_warehouse_storage_bin set storage_bin = '01-31-04' where id = 1287;
update tasly_warehouse_storage_bin set storage_bin = '01-32-04' where id = 1288;
update tasly_warehouse_storage_bin set storage_bin = '01-02-03' where id = 1289;
update tasly_warehouse_storage_bin set storage_bin = '01-03-03' where id = 1290;
update tasly_warehouse_storage_bin set storage_bin = '01-04-03' where id = 1291;
update tasly_warehouse_storage_bin set storage_bin = '01-05-03' where id = 1292;
update tasly_warehouse_storage_bin set storage_bin = '01-06-03' where id = 1293;
update tasly_warehouse_storage_bin set storage_bin = '01-07-03' where id = 1294;
update tasly_warehouse_storage_bin set storage_bin = '01-08-03' where id = 1295;
update tasly_warehouse_storage_bin set storage_bin = '01-09-03' where id = 1296;
update tasly_warehouse_storage_bin set storage_bin = '01-10-03' where id = 1297;
update tasly_warehouse_storage_bin set storage_bin = '01-11-03' where id = 1298;
update tasly_warehouse_storage_bin set storage_bin = '01-12-03' where id = 1299;
update tasly_warehouse_storage_bin set storage_bin = '01-13-03' where id = 1300;
update tasly_warehouse_storage_bin set storage_bin = '01-14-03' where id = 1301;
update tasly_warehouse_storage_bin set storage_bin = '01-15-03' where id = 1302;
update tasly_warehouse_storage_bin set storage_bin = '01-16-03' where id = 1303;
update tasly_warehouse_storage_bin set storage_bin = '01-17-03' where id = 1304;
update tasly_warehouse_storage_bin set storage_bin = '01-18-03' where id = 1305;
update tasly_warehouse_storage_bin set storage_bin = '01-19-03' where id = 1306;
update tasly_warehouse_storage_bin set storage_bin = '01-20-03' where id = 1307;
update tasly_warehouse_storage_bin set storage_bin = '01-21-03' where id = 1308;
update tasly_warehouse_storage_bin set storage_bin = '01-22-03' where id = 1309;
update tasly_warehouse_storage_bin set storage_bin = '01-23-03' where id = 1310;
update tasly_warehouse_storage_bin set storage_bin = '01-24-03' where id = 1311;
update tasly_warehouse_storage_bin set storage_bin = '01-25-03' where id = 1312;
update tasly_warehouse_storage_bin set storage_bin = '01-26-03' where id = 1313;
update tasly_warehouse_storage_bin set storage_bin = '01-27-03' where id = 1314;
update tasly_warehouse_storage_bin set storage_bin = '01-28-03' where id = 1315;
update tasly_warehouse_storage_bin set storage_bin = '01-29-03' where id = 1316;
update tasly_warehouse_storage_bin set storage_bin = '01-30-03' where id = 1317;
update tasly_warehouse_storage_bin set storage_bin = '01-31-03' where id = 1318;
update tasly_warehouse_storage_bin set storage_bin = '01-32-03' where id = 1319;
update tasly_warehouse_storage_bin set storage_bin = '01-02-02' where id = 1320;
update tasly_warehouse_storage_bin set storage_bin = '01-03-02' where id = 1321;
update tasly_warehouse_storage_bin set storage_bin = '01-04-02' where id = 1322;
update tasly_warehouse_storage_bin set storage_bin = '01-05-02' where id = 1323;
update tasly_warehouse_storage_bin set storage_bin = '01-06-02' where id = 1324;
update tasly_warehouse_storage_bin set storage_bin = '01-07-02' where id = 1325;
update tasly_warehouse_storage_bin set storage_bin = '01-08-02' where id = 1326;
update tasly_warehouse_storage_bin set storage_bin = '01-09-02' where id = 1327;
update tasly_warehouse_storage_bin set storage_bin = '01-10-02' where id = 1328;
update tasly_warehouse_storage_bin set storage_bin = '01-11-02' where id = 1329;
update tasly_warehouse_storage_bin set storage_bin = '01-12-02' where id = 1330;
update tasly_warehouse_storage_bin set storage_bin = '01-13-02' where id = 1331;
update tasly_warehouse_storage_bin set storage_bin = '01-14-02' where id = 1332;
update tasly_warehouse_storage_bin set storage_bin = '01-15-02' where id = 1333;
update tasly_warehouse_storage_bin set storage_bin = '01-16-02' where id = 1334;
update tasly_warehouse_storage_bin set storage_bin = '01-17-02' where id = 1335;
update tasly_warehouse_storage_bin set storage_bin = '01-18-02' where id = 1336;
update tasly_warehouse_storage_bin set storage_bin = '01-19-02' where id = 1337;
update tasly_warehouse_storage_bin set storage_bin = '01-20-02' where id = 1338;
update tasly_warehouse_storage_bin set storage_bin = '01-21-02' where id = 1339;
update tasly_warehouse_storage_bin set storage_bin = '01-22-02' where id = 1340;
update tasly_warehouse_storage_bin set storage_bin = '01-23-02' where id = 1341;
update tasly_warehouse_storage_bin set storage_bin = '01-24-02' where id = 1342;
update tasly_warehouse_storage_bin set storage_bin = '01-25-02' where id = 1343;
update tasly_warehouse_storage_bin set storage_bin = '01-26-02' where id = 1344;
update tasly_warehouse_storage_bin set storage_bin = '01-27-02' where id = 1345;
update tasly_warehouse_storage_bin set storage_bin = '01-28-02' where id = 1346;
update tasly_warehouse_storage_bin set storage_bin = '01-29-02' where id = 1347;
update tasly_warehouse_storage_bin set storage_bin = '01-30-02' where id = 1348;
update tasly_warehouse_storage_bin set storage_bin = '01-31-02' where id = 1349;
update tasly_warehouse_storage_bin set storage_bin = '01-32-02' where id = 1350;
update tasly_warehouse_storage_bin set storage_bin = '01-02-01' where id = 1351;
update tasly_warehouse_storage_bin set storage_bin = '01-03-01' where id = 1352;
update tasly_warehouse_storage_bin set storage_bin = '01-04-01' where id = 1353;
update tasly_warehouse_storage_bin set storage_bin = '01-05-01' where id = 1354;
update tasly_warehouse_storage_bin set storage_bin = '01-06-01' where id = 1355;
update tasly_warehouse_storage_bin set storage_bin = '01-07-01' where id = 1356;
update tasly_warehouse_storage_bin set storage_bin = '01-08-01' where id = 1357;
update tasly_warehouse_storage_bin set storage_bin = '01-09-01' where id = 1358;
update tasly_warehouse_storage_bin set storage_bin = '01-10-01' where id = 1359;
update tasly_warehouse_storage_bin set storage_bin = '01-11-01' where id = 1360;
update tasly_warehouse_storage_bin set storage_bin = '01-12-01' where id = 1361;
update tasly_warehouse_storage_bin set storage_bin = '01-13-01' where id = 1362;
update tasly_warehouse_storage_bin set storage_bin = '01-14-01' where id = 1363;
update tasly_warehouse_storage_bin set storage_bin = '01-15-01' where id = 1364;
update tasly_warehouse_storage_bin set storage_bin = '01-16-01' where id = 1365;
update tasly_warehouse_storage_bin set storage_bin = '01-17-01' where id = 1366;
update tasly_warehouse_storage_bin set storage_bin = '01-18-01' where id = 1367;
update tasly_warehouse_storage_bin set storage_bin = '01-19-01' where id = 1368;
update tasly_warehouse_storage_bin set storage_bin = '01-20-01' where id = 1369;
update tasly_warehouse_storage_bin set storage_bin = '01-21-01' where id = 1370;
update tasly_warehouse_storage_bin set storage_bin = '01-22-01' where id = 1371;
update tasly_warehouse_storage_bin set storage_bin = '01-23-01' where id = 1372;
update tasly_warehouse_storage_bin set storage_bin = '01-24-01' where id = 1373;
update tasly_warehouse_storage_bin set storage_bin = '01-25-01' where id = 1374;
update tasly_warehouse_storage_bin set storage_bin = '01-26-01' where id = 1375;
update tasly_warehouse_storage_bin set storage_bin = '01-27-01' where id = 1376;
update tasly_warehouse_storage_bin set storage_bin = '01-28-01' where id = 1377;
update tasly_warehouse_storage_bin set storage_bin = '01-29-01' where id = 1378;
update tasly_warehouse_storage_bin set storage_bin = '01-30-01' where id = 1379;
update tasly_warehouse_storage_bin set storage_bin = '01-31-01' where id = 1380;
update tasly_warehouse_storage_bin set storage_bin = '01-32-01' where id = 1381;
update tasly_warehouse_storage_bin set storage_bin = '02-02-01' where id = 1382;
update tasly_warehouse_storage_bin set storage_bin = '02-03-01' where id = 1383;
update tasly_warehouse_storage_bin set storage_bin = '02-04-01' where id = 1384;
update tasly_warehouse_storage_bin set storage_bin = '02-05-01' where id = 1385;
update tasly_warehouse_storage_bin set storage_bin = '02-06-01' where id = 1386;
update tasly_warehouse_storage_bin set storage_bin = '02-07-01' where id = 1387;
update tasly_warehouse_storage_bin set storage_bin = '02-08-01' where id = 1388;
update tasly_warehouse_storage_bin set storage_bin = '02-09-01' where id = 1389;
update tasly_warehouse_storage_bin set storage_bin = '02-10-01' where id = 1390;
update tasly_warehouse_storage_bin set storage_bin = '02-11-01' where id = 1391;
update tasly_warehouse_storage_bin set storage_bin = '02-12-01' where id = 1392;
update tasly_warehouse_storage_bin set storage_bin = '02-13-01' where id = 1393;
update tasly_warehouse_storage_bin set storage_bin = '02-14-01' where id = 1394;
update tasly_warehouse_storage_bin set storage_bin = '02-15-01' where id = 1395;
update tasly_warehouse_storage_bin set storage_bin = '02-16-01' where id = 1396;
update tasly_warehouse_storage_bin set storage_bin = '02-17-01' where id = 1397;
update tasly_warehouse_storage_bin set storage_bin = '02-18-01' where id = 1398;
update tasly_warehouse_storage_bin set storage_bin = '02-19-01' where id = 1399;
update tasly_warehouse_storage_bin set storage_bin = '02-20-01' where id = 1400;
update tasly_warehouse_storage_bin set storage_bin = '02-21-01' where id = 1401;
update tasly_warehouse_storage_bin set storage_bin = '02-22-01' where id = 1402;
update tasly_warehouse_storage_bin set storage_bin = '02-23-01' where id = 1403;
update tasly_warehouse_storage_bin set storage_bin = '02-24-01' where id = 1404;
update tasly_warehouse_storage_bin set storage_bin = '02-25-01' where id = 1405;
update tasly_warehouse_storage_bin set storage_bin = '02-26-01' where id = 1406;
update tasly_warehouse_storage_bin set storage_bin = '02-27-01' where id = 1407;
update tasly_warehouse_storage_bin set storage_bin = '02-28-01' where id = 1408;
update tasly_warehouse_storage_bin set storage_bin = '02-29-01' where id = 1409;
update tasly_warehouse_storage_bin set storage_bin = '02-30-01' where id = 1410;
update tasly_warehouse_storage_bin set storage_bin = '02-31-01' where id = 1411;
update tasly_warehouse_storage_bin set storage_bin = '02-32-01' where id = 1412;
update tasly_warehouse_storage_bin set storage_bin = '02-02-02' where id = 1413;
update tasly_warehouse_storage_bin set storage_bin = '02-03-02' where id = 1414;
update tasly_warehouse_storage_bin set storage_bin = '02-04-02' where id = 1415;
update tasly_warehouse_storage_bin set storage_bin = '02-05-02' where id = 1416;
update tasly_warehouse_storage_bin set storage_bin = '02-06-02' where id = 1417;
update tasly_warehouse_storage_bin set storage_bin = '02-07-02' where id = 1418;
update tasly_warehouse_storage_bin set storage_bin = '02-08-02' where id = 1419;
update tasly_warehouse_storage_bin set storage_bin = '02-09-02' where id = 1420;
update tasly_warehouse_storage_bin set storage_bin = '02-10-02' where id = 1421;
update tasly_warehouse_storage_bin set storage_bin = '02-11-02' where id = 1422;
update tasly_warehouse_storage_bin set storage_bin = '02-12-02' where id = 1423;
update tasly_warehouse_storage_bin set storage_bin = '02-13-02' where id = 1424;
update tasly_warehouse_storage_bin set storage_bin = '02-14-02' where id = 1425;
update tasly_warehouse_storage_bin set storage_bin = '02-15-02' where id = 1426;
update tasly_warehouse_storage_bin set storage_bin = '02-16-02' where id = 1427;
update tasly_warehouse_storage_bin set storage_bin = '02-17-02' where id = 1428;
update tasly_warehouse_storage_bin set storage_bin = '02-18-02' where id = 1429;
update tasly_warehouse_storage_bin set storage_bin = '02-19-02' where id = 1430;
update tasly_warehouse_storage_bin set storage_bin = '02-20-02' where id = 1431;
update tasly_warehouse_storage_bin set storage_bin = '02-21-02' where id = 1432;
update tasly_warehouse_storage_bin set storage_bin = '02-22-02' where id = 1433;
update tasly_warehouse_storage_bin set storage_bin = '02-23-02' where id = 1434;
update tasly_warehouse_storage_bin set storage_bin = '02-24-02' where id = 1435;
update tasly_warehouse_storage_bin set storage_bin = '02-25-02' where id = 1436;
update tasly_warehouse_storage_bin set storage_bin = '02-26-02' where id = 1437;
update tasly_warehouse_storage_bin set storage_bin = '02-27-02' where id = 1438;
update tasly_warehouse_storage_bin set storage_bin = '02-28-02' where id = 1439;
update tasly_warehouse_storage_bin set storage_bin = '02-29-02' where id = 1440;
update tasly_warehouse_storage_bin set storage_bin = '02-30-02' where id = 1441;
update tasly_warehouse_storage_bin set storage_bin = '02-31-02' where id = 1442;
update tasly_warehouse_storage_bin set storage_bin = '02-32-02' where id = 1443;
update tasly_warehouse_storage_bin set storage_bin = '02-01-03' where id = 1444;
update tasly_warehouse_storage_bin set storage_bin = '02-02-03' where id = 1445;
update tasly_warehouse_storage_bin set storage_bin = '02-03-03' where id = 1446;
update tasly_warehouse_storage_bin set storage_bin = '02-04-03' where id = 1447;
update tasly_warehouse_storage_bin set storage_bin = '02-05-03' where id = 1448;
update tasly_warehouse_storage_bin set storage_bin = '02-06-03' where id = 1449;
update tasly_warehouse_storage_bin set storage_bin = '02-07-03' where id = 1450;
update tasly_warehouse_storage_bin set storage_bin = '02-08-03' where id = 1451;
update tasly_warehouse_storage_bin set storage_bin = '02-09-03' where id = 1452;
update tasly_warehouse_storage_bin set storage_bin = '02-10-03' where id = 1453;
update tasly_warehouse_storage_bin set storage_bin = '02-11-03' where id = 1454;
update tasly_warehouse_storage_bin set storage_bin = '02-12-03' where id = 1455;
update tasly_warehouse_storage_bin set storage_bin = '02-13-03' where id = 1456;
update tasly_warehouse_storage_bin set storage_bin = '02-14-03' where id = 1457;
update tasly_warehouse_storage_bin set storage_bin = '02-15-03' where id = 1458;
update tasly_warehouse_storage_bin set storage_bin = '02-16-03' where id = 1459;
update tasly_warehouse_storage_bin set storage_bin = '02-17-03' where id = 1460;
update tasly_warehouse_storage_bin set storage_bin = '02-18-03' where id = 1461;
update tasly_warehouse_storage_bin set storage_bin = '02-19-03' where id = 1462;
update tasly_warehouse_storage_bin set storage_bin = '02-20-03' where id = 1463;
update tasly_warehouse_storage_bin set storage_bin = '02-21-03' where id = 1464;
update tasly_warehouse_storage_bin set storage_bin = '02-22-03' where id = 1465;
update tasly_warehouse_storage_bin set storage_bin = '02-23-03' where id = 1466;
update tasly_warehouse_storage_bin set storage_bin = '02-24-03' where id = 1467;
update tasly_warehouse_storage_bin set storage_bin = '02-25-03' where id = 1468;
update tasly_warehouse_storage_bin set storage_bin = '02-26-03' where id = 1469;
update tasly_warehouse_storage_bin set storage_bin = '02-27-03' where id = 1470;
update tasly_warehouse_storage_bin set storage_bin = '02-28-03' where id = 1471;
update tasly_warehouse_storage_bin set storage_bin = '02-29-03' where id = 1472;
update tasly_warehouse_storage_bin set storage_bin = '02-30-03' where id = 1473;
update tasly_warehouse_storage_bin set storage_bin = '02-31-03' where id = 1474;
update tasly_warehouse_storage_bin set storage_bin = '02-32-03' where id = 1475;
update tasly_warehouse_storage_bin set storage_bin = '02-01-04' where id = 1476;
update tasly_warehouse_storage_bin set storage_bin = '02-02-04' where id = 1477;
update tasly_warehouse_storage_bin set storage_bin = '02-03-04' where id = 1478;
update tasly_warehouse_storage_bin set storage_bin = '02-04-04' where id = 1479;
update tasly_warehouse_storage_bin set storage_bin = '02-05-04' where id = 1480;
update tasly_warehouse_storage_bin set storage_bin = '02-06-04' where id = 1481;
update tasly_warehouse_storage_bin set storage_bin = '02-07-04' where id = 1482;
update tasly_warehouse_storage_bin set storage_bin = '02-08-04' where id = 1483;
update tasly_warehouse_storage_bin set storage_bin = '02-09-04' where id = 1484;
update tasly_warehouse_storage_bin set storage_bin = '02-10-04' where id = 1485;
update tasly_warehouse_storage_bin set storage_bin = '02-11-04' where id = 1486;
update tasly_warehouse_storage_bin set storage_bin = '02-12-04' where id = 1487;
update tasly_warehouse_storage_bin set storage_bin = '02-13-04' where id = 1488;
update tasly_warehouse_storage_bin set storage_bin = '02-14-04' where id = 1489;
update tasly_warehouse_storage_bin set storage_bin = '02-15-04' where id = 1490;
update tasly_warehouse_storage_bin set storage_bin = '02-16-04' where id = 1491;
update tasly_warehouse_storage_bin set storage_bin = '02-17-04' where id = 1492;
update tasly_warehouse_storage_bin set storage_bin = '02-18-04' where id = 1493;
update tasly_warehouse_storage_bin set storage_bin = '02-19-04' where id = 1494;
update tasly_warehouse_storage_bin set storage_bin = '02-20-04' where id = 1495;
update tasly_warehouse_storage_bin set storage_bin = '02-21-04' where id = 1496;
update tasly_warehouse_storage_bin set storage_bin = '02-22-04' where id = 1497;
update tasly_warehouse_storage_bin set storage_bin = '02-23-04' where id = 1498;
update tasly_warehouse_storage_bin set storage_bin = '02-24-04' where id = 1499;
update tasly_warehouse_storage_bin set storage_bin = '02-25-04' where id = 1500;
update tasly_warehouse_storage_bin set storage_bin = '02-26-04' where id = 1501;
update tasly_warehouse_storage_bin set storage_bin = '02-27-04' where id = 1502;
update tasly_warehouse_storage_bin set storage_bin = '02-28-04' where id = 1503;
update tasly_warehouse_storage_bin set storage_bin = '02-29-04' where id = 1504;
update tasly_warehouse_storage_bin set storage_bin = '02-30-04' where id = 1505;
update tasly_warehouse_storage_bin set storage_bin = '02-31-04' where id = 1506;
update tasly_warehouse_storage_bin set storage_bin = '02-32-04' where id = 1507;
update tasly_warehouse_storage_bin set storage_bin = '02-01-05' where id = 1508;
update tasly_warehouse_storage_bin set storage_bin = '02-02-05' where id = 1509;
update tasly_warehouse_storage_bin set storage_bin = '02-03-05' where id = 1510;
update tasly_warehouse_storage_bin set storage_bin = '02-04-05' where id = 1511;
update tasly_warehouse_storage_bin set storage_bin = '02-05-05' where id = 1512;
update tasly_warehouse_storage_bin set storage_bin = '02-06-05' where id = 1513;
update tasly_warehouse_storage_bin set storage_bin = '02-07-05' where id = 1514;
update tasly_warehouse_storage_bin set storage_bin = '02-08-05' where id = 1515;
update tasly_warehouse_storage_bin set storage_bin = '02-09-05' where id = 1516;
update tasly_warehouse_storage_bin set storage_bin = '02-10-05' where id = 1517;
update tasly_warehouse_storage_bin set storage_bin = '02-11-05' where id = 1518;
update tasly_warehouse_storage_bin set storage_bin = '02-12-05' where id = 1519;
update tasly_warehouse_storage_bin set storage_bin = '02-13-05' where id = 1520;
update tasly_warehouse_storage_bin set storage_bin = '02-14-05' where id = 1521;
update tasly_warehouse_storage_bin set storage_bin = '02-15-05' where id = 1522;
update tasly_warehouse_storage_bin set storage_bin = '02-16-05' where id = 1523;
update tasly_warehouse_storage_bin set storage_bin = '02-17-05' where id = 1524;
update tasly_warehouse_storage_bin set storage_bin = '02-18-05' where id = 1525;
update tasly_warehouse_storage_bin set storage_bin = '02-19-05' where id = 1526;
update tasly_warehouse_storage_bin set storage_bin = '02-20-05' where id = 1527;
update tasly_warehouse_storage_bin set storage_bin = '02-21-05' where id = 1528;
update tasly_warehouse_storage_bin set storage_bin = '02-22-05' where id = 1529;
update tasly_warehouse_storage_bin set storage_bin = '02-23-05' where id = 1530;
update tasly_warehouse_storage_bin set storage_bin = '02-24-05' where id = 1531;
update tasly_warehouse_storage_bin set storage_bin = '02-25-05' where id = 1532;
update tasly_warehouse_storage_bin set storage_bin = '02-26-05' where id = 1533;
update tasly_warehouse_storage_bin set storage_bin = '02-27-05' where id = 1534;
update tasly_warehouse_storage_bin set storage_bin = '02-28-05' where id = 1535;
update tasly_warehouse_storage_bin set storage_bin = '02-29-05' where id = 1536;
update tasly_warehouse_storage_bin set storage_bin = '02-30-05' where id = 1537;
update tasly_warehouse_storage_bin set storage_bin = '02-31-05' where id = 1538;
update tasly_warehouse_storage_bin set storage_bin = '02-32-05' where id = 1539;
update tasly_warehouse_storage_bin set storage_bin = '02-02-06' where id = 1540;
update tasly_warehouse_storage_bin set storage_bin = '02-03-06' where id = 1541;
update tasly_warehouse_storage_bin set storage_bin = '02-04-06' where id = 1542;
update tasly_warehouse_storage_bin set storage_bin = '02-05-06' where id = 1543;
update tasly_warehouse_storage_bin set storage_bin = '02-06-06' where id = 1544;
update tasly_warehouse_storage_bin set storage_bin = '02-07-06' where id = 1545;
update tasly_warehouse_storage_bin set storage_bin = '02-08-06' where id = 1546;
update tasly_warehouse_storage_bin set storage_bin = '02-09-06' where id = 1547;
update tasly_warehouse_storage_bin set storage_bin = '02-10-06' where id = 1548;
update tasly_warehouse_storage_bin set storage_bin = '02-11-06' where id = 1549;
update tasly_warehouse_storage_bin set storage_bin = '02-12-06' where id = 1550;
update tasly_warehouse_storage_bin set storage_bin = '02-13-06' where id = 1551;
update tasly_warehouse_storage_bin set storage_bin = '02-14-06' where id = 1552;
update tasly_warehouse_storage_bin set storage_bin = '02-15-06' where id = 1553;
update tasly_warehouse_storage_bin set storage_bin = '02-16-06' where id = 1554;
update tasly_warehouse_storage_bin set storage_bin = '02-17-06' where id = 1555;
update tasly_warehouse_storage_bin set storage_bin = '02-18-06' where id = 1556;
update tasly_warehouse_storage_bin set storage_bin = '02-19-06' where id = 1557;
update tasly_warehouse_storage_bin set storage_bin = '02-20-06' where id = 1558;
update tasly_warehouse_storage_bin set storage_bin = '02-21-06' where id = 1559;
update tasly_warehouse_storage_bin set storage_bin = '02-22-06' where id = 1560;
update tasly_warehouse_storage_bin set storage_bin = '02-23-06' where id = 1561;
update tasly_warehouse_storage_bin set storage_bin = '02-24-06' where id = 1562;
update tasly_warehouse_storage_bin set storage_bin = '02-25-06' where id = 1563;
update tasly_warehouse_storage_bin set storage_bin = '02-26-06' where id = 1564;
update tasly_warehouse_storage_bin set storage_bin = '02-27-06' where id = 1565;
update tasly_warehouse_storage_bin set storage_bin = '02-28-06' where id = 1566;
update tasly_warehouse_storage_bin set storage_bin = '02-29-06' where id = 1567;
update tasly_warehouse_storage_bin set storage_bin = '02-30-06' where id = 1568;
update tasly_warehouse_storage_bin set storage_bin = '02-31-06' where id = 1569;
update tasly_warehouse_storage_bin set storage_bin = '02-32-06' where id = 1570;
update tasly_warehouse_storage_bin set storage_bin = '03-02-06' where id = 1571;
update tasly_warehouse_storage_bin set storage_bin = '03-03-06' where id = 1572;
update tasly_warehouse_storage_bin set storage_bin = '03-04-06' where id = 1573;
update tasly_warehouse_storage_bin set storage_bin = '03-05-06' where id = 1574;
update tasly_warehouse_storage_bin set storage_bin = '03-06-06' where id = 1575;
update tasly_warehouse_storage_bin set storage_bin = '03-07-06' where id = 1576;
update tasly_warehouse_storage_bin set storage_bin = '03-08-06' where id = 1577;
update tasly_warehouse_storage_bin set storage_bin = '03-09-06' where id = 1578;
update tasly_warehouse_storage_bin set storage_bin = '03-10-06' where id = 1579;
update tasly_warehouse_storage_bin set storage_bin = '03-11-06' where id = 1580;
update tasly_warehouse_storage_bin set storage_bin = '03-12-06' where id = 1581;
update tasly_warehouse_storage_bin set storage_bin = '03-13-06' where id = 1582;
update tasly_warehouse_storage_bin set storage_bin = '03-14-06' where id = 1583;
update tasly_warehouse_storage_bin set storage_bin = '03-15-06' where id = 1584;
update tasly_warehouse_storage_bin set storage_bin = '03-16-06' where id = 1585;
update tasly_warehouse_storage_bin set storage_bin = '03-17-06' where id = 1586;
update tasly_warehouse_storage_bin set storage_bin = '03-18-06' where id = 1587;
update tasly_warehouse_storage_bin set storage_bin = '03-19-06' where id = 1588;
update tasly_warehouse_storage_bin set storage_bin = '03-20-06' where id = 1589;
update tasly_warehouse_storage_bin set storage_bin = '03-21-06' where id = 1590;
update tasly_warehouse_storage_bin set storage_bin = '03-22-06' where id = 1591;
update tasly_warehouse_storage_bin set storage_bin = '03-23-06' where id = 1592;
update tasly_warehouse_storage_bin set storage_bin = '03-24-06' where id = 1593;
update tasly_warehouse_storage_bin set storage_bin = '03-25-06' where id = 1594;
update tasly_warehouse_storage_bin set storage_bin = '03-26-06' where id = 1595;
update tasly_warehouse_storage_bin set storage_bin = '03-27-06' where id = 1596;
update tasly_warehouse_storage_bin set storage_bin = '03-28-06' where id = 1597;
update tasly_warehouse_storage_bin set storage_bin = '03-29-06' where id = 1598;
update tasly_warehouse_storage_bin set storage_bin = '03-30-06' where id = 1599;
update tasly_warehouse_storage_bin set storage_bin = '03-31-06' where id = 1600;
update tasly_warehouse_storage_bin set storage_bin = '03-32-06' where id = 1601;
update tasly_warehouse_storage_bin set storage_bin = '03-01-05' where id = 1602;
update tasly_warehouse_storage_bin set storage_bin = '03-02-05' where id = 1603;
update tasly_warehouse_storage_bin set storage_bin = '03-03-05' where id = 1604;
update tasly_warehouse_storage_bin set storage_bin = '03-04-05' where id = 1605;
update tasly_warehouse_storage_bin set storage_bin = '03-05-05' where id = 1606;
update tasly_warehouse_storage_bin set storage_bin = '03-06-05' where id = 1607;
update tasly_warehouse_storage_bin set storage_bin = '03-07-05' where id = 1608;
update tasly_warehouse_storage_bin set storage_bin = '03-08-05' where id = 1609;
update tasly_warehouse_storage_bin set storage_bin = '03-09-05' where id = 1610;
update tasly_warehouse_storage_bin set storage_bin = '03-10-05' where id = 1611;
update tasly_warehouse_storage_bin set storage_bin = '03-11-05' where id = 1612;
update tasly_warehouse_storage_bin set storage_bin = '03-12-05' where id = 1613;
update tasly_warehouse_storage_bin set storage_bin = '03-13-05' where id = 1614;
update tasly_warehouse_storage_bin set storage_bin = '03-14-05' where id = 1615;
update tasly_warehouse_storage_bin set storage_bin = '03-15-05' where id = 1616;
update tasly_warehouse_storage_bin set storage_bin = '03-16-05' where id = 1617;
update tasly_warehouse_storage_bin set storage_bin = '03-17-05' where id = 1618;
update tasly_warehouse_storage_bin set storage_bin = '03-18-05' where id = 1619;
update tasly_warehouse_storage_bin set storage_bin = '03-19-05' where id = 1620;
update tasly_warehouse_storage_bin set storage_bin = '03-20-05' where id = 1621;
update tasly_warehouse_storage_bin set storage_bin = '03-21-05' where id = 1622;
update tasly_warehouse_storage_bin set storage_bin = '03-22-05' where id = 1623;
update tasly_warehouse_storage_bin set storage_bin = '03-23-05' where id = 1624;
update tasly_warehouse_storage_bin set storage_bin = '03-24-05' where id = 1625;
update tasly_warehouse_storage_bin set storage_bin = '03-25-05' where id = 1626;
update tasly_warehouse_storage_bin set storage_bin = '03-26-05' where id = 1627;
update tasly_warehouse_storage_bin set storage_bin = '03-27-05' where id = 1628;
update tasly_warehouse_storage_bin set storage_bin = '03-28-05' where id = 1629;
update tasly_warehouse_storage_bin set storage_bin = '03-29-05' where id = 1630;
update tasly_warehouse_storage_bin set storage_bin = '03-30-05' where id = 1631;
update tasly_warehouse_storage_bin set storage_bin = '03-31-05' where id = 1632;
update tasly_warehouse_storage_bin set storage_bin = '03-32-05' where id = 1633;
update tasly_warehouse_storage_bin set storage_bin = '03-01-04' where id = 1634;
update tasly_warehouse_storage_bin set storage_bin = '03-02-04' where id = 1635;
update tasly_warehouse_storage_bin set storage_bin = '03-03-04' where id = 1636;
update tasly_warehouse_storage_bin set storage_bin = '03-04-04' where id = 1637;
update tasly_warehouse_storage_bin set storage_bin = '03-05-04' where id = 1638;
update tasly_warehouse_storage_bin set storage_bin = '03-06-04' where id = 1639;
update tasly_warehouse_storage_bin set storage_bin = '03-07-04' where id = 1640;
update tasly_warehouse_storage_bin set storage_bin = '03-08-04' where id = 1641;
update tasly_warehouse_storage_bin set storage_bin = '03-09-04' where id = 1642;
update tasly_warehouse_storage_bin set storage_bin = '03-10-04' where id = 1643;
update tasly_warehouse_storage_bin set storage_bin = '03-11-04' where id = 1644;
update tasly_warehouse_storage_bin set storage_bin = '03-12-04' where id = 1645;
update tasly_warehouse_storage_bin set storage_bin = '03-13-04' where id = 1646;
update tasly_warehouse_storage_bin set storage_bin = '03-14-04' where id = 1647;
update tasly_warehouse_storage_bin set storage_bin = '03-15-04' where id = 1648;
update tasly_warehouse_storage_bin set storage_bin = '03-16-04' where id = 1649;
update tasly_warehouse_storage_bin set storage_bin = '03-17-04' where id = 1650;
update tasly_warehouse_storage_bin set storage_bin = '03-18-04' where id = 1651;
update tasly_warehouse_storage_bin set storage_bin = '03-19-04' where id = 1652;
update tasly_warehouse_storage_bin set storage_bin = '03-20-04' where id = 1653;
update tasly_warehouse_storage_bin set storage_bin = '03-21-04' where id = 1654;
update tasly_warehouse_storage_bin set storage_bin = '03-22-04' where id = 1655;
update tasly_warehouse_storage_bin set storage_bin = '03-23-04' where id = 1656;
update tasly_warehouse_storage_bin set storage_bin = '03-24-04' where id = 1657;
update tasly_warehouse_storage_bin set storage_bin = '03-25-04' where id = 1658;
update tasly_warehouse_storage_bin set storage_bin = '03-26-04' where id = 1659;
update tasly_warehouse_storage_bin set storage_bin = '03-27-04' where id = 1660;
update tasly_warehouse_storage_bin set storage_bin = '03-28-04' where id = 1661;
update tasly_warehouse_storage_bin set storage_bin = '03-29-04' where id = 1662;
update tasly_warehouse_storage_bin set storage_bin = '03-30-04' where id = 1663;
update tasly_warehouse_storage_bin set storage_bin = '03-31-04' where id = 1664;
update tasly_warehouse_storage_bin set storage_bin = '03-32-04' where id = 1665;
update tasly_warehouse_storage_bin set storage_bin = '03-01-03' where id = 1666;
update tasly_warehouse_storage_bin set storage_bin = '03-02-03' where id = 1667;
update tasly_warehouse_storage_bin set storage_bin = '03-03-03' where id = 1668;
update tasly_warehouse_storage_bin set storage_bin = '03-04-03' where id = 1669;
update tasly_warehouse_storage_bin set storage_bin = '03-05-03' where id = 1670;
update tasly_warehouse_storage_bin set storage_bin = '03-06-03' where id = 1671;
update tasly_warehouse_storage_bin set storage_bin = '03-07-03' where id = 1672;
update tasly_warehouse_storage_bin set storage_bin = '03-08-03' where id = 1673;
update tasly_warehouse_storage_bin set storage_bin = '03-09-03' where id = 1674;
update tasly_warehouse_storage_bin set storage_bin = '03-10-03' where id = 1675;
update tasly_warehouse_storage_bin set storage_bin = '03-11-03' where id = 1676;
update tasly_warehouse_storage_bin set storage_bin = '03-12-03' where id = 1677;
update tasly_warehouse_storage_bin set storage_bin = '03-13-03' where id = 1678;
update tasly_warehouse_storage_bin set storage_bin = '03-14-03' where id = 1679;
update tasly_warehouse_storage_bin set storage_bin = '03-15-03' where id = 1680;
update tasly_warehouse_storage_bin set storage_bin = '03-16-03' where id = 1681;
update tasly_warehouse_storage_bin set storage_bin = '03-17-03' where id = 1682;
update tasly_warehouse_storage_bin set storage_bin = '03-18-03' where id = 1683;
update tasly_warehouse_storage_bin set storage_bin = '03-19-03' where id = 1684;
update tasly_warehouse_storage_bin set storage_bin = '03-20-03' where id = 1685;
update tasly_warehouse_storage_bin set storage_bin = '03-21-03' where id = 1686;
update tasly_warehouse_storage_bin set storage_bin = '03-22-03' where id = 1687;
update tasly_warehouse_storage_bin set storage_bin = '03-23-03' where id = 1688;
update tasly_warehouse_storage_bin set storage_bin = '03-24-03' where id = 1689;
update tasly_warehouse_storage_bin set storage_bin = '03-25-03' where id = 1690;
update tasly_warehouse_storage_bin set storage_bin = '03-26-03' where id = 1691;
update tasly_warehouse_storage_bin set storage_bin = '03-27-03' where id = 1692;
update tasly_warehouse_storage_bin set storage_bin = '03-28-03' where id = 1693;
update tasly_warehouse_storage_bin set storage_bin = '03-29-03' where id = 1694;
update tasly_warehouse_storage_bin set storage_bin = '03-30-03' where id = 1695;
update tasly_warehouse_storage_bin set storage_bin = '03-31-03' where id = 1696;
update tasly_warehouse_storage_bin set storage_bin = '03-32-03' where id = 1697;
update tasly_warehouse_storage_bin set storage_bin = '03-02-02' where id = 1698;
update tasly_warehouse_storage_bin set storage_bin = '03-03-02' where id = 1699;
update tasly_warehouse_storage_bin set storage_bin = '03-04-02' where id = 1700;
update tasly_warehouse_storage_bin set storage_bin = '03-05-02' where id = 1701;
update tasly_warehouse_storage_bin set storage_bin = '03-06-02' where id = 1702;
update tasly_warehouse_storage_bin set storage_bin = '03-07-02' where id = 1703;
update tasly_warehouse_storage_bin set storage_bin = '03-08-02' where id = 1704;
update tasly_warehouse_storage_bin set storage_bin = '03-09-02' where id = 1705;
update tasly_warehouse_storage_bin set storage_bin = '03-10-02' where id = 1706;
update tasly_warehouse_storage_bin set storage_bin = '03-11-02' where id = 1707;
update tasly_warehouse_storage_bin set storage_bin = '03-12-02' where id = 1708;
update tasly_warehouse_storage_bin set storage_bin = '03-13-02' where id = 1709;
update tasly_warehouse_storage_bin set storage_bin = '03-14-02' where id = 1710;
update tasly_warehouse_storage_bin set storage_bin = '03-15-02' where id = 1711;
update tasly_warehouse_storage_bin set storage_bin = '03-16-02' where id = 1712;
update tasly_warehouse_storage_bin set storage_bin = '03-17-02' where id = 1713;
update tasly_warehouse_storage_bin set storage_bin = '03-18-02' where id = 1714;
update tasly_warehouse_storage_bin set storage_bin = '03-19-02' where id = 1715;
update tasly_warehouse_storage_bin set storage_bin = '03-20-02' where id = 1716;
update tasly_warehouse_storage_bin set storage_bin = '03-21-02' where id = 1717;
update tasly_warehouse_storage_bin set storage_bin = '03-22-02' where id = 1718;
update tasly_warehouse_storage_bin set storage_bin = '03-23-02' where id = 1719;
update tasly_warehouse_storage_bin set storage_bin = '03-24-02' where id = 1720;
update tasly_warehouse_storage_bin set storage_bin = '03-25-02' where id = 1721;
update tasly_warehouse_storage_bin set storage_bin = '03-26-02' where id = 1722;
update tasly_warehouse_storage_bin set storage_bin = '03-27-02' where id = 1723;
update tasly_warehouse_storage_bin set storage_bin = '03-28-02' where id = 1724;
update tasly_warehouse_storage_bin set storage_bin = '03-29-02' where id = 1725;
update tasly_warehouse_storage_bin set storage_bin = '03-30-02' where id = 1726;
update tasly_warehouse_storage_bin set storage_bin = '03-31-02' where id = 1727;
update tasly_warehouse_storage_bin set storage_bin = '03-32-02' where id = 1728;
update tasly_warehouse_storage_bin set storage_bin = '03-02-01' where id = 1729;
update tasly_warehouse_storage_bin set storage_bin = '03-03-01' where id = 1730;
update tasly_warehouse_storage_bin set storage_bin = '03-04-01' where id = 1731;
update tasly_warehouse_storage_bin set storage_bin = '03-05-01' where id = 1732;
update tasly_warehouse_storage_bin set storage_bin = '03-06-01' where id = 1733;
update tasly_warehouse_storage_bin set storage_bin = '03-07-01' where id = 1734;
update tasly_warehouse_storage_bin set storage_bin = '03-08-01' where id = 1735;
update tasly_warehouse_storage_bin set storage_bin = '03-09-01' where id = 1736;
update tasly_warehouse_storage_bin set storage_bin = '03-10-01' where id = 1737;
update tasly_warehouse_storage_bin set storage_bin = '03-11-01' where id = 1738;
update tasly_warehouse_storage_bin set storage_bin = '03-12-01' where id = 1739;
update tasly_warehouse_storage_bin set storage_bin = '03-13-01' where id = 1740;
update tasly_warehouse_storage_bin set storage_bin = '03-14-01' where id = 1741;
update tasly_warehouse_storage_bin set storage_bin = '03-15-01' where id = 1742;
update tasly_warehouse_storage_bin set storage_bin = '03-16-01' where id = 1743;
update tasly_warehouse_storage_bin set storage_bin = '03-17-01' where id = 1744;
update tasly_warehouse_storage_bin set storage_bin = '03-18-01' where id = 1745;
update tasly_warehouse_storage_bin set storage_bin = '03-19-01' where id = 1746;
update tasly_warehouse_storage_bin set storage_bin = '03-20-01' where id = 1747;
update tasly_warehouse_storage_bin set storage_bin = '03-21-01' where id = 1748;
update tasly_warehouse_storage_bin set storage_bin = '03-22-01' where id = 1749;
update tasly_warehouse_storage_bin set storage_bin = '03-23-01' where id = 1750;
update tasly_warehouse_storage_bin set storage_bin = '03-24-01' where id = 1751;
update tasly_warehouse_storage_bin set storage_bin = '03-25-01' where id = 1752;
update tasly_warehouse_storage_bin set storage_bin = '03-26-01' where id = 1753;
update tasly_warehouse_storage_bin set storage_bin = '03-27-01' where id = 1754;
update tasly_warehouse_storage_bin set storage_bin = '03-28-01' where id = 1755;
update tasly_warehouse_storage_bin set storage_bin = '03-29-01' where id = 1756;
update tasly_warehouse_storage_bin set storage_bin = '03-30-01' where id = 1757;
update tasly_warehouse_storage_bin set storage_bin = '03-31-01' where id = 1758;
update tasly_warehouse_storage_bin set storage_bin = '03-32-01' where id = 1759;
update tasly_warehouse_storage_bin set storage_bin = '04-02-01' where id = 1760;
update tasly_warehouse_storage_bin set storage_bin = '04-03-01' where id = 1761;
update tasly_warehouse_storage_bin set storage_bin = '04-04-01' where id = 1762;
update tasly_warehouse_storage_bin set storage_bin = '04-05-01' where id = 1763;
update tasly_warehouse_storage_bin set storage_bin = '04-06-01' where id = 1764;
update tasly_warehouse_storage_bin set storage_bin = '04-07-01' where id = 1765;
update tasly_warehouse_storage_bin set storage_bin = '04-08-01' where id = 1766;
update tasly_warehouse_storage_bin set storage_bin = '04-09-01' where id = 1767;
update tasly_warehouse_storage_bin set storage_bin = '04-10-01' where id = 1768;
update tasly_warehouse_storage_bin set storage_bin = '04-11-01' where id = 1769;
update tasly_warehouse_storage_bin set storage_bin = '04-12-01' where id = 1770;
update tasly_warehouse_storage_bin set storage_bin = '04-13-01' where id = 1771;
update tasly_warehouse_storage_bin set storage_bin = '04-14-01' where id = 1772;
update tasly_warehouse_storage_bin set storage_bin = '04-15-01' where id = 1773;
update tasly_warehouse_storage_bin set storage_bin = '04-16-01' where id = 1774;
update tasly_warehouse_storage_bin set storage_bin = '04-17-01' where id = 1775;
update tasly_warehouse_storage_bin set storage_bin = '04-18-01' where id = 1776;
update tasly_warehouse_storage_bin set storage_bin = '04-19-01' where id = 1777;
update tasly_warehouse_storage_bin set storage_bin = '04-20-01' where id = 1778;
update tasly_warehouse_storage_bin set storage_bin = '04-21-01' where id = 1779;
update tasly_warehouse_storage_bin set storage_bin = '04-22-01' where id = 1780;
update tasly_warehouse_storage_bin set storage_bin = '04-23-01' where id = 1781;
update tasly_warehouse_storage_bin set storage_bin = '04-24-01' where id = 1782;
update tasly_warehouse_storage_bin set storage_bin = '04-25-01' where id = 1783;
update tasly_warehouse_storage_bin set storage_bin = '04-26-01' where id = 1784;
update tasly_warehouse_storage_bin set storage_bin = '04-27-01' where id = 1785;
update tasly_warehouse_storage_bin set storage_bin = '04-28-01' where id = 1786;
update tasly_warehouse_storage_bin set storage_bin = '04-29-01' where id = 1787;
update tasly_warehouse_storage_bin set storage_bin = '04-30-01' where id = 1788;
update tasly_warehouse_storage_bin set storage_bin = '04-31-01' where id = 1789;
update tasly_warehouse_storage_bin set storage_bin = '04-32-01' where id = 1790;
update tasly_warehouse_storage_bin set storage_bin = '04-02-02' where id = 1791;
update tasly_warehouse_storage_bin set storage_bin = '04-03-02' where id = 1792;
update tasly_warehouse_storage_bin set storage_bin = '04-04-02' where id = 1793;
update tasly_warehouse_storage_bin set storage_bin = '04-05-02' where id = 1794;
update tasly_warehouse_storage_bin set storage_bin = '04-06-02' where id = 1795;
update tasly_warehouse_storage_bin set storage_bin = '04-07-02' where id = 1796;
update tasly_warehouse_storage_bin set storage_bin = '04-08-02' where id = 1797;
update tasly_warehouse_storage_bin set storage_bin = '04-09-02' where id = 1798;
update tasly_warehouse_storage_bin set storage_bin = '04-10-02' where id = 1799;
update tasly_warehouse_storage_bin set storage_bin = '04-11-02' where id = 1800;
update tasly_warehouse_storage_bin set storage_bin = '04-12-02' where id = 1801;
update tasly_warehouse_storage_bin set storage_bin = '04-13-02' where id = 1802;
update tasly_warehouse_storage_bin set storage_bin = '04-14-02' where id = 1803;
update tasly_warehouse_storage_bin set storage_bin = '04-15-02' where id = 1804;
update tasly_warehouse_storage_bin set storage_bin = '04-16-02' where id = 1805;
update tasly_warehouse_storage_bin set storage_bin = '04-17-02' where id = 1806;
update tasly_warehouse_storage_bin set storage_bin = '04-18-02' where id = 1807;
update tasly_warehouse_storage_bin set storage_bin = '04-19-02' where id = 1808;
update tasly_warehouse_storage_bin set storage_bin = '04-20-02' where id = 1809;
update tasly_warehouse_storage_bin set storage_bin = '04-21-02' where id = 1810;
update tasly_warehouse_storage_bin set storage_bin = '04-22-02' where id = 1811;
update tasly_warehouse_storage_bin set storage_bin = '04-23-02' where id = 1812;
update tasly_warehouse_storage_bin set storage_bin = '04-24-02' where id = 1813;
update tasly_warehouse_storage_bin set storage_bin = '04-25-02' where id = 1814;
update tasly_warehouse_storage_bin set storage_bin = '04-26-02' where id = 1815;
update tasly_warehouse_storage_bin set storage_bin = '04-27-02' where id = 1816;
update tasly_warehouse_storage_bin set storage_bin = '04-28-02' where id = 1817;
update tasly_warehouse_storage_bin set storage_bin = '04-29-02' where id = 1818;
update tasly_warehouse_storage_bin set storage_bin = '04-30-02' where id = 1819;
update tasly_warehouse_storage_bin set storage_bin = '04-31-02' where id = 1820;
update tasly_warehouse_storage_bin set storage_bin = '04-32-02' where id = 1821;
update tasly_warehouse_storage_bin set storage_bin = '04-02-03' where id = 1822;
update tasly_warehouse_storage_bin set storage_bin = '04-03-03' where id = 1823;
update tasly_warehouse_storage_bin set storage_bin = '04-04-03' where id = 1824;
update tasly_warehouse_storage_bin set storage_bin = '04-05-03' where id = 1825;
update tasly_warehouse_storage_bin set storage_bin = '04-06-03' where id = 1826;
update tasly_warehouse_storage_bin set storage_bin = '04-07-03' where id = 1827;
update tasly_warehouse_storage_bin set storage_bin = '04-08-03' where id = 1828;
update tasly_warehouse_storage_bin set storage_bin = '04-09-03' where id = 1829;
update tasly_warehouse_storage_bin set storage_bin = '04-10-03' where id = 1830;
update tasly_warehouse_storage_bin set storage_bin = '04-11-03' where id = 1831;
update tasly_warehouse_storage_bin set storage_bin = '04-12-03' where id = 1832;
update tasly_warehouse_storage_bin set storage_bin = '04-13-03' where id = 1833;
update tasly_warehouse_storage_bin set storage_bin = '04-14-03' where id = 1834;
update tasly_warehouse_storage_bin set storage_bin = '04-15-03' where id = 1835;
update tasly_warehouse_storage_bin set storage_bin = '04-16-03' where id = 1836;
update tasly_warehouse_storage_bin set storage_bin = '04-17-03' where id = 1837;
update tasly_warehouse_storage_bin set storage_bin = '04-18-03' where id = 1838;
update tasly_warehouse_storage_bin set storage_bin = '04-19-03' where id = 1839;
update tasly_warehouse_storage_bin set storage_bin = '04-20-03' where id = 1840;
update tasly_warehouse_storage_bin set storage_bin = '04-21-03' where id = 1841;
update tasly_warehouse_storage_bin set storage_bin = '04-22-03' where id = 1842;
update tasly_warehouse_storage_bin set storage_bin = '04-23-03' where id = 1843;
update tasly_warehouse_storage_bin set storage_bin = '04-24-03' where id = 1844;
update tasly_warehouse_storage_bin set storage_bin = '04-25-03' where id = 1845;
update tasly_warehouse_storage_bin set storage_bin = '04-26-03' where id = 1846;
update tasly_warehouse_storage_bin set storage_bin = '04-27-03' where id = 1847;
update tasly_warehouse_storage_bin set storage_bin = '04-28-03' where id = 1848;
update tasly_warehouse_storage_bin set storage_bin = '04-29-03' where id = 1849;
update tasly_warehouse_storage_bin set storage_bin = '04-30-03' where id = 1850;
update tasly_warehouse_storage_bin set storage_bin = '04-31-03' where id = 1851;
update tasly_warehouse_storage_bin set storage_bin = '04-32-03' where id = 1852;
update tasly_warehouse_storage_bin set storage_bin = '04-02-04' where id = 1853;
update tasly_warehouse_storage_bin set storage_bin = '04-03-04' where id = 1854;
update tasly_warehouse_storage_bin set storage_bin = '04-04-04' where id = 1855;
update tasly_warehouse_storage_bin set storage_bin = '04-05-04' where id = 1856;
update tasly_warehouse_storage_bin set storage_bin = '04-06-04' where id = 1857;
update tasly_warehouse_storage_bin set storage_bin = '04-07-04' where id = 1858;
update tasly_warehouse_storage_bin set storage_bin = '04-08-04' where id = 1859;
update tasly_warehouse_storage_bin set storage_bin = '04-09-04' where id = 1860;
update tasly_warehouse_storage_bin set storage_bin = '04-10-04' where id = 1861;
update tasly_warehouse_storage_bin set storage_bin = '04-11-04' where id = 1862;
update tasly_warehouse_storage_bin set storage_bin = '04-12-04' where id = 1863;
update tasly_warehouse_storage_bin set storage_bin = '04-13-04' where id = 1864;
update tasly_warehouse_storage_bin set storage_bin = '04-14-04' where id = 1865;
update tasly_warehouse_storage_bin set storage_bin = '04-15-04' where id = 1866;
update tasly_warehouse_storage_bin set storage_bin = '04-16-04' where id = 1867;
update tasly_warehouse_storage_bin set storage_bin = '04-17-04' where id = 1868;
update tasly_warehouse_storage_bin set storage_bin = '04-18-04' where id = 1869;
update tasly_warehouse_storage_bin set storage_bin = '04-19-04' where id = 1870;
update tasly_warehouse_storage_bin set storage_bin = '04-20-04' where id = 1871;
update tasly_warehouse_storage_bin set storage_bin = '04-21-04' where id = 1872;
update tasly_warehouse_storage_bin set storage_bin = '04-22-04' where id = 1873;
update tasly_warehouse_storage_bin set storage_bin = '04-23-04' where id = 1874;
update tasly_warehouse_storage_bin set storage_bin = '04-24-04' where id = 1875;
update tasly_warehouse_storage_bin set storage_bin = '04-25-04' where id = 1876;
update tasly_warehouse_storage_bin set storage_bin = '04-26-04' where id = 1877;
update tasly_warehouse_storage_bin set storage_bin = '04-27-04' where id = 1878;
update tasly_warehouse_storage_bin set storage_bin = '04-28-04' where id = 1879;
update tasly_warehouse_storage_bin set storage_bin = '04-29-04' where id = 1880;
update tasly_warehouse_storage_bin set storage_bin = '04-30-04' where id = 1881;
update tasly_warehouse_storage_bin set storage_bin = '04-31-04' where id = 1882;
update tasly_warehouse_storage_bin set storage_bin = '04-32-04' where id = 1883;
update tasly_warehouse_storage_bin set storage_bin = '04-02-05' where id = 1884;
update tasly_warehouse_storage_bin set storage_bin = '04-03-05' where id = 1885;
update tasly_warehouse_storage_bin set storage_bin = '04-04-05' where id = 1886;
update tasly_warehouse_storage_bin set storage_bin = '04-05-05' where id = 1887;
update tasly_warehouse_storage_bin set storage_bin = '04-06-05' where id = 1888;
update tasly_warehouse_storage_bin set storage_bin = '04-07-05' where id = 1889;
update tasly_warehouse_storage_bin set storage_bin = '04-08-05' where id = 1890;
update tasly_warehouse_storage_bin set storage_bin = '04-09-05' where id = 1891;
update tasly_warehouse_storage_bin set storage_bin = '04-10-05' where id = 1892;
update tasly_warehouse_storage_bin set storage_bin = '04-11-05' where id = 1893;
update tasly_warehouse_storage_bin set storage_bin = '04-12-05' where id = 1894;
update tasly_warehouse_storage_bin set storage_bin = '04-13-05' where id = 1895;
update tasly_warehouse_storage_bin set storage_bin = '04-14-05' where id = 1896;
update tasly_warehouse_storage_bin set storage_bin = '04-15-05' where id = 1897;
update tasly_warehouse_storage_bin set storage_bin = '04-16-05' where id = 1898;
update tasly_warehouse_storage_bin set storage_bin = '04-17-05' where id = 1899;
update tasly_warehouse_storage_bin set storage_bin = '04-18-05' where id = 1900;
update tasly_warehouse_storage_bin set storage_bin = '04-19-05' where id = 1901;
update tasly_warehouse_storage_bin set storage_bin = '04-20-05' where id = 1902;
update tasly_warehouse_storage_bin set storage_bin = '04-21-05' where id = 1903;
update tasly_warehouse_storage_bin set storage_bin = '04-22-05' where id = 1904;
update tasly_warehouse_storage_bin set storage_bin = '04-23-05' where id = 1905;
update tasly_warehouse_storage_bin set storage_bin = '04-24-05' where id = 1906;
update tasly_warehouse_storage_bin set storage_bin = '04-25-05' where id = 1907;
update tasly_warehouse_storage_bin set storage_bin = '04-26-05' where id = 1908;
update tasly_warehouse_storage_bin set storage_bin = '04-27-05' where id = 1909;
update tasly_warehouse_storage_bin set storage_bin = '04-28-05' where id = 1910;
update tasly_warehouse_storage_bin set storage_bin = '04-29-05' where id = 1911;
update tasly_warehouse_storage_bin set storage_bin = '04-30-05' where id = 1912;
update tasly_warehouse_storage_bin set storage_bin = '04-31-05' where id = 1913;
update tasly_warehouse_storage_bin set storage_bin = '04-32-05' where id = 1914;
update tasly_warehouse_storage_bin set storage_bin = '04-02-06' where id = 1915;
update tasly_warehouse_storage_bin set storage_bin = '04-03-06' where id = 1916;
update tasly_warehouse_storage_bin set storage_bin = '04-04-06' where id = 1917;
update tasly_warehouse_storage_bin set storage_bin = '04-05-06' where id = 1918;
update tasly_warehouse_storage_bin set storage_bin = '04-06-06' where id = 1919;
update tasly_warehouse_storage_bin set storage_bin = '04-07-06' where id = 1920;
update tasly_warehouse_storage_bin set storage_bin = '04-08-06' where id = 1921;
update tasly_warehouse_storage_bin set storage_bin = '04-09-06' where id = 1922;
update tasly_warehouse_storage_bin set storage_bin = '04-10-06' where id = 1923;
update tasly_warehouse_storage_bin set storage_bin = '04-11-06' where id = 1924;
update tasly_warehouse_storage_bin set storage_bin = '04-12-06' where id = 1925;
update tasly_warehouse_storage_bin set storage_bin = '04-13-06' where id = 1926;
update tasly_warehouse_storage_bin set storage_bin = '04-14-06' where id = 1927;
update tasly_warehouse_storage_bin set storage_bin = '04-15-06' where id = 1928;
update tasly_warehouse_storage_bin set storage_bin = '04-16-06' where id = 1929;
update tasly_warehouse_storage_bin set storage_bin = '04-17-06' where id = 1930;
update tasly_warehouse_storage_bin set storage_bin = '04-18-06' where id = 1931;
update tasly_warehouse_storage_bin set storage_bin = '04-19-06' where id = 1932;
update tasly_warehouse_storage_bin set storage_bin = '04-20-06' where id = 1933;
update tasly_warehouse_storage_bin set storage_bin = '04-21-06' where id = 1934;
update tasly_warehouse_storage_bin set storage_bin = '04-22-06' where id = 1935;
update tasly_warehouse_storage_bin set storage_bin = '04-23-06' where id = 1936;
update tasly_warehouse_storage_bin set storage_bin = '04-24-06' where id = 1937;
update tasly_warehouse_storage_bin set storage_bin = '04-25-06' where id = 1938;
update tasly_warehouse_storage_bin set storage_bin = '04-26-06' where id = 1939;
update tasly_warehouse_storage_bin set storage_bin = '04-27-06' where id = 1940;
update tasly_warehouse_storage_bin set storage_bin = '04-28-06' where id = 1941;
update tasly_warehouse_storage_bin set storage_bin = '04-29-06' where id = 1942;
update tasly_warehouse_storage_bin set storage_bin = '04-30-06' where id = 1943;
update tasly_warehouse_storage_bin set storage_bin = '04-31-06' where id = 1944;
update tasly_warehouse_storage_bin set storage_bin = '04-32-06' where id = 1945;
update tasly_warehouse_storage_bin set storage_bin = '05-02-06' where id = 1946;
update tasly_warehouse_storage_bin set storage_bin = '05-03-06' where id = 1947;
update tasly_warehouse_storage_bin set storage_bin = '05-04-06' where id = 1948;
update tasly_warehouse_storage_bin set storage_bin = '05-05-06' where id = 1949;
update tasly_warehouse_storage_bin set storage_bin = '05-06-06' where id = 1950;
update tasly_warehouse_storage_bin set storage_bin = '05-07-06' where id = 1951;
update tasly_warehouse_storage_bin set storage_bin = '05-08-06' where id = 1952;
update tasly_warehouse_storage_bin set storage_bin = '05-09-06' where id = 1953;
update tasly_warehouse_storage_bin set storage_bin = '05-10-06' where id = 1954;
update tasly_warehouse_storage_bin set storage_bin = '05-11-06' where id = 1955;
update tasly_warehouse_storage_bin set storage_bin = '05-12-06' where id = 1956;
update tasly_warehouse_storage_bin set storage_bin = '05-13-06' where id = 1957;
update tasly_warehouse_storage_bin set storage_bin = '05-14-06' where id = 1958;
update tasly_warehouse_storage_bin set storage_bin = '05-15-06' where id = 1959;
update tasly_warehouse_storage_bin set storage_bin = '05-16-06' where id = 1960;
update tasly_warehouse_storage_bin set storage_bin = '05-17-06' where id = 1961;
update tasly_warehouse_storage_bin set storage_bin = '05-18-06' where id = 1962;
update tasly_warehouse_storage_bin set storage_bin = '05-19-06' where id = 1963;
update tasly_warehouse_storage_bin set storage_bin = '05-20-06' where id = 1964;
update tasly_warehouse_storage_bin set storage_bin = '05-21-06' where id = 1965;
update tasly_warehouse_storage_bin set storage_bin = '05-22-06' where id = 1966;
update tasly_warehouse_storage_bin set storage_bin = '05-23-06' where id = 1967;
update tasly_warehouse_storage_bin set storage_bin = '05-24-06' where id = 1968;
update tasly_warehouse_storage_bin set storage_bin = '05-25-06' where id = 1969;
update tasly_warehouse_storage_bin set storage_bin = '05-26-06' where id = 1970;
update tasly_warehouse_storage_bin set storage_bin = '05-27-06' where id = 1971;
update tasly_warehouse_storage_bin set storage_bin = '05-28-06' where id = 1972;
update tasly_warehouse_storage_bin set storage_bin = '05-29-06' where id = 1973;
update tasly_warehouse_storage_bin set storage_bin = '05-30-06' where id = 1974;
update tasly_warehouse_storage_bin set storage_bin = '05-31-06' where id = 1975;
update tasly_warehouse_storage_bin set storage_bin = '05-32-06' where id = 1976;
update tasly_warehouse_storage_bin set storage_bin = '05-33-06' where id = 1977;
update tasly_warehouse_storage_bin set storage_bin = '05-34-06' where id = 1978;
update tasly_warehouse_storage_bin set storage_bin = '05-01-05' where id = 1979;
update tasly_warehouse_storage_bin set storage_bin = '05-02-05' where id = 1981;
update tasly_warehouse_storage_bin set storage_bin = '05-03-05' where id = 1982;
update tasly_warehouse_storage_bin set storage_bin = '05-04-05' where id = 1983;
update tasly_warehouse_storage_bin set storage_bin = '05-05-05' where id = 1984;
update tasly_warehouse_storage_bin set storage_bin = '05-06-05' where id = 1985;
update tasly_warehouse_storage_bin set storage_bin = '05-07-05' where id = 1986;
update tasly_warehouse_storage_bin set storage_bin = '05-08-05' where id = 1987;
update tasly_warehouse_storage_bin set storage_bin = '05-09-05' where id = 1988;
update tasly_warehouse_storage_bin set storage_bin = '05-10-05' where id = 1989;
update tasly_warehouse_storage_bin set storage_bin = '05-11-05' where id = 1990;
update tasly_warehouse_storage_bin set storage_bin = '05-12-05' where id = 1991;
update tasly_warehouse_storage_bin set storage_bin = '05-13-05' where id = 1992;
update tasly_warehouse_storage_bin set storage_bin = '05-14-05' where id = 1993;
update tasly_warehouse_storage_bin set storage_bin = '05-15-05' where id = 1994;
update tasly_warehouse_storage_bin set storage_bin = '05-16-05' where id = 1995;
update tasly_warehouse_storage_bin set storage_bin = '05-17-05' where id = 1996;
update tasly_warehouse_storage_bin set storage_bin = '05-18-05' where id = 1997;
update tasly_warehouse_storage_bin set storage_bin = '05-19-05' where id = 1998;
update tasly_warehouse_storage_bin set storage_bin = '05-20-05' where id = 1999;
update tasly_warehouse_storage_bin set storage_bin = '05-21-05' where id = 2000;
update tasly_warehouse_storage_bin set storage_bin = '05-22-05' where id = 2001;
update tasly_warehouse_storage_bin set storage_bin = '05-23-05' where id = 2002;
update tasly_warehouse_storage_bin set storage_bin = '05-24-05' where id = 2003;
update tasly_warehouse_storage_bin set storage_bin = '05-25-05' where id = 2004;
update tasly_warehouse_storage_bin set storage_bin = '05-26-05' where id = 2005;
update tasly_warehouse_storage_bin set storage_bin = '05-27-05' where id = 2006;
update tasly_warehouse_storage_bin set storage_bin = '05-28-05' where id = 2007;
update tasly_warehouse_storage_bin set storage_bin = '05-29-05' where id = 2008;
update tasly_warehouse_storage_bin set storage_bin = '05-30-05' where id = 2009;
update tasly_warehouse_storage_bin set storage_bin = '05-31-05' where id = 2010;
update tasly_warehouse_storage_bin set storage_bin = '05-32-05' where id = 2011;
update tasly_warehouse_storage_bin set storage_bin = '05-33-05' where id = 2012;
update tasly_warehouse_storage_bin set storage_bin = '05-34-05' where id = 2013;
update tasly_warehouse_storage_bin set storage_bin = '05-01-04' where id = 2014;
update tasly_warehouse_storage_bin set storage_bin = '05-02-04' where id = 2016;
update tasly_warehouse_storage_bin set storage_bin = '05-03-04' where id = 2017;
update tasly_warehouse_storage_bin set storage_bin = '05-04-04' where id = 2018;
update tasly_warehouse_storage_bin set storage_bin = '05-05-04' where id = 2019;
update tasly_warehouse_storage_bin set storage_bin = '05-06-04' where id = 2020;
update tasly_warehouse_storage_bin set storage_bin = '05-07-04' where id = 2021;
update tasly_warehouse_storage_bin set storage_bin = '05-08-04' where id = 2022;
update tasly_warehouse_storage_bin set storage_bin = '05-09-04' where id = 2023;
update tasly_warehouse_storage_bin set storage_bin = '05-10-04' where id = 2024;
update tasly_warehouse_storage_bin set storage_bin = '05-11-04' where id = 2025;
update tasly_warehouse_storage_bin set storage_bin = '05-12-04' where id = 2026;
update tasly_warehouse_storage_bin set storage_bin = '05-13-04' where id = 2027;
update tasly_warehouse_storage_bin set storage_bin = '05-14-04' where id = 2028;
update tasly_warehouse_storage_bin set storage_bin = '05-15-04' where id = 2029;
update tasly_warehouse_storage_bin set storage_bin = '05-16-04' where id = 2030;
update tasly_warehouse_storage_bin set storage_bin = '05-17-04' where id = 2031;
update tasly_warehouse_storage_bin set storage_bin = '05-18-04' where id = 2032;
update tasly_warehouse_storage_bin set storage_bin = '05-19-04' where id = 2033;
update tasly_warehouse_storage_bin set storage_bin = '05-20-04' where id = 2034;
update tasly_warehouse_storage_bin set storage_bin = '05-21-04' where id = 2035;
update tasly_warehouse_storage_bin set storage_bin = '05-22-04' where id = 2036;
update tasly_warehouse_storage_bin set storage_bin = '05-23-04' where id = 2037;
update tasly_warehouse_storage_bin set storage_bin = '05-24-04' where id = 2038;
update tasly_warehouse_storage_bin set storage_bin = '05-25-04' where id = 2039;
update tasly_warehouse_storage_bin set storage_bin = '05-26-04' where id = 2040;
update tasly_warehouse_storage_bin set storage_bin = '05-27-04' where id = 2041;
update tasly_warehouse_storage_bin set storage_bin = '05-28-04' where id = 2042;
update tasly_warehouse_storage_bin set storage_bin = '05-29-04' where id = 2043;
update tasly_warehouse_storage_bin set storage_bin = '05-30-04' where id = 2044;
update tasly_warehouse_storage_bin set storage_bin = '05-31-04' where id = 2045;
update tasly_warehouse_storage_bin set storage_bin = '05-32-04' where id = 2046;
update tasly_warehouse_storage_bin set storage_bin = '05-33-04' where id = 2047;
update tasly_warehouse_storage_bin set storage_bin = '05-34-04' where id = 2048;
update tasly_warehouse_storage_bin set storage_bin = '05-01-03' where id = 2049;
update tasly_warehouse_storage_bin set storage_bin = '05-02-03' where id = 2051;
update tasly_warehouse_storage_bin set storage_bin = '05-03-03' where id = 2052;
update tasly_warehouse_storage_bin set storage_bin = '05-04-03' where id = 2053;
update tasly_warehouse_storage_bin set storage_bin = '05-05-03' where id = 2054;
update tasly_warehouse_storage_bin set storage_bin = '05-06-03' where id = 2055;
update tasly_warehouse_storage_bin set storage_bin = '05-07-03' where id = 2056;
update tasly_warehouse_storage_bin set storage_bin = '05-08-03' where id = 2057;
update tasly_warehouse_storage_bin set storage_bin = '05-09-03' where id = 2058;
update tasly_warehouse_storage_bin set storage_bin = '05-10-03' where id = 2059;
update tasly_warehouse_storage_bin set storage_bin = '05-11-03' where id = 2060;
update tasly_warehouse_storage_bin set storage_bin = '05-12-03' where id = 2061;
update tasly_warehouse_storage_bin set storage_bin = '05-13-03' where id = 2062;
update tasly_warehouse_storage_bin set storage_bin = '05-14-03' where id = 2063;
update tasly_warehouse_storage_bin set storage_bin = '05-15-03' where id = 2064;
update tasly_warehouse_storage_bin set storage_bin = '05-16-03' where id = 2065;
update tasly_warehouse_storage_bin set storage_bin = '05-17-03' where id = 2066;
update tasly_warehouse_storage_bin set storage_bin = '05-18-03' where id = 2067;
update tasly_warehouse_storage_bin set storage_bin = '05-19-03' where id = 2068;
update tasly_warehouse_storage_bin set storage_bin = '05-20-03' where id = 2069;
update tasly_warehouse_storage_bin set storage_bin = '05-21-03' where id = 2070;
update tasly_warehouse_storage_bin set storage_bin = '05-22-03' where id = 2071;
update tasly_warehouse_storage_bin set storage_bin = '05-23-03' where id = 2072;
update tasly_warehouse_storage_bin set storage_bin = '05-24-03' where id = 2073;
update tasly_warehouse_storage_bin set storage_bin = '05-25-03' where id = 2074;
update tasly_warehouse_storage_bin set storage_bin = '05-26-03' where id = 2075;
update tasly_warehouse_storage_bin set storage_bin = '05-27-03' where id = 2076;
update tasly_warehouse_storage_bin set storage_bin = '05-28-03' where id = 2077;
update tasly_warehouse_storage_bin set storage_bin = '05-29-03' where id = 2078;
update tasly_warehouse_storage_bin set storage_bin = '05-30-03' where id = 2079;
update tasly_warehouse_storage_bin set storage_bin = '05-31-03' where id = 2080;
update tasly_warehouse_storage_bin set storage_bin = '05-32-03' where id = 2081;
update tasly_warehouse_storage_bin set storage_bin = '05-33-03' where id = 2082;
update tasly_warehouse_storage_bin set storage_bin = '05-34-03' where id = 2083;
update tasly_warehouse_storage_bin set storage_bin = '05-02-02' where id = 2084;
update tasly_warehouse_storage_bin set storage_bin = '05-03-02' where id = 2085;
update tasly_warehouse_storage_bin set storage_bin = '05-04-02' where id = 2086;
update tasly_warehouse_storage_bin set storage_bin = '05-05-02' where id = 2087;
update tasly_warehouse_storage_bin set storage_bin = '05-06-02' where id = 2088;
update tasly_warehouse_storage_bin set storage_bin = '05-07-02' where id = 2089;
update tasly_warehouse_storage_bin set storage_bin = '05-08-02' where id = 2090;
update tasly_warehouse_storage_bin set storage_bin = '05-09-02' where id = 2091;
update tasly_warehouse_storage_bin set storage_bin = '05-10-02' where id = 2092;
update tasly_warehouse_storage_bin set storage_bin = '05-11-02' where id = 2093;
update tasly_warehouse_storage_bin set storage_bin = '05-12-02' where id = 2094;
update tasly_warehouse_storage_bin set storage_bin = '05-13-02' where id = 2095;
update tasly_warehouse_storage_bin set storage_bin = '05-14-02' where id = 2096;
update tasly_warehouse_storage_bin set storage_bin = '05-15-02' where id = 2097;
update tasly_warehouse_storage_bin set storage_bin = '05-16-02' where id = 2098;
update tasly_warehouse_storage_bin set storage_bin = '05-17-02' where id = 2099;
update tasly_warehouse_storage_bin set storage_bin = '05-18-02' where id = 2100;
update tasly_warehouse_storage_bin set storage_bin = '05-19-02' where id = 2101;
update tasly_warehouse_storage_bin set storage_bin = '05-20-02' where id = 2102;
update tasly_warehouse_storage_bin set storage_bin = '05-21-02' where id = 2103;
update tasly_warehouse_storage_bin set storage_bin = '05-22-02' where id = 2104;
update tasly_warehouse_storage_bin set storage_bin = '05-23-02' where id = 2105;
update tasly_warehouse_storage_bin set storage_bin = '05-24-02' where id = 2106;
update tasly_warehouse_storage_bin set storage_bin = '05-25-02' where id = 2107;
update tasly_warehouse_storage_bin set storage_bin = '05-26-02' where id = 2108;
update tasly_warehouse_storage_bin set storage_bin = '05-27-02' where id = 2109;
update tasly_warehouse_storage_bin set storage_bin = '05-28-02' where id = 2110;
update tasly_warehouse_storage_bin set storage_bin = '05-29-02' where id = 2111;
update tasly_warehouse_storage_bin set storage_bin = '05-30-02' where id = 2112;
update tasly_warehouse_storage_bin set storage_bin = '05-31-02' where id = 2113;
update tasly_warehouse_storage_bin set storage_bin = '05-32-02' where id = 2114;
update tasly_warehouse_storage_bin set storage_bin = '05-33-02' where id = 2115;
update tasly_warehouse_storage_bin set storage_bin = '05-34-02' where id = 2116;
update tasly_warehouse_storage_bin set storage_bin = '05-02-01' where id = 2117;
update tasly_warehouse_storage_bin set storage_bin = '05-03-01' where id = 2118;
update tasly_warehouse_storage_bin set storage_bin = '05-04-01' where id = 2119;
update tasly_warehouse_storage_bin set storage_bin = '05-05-01' where id = 2120;
update tasly_warehouse_storage_bin set storage_bin = '05-06-01' where id = 2121;
update tasly_warehouse_storage_bin set storage_bin = '05-07-01' where id = 2122;
update tasly_warehouse_storage_bin set storage_bin = '05-08-01' where id = 2123;
update tasly_warehouse_storage_bin set storage_bin = '05-09-01' where id = 2124;
update tasly_warehouse_storage_bin set storage_bin = '05-10-01' where id = 2125;
update tasly_warehouse_storage_bin set storage_bin = '05-11-01' where id = 2126;
update tasly_warehouse_storage_bin set storage_bin = '05-12-01' where id = 2127;
update tasly_warehouse_storage_bin set storage_bin = '05-13-01' where id = 2128;
update tasly_warehouse_storage_bin set storage_bin = '05-14-01' where id = 2129;
update tasly_warehouse_storage_bin set storage_bin = '05-15-01' where id = 2130;
update tasly_warehouse_storage_bin set storage_bin = '05-16-01' where id = 2131;
update tasly_warehouse_storage_bin set storage_bin = '05-17-01' where id = 2132;
update tasly_warehouse_storage_bin set storage_bin = '05-18-01' where id = 2133;
update tasly_warehouse_storage_bin set storage_bin = '05-19-01' where id = 2134;
update tasly_warehouse_storage_bin set storage_bin = '05-20-01' where id = 2135;
update tasly_warehouse_storage_bin set storage_bin = '05-21-01' where id = 2136;
update tasly_warehouse_storage_bin set storage_bin = '05-22-01' where id = 2137;
update tasly_warehouse_storage_bin set storage_bin = '05-23-01' where id = 2138;
update tasly_warehouse_storage_bin set storage_bin = '05-24-01' where id = 2139;
update tasly_warehouse_storage_bin set storage_bin = '05-25-01' where id = 2140;
update tasly_warehouse_storage_bin set storage_bin = '05-26-01' where id = 2141;
update tasly_warehouse_storage_bin set storage_bin = '05-27-01' where id = 2142;
update tasly_warehouse_storage_bin set storage_bin = '05-28-01' where id = 2143;
update tasly_warehouse_storage_bin set storage_bin = '05-29-01' where id = 2144;
update tasly_warehouse_storage_bin set storage_bin = '05-30-01' where id = 2145;
update tasly_warehouse_storage_bin set storage_bin = '05-31-01' where id = 2146;
update tasly_warehouse_storage_bin set storage_bin = '05-32-01' where id = 2147;
update tasly_warehouse_storage_bin set storage_bin = '05-33-01' where id = 2148;
update tasly_warehouse_storage_bin set storage_bin = '05-34-01' where id = 2149;
update tasly_warehouse_storage_bin set storage_bin = '06-02-01' where id = 2150;
update tasly_warehouse_storage_bin set storage_bin = '06-03-01' where id = 2151;
update tasly_warehouse_storage_bin set storage_bin = '06-04-01' where id = 2152;
update tasly_warehouse_storage_bin set storage_bin = '06-05-01' where id = 2153;
update tasly_warehouse_storage_bin set storage_bin = '06-06-01' where id = 2154;
update tasly_warehouse_storage_bin set storage_bin = '06-07-01' where id = 2155;
update tasly_warehouse_storage_bin set storage_bin = '06-08-01' where id = 2156;
update tasly_warehouse_storage_bin set storage_bin = '06-09-01' where id = 2157;
update tasly_warehouse_storage_bin set storage_bin = '06-10-01' where id = 2158;
update tasly_warehouse_storage_bin set storage_bin = '06-11-01' where id = 2159;
update tasly_warehouse_storage_bin set storage_bin = '06-12-01' where id = 2160;
update tasly_warehouse_storage_bin set storage_bin = '06-13-01' where id = 2161;
update tasly_warehouse_storage_bin set storage_bin = '06-14-01' where id = 2162;
update tasly_warehouse_storage_bin set storage_bin = '06-15-01' where id = 2163;
update tasly_warehouse_storage_bin set storage_bin = '06-16-01' where id = 2164;
update tasly_warehouse_storage_bin set storage_bin = '06-17-01' where id = 2165;
update tasly_warehouse_storage_bin set storage_bin = '06-18-01' where id = 2166;
update tasly_warehouse_storage_bin set storage_bin = '06-19-01' where id = 2167;
update tasly_warehouse_storage_bin set storage_bin = '06-20-01' where id = 2168;
update tasly_warehouse_storage_bin set storage_bin = '06-21-01' where id = 2169;
update tasly_warehouse_storage_bin set storage_bin = '06-22-01' where id = 2170;
update tasly_warehouse_storage_bin set storage_bin = '06-23-01' where id = 2171;
update tasly_warehouse_storage_bin set storage_bin = '06-24-01' where id = 2172;
update tasly_warehouse_storage_bin set storage_bin = '06-25-01' where id = 2173;
update tasly_warehouse_storage_bin set storage_bin = '06-26-01' where id = 2174;
update tasly_warehouse_storage_bin set storage_bin = '06-27-01' where id = 2175;
update tasly_warehouse_storage_bin set storage_bin = '06-28-01' where id = 2176;
update tasly_warehouse_storage_bin set storage_bin = '06-29-01' where id = 2177;
update tasly_warehouse_storage_bin set storage_bin = '06-30-01' where id = 2178;
update tasly_warehouse_storage_bin set storage_bin = '06-31-01' where id = 2179;
update tasly_warehouse_storage_bin set storage_bin = '06-32-01' where id = 2180;
update tasly_warehouse_storage_bin set storage_bin = '06-33-01' where id = 2181;
update tasly_warehouse_storage_bin set storage_bin = '06-34-01' where id = 2182;
update tasly_warehouse_storage_bin set storage_bin = '06-02-02' where id = 2183;
update tasly_warehouse_storage_bin set storage_bin = '06-03-02' where id = 2184;
update tasly_warehouse_storage_bin set storage_bin = '06-04-02' where id = 2185;
update tasly_warehouse_storage_bin set storage_bin = '06-05-02' where id = 2186;
update tasly_warehouse_storage_bin set storage_bin = '06-06-02' where id = 2187;
update tasly_warehouse_storage_bin set storage_bin = '06-07-02' where id = 2188;
update tasly_warehouse_storage_bin set storage_bin = '06-08-02' where id = 2189;
update tasly_warehouse_storage_bin set storage_bin = '06-09-02' where id = 2190;
update tasly_warehouse_storage_bin set storage_bin = '06-10-02' where id = 2191;
update tasly_warehouse_storage_bin set storage_bin = '06-11-02' where id = 2192;
update tasly_warehouse_storage_bin set storage_bin = '06-12-02' where id = 2193;
update tasly_warehouse_storage_bin set storage_bin = '06-13-02' where id = 2194;
update tasly_warehouse_storage_bin set storage_bin = '06-14-02' where id = 2195;
update tasly_warehouse_storage_bin set storage_bin = '06-15-02' where id = 2196;
update tasly_warehouse_storage_bin set storage_bin = '06-16-02' where id = 2197;
update tasly_warehouse_storage_bin set storage_bin = '06-17-02' where id = 2198;
update tasly_warehouse_storage_bin set storage_bin = '06-18-02' where id = 2199;
update tasly_warehouse_storage_bin set storage_bin = '06-19-02' where id = 2200;
update tasly_warehouse_storage_bin set storage_bin = '06-20-02' where id = 2201;
update tasly_warehouse_storage_bin set storage_bin = '06-21-02' where id = 2202;
update tasly_warehouse_storage_bin set storage_bin = '06-22-02' where id = 2203;
update tasly_warehouse_storage_bin set storage_bin = '06-23-02' where id = 2204;
update tasly_warehouse_storage_bin set storage_bin = '06-24-02' where id = 2205;
update tasly_warehouse_storage_bin set storage_bin = '06-25-02' where id = 2206;
update tasly_warehouse_storage_bin set storage_bin = '06-26-02' where id = 2207;
update tasly_warehouse_storage_bin set storage_bin = '06-27-02' where id = 2208;
update tasly_warehouse_storage_bin set storage_bin = '06-28-02' where id = 2209;
update tasly_warehouse_storage_bin set storage_bin = '06-29-02' where id = 2210;
update tasly_warehouse_storage_bin set storage_bin = '06-30-02' where id = 2211;
update tasly_warehouse_storage_bin set storage_bin = '06-31-02' where id = 2212;
update tasly_warehouse_storage_bin set storage_bin = '06-32-02' where id = 2213;
update tasly_warehouse_storage_bin set storage_bin = '06-33-02' where id = 2214;
update tasly_warehouse_storage_bin set storage_bin = '06-34-02' where id = 2215;
update tasly_warehouse_storage_bin set storage_bin = '06-02-03' where id = 2216;
update tasly_warehouse_storage_bin set storage_bin = '06-03-03' where id = 2217;
update tasly_warehouse_storage_bin set storage_bin = '06-04-03' where id = 2218;
update tasly_warehouse_storage_bin set storage_bin = '06-05-03' where id = 2219;
update tasly_warehouse_storage_bin set storage_bin = '06-06-03' where id = 2220;
update tasly_warehouse_storage_bin set storage_bin = '06-07-03' where id = 2221;
update tasly_warehouse_storage_bin set storage_bin = '06-08-03' where id = 2222;
update tasly_warehouse_storage_bin set storage_bin = '06-09-03' where id = 2223;
update tasly_warehouse_storage_bin set storage_bin = '06-10-03' where id = 2224;
update tasly_warehouse_storage_bin set storage_bin = '06-11-03' where id = 2225;
update tasly_warehouse_storage_bin set storage_bin = '06-12-03' where id = 2226;
update tasly_warehouse_storage_bin set storage_bin = '06-13-03' where id = 2227;
update tasly_warehouse_storage_bin set storage_bin = '06-14-03' where id = 2228;
update tasly_warehouse_storage_bin set storage_bin = '06-15-03' where id = 2229;
update tasly_warehouse_storage_bin set storage_bin = '06-16-03' where id = 2230;
update tasly_warehouse_storage_bin set storage_bin = '06-17-03' where id = 2231;
update tasly_warehouse_storage_bin set storage_bin = '06-18-03' where id = 2232;
update tasly_warehouse_storage_bin set storage_bin = '06-19-03' where id = 2233;
update tasly_warehouse_storage_bin set storage_bin = '06-20-03' where id = 2234;
update tasly_warehouse_storage_bin set storage_bin = '06-21-03' where id = 2235;
update tasly_warehouse_storage_bin set storage_bin = '06-22-03' where id = 2236;
update tasly_warehouse_storage_bin set storage_bin = '06-23-03' where id = 2237;
update tasly_warehouse_storage_bin set storage_bin = '06-24-03' where id = 2238;
update tasly_warehouse_storage_bin set storage_bin = '06-25-03' where id = 2239;
update tasly_warehouse_storage_bin set storage_bin = '06-26-03' where id = 2240;
update tasly_warehouse_storage_bin set storage_bin = '06-27-03' where id = 2241;
update tasly_warehouse_storage_bin set storage_bin = '06-28-03' where id = 2242;
update tasly_warehouse_storage_bin set storage_bin = '06-29-03' where id = 2243;
update tasly_warehouse_storage_bin set storage_bin = '06-30-03' where id = 2244;
update tasly_warehouse_storage_bin set storage_bin = '06-31-03' where id = 2245;
update tasly_warehouse_storage_bin set storage_bin = '06-32-03' where id = 2246;
update tasly_warehouse_storage_bin set storage_bin = '06-33-03' where id = 2247;
update tasly_warehouse_storage_bin set storage_bin = '06-34-03' where id = 2248;
update tasly_warehouse_storage_bin set storage_bin = '06-02-04' where id = 2249;
update tasly_warehouse_storage_bin set storage_bin = '06-03-04' where id = 2250;
update tasly_warehouse_storage_bin set storage_bin = '06-04-04' where id = 2251;
update tasly_warehouse_storage_bin set storage_bin = '06-05-04' where id = 2252;
update tasly_warehouse_storage_bin set storage_bin = '06-06-04' where id = 2253;
update tasly_warehouse_storage_bin set storage_bin = '06-07-04' where id = 2254;
update tasly_warehouse_storage_bin set storage_bin = '06-08-04' where id = 2255;
update tasly_warehouse_storage_bin set storage_bin = '06-09-04' where id = 2256;
update tasly_warehouse_storage_bin set storage_bin = '06-10-04' where id = 2257;
update tasly_warehouse_storage_bin set storage_bin = '06-11-04' where id = 2258;
update tasly_warehouse_storage_bin set storage_bin = '06-12-04' where id = 2259;
update tasly_warehouse_storage_bin set storage_bin = '06-13-04' where id = 2260;
update tasly_warehouse_storage_bin set storage_bin = '06-14-04' where id = 2261;
update tasly_warehouse_storage_bin set storage_bin = '06-15-04' where id = 2262;
update tasly_warehouse_storage_bin set storage_bin = '06-16-04' where id = 2263;
update tasly_warehouse_storage_bin set storage_bin = '06-17-04' where id = 2264;
update tasly_warehouse_storage_bin set storage_bin = '06-18-04' where id = 2265;
update tasly_warehouse_storage_bin set storage_bin = '06-19-04' where id = 2266;
update tasly_warehouse_storage_bin set storage_bin = '06-20-04' where id = 2267;
update tasly_warehouse_storage_bin set storage_bin = '06-21-04' where id = 2268;
update tasly_warehouse_storage_bin set storage_bin = '06-22-04' where id = 2269;
update tasly_warehouse_storage_bin set storage_bin = '06-23-04' where id = 2270;
update tasly_warehouse_storage_bin set storage_bin = '06-24-04' where id = 2271;
update tasly_warehouse_storage_bin set storage_bin = '06-25-04' where id = 2272;
update tasly_warehouse_storage_bin set storage_bin = '06-26-04' where id = 2273;
update tasly_warehouse_storage_bin set storage_bin = '06-27-04' where id = 2274;
update tasly_warehouse_storage_bin set storage_bin = '06-28-04' where id = 2275;
update tasly_warehouse_storage_bin set storage_bin = '06-29-04' where id = 2276;
update tasly_warehouse_storage_bin set storage_bin = '06-30-04' where id = 2277;
update tasly_warehouse_storage_bin set storage_bin = '06-31-04' where id = 2278;
update tasly_warehouse_storage_bin set storage_bin = '06-32-04' where id = 2279;
update tasly_warehouse_storage_bin set storage_bin = '06-33-04' where id = 2280;
update tasly_warehouse_storage_bin set storage_bin = '06-34-04' where id = 2281;
update tasly_warehouse_storage_bin set storage_bin = '06-02-05' where id = 2282;
update tasly_warehouse_storage_bin set storage_bin = '06-03-05' where id = 2283;
update tasly_warehouse_storage_bin set storage_bin = '06-04-05' where id = 2284;
update tasly_warehouse_storage_bin set storage_bin = '06-05-05' where id = 2285;
update tasly_warehouse_storage_bin set storage_bin = '06-06-05' where id = 2286;
update tasly_warehouse_storage_bin set storage_bin = '06-07-05' where id = 2287;
update tasly_warehouse_storage_bin set storage_bin = '06-08-05' where id = 2288;
update tasly_warehouse_storage_bin set storage_bin = '06-09-05' where id = 2289;
update tasly_warehouse_storage_bin set storage_bin = '06-10-05' where id = 2290;
update tasly_warehouse_storage_bin set storage_bin = '06-11-05' where id = 2291;
update tasly_warehouse_storage_bin set storage_bin = '06-12-05' where id = 2292;
update tasly_warehouse_storage_bin set storage_bin = '06-13-05' where id = 2293;
update tasly_warehouse_storage_bin set storage_bin = '06-14-05' where id = 2294;
update tasly_warehouse_storage_bin set storage_bin = '06-15-05' where id = 2295;
update tasly_warehouse_storage_bin set storage_bin = '06-16-05' where id = 2296;
update tasly_warehouse_storage_bin set storage_bin = '06-17-05' where id = 2297;
update tasly_warehouse_storage_bin set storage_bin = '06-18-05' where id = 2298;
update tasly_warehouse_storage_bin set storage_bin = '06-19-05' where id = 2299;
update tasly_warehouse_storage_bin set storage_bin = '06-20-05' where id = 2300;
update tasly_warehouse_storage_bin set storage_bin = '06-21-05' where id = 2301;
update tasly_warehouse_storage_bin set storage_bin = '06-22-05' where id = 2302;
update tasly_warehouse_storage_bin set storage_bin = '06-23-05' where id = 2303;
update tasly_warehouse_storage_bin set storage_bin = '06-24-05' where id = 2304;
update tasly_warehouse_storage_bin set storage_bin = '06-25-05' where id = 2305;
update tasly_warehouse_storage_bin set storage_bin = '06-26-05' where id = 2306;
update tasly_warehouse_storage_bin set storage_bin = '06-27-05' where id = 2307;
update tasly_warehouse_storage_bin set storage_bin = '06-28-05' where id = 2308;
update tasly_warehouse_storage_bin set storage_bin = '06-29-05' where id = 2309;
update tasly_warehouse_storage_bin set storage_bin = '06-30-05' where id = 2310;
update tasly_warehouse_storage_bin set storage_bin = '06-31-05' where id = 2311;
update tasly_warehouse_storage_bin set storage_bin = '06-32-05' where id = 2312;
update tasly_warehouse_storage_bin set storage_bin = '06-33-05' where id = 2313;
update tasly_warehouse_storage_bin set storage_bin = '06-34-05' where id = 2314;
update tasly_warehouse_storage_bin set storage_bin = '06-02-06' where id = 2315;
update tasly_warehouse_storage_bin set storage_bin = '06-03-06' where id = 2316;
update tasly_warehouse_storage_bin set storage_bin = '06-04-06' where id = 2317;
update tasly_warehouse_storage_bin set storage_bin = '06-05-06' where id = 2318;
update tasly_warehouse_storage_bin set storage_bin = '06-06-06' where id = 2319;
update tasly_warehouse_storage_bin set storage_bin = '06-07-06' where id = 2320;
update tasly_warehouse_storage_bin set storage_bin = '06-08-06' where id = 2321;
update tasly_warehouse_storage_bin set storage_bin = '06-09-06' where id = 2322;
update tasly_warehouse_storage_bin set storage_bin = '06-10-06' where id = 2323;
update tasly_warehouse_storage_bin set storage_bin = '06-11-06' where id = 2324;
update tasly_warehouse_storage_bin set storage_bin = '06-12-06' where id = 2325;
update tasly_warehouse_storage_bin set storage_bin = '06-13-06' where id = 2326;
update tasly_warehouse_storage_bin set storage_bin = '06-14-06' where id = 2327;
update tasly_warehouse_storage_bin set storage_bin = '06-15-06' where id = 2328;
update tasly_warehouse_storage_bin set storage_bin = '06-16-06' where id = 2329;
update tasly_warehouse_storage_bin set storage_bin = '06-17-06' where id = 2330;
update tasly_warehouse_storage_bin set storage_bin = '06-18-06' where id = 2331;
update tasly_warehouse_storage_bin set storage_bin = '06-19-06' where id = 2332;
update tasly_warehouse_storage_bin set storage_bin = '06-20-06' where id = 2333;
update tasly_warehouse_storage_bin set storage_bin = '06-21-06' where id = 2334;
update tasly_warehouse_storage_bin set storage_bin = '06-22-06' where id = 2335;
update tasly_warehouse_storage_bin set storage_bin = '06-23-06' where id = 2336;
update tasly_warehouse_storage_bin set storage_bin = '06-24-06' where id = 2337;
update tasly_warehouse_storage_bin set storage_bin = '06-25-06' where id = 2338;
update tasly_warehouse_storage_bin set storage_bin = '06-26-06' where id = 2339;
update tasly_warehouse_storage_bin set storage_bin = '06-27-06' where id = 2340;
update tasly_warehouse_storage_bin set storage_bin = '06-28-06' where id = 2341;
update tasly_warehouse_storage_bin set storage_bin = '06-29-06' where id = 2342;
update tasly_warehouse_storage_bin set storage_bin = '06-30-06' where id = 2343;
update tasly_warehouse_storage_bin set storage_bin = '06-31-06' where id = 2344;
update tasly_warehouse_storage_bin set storage_bin = '06-32-06' where id = 2345;
update tasly_warehouse_storage_bin set storage_bin = '06-33-06' where id = 2346;
update tasly_warehouse_storage_bin set storage_bin = '06-34-06' where id = 2347;
```
