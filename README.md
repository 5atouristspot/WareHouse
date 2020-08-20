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
搜索接口
curl -i -u eyJhbGciOiJIUzUxMiIsImlhdCI6MTU5NjQ0NjEzNywiZXhwIjoxNTk2NDQ2NzM3fQ.eyJpZCI6M30.4BHm99cMmKkl-nBCTVt0_rOGCXZIJ2s_I0CZCt8SN25HZQ_mPkdOaJ-yn-VDgAB3IPrDz78tBNAHl8nVSV2nzA:unused -X GET -H "Content-Type: application/json" http://127.0.0.1:3622/api/v1000/elevated/searchinfo?search_type=storage_bin\&search_keys="04-01-18+04-01-17"

curl -i -u eyJhbGciOiJIUzUxMiIsImlhdCI6MTU5NjQ0NjEzNywiZXhwIjoxNTk2NDQ2NzM3fQ.eyJpZCI6M30.4BHm99cMmKkl-nBCTVt0_rOGCXZIJ2s_I0CZCt8SN25HZQ_mPkdOaJ-yn-VDgAB3IPrDz78tBNAHl8nVSV2nzA:unused -X GET -H "Content-Type: application/json" http://127.0.0.1:3622/api/v1000/elevated/searchinfo?search_type=material_desc\&search_keys='100ml+ml'

curl -i -u eyJhbGciOiJIUzUxMiIsImlhdCI6MTU5NjQ0NjEzNywiZXhwIjoxNTk2NDQ2NzM3fQ.eyJpZCI6M30.4BHm99cMmKkl-nBCTVt0_rOGCXZIJ2s_I0CZCt8SN25HZQ_mPkdOaJ-yn-VDgAB3IPrDz78tBNAHl8nVSV2nzA:unused -X GET -H "Content-Type: application/json" http://127.0.0.1:3622/api/v1000/elevated/searchinfo?search_type=batch\&search_keys='1702001+17011'

curl -i -u eyJhbGciOiJIUzUxMiIsImlhdCI6MTU5NjQ0NjEzNywiZXhwIjoxNTk2NDQ2NzM3fQ.eyJpZCI6M30.4BHm99cMmKkl-nBCTVt0_rOGCXZIJ2s_I0CZCt8SN25HZQ_mPkdOaJ-yn-VDgAB3IPrDz78tBNAHl8nVSV2nzA:unused -X GET -H "Content-Type: application/json" http://127.0.0.1:3622/api/v1000/elevated/searchinfo?search_type=material\&search_keys='NA+0.0'


返回json格式
[
    {
        "id":6162,
        "material":"NA",
        "storage_bin":"04-01-17",
        "batch":"1702001",
        "material_desc":"100ml瓶盖",
        "avail_stock":"1657.0",
        "unit":"EA",
        "last_goods_rec":"2019-04-15",
        "date_of_manuf":"2017-01-12",
        "sled_bbd":"0",
        "next_inspection":"0"
    },
    {
        "id":6163,
        "material":"NA",
        "storage_bin":"04-01-17",
        "batch":"1802001",
        "material_desc":"100ml新品瓶体",
        "avail_stock":"683.0",
        "unit":"EA",
        "last_goods_rec":"2019-04-15",
        "date_of_manuf":"2018-01-25",
        "sled_bbd":"0",
        "next_inspection":"0"
    }
]
```
```
物料追溯接口：

curl -i -u eyJhbGciOiJIUzUxMiIsImlhdCI6MTU5NzkxMDcxMiwiZXhwIjoxNTk3OTExMzEyfQ.eyJpZCI6M30.6i9LSfKcNSAvQJKkaEmIt1AmOOxlRGTUwUSFLwMuiyPAnn3TT_pQWKyeSuAtOhCm5sBUXzhrp5QunnA7WvFO3A:unused -X GET -H "Content-Type: application/json" http://127.0.0.1:3622/api/v1000/elevated/materialtrace?batch='650605018'

返回json格式
[
	[{
		"id": 159935,
		"material": "40018",
		"material_description": "Silibinin Capsules Leaflet",
		"order_num": "101632",
		"batch": "16000106",
		"quantity_wi": 32900.0,
		"unit": "EA",
		"pid": 0,
		"posting_date": "2016-08-22"
	}, {
		"id": 159937,
		"material": "40022",
		"material_description": "Silibinin Capsules35mg*3*10EA Carton",
		"order_num": "101632",
		"batch": "16000110",
		"quantity_wi": 32655.0,
		"unit": "EA",
		"pid": 0,
		"posting_date": "2016-08-22"
	}, {
		"id": 159939,
		"material": "40010",
		"material_description": "BOPP Film 178mm",
		"order_num": "101632",
		"batch": "16000075",
		"quantity_wi": 13.09,
		"unit": "KG",
		"pid": 0,
		"posting_date": "2016-08-22"
	}, {
		"id": 159941,
		"material": "40023",
		"material_description": "Silibinin Capsules 35mg*3*10EA Shipper",
		"order_num": "101632",
		"batch": "16000093",
		"quantity_wi": 114.0,
		"unit": "EA",
		"pid": 0,
		"posting_date": "2016-08-22"
	}, {
		"id": 159942,
		"material": "40023",
		"material_description": "Silibinin Capsules 35mg*3*10EA Shipper",
		"order_num": "101632",
		"batch": "16000119",
		"quantity_wi": 50.0,
		"unit": "EA",
		"pid": 0,
		"posting_date": "2016-08-22"
	}, {
		"id": 159944,
		"material": "40024",
		"material_description": "Silibinin Capsules35mg*3*10EA Paperboard",
		"order_num": "101632",
		"batch": "16000094",
		"quantity_wi": 330.0,
		"unit": "EA",
		"pid": 0,
		"posting_date": "2016-08-22"
	}, {
		"id": 159945,
		"material": "70008",
		"material_description": "Silibinin Capsules 35mg*2*10EA",
		"order_num": "101632",
		"batch": "650605018",
		"quantity_wi": 972700.0,
		"unit": "EA",
		"pid": 0,
		"posting_date": "2016-08-22",
		"children": [{
			"id": 158825,
			"material": "60010",
			"material_description": "Silibinin Capsules 35mg",
			"order_num": "101563",
			"batch": "600903050",
			"quantity_wi": 975181.0,
			"unit": "EA",
			"pid": 159945,
			"posting_date": "2016-08-22",
			"children": [{
				"id": 157823,
				"material": "10001",
				"material_description": "silibinin",
				"order_num": "101503",
				"batch": "15000383",
				"quantity_wi": 35.0,
				"unit": "KG",
				"pid": 158825,
				"posting_date": "2016-05-09"
			}, {
				"id": 157825,
				"material": "20028",
				"material_description": "Soya Lecithin",
				"order_num": "101503",
				"batch": "15000354",
				"quantity_wi": 0.39,
				"unit": "KG",
				"pid": 158825,
				"posting_date": "2016-05-09"
			}, {
				"id": 157826,
				"material": "20028",
				"material_description": "Soya Lecithin",
				"order_num": "101503",
				"batch": "16000033",
				"quantity_wi": 64.61,
				"unit": "KG",
				"pid": 158825,
				"posting_date": "2016-05-09"
			}, {
				"id": 157828,
				"material": "20035",
				"material_description": "Anhydrous Ethanol",
				"order_num": "101503",
				"batch": "16000029",
				"quantity_wi": 480.0,
				"unit": "KG",
				"pid": 158825,
				"posting_date": "2016-05-09"
			}, {
				"id": 157830,
				"material": "20035",
				"material_description": "Anhydrous Ethanol",
				"order_num": "101503",
				"batch": "16000029",
				"quantity_wi": 20.0,
				"unit": "KG",
				"pid": 158825,
				"posting_date": "2016-05-09"
			}, {
				"id": 157832,
				"material": "20033",
				"material_description": "Lactose (SpheroLac 100)",
				"order_num": "101503",
				"batch": "15000369",
				"quantity_wi": 106.0,
				"unit": "KG",
				"pid": 158825,
				"posting_date": "2016-05-09"
			}, {
				"id": 157834,
				"material": "20034",
				"material_description": "Talc Powder",
				"order_num": "101503",
				"batch": "16000036",
				"quantity_wi": 31.46,
				"unit": "KG",
				"pid": 158825,
				"posting_date": "2016-05-09"
			}, {
				"id": 157836,
				"material": "20029",
				"material_description": "Glycolys STD",
				"order_num": "101503",
				"batch": "16000006",
				"quantity_wi": 20.6,
				"unit": "KG",
				"pid": 158825,
				"posting_date": "2016-05-09"
			}, {
				"id": 157838,
				"material": "20036",
				"material_description": "Silibinin printing 1#vacant capsules",
				"order_num": "101503",
				"batch": "15000366",
				"quantity_wi": 975395.0,
				"unit": "EA",
				"pid": 158825,
				"posting_date": "2016-05-09"
			}]
		}, {
			"id": 158827,
			"material": "30010",
			"material_description": "PVC/PVDC Colorless 231mm",
			"order_num": "101563",
			"batch": "16000038",
			"quantity_wi": 175.2,
			"unit": "KG",
			"pid": 159945,
			"posting_date": "2016-08-22"
		}, {
			"id": 158829,
			"material": "30011",
			"material_description": "AluminumFoil231mm SilibininCapsules 35mg",
			"order_num": "101563",
			"batch": "16000026",
			"quantity_wi": 29.65,
			"unit": "KG",
			"pid": 159945,
			"posting_date": "2016-08-22"
		}, {
			"id": 158831,
			"material": "30012",
			"material_description": "Tropical Type Blister AluminumFoil 231mm",
			"order_num": "101563",
			"batch": "16000027",
			"quantity_wi": 96.91,
			"unit": "KG",
			"pid": 159945,
			"posting_date": "2016-08-22"
		}, {
			"id": 158833,
			"material": "40018",
			"material_description": "Silibinin Capsules Leaflet",
			"order_num": "101563",
			"batch": "16000025",
			"quantity_wi": 3244.0,
			"unit": "EA",
			"pid": 159945,
			"posting_date": "2016-08-22"
		}, {
			"id": 158834,
			"material": "40018",
			"material_description": "Silibinin Capsules Leaflet",
			"order_num": "101563",
			"batch": "16000044",
			"quantity_wi": 45495.0,
			"unit": "EA",
			"pid": 159945,
			"posting_date": "2016-08-22"
		}, {
			"id": 158836,
			"material": "40019",
			"material_description": "Silibinin Capsules 35mg*2*10EA Carton",
			"order_num": "101563",
			"batch": "16000068",
			"quantity_wi": 30509.0,
			"unit": "EA",
			"pid": 159945,
			"posting_date": "2016-08-22"
		}, {
			"id": 158837,
			"material": "40019",
			"material_description": "Silibinin Capsules 35mg*2*10EA Carton",
			"order_num": "101563",
			"batch": "16000085",
			"quantity_wi": 18226.0,
			"unit": "EA",
			"pid": 159945,
			"posting_date": "2016-08-22"
		}, {
			"id": 158839,
			"material": "40010",
			"material_description": "BOPP Film 178mm",
			"order_num": "101563",
			"batch": "16000013",
			"quantity_wi": 7.33,
			"unit": "KG",
			"pid": 159945,
			"posting_date": "2016-08-22"
		}, {
			"id": 158840,
			"material": "40010",
			"material_description": "BOPP Film 178mm",
			"order_num": "101563",
			"batch": "16000018",
			"quantity_wi": 8.36,
			"unit": "KG",
			"pid": 159945,
			"posting_date": "2016-08-22"
		}, {
			"id": 158842,
			"material": "40020",
			"material_description": "Silibinin Capsules 35mg*2*10EA Shipper",
			"order_num": "101563",
			"batch": "16000060",
			"quantity_wi": 8.0,
			"unit": "EA",
			"pid": 159945,
			"posting_date": "2016-08-22"
		}, {
			"id": 158843,
			"material": "40020",
			"material_description": "Silibinin Capsules 35mg*2*10EA Shipper",
			"order_num": "101563",
			"batch": "16000069",
			"quantity_wi": 157.0,
			"unit": "EA",
			"pid": 159945,
			"posting_date": "2016-08-22"
		}, {
			"id": 158845,
			"material": "40021",
			"material_description": "Silibinin Capsules35mg*2*10EA Paperboard",
			"order_num": "101563",
			"batch": "16000061",
			"quantity_wi": 336.0,
			"unit": "EA",
			"pid": 159945,
			"posting_date": "2016-08-22"
		}]
	}, {
		"id": 158825,
		"material": "60010",
		"material_description": "Silibinin Capsules 35mg",
		"order_num": "101563",
		"batch": "600903050",
		"quantity_wi": 975181.0,
		"unit": "EA",
		"pid": 159945,
		"posting_date": "2016-08-22",
		"children": [{
			"id": 157823,
			"material": "10001",
			"material_description": "silibinin",
			"order_num": "101503",
			"batch": "15000383",
			"quantity_wi": 35.0,
			"unit": "KG",
			"pid": 158825,
			"posting_date": "2016-05-09"
		}, {
			"id": 157825,
			"material": "20028",
			"material_description": "Soya Lecithin",
			"order_num": "101503",
			"batch": "15000354",
			"quantity_wi": 0.39,
			"unit": "KG",
			"pid": 158825,
			"posting_date": "2016-05-09"
		}, {
			"id": 157826,
			"material": "20028",
			"material_description": "Soya Lecithin",
			"order_num": "101503",
			"batch": "16000033",
			"quantity_wi": 64.61,
			"unit": "KG",
			"pid": 158825,
			"posting_date": "2016-05-09"
		}, {
			"id": 157828,
			"material": "20035",
			"material_description": "Anhydrous Ethanol",
			"order_num": "101503",
			"batch": "16000029",
			"quantity_wi": 480.0,
			"unit": "KG",
			"pid": 158825,
			"posting_date": "2016-05-09"
		}, {
			"id": 157830,
			"material": "20035",
			"material_description": "Anhydrous Ethanol",
			"order_num": "101503",
			"batch": "16000029",
			"quantity_wi": 20.0,
			"unit": "KG",
			"pid": 158825,
			"posting_date": "2016-05-09"
		}, {
			"id": 157832,
			"material": "20033",
			"material_description": "Lactose (SpheroLac 100)",
			"order_num": "101503",
			"batch": "15000369",
			"quantity_wi": 106.0,
			"unit": "KG",
			"pid": 158825,
			"posting_date": "2016-05-09"
		}, {
			"id": 157834,
			"material": "20034",
			"material_description": "Talc Powder",
			"order_num": "101503",
			"batch": "16000036",
			"quantity_wi": 31.46,
			"unit": "KG",
			"pid": 158825,
			"posting_date": "2016-05-09"
		}, {
			"id": 157836,
			"material": "20029",
			"material_description": "Glycolys STD",
			"order_num": "101503",
			"batch": "16000006",
			"quantity_wi": 20.6,
			"unit": "KG",
			"pid": 158825,
			"posting_date": "2016-05-09"
		}, {
			"id": 157838,
			"material": "20036",
			"material_description": "Silibinin printing 1#vacant capsules",
			"order_num": "101503",
			"batch": "15000366",
			"quantity_wi": 975395.0,
			"unit": "EA",
			"pid": 158825,
			"posting_date": "2016-05-09"
		}]
	}, {
		"id": 157823,
		"material": "10001",
		"material_description": "silibinin",
		"order_num": "101503",
		"batch": "15000383",
		"quantity_wi": 35.0,
		"unit": "KG",
		"pid": 158825,
		"posting_date": "2016-05-09"
	}, {
		"id": 157825,
		"material": "20028",
		"material_description": "Soya Lecithin",
		"order_num": "101503",
		"batch": "15000354",
		"quantity_wi": 0.39,
		"unit": "KG",
		"pid": 158825,
		"posting_date": "2016-05-09"
	}, {
		"id": 157826,
		"material": "20028",
		"material_description": "Soya Lecithin",
		"order_num": "101503",
		"batch": "16000033",
		"quantity_wi": 64.61,
		"unit": "KG",
		"pid": 158825,
		"posting_date": "2016-05-09"
	}, {
		"id": 157828,
		"material": "20035",
		"material_description": "Anhydrous Ethanol",
		"order_num": "101503",
		"batch": "16000029",
		"quantity_wi": 480.0,
		"unit": "KG",
		"pid": 158825,
		"posting_date": "2016-05-09"
	}, {
		"id": 157830,
		"material": "20035",
		"material_description": "Anhydrous Ethanol",
		"order_num": "101503",
		"batch": "16000029",
		"quantity_wi": 20.0,
		"unit": "KG",
		"pid": 158825,
		"posting_date": "2016-05-09"
	}, {
		"id": 157832,
		"material": "20033",
		"material_description": "Lactose (SpheroLac 100)",
		"order_num": "101503",
		"batch": "15000369",
		"quantity_wi": 106.0,
		"unit": "KG",
		"pid": 158825,
		"posting_date": "2016-05-09"
	}, {
		"id": 157834,
		"material": "20034",
		"material_description": "Talc Powder",
		"order_num": "101503",
		"batch": "16000036",
		"quantity_wi": 31.46,
		"unit": "KG",
		"pid": 158825,
		"posting_date": "2016-05-09"
	}, {
		"id": 157836,
		"material": "20029",
		"material_description": "Glycolys STD",
		"order_num": "101503",
		"batch": "16000006",
		"quantity_wi": 20.6,
		"unit": "KG",
		"pid": 158825,
		"posting_date": "2016-05-09"
	}, {
		"id": 157838,
		"material": "20036",
		"material_description": "Silibinin printing 1#vacant capsules",
		"order_num": "101503",
		"batch": "15000366",
		"quantity_wi": 975395.0,
		"unit": "EA",
		"pid": 158825,
		"posting_date": "2016-05-09"
	}, {
		"id": 158827,
		"material": "30010",
		"material_description": "PVC/PVDC Colorless 231mm",
		"order_num": "101563",
		"batch": "16000038",
		"quantity_wi": 175.2,
		"unit": "KG",
		"pid": 159945,
		"posting_date": "2016-08-22"
	}, {
		"id": 158829,
		"material": "30011",
		"material_description": "AluminumFoil231mm SilibininCapsules 35mg",
		"order_num": "101563",
		"batch": "16000026",
		"quantity_wi": 29.65,
		"unit": "KG",
		"pid": 159945,
		"posting_date": "2016-08-22"
	}, {
		"id": 158831,
		"material": "30012",
		"material_description": "Tropical Type Blister AluminumFoil 231mm",
		"order_num": "101563",
		"batch": "16000027",
		"quantity_wi": 96.91,
		"unit": "KG",
		"pid": 159945,
		"posting_date": "2016-08-22"
	}, {
		"id": 158833,
		"material": "40018",
		"material_description": "Silibinin Capsules Leaflet",
		"order_num": "101563",
		"batch": "16000025",
		"quantity_wi": 3244.0,
		"unit": "EA",
		"pid": 159945,
		"posting_date": "2016-08-22"
	}, {
		"id": 158834,
		"material": "40018",
		"material_description": "Silibinin Capsules Leaflet",
		"order_num": "101563",
		"batch": "16000044",
		"quantity_wi": 45495.0,
		"unit": "EA",
		"pid": 159945,
		"posting_date": "2016-08-22"
	}, {
		"id": 158836,
		"material": "40019",
		"material_description": "Silibinin Capsules 35mg*2*10EA Carton",
		"order_num": "101563",
		"batch": "16000068",
		"quantity_wi": 30509.0,
		"unit": "EA",
		"pid": 159945,
		"posting_date": "2016-08-22"
	}, {
		"id": 158837,
		"material": "40019",
		"material_description": "Silibinin Capsules 35mg*2*10EA Carton",
		"order_num": "101563",
		"batch": "16000085",
		"quantity_wi": 18226.0,
		"unit": "EA",
		"pid": 159945,
		"posting_date": "2016-08-22"
	}, {
		"id": 158839,
		"material": "40010",
		"material_description": "BOPP Film 178mm",
		"order_num": "101563",
		"batch": "16000013",
		"quantity_wi": 7.33,
		"unit": "KG",
		"pid": 159945,
		"posting_date": "2016-08-22"
	}, {
		"id": 158840,
		"material": "40010",
		"material_description": "BOPP Film 178mm",
		"order_num": "101563",
		"batch": "16000018",
		"quantity_wi": 8.36,
		"unit": "KG",
		"pid": 159945,
		"posting_date": "2016-08-22"
	}, {
		"id": 158842,
		"material": "40020",
		"material_description": "Silibinin Capsules 35mg*2*10EA Shipper",
		"order_num": "101563",
		"batch": "16000060",
		"quantity_wi": 8.0,
		"unit": "EA",
		"pid": 159945,
		"posting_date": "2016-08-22"
	}, {
		"id": 158843,
		"material": "40020",
		"material_description": "Silibinin Capsules 35mg*2*10EA Shipper",
		"order_num": "101563",
		"batch": "16000069",
		"quantity_wi": 157.0,
		"unit": "EA",
		"pid": 159945,
		"posting_date": "2016-08-22"
	}, {
		"id": 158845,
		"material": "40021",
		"material_description": "Silibinin Capsules35mg*2*10EA Paperboard",
		"order_num": "101563",
		"batch": "16000061",
		"quantity_wi": 336.0,
		"unit": "EA",
		"pid": 159945,
		"posting_date": "2016-08-22"
	}],
	[{
		"id": 159935,
		"material": "40018",
		"material_description": "Silibinin Capsules Leaflet",
		"order_num": "101632",
		"batch": "16000106",
		"quantity_wi": 32900.0,
		"unit": "EA",
		"pid": 0,
		"posting_date": "2016-08-22"
	}, {
		"id": 159937,
		"material": "40022",
		"material_description": "Silibinin Capsules35mg*3*10EA Carton",
		"order_num": "101632",
		"batch": "16000110",
		"quantity_wi": 32655.0,
		"unit": "EA",
		"pid": 0,
		"posting_date": "2016-08-22"
	}, {
		"id": 159939,
		"material": "40010",
		"material_description": "BOPP Film 178mm",
		"order_num": "101632",
		"batch": "16000075",
		"quantity_wi": 13.09,
		"unit": "KG",
		"pid": 0,
		"posting_date": "2016-08-22"
	}, {
		"id": 159941,
		"material": "40023",
		"material_description": "Silibinin Capsules 35mg*3*10EA Shipper",
		"order_num": "101632",
		"batch": "16000093",
		"quantity_wi": 114.0,
		"unit": "EA",
		"pid": 0,
		"posting_date": "2016-08-22"
	}, {
		"id": 159942,
		"material": "40023",
		"material_description": "Silibinin Capsules 35mg*3*10EA Shipper",
		"order_num": "101632",
		"batch": "16000119",
		"quantity_wi": 50.0,
		"unit": "EA",
		"pid": 0,
		"posting_date": "2016-08-22"
	}, {
		"id": 159944,
		"material": "40024",
		"material_description": "Silibinin Capsules35mg*3*10EA Paperboard",
		"order_num": "101632",
		"batch": "16000094",
		"quantity_wi": 330.0,
		"unit": "EA",
		"pid": 0,
		"posting_date": "2016-08-22"
	}, {
		"id": 159945,
		"material": "70008",
		"material_description": "Silibinin Capsules 35mg*2*10EA",
		"order_num": "101632",
		"batch": "650605018",
		"quantity_wi": 972700.0,
		"unit": "EA",
		"pid": 0,
		"posting_date": "2016-08-22",
		"children": [{
			"id": 158825,
			"material": "60010",
			"material_description": "Silibinin Capsules 35mg",
			"order_num": "101563",
			"batch": "600903050",
			"quantity_wi": 975181.0,
			"unit": "EA",
			"pid": 159945,
			"posting_date": "2016-08-22",
			"children": [{
				"id": 157823,
				"material": "10001",
				"material_description": "silibinin",
				"order_num": "101503",
				"batch": "15000383",
				"quantity_wi": 35.0,
				"unit": "KG",
				"pid": 158825,
				"posting_date": "2016-05-09"
			}, {
				"id": 157825,
				"material": "20028",
				"material_description": "Soya Lecithin",
				"order_num": "101503",
				"batch": "15000354",
				"quantity_wi": 0.39,
				"unit": "KG",
				"pid": 158825,
				"posting_date": "2016-05-09"
			}, {
				"id": 157826,
				"material": "20028",
				"material_description": "Soya Lecithin",
				"order_num": "101503",
				"batch": "16000033",
				"quantity_wi": 64.61,
				"unit": "KG",
				"pid": 158825,
				"posting_date": "2016-05-09"
			}, {
				"id": 157828,
				"material": "20035",
				"material_description": "Anhydrous Ethanol",
				"order_num": "101503",
				"batch": "16000029",
				"quantity_wi": 480.0,
				"unit": "KG",
				"pid": 158825,
				"posting_date": "2016-05-09"
			}, {
				"id": 157830,
				"material": "20035",
				"material_description": "Anhydrous Ethanol",
				"order_num": "101503",
				"batch": "16000029",
				"quantity_wi": 20.0,
				"unit": "KG",
				"pid": 158825,
				"posting_date": "2016-05-09"
			}, {
				"id": 157832,
				"material": "20033",
				"material_description": "Lactose (SpheroLac 100)",
				"order_num": "101503",
				"batch": "15000369",
				"quantity_wi": 106.0,
				"unit": "KG",
				"pid": 158825,
				"posting_date": "2016-05-09"
			}, {
				"id": 157834,
				"material": "20034",
				"material_description": "Talc Powder",
				"order_num": "101503",
				"batch": "16000036",
				"quantity_wi": 31.46,
				"unit": "KG",
				"pid": 158825,
				"posting_date": "2016-05-09"
			}, {
				"id": 157836,
				"material": "20029",
				"material_description": "Glycolys STD",
				"order_num": "101503",
				"batch": "16000006",
				"quantity_wi": 20.6,
				"unit": "KG",
				"pid": 158825,
				"posting_date": "2016-05-09"
			}, {
				"id": 157838,
				"material": "20036",
				"material_description": "Silibinin printing 1#vacant capsules",
				"order_num": "101503",
				"batch": "15000366",
				"quantity_wi": 975395.0,
				"unit": "EA",
				"pid": 158825,
				"posting_date": "2016-05-09"
			}]
		}, {
			"id": 158827,
			"material": "30010",
			"material_description": "PVC/PVDC Colorless 231mm",
			"order_num": "101563",
			"batch": "16000038",
			"quantity_wi": 175.2,
			"unit": "KG",
			"pid": 159945,
			"posting_date": "2016-08-22"
		}, {
			"id": 158829,
			"material": "30011",
			"material_description": "AluminumFoil231mm SilibininCapsules 35mg",
			"order_num": "101563",
			"batch": "16000026",
			"quantity_wi": 29.65,
			"unit": "KG",
			"pid": 159945,
			"posting_date": "2016-08-22"
		}, {
			"id": 158831,
			"material": "30012",
			"material_description": "Tropical Type Blister AluminumFoil 231mm",
			"order_num": "101563",
			"batch": "16000027",
			"quantity_wi": 96.91,
			"unit": "KG",
			"pid": 159945,
			"posting_date": "2016-08-22"
		}, {
			"id": 158833,
			"material": "40018",
			"material_description": "Silibinin Capsules Leaflet",
			"order_num": "101563",
			"batch": "16000025",
			"quantity_wi": 3244.0,
			"unit": "EA",
			"pid": 159945,
			"posting_date": "2016-08-22"
		}, {
			"id": 158834,
			"material": "40018",
			"material_description": "Silibinin Capsules Leaflet",
			"order_num": "101563",
			"batch": "16000044",
			"quantity_wi": 45495.0,
			"unit": "EA",
			"pid": 159945,
			"posting_date": "2016-08-22"
		}, {
			"id": 158836,
			"material": "40019",
			"material_description": "Silibinin Capsules 35mg*2*10EA Carton",
			"order_num": "101563",
			"batch": "16000068",
			"quantity_wi": 30509.0,
			"unit": "EA",
			"pid": 159945,
			"posting_date": "2016-08-22"
		}, {
			"id": 158837,
			"material": "40019",
			"material_description": "Silibinin Capsules 35mg*2*10EA Carton",
			"order_num": "101563",
			"batch": "16000085",
			"quantity_wi": 18226.0,
			"unit": "EA",
			"pid": 159945,
			"posting_date": "2016-08-22"
		}, {
			"id": 158839,
			"material": "40010",
			"material_description": "BOPP Film 178mm",
			"order_num": "101563",
			"batch": "16000013",
			"quantity_wi": 7.33,
			"unit": "KG",
			"pid": 159945,
			"posting_date": "2016-08-22"
		}, {
			"id": 158840,
			"material": "40010",
			"material_description": "BOPP Film 178mm",
			"order_num": "101563",
			"batch": "16000018",
			"quantity_wi": 8.36,
			"unit": "KG",
			"pid": 159945,
			"posting_date": "2016-08-22"
		}, {
			"id": 158842,
			"material": "40020",
			"material_description": "Silibinin Capsules 35mg*2*10EA Shipper",
			"order_num": "101563",
			"batch": "16000060",
			"quantity_wi": 8.0,
			"unit": "EA",
			"pid": 159945,
			"posting_date": "2016-08-22"
		}, {
			"id": 158843,
			"material": "40020",
			"material_description": "Silibinin Capsules 35mg*2*10EA Shipper",
			"order_num": "101563",
			"batch": "16000069",
			"quantity_wi": 157.0,
			"unit": "EA",
			"pid": 159945,
			"posting_date": "2016-08-22"
		}, {
			"id": 158845,
			"material": "40021",
			"material_description": "Silibinin Capsules35mg*2*10EA Paperboard",
			"order_num": "101563",
			"batch": "16000061",
			"quantity_wi": 336.0,
			"unit": "EA",
			"pid": 159945,
			"posting_date": "2016-08-22"
		}]
	}, {
		"id": 158825,
		"material": "60010",
		"material_description": "Silibinin Capsules 35mg",
		"order_num": "101563",
		"batch": "600903050",
		"quantity_wi": 975181.0,
		"unit": "EA",
		"pid": 159945,
		"posting_date": "2016-08-22",
		"children": [{
			"id": 157823,
			"material": "10001",
			"material_description": "silibinin",
			"order_num": "101503",
			"batch": "15000383",
			"quantity_wi": 35.0,
			"unit": "KG",
			"pid": 158825,
			"posting_date": "2016-05-09"
		}, {
			"id": 157825,
			"material": "20028",
			"material_description": "Soya Lecithin",
			"order_num": "101503",
			"batch": "15000354",
			"quantity_wi": 0.39,
			"unit": "KG",
			"pid": 158825,
			"posting_date": "2016-05-09"
		}, {
			"id": 157826,
			"material": "20028",
			"material_description": "Soya Lecithin",
			"order_num": "101503",
			"batch": "16000033",
			"quantity_wi": 64.61,
			"unit": "KG",
			"pid": 158825,
			"posting_date": "2016-05-09"
		}, {
			"id": 157828,
			"material": "20035",
			"material_description": "Anhydrous Ethanol",
			"order_num": "101503",
			"batch": "16000029",
			"quantity_wi": 480.0,
			"unit": "KG",
			"pid": 158825,
			"posting_date": "2016-05-09"
		}, {
			"id": 157830,
			"material": "20035",
			"material_description": "Anhydrous Ethanol",
			"order_num": "101503",
			"batch": "16000029",
			"quantity_wi": 20.0,
			"unit": "KG",
			"pid": 158825,
			"posting_date": "2016-05-09"
		}, {
			"id": 157832,
			"material": "20033",
			"material_description": "Lactose (SpheroLac 100)",
			"order_num": "101503",
			"batch": "15000369",
			"quantity_wi": 106.0,
			"unit": "KG",
			"pid": 158825,
			"posting_date": "2016-05-09"
		}, {
			"id": 157834,
			"material": "20034",
			"material_description": "Talc Powder",
			"order_num": "101503",
			"batch": "16000036",
			"quantity_wi": 31.46,
			"unit": "KG",
			"pid": 158825,
			"posting_date": "2016-05-09"
		}, {
			"id": 157836,
			"material": "20029",
			"material_description": "Glycolys STD",
			"order_num": "101503",
			"batch": "16000006",
			"quantity_wi": 20.6,
			"unit": "KG",
			"pid": 158825,
			"posting_date": "2016-05-09"
		}, {
			"id": 157838,
			"material": "20036",
			"material_description": "Silibinin printing 1#vacant capsules",
			"order_num": "101503",
			"batch": "15000366",
			"quantity_wi": 975395.0,
			"unit": "EA",
			"pid": 158825,
			"posting_date": "2016-05-09"
		}]
	}, {
		"id": 157823,
		"material": "10001",
		"material_description": "silibinin",
		"order_num": "101503",
		"batch": "15000383",
		"quantity_wi": 35.0,
		"unit": "KG",
		"pid": 158825,
		"posting_date": "2016-05-09"
	}, {
		"id": 157825,
		"material": "20028",
		"material_description": "Soya Lecithin",
		"order_num": "101503",
		"batch": "15000354",
		"quantity_wi": 0.39,
		"unit": "KG",
		"pid": 158825,
		"posting_date": "2016-05-09"
	}, {
		"id": 157826,
		"material": "20028",
		"material_description": "Soya Lecithin",
		"order_num": "101503",
		"batch": "16000033",
		"quantity_wi": 64.61,
		"unit": "KG",
		"pid": 158825,
		"posting_date": "2016-05-09"
	}, {
		"id": 157828,
		"material": "20035",
		"material_description": "Anhydrous Ethanol",
		"order_num": "101503",
		"batch": "16000029",
		"quantity_wi": 480.0,
		"unit": "KG",
		"pid": 158825,
		"posting_date": "2016-05-09"
	}, {
		"id": 157830,
		"material": "20035",
		"material_description": "Anhydrous Ethanol",
		"order_num": "101503",
		"batch": "16000029",
		"quantity_wi": 20.0,
		"unit": "KG",
		"pid": 158825,
		"posting_date": "2016-05-09"
	}, {
		"id": 157832,
		"material": "20033",
		"material_description": "Lactose (SpheroLac 100)",
		"order_num": "101503",
		"batch": "15000369",
		"quantity_wi": 106.0,
		"unit": "KG",
		"pid": 158825,
		"posting_date": "2016-05-09"
	}, {
		"id": 157834,
		"material": "20034",
		"material_description": "Talc Powder",
		"order_num": "101503",
		"batch": "16000036",
		"quantity_wi": 31.46,
		"unit": "KG",
		"pid": 158825,
		"posting_date": "2016-05-09"
	}, {
		"id": 157836,
		"material": "20029",
		"material_description": "Glycolys STD",
		"order_num": "101503",
		"batch": "16000006",
		"quantity_wi": 20.6,
		"unit": "KG",
		"pid": 158825,
		"posting_date": "2016-05-09"
	}, {
		"id": 157838,
		"material": "20036",
		"material_description": "Silibinin printing 1#vacant capsules",
		"order_num": "101503",
		"batch": "15000366",
		"quantity_wi": 975395.0,
		"unit": "EA",
		"pid": 158825,
		"posting_date": "2016-05-09"
	}, {
		"id": 158827,
		"material": "30010",
		"material_description": "PVC/PVDC Colorless 231mm",
		"order_num": "101563",
		"batch": "16000038",
		"quantity_wi": 175.2,
		"unit": "KG",
		"pid": 159945,
		"posting_date": "2016-08-22"
	}, {
		"id": 158829,
		"material": "30011",
		"material_description": "AluminumFoil231mm SilibininCapsules 35mg",
		"order_num": "101563",
		"batch": "16000026",
		"quantity_wi": 29.65,
		"unit": "KG",
		"pid": 159945,
		"posting_date": "2016-08-22"
	}, {
		"id": 158831,
		"material": "30012",
		"material_description": "Tropical Type Blister AluminumFoil 231mm",
		"order_num": "101563",
		"batch": "16000027",
		"quantity_wi": 96.91,
		"unit": "KG",
		"pid": 159945,
		"posting_date": "2016-08-22"
	}, {
		"id": 158833,
		"material": "40018",
		"material_description": "Silibinin Capsules Leaflet",
		"order_num": "101563",
		"batch": "16000025",
		"quantity_wi": 3244.0,
		"unit": "EA",
		"pid": 159945,
		"posting_date": "2016-08-22"
	}, {
		"id": 158834,
		"material": "40018",
		"material_description": "Silibinin Capsules Leaflet",
		"order_num": "101563",
		"batch": "16000044",
		"quantity_wi": 45495.0,
		"unit": "EA",
		"pid": 159945,
		"posting_date": "2016-08-22"
	}, {
		"id": 158836,
		"material": "40019",
		"material_description": "Silibinin Capsules 35mg*2*10EA Carton",
		"order_num": "101563",
		"batch": "16000068",
		"quantity_wi": 30509.0,
		"unit": "EA",
		"pid": 159945,
		"posting_date": "2016-08-22"
	}, {
		"id": 158837,
		"material": "40019",
		"material_description": "Silibinin Capsules 35mg*2*10EA Carton",
		"order_num": "101563",
		"batch": "16000085",
		"quantity_wi": 18226.0,
		"unit": "EA",
		"pid": 159945,
		"posting_date": "2016-08-22"
	}, {
		"id": 158839,
		"material": "40010",
		"material_description": "BOPP Film 178mm",
		"order_num": "101563",
		"batch": "16000013",
		"quantity_wi": 7.33,
		"unit": "KG",
		"pid": 159945,
		"posting_date": "2016-08-22"
	}, {
		"id": 158840,
		"material": "40010",
		"material_description": "BOPP Film 178mm",
		"order_num": "101563",
		"batch": "16000018",
		"quantity_wi": 8.36,
		"unit": "KG",
		"pid": 159945,
		"posting_date": "2016-08-22"
	}, {
		"id": 158842,
		"material": "40020",
		"material_description": "Silibinin Capsules 35mg*2*10EA Shipper",
		"order_num": "101563",
		"batch": "16000060",
		"quantity_wi": 8.0,
		"unit": "EA",
		"pid": 159945,
		"posting_date": "2016-08-22"
	}, {
		"id": 158843,
		"material": "40020",
		"material_description": "Silibinin Capsules 35mg*2*10EA Shipper",
		"order_num": "101563",
		"batch": "16000069",
		"quantity_wi": 157.0,
		"unit": "EA",
		"pid": 159945,
		"posting_date": "2016-08-22"
	}, {
		"id": 158845,
		"material": "40021",
		"material_description": "Silibinin Capsules35mg*2*10EA Paperboard",
		"order_num": "101563",
		"batch": "16000061",
		"quantity_wi": 336.0,
		"unit": "EA",
		"pid": 159945,
		"posting_date": "2016-08-22"
	}],
	[{
		"id": 158825,
		"material": "60010",
		"material_description": "Silibinin Capsules 35mg",
		"order_num": "101563",
		"batch": "600903050",
		"quantity_wi": 975181.0,
		"unit": "EA",
		"pid": 0,
		"posting_date": "2016-08-22",
		"children": [{
			"id": 157823,
			"material": "10001",
			"material_description": "silibinin",
			"order_num": "101503",
			"batch": "15000383",
			"quantity_wi": 35.0,
			"unit": "KG",
			"pid": 158825,
			"posting_date": "2016-05-09"
		}, {
			"id": 157825,
			"material": "20028",
			"material_description": "Soya Lecithin",
			"order_num": "101503",
			"batch": "15000354",
			"quantity_wi": 0.39,
			"unit": "KG",
			"pid": 158825,
			"posting_date": "2016-05-09"
		}, {
			"id": 157826,
			"material": "20028",
			"material_description": "Soya Lecithin",
			"order_num": "101503",
			"batch": "16000033",
			"quantity_wi": 64.61,
			"unit": "KG",
			"pid": 158825,
			"posting_date": "2016-05-09"
		}, {
			"id": 157828,
			"material": "20035",
			"material_description": "Anhydrous Ethanol",
			"order_num": "101503",
			"batch": "16000029",
			"quantity_wi": 480.0,
			"unit": "KG",
			"pid": 158825,
			"posting_date": "2016-05-09"
		}, {
			"id": 157830,
			"material": "20035",
			"material_description": "Anhydrous Ethanol",
			"order_num": "101503",
			"batch": "16000029",
			"quantity_wi": 20.0,
			"unit": "KG",
			"pid": 158825,
			"posting_date": "2016-05-09"
		}, {
			"id": 157832,
			"material": "20033",
			"material_description": "Lactose (SpheroLac 100)",
			"order_num": "101503",
			"batch": "15000369",
			"quantity_wi": 106.0,
			"unit": "KG",
			"pid": 158825,
			"posting_date": "2016-05-09"
		}, {
			"id": 157834,
			"material": "20034",
			"material_description": "Talc Powder",
			"order_num": "101503",
			"batch": "16000036",
			"quantity_wi": 31.46,
			"unit": "KG",
			"pid": 158825,
			"posting_date": "2016-05-09"
		}, {
			"id": 157836,
			"material": "20029",
			"material_description": "Glycolys STD",
			"order_num": "101503",
			"batch": "16000006",
			"quantity_wi": 20.6,
			"unit": "KG",
			"pid": 158825,
			"posting_date": "2016-05-09"
		}, {
			"id": 157838,
			"material": "20036",
			"material_description": "Silibinin printing 1#vacant capsules",
			"order_num": "101503",
			"batch": "15000366",
			"quantity_wi": 975395.0,
			"unit": "EA",
			"pid": 158825,
			"posting_date": "2016-05-09"
		}]
	}, {
		"id": 157823,
		"material": "10001",
		"material_description": "silibinin",
		"order_num": "101503",
		"batch": "15000383",
		"quantity_wi": 35.0,
		"unit": "KG",
		"pid": 158825,
		"posting_date": "2016-05-09"
	}, {
		"id": 157825,
		"material": "20028",
		"material_description": "Soya Lecithin",
		"order_num": "101503",
		"batch": "15000354",
		"quantity_wi": 0.39,
		"unit": "KG",
		"pid": 158825,
		"posting_date": "2016-05-09"
	}, {
		"id": 157826,
		"material": "20028",
		"material_description": "Soya Lecithin",
		"order_num": "101503",
		"batch": "16000033",
		"quantity_wi": 64.61,
		"unit": "KG",
		"pid": 158825,
		"posting_date": "2016-05-09"
	}, {
		"id": 157828,
		"material": "20035",
		"material_description": "Anhydrous Ethanol",
		"order_num": "101503",
		"batch": "16000029",
		"quantity_wi": 480.0,
		"unit": "KG",
		"pid": 158825,
		"posting_date": "2016-05-09"
	}, {
		"id": 157830,
		"material": "20035",
		"material_description": "Anhydrous Ethanol",
		"order_num": "101503",
		"batch": "16000029",
		"quantity_wi": 20.0,
		"unit": "KG",
		"pid": 158825,
		"posting_date": "2016-05-09"
	}, {
		"id": 157832,
		"material": "20033",
		"material_description": "Lactose (SpheroLac 100)",
		"order_num": "101503",
		"batch": "15000369",
		"quantity_wi": 106.0,
		"unit": "KG",
		"pid": 158825,
		"posting_date": "2016-05-09"
	}, {
		"id": 157834,
		"material": "20034",
		"material_description": "Talc Powder",
		"order_num": "101503",
		"batch": "16000036",
		"quantity_wi": 31.46,
		"unit": "KG",
		"pid": 158825,
		"posting_date": "2016-05-09"
	}, {
		"id": 157836,
		"material": "20029",
		"material_description": "Glycolys STD",
		"order_num": "101503",
		"batch": "16000006",
		"quantity_wi": 20.6,
		"unit": "KG",
		"pid": 158825,
		"posting_date": "2016-05-09"
	}, {
		"id": 157838,
		"material": "20036",
		"material_description": "Silibinin printing 1#vacant capsules",
		"order_num": "101503",
		"batch": "15000366",
		"quantity_wi": 975395.0,
		"unit": "EA",
		"pid": 158825,
		"posting_date": "2016-05-09"
	}, {
		"id": 158827,
		"material": "30010",
		"material_description": "PVC/PVDC Colorless 231mm",
		"order_num": "101563",
		"batch": "16000038",
		"quantity_wi": 175.2,
		"unit": "KG",
		"pid": 0,
		"posting_date": "2016-08-22"
	}, {
		"id": 158829,
		"material": "30011",
		"material_description": "AluminumFoil231mm SilibininCapsules 35mg",
		"order_num": "101563",
		"batch": "16000026",
		"quantity_wi": 29.65,
		"unit": "KG",
		"pid": 0,
		"posting_date": "2016-08-22"
	}, {
		"id": 158831,
		"material": "30012",
		"material_description": "Tropical Type Blister AluminumFoil 231mm",
		"order_num": "101563",
		"batch": "16000027",
		"quantity_wi": 96.91,
		"unit": "KG",
		"pid": 0,
		"posting_date": "2016-08-22"
	}, {
		"id": 158833,
		"material": "40018",
		"material_description": "Silibinin Capsules Leaflet",
		"order_num": "101563",
		"batch": "16000025",
		"quantity_wi": 3244.0,
		"unit": "EA",
		"pid": 0,
		"posting_date": "2016-08-22"
	}, {
		"id": 158834,
		"material": "40018",
		"material_description": "Silibinin Capsules Leaflet",
		"order_num": "101563",
		"batch": "16000044",
		"quantity_wi": 45495.0,
		"unit": "EA",
		"pid": 0,
		"posting_date": "2016-08-22"
	}, {
		"id": 158836,
		"material": "40019",
		"material_description": "Silibinin Capsules 35mg*2*10EA Carton",
		"order_num": "101563",
		"batch": "16000068",
		"quantity_wi": 30509.0,
		"unit": "EA",
		"pid": 0,
		"posting_date": "2016-08-22"
	}, {
		"id": 158837,
		"material": "40019",
		"material_description": "Silibinin Capsules 35mg*2*10EA Carton",
		"order_num": "101563",
		"batch": "16000085",
		"quantity_wi": 18226.0,
		"unit": "EA",
		"pid": 0,
		"posting_date": "2016-08-22"
	}, {
		"id": 158839,
		"material": "40010",
		"material_description": "BOPP Film 178mm",
		"order_num": "101563",
		"batch": "16000013",
		"quantity_wi": 7.33,
		"unit": "KG",
		"pid": 0,
		"posting_date": "2016-08-22"
	}, {
		"id": 158840,
		"material": "40010",
		"material_description": "BOPP Film 178mm",
		"order_num": "101563",
		"batch": "16000018",
		"quantity_wi": 8.36,
		"unit": "KG",
		"pid": 0,
		"posting_date": "2016-08-22"
	}, {
		"id": 158842,
		"material": "40020",
		"material_description": "Silibinin Capsules 35mg*2*10EA Shipper",
		"order_num": "101563",
		"batch": "16000060",
		"quantity_wi": 8.0,
		"unit": "EA",
		"pid": 0,
		"posting_date": "2016-08-22"
	}, {
		"id": 158843,
		"material": "40020",
		"material_description": "Silibinin Capsules 35mg*2*10EA Shipper",
		"order_num": "101563",
		"batch": "16000069",
		"quantity_wi": 157.0,
		"unit": "EA",
		"pid": 0,
		"posting_date": "2016-08-22"
	}, {
		"id": 158845,
		"material": "40021",
		"material_description": "Silibinin Capsules35mg*2*10EA Paperboard",
		"order_num": "101563",
		"batch": "16000061",
		"quantity_wi": 336.0,
		"unit": "EA",
		"pid": 0,
		"posting_date": "2016-08-22"
	}]
]

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
