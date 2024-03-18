db_ip = '127.0.0.1'
db_port = '5432'

bd_datalake_poc = 'tfmdatalake_poc'
bd_warehouse_poc = 'tfmwarehouse_poc'

bd_datalake = 'tfmdatalake'
bd_warehouse = 'tfmwarehouse'

passw = 'abc'


def set_password_db(cont):
    global passw
    passw = cont
