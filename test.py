import pandas as pd
import pyodbc

# Kết nối tới cơ sở dữ liệu
conn_str = 'DRIVER={ODBC Driver 17 for SQL Server};\
            SERVER=MSI\DUCNAM;\
            DATABASE=my_database;\
            UID=dn;\
            PWD=123456'

# Thêm dữ liệu vào DataFrame
new_data = {'StudentID':[15,16,17,18],
            'fname':['Dinh Le Duc Nam', 'Le Thuy Huyen','Tran Binh Nguyen','Nguyen Minh Duc'],
            'sex':[1,1,1,0],
            'dob':['2003-10-18','2003-2-3','2003-10-19','2003-10-10']}
new_df = pd.DataFrame(new_data)

with pyodbc.connect(conn_str) as conn:
    cursor = conn.cursor()

    # Thêm dữ liệu vào bảng
    for index, row in new_df.iterrows():
        values = (row['Name'], row['Age'])
        cursor.execute("INSERT INTO TblStudent (Name, Age) VALUES (?, ?)", values)

    # Commit các thay đổi vào cơ sở dữ liệu
    conn.commit()

# Đọc lại dữ liệu sau khi thêm
with pyodbc.connect(conn_str) as conn:
    updated_df = pd.read_sql("SELECT * FROM TblStudent", conn)

# Hiển thị dữ liệu sau khi thêm
print(updated_df)