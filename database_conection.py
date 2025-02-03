import pymysql, os, ast

def database_connection():
    db = None

    port_num = 3306
    host_address = 'localhost'
    user_name = 'root'
    password = ''
    database_name = 'zomata'
    db = pymysql.connect(host=host_address, user=user_name,
                         passwd=password, port=port_num, db=database_name, cursorclass=pymysql.cursors.DictCursor)

    return db