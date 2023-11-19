import pandas as pd
import pyodbc 

# Kết nối tới cơ sở dữ liệu
conn_str = 'DRIVER={ODBC Driver 17 for SQL Server};\
            SERVER=MSI\DUCNAM;\
            DATABASE=my_database;\
            UID=dn;\
            PWD=123456'
conn = pyodbc.connect(conn_str)

# Đọc dữ liệu từ bảng Student vào DataFrame
query = "SELECT * FROM dbo.TblStudent"
df = pd.read_sql(query, conn)
print(df)
# Xóa dòng có ID là 3
row_to_delete = df[df['StudentID'] == 3]
df = df[df['StudentID'] != 3]

# Cập nhật lại cơ sở dữ liệu với DataFrame đã xóa dòng
df.to_sql('Student', conn, if_exists='replace', index=False)

# Đóng kết nối
conn.close()