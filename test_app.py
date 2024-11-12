import streamlit as st
import mysql.connector
from mysql.connector import Error

# 连接到 MySQL 数据库
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",  # 如 localhost 或云服务器地址
            user="root",
            password="12345",
            database="test_db" # 数据库名
        )
        st.success("connect to database successfully!")
    except Error as e:
        st.error(f"connect failed: {e}")
    return connection

# 从数据库中获取用户信息
def fetch_users(connection):
    query = "SELECT * FROM users"
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows

# Streamlit 应用
st.title("User Showcase")

# 创建数据库连接
connection = create_connection()

# 如果连接成功，展示用户数据
if connection:
    users = fetch_users(connection)
    for user in users:
        st.write(f"ID: {user[0]}, name: {user[1]}, age: {user[2]}, email: {user[3]}")
