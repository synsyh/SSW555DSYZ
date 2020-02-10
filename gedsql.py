"""
SSW555DSYZ-MySQL_test by Yuning Sun
16:34 2020/2/7
Module documentation: 
"""
import mysql.connector


def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('create table if not exists 555test1 ('
                   'id varchar(5) primary key, '
                   'name varchar(20),'
                   'gender varchar(2),'
                   'birthday varchar(20),'
                   'age varchar(3),'
                   'alive varchar(1),'
                   'death varchar(20),'
                   'child varchar(5),'
                   'spouse varchar(5))')
    # TODO: return create result
    conn.commit()
    cursor.close()


def insert_data(id, name, gender, birthday, age, alive, death, child, spouse):
    cursor = conn.cursor()
    cursor.execute('insert into 555test '
                   '(id, name, gender, birthday, age, alive, death, child, spouse) '
                   'values (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
                   [id, name, gender, birthday, age, alive, death, child, spouse])
    conn.commit()
    cursor.close()


def find_data():
    cursor = conn.cursor()
    cursor.execute('select * from 555test')
    values = cursor.fetchall()
    print(values)
    cursor.close()


def init():
    user_name = 'root'
    password = 'password'
    database = '555test'
    return mysql.connector.connect(user=user_name, password=password, database=database)


if __name__ == '__main__':
    conn = init()
    # insert_data('I06', 'Joe', 'M', '2019-1-1', '53', '0', '2018-1-1', 'NA', 'F23')
    find_data()
    conn.close()
