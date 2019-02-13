# -*- coding: utf-8 -*-

import paramiko
import MySQLdb


def connect_ssh(host, port, user, pwd):
    """远程连接服务器"""
    transport = paramiko.Transport(host, port)
    transport.connect(username=user, password=pwd)
    ssh = paramiko.SSHClient()
    ssh._transport = transport
    return ssh


def connect_database(host, user, pwd, db, sql):
    """连接数据库"""
    conn = MySQLdb.connect(host=host, user=user, passwd=pwd, db=db, charset="utf8")
    cursor = conn.cursor()
    cursor.execute(sql)
    return cursor.fetchall()


def operate():
    query_sql = '执行的SQL语句'
    files = "/Users/jingxiaotao/11.txt"
    try:
        conn = MySQLdb.connect("localhost", "root", "jxt", "test_port", charset="utf8")
        cursor = conn.cursor()
        cursor.execute(query_sql)
        result = cursor.fetchall()
        count = 0
        fr = open(files, "r")
        lines = fr.readlines()
        inserts = []
        for num, value in enumerate(lines):
            inserts.append(value)
            if "bindadress" in value:
                for info in result:
                    count += 1
                    if info[0] == "192.168.55.205":
                        print info[1]
                        continue
                    inserts.append("0.0.0.0" + " " + info[1] + "     " + info[0] + "     " + info[1] + "\n")
                    write_info = "".join(inserts)
                f = open(files, 'w')
                f.write(write_info)
            break
    except Exception as err:
        return err
    finally:
        conn.close()
        f.close()
        fr.close()


if __name__ == "__main__":
    operate()
