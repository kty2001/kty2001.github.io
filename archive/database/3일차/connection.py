import mysql.connector

connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
    database = 'python_test'
)

# 연결 확인
if connection.is_connected():
    print("MySQL에 성공적으로 연결되었습니다.")  # 연결 성공 메시지 출력

connection.close()