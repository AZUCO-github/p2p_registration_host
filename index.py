#!/usr/local/bin/python

import  cgi
from datetime import datetime, timedelta
import  sqlite3
sqlite3_db_path = "azuco.db"

def make_database():
    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            time TEXT,
            software_id TEXT,
            software_pw TEXT,
            user_ip TEXT,
            user_port TEXT,
            software_ex1 TEXT,
            software_ex2 TEXT,
            software_ex3 TEXT,
            software_ex4 TEXT
        )
    """)
    conn.commit()
    print("sqlile3 databese Initialized<br>")



def command_add():
    time=datetime.now()
    software_id=query_string.getvalue("id")
    software_pw=query_string.getvalue("pw")
    user_ip=query_string.getvalue("ip")
    user_port=query_string.getvalue("pt")
    software_ex1=query_string.getvalue("e1")
    software_ex2=query_string.getvalue("e2")
    software_ex3=query_string.getvalue("e3")
    software_ex4=query_string.getvalue("e4")
    cursor.execute("INSERT INTO users (time,software_id,software_pw,user_ip,user_port,software_ex1,software_ex2,software_ex3,software_ex4) VALUES (?,?,?,?,?,?,?,?,?)", (time,software_id,software_pw,user_ip,user_port,software_ex1,software_ex2,software_ex3,software_ex4))
    conn.commit()
    print(f"command = add<br>")
    print(f"    time = {time}<br>")
    print(f"    software_id = {software_id}<br>")
    print(f"    software_pw = {software_pw}<br>")
    print(f"    user_ip = {user_ip}<br>")
    print(f"    user_port = {user_port}<br>")
    print(f"    software_ex1 = {software_ex1}<br>")
    print(f"    software_ex2 = {software_ex2}<br>")
    print(f"    software_ex3 = {software_ex3}<br>")
    print(f"    software_ex4 = {software_ex4}<br>")
    print(f"<br>")



def command_del():
    software_id=query_string.getvalue("id")
    software_pw=query_string.getvalue("pw")

    cursor.execute("SELECT MAX(id) FROM users")
    maxid = cursor.fetchone()[0]
    rowid = 1
    while rowid <= maxid:
        cursor.execute("SELECT * FROM users WHERE id=?",(rowid,))
        row = cursor.fetchone()
        if row is not None:

            if ((row[2]==software_id) and (row[3]==software_pw)):
                cursor.execute("DELETE FROM users WHERE id=?", (row[0],))
                conn.commit()

                print(f"command = del<br>")
                print(f"    time = {row[1]}<br>")
                print(f"    software_id = {row[2]}<br>")
                print(f"    software_pw = {row[3]}<br>")
                print(f"    user_ip = {row[4]}<br>")
                print(f"    user_port = {row[5]}<br>")
                print(f"    software_ex1 = {row[6]}<br>")
                print(f"    software_ex2 = {row[7]}<br>")
                print(f"    software_ex3 = {row[8]}<br>")
                print(f"    software_ex4 = {row[9]}<br>")
                print(f"<br>")
        rowid = rowid + 1



def command_list():
    cursor.execute("SELECT MAX(id) FROM users")
    maxid = cursor.fetchone()[0]
    rowid = 1
    while rowid <= maxid:
        cursor.execute("SELECT * FROM users WHERE id=?",(rowid,))
        row = cursor.fetchone()
        if row is not None:
            print(f"    No = {row[0]}<br>")
            print(f"    time = {row[1]}<br>")
            print(f"    software_id = {row[2]}<br>")
            print(f"    software_pw = {row[3]}<br>")
            print(f"    user_ip = {row[4]}<br>")
            print(f"    user_port = {row[5]}<br>")
            print(f"    software_ex1 = {row[6]}<br>")
            print(f"    software_ex2 = {row[7]}<br>")
            print(f"    software_ex3 = {row[8]}<br>")
            print(f"    software_ex4 = {row[9]}<br>")
            print(f"<br>")
        rowid = rowid + 1
    


def epilogue_delete():
    print("epilogue delete<br>")
    oneday_ago_time = datetime.now() - timedelta(hours=24)
    cursor.execute("SELECT MAX(id) FROM users")
    maxid = cursor.fetchone()[0]
    rowid = 1
    while rowid <= maxid:
        cursor.execute("SELECT * FROM users WHERE id=?",(rowid,))
        row = cursor.fetchone()
        if row is not None:
            time = datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S")
            if (time < oneday_ago_time):
                cursor.execute("DELETE FROM users WHERE id=?", (row[0],))
                conn.commit()
                print(f"command = del<br>")
                print(f"    time = {row[1]}<br>")
                print(f"    software_id = {row[2]}<br>")
                print(f"    software_pw = {row[3]}<br>")
                print(f"    user_ip = {row[4]}<br>")
                print(f"    user_port = {row[5]}<br>")
                print(f"    software_ex1 = {row[6]}<br>")
                print(f"    software_ex2 = {row[7]}<br>")
                print(f"    software_ex3 = {row[8]}<br>")
                print(f"    software_ex4 = {row[9]}<br>")
                print(f"<br>")
        rowid = rowid + 1



print("Content-Type: text/html; charset=utf-8\n\n")
print("<html><body>")
print("code Initialize<br>")

print("sqlile3 Initialize<br>")
conn = sqlite3.connect(sqlite3_db_path)
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
table_exists = cursor.fetchone()

if not table_exists:
    make_database()

query_string = cgi.FieldStorage()
query_command=query_string.getvalue("cm")
print(f"command = {query_command}<br>")

if query_command == "add":
    command_add()

if query_command == "del":
    command_del()

if query_command == "list":
    command_list()

epilogue_delete()
print("</body></html>")
