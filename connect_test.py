import pandas as pd
import pyodbc

# Chuỗi kết nối ODBC
conn_str = 'Driver={ODBC Driver 17 for SQL Server};Server=MSI\DUCNAM;Database=MyDatabase;UID=dn;PWD=123456'

# Tạo kết nối ODBC
conn = pyodbc.connect(conn_str)

# Đọc dữ liệu từ bảng Student vào DataFrame
query = "SELECT * FROM Student"
df = pd.read_sql(query, conn)

# Xóa dòng có ID là 3
df = df[df['ID'] != 3]

# Chuyển DataFrame thành danh sách các bản ghi
records = df.to_dict('records')

# Tạo con trỏ cursor
cursor = conn.cursor()

# Xóa dữ liệu cũ trong bảng Student
cursor.execute("DELETE FROM Student")

# Thêm dữ liệu mới vào bảng Student
cursor.executemany("INSERT INTO Student (ID, Name, Age) VALUES (?, ?, ?)", [(record['ID'], record['Name'], record['Age']) for record in records])

# Lưu thay đổi
conn.commit()

# Đóng kết nối
conn.close()