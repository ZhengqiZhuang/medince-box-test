import pandas as pd
import mysql.connector
import numpy as np

# 读取 Excel 文件
df = pd.read_excel('/Users/jinanzai/东北大学/大创/论文/药品识别/数据库/国家药品编码本位码信息（国产药品）.xlsx')

# 替换 NaN 为 None
df = df.where(pd.notnull(df), None)

# 连接到 MySQL 数据库
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="zzq123",
    database="medicine"
)
cursor = conn.cursor()

# 生成 SQL 插入语句
sql = """
INSERT INTO medicine (number, verifyNumber, name, class, specifications, hasCompany, produceCompany, medicineNumber, memo) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# 将数据框中的数据插入到 MySQL 表中
for i, row in df.iterrows():
    try:
        # 打印调试信息
        print(f"Executing: {sql} with values: {tuple(row)}")
        cursor.execute(sql, tuple(row))
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        print(f"Failed to insert row: {tuple(row)}")
        continue

# 提交事务
conn.commit()

# 关闭数据库连接
cursor.close()
conn.close()
