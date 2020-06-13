from flask import jsonify
from decimal import Decimal
import pymysql

def query(querystr):
    connection = pymysql.connect(
        host='localhost',
        user='hruday',
        password='hruday@30', 
        db='testapi',
        cursorclass = pymysql.cursors.DictCursor
    )
    connection.begin()
    cursor=connection.cursor()
    cursor.execute(querystr)
    result = encode(cursor.fetchall())
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify(result)

def encode(data):
    for row in data:
        for key,value in row.items():
            if isinstance(value,Decimal):
                row[key]=str(value)
    return data
