import mysql.connector

# MySQL 연결 설정
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="python_test"
)

cursor = connection.cursor()  # 데이터베이스 작업을 위한 커서 생성

# 데이터 조회 쿼리
cursor.execute("SELECT * FROM users")  # 모든 사용자 데이터를 조회하는 SQL 쿼리

rows = cursor.fetchall()  # 조회 결과를 모두 가져옴
for row in rows:
    print(row)  # 각 행 출력

cursor.close()  # 커서 종료
connection.close()  # 연결 종료