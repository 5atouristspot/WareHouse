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
