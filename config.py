import os

# 是否开启debug模式
DEBUG = True

# 读取数据库环境变量
username = os.environ.get("MYSQL_USERNAME", r'root')
password = os.environ.get("MYSQL_PASSWORD", r'lubupangAdmin123!!!')
db_address =os.environ.get("MYSQL_ADDRESS", r'10.0.224.8:3306')
