import mysql.connector

# MySQL 연결 설정
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="python_test"
)

cursor = connection.cursor()  # 데이터베이스 작업을 위한 커서 생성

# 데이터 삽입 쿼리
sql = "INSERT INTO users (name, email) VALUES (%s, %s)"  # 사용자 데이터를 삽입하는 SQL 쿼리
values = ("Encore", "encore@example.com")  # 삽입할 데이터 값

cursor.execute(sql, values)  # 쿼리 실행
connection.commit()  # 변경 사항 커밋

print(f"{cursor.rowcount}개의 행이 삽입되었습니다.")  # 삽입된 행 수 출력

cursor.close()  # 커서 종료
connection.close()  # 연결 종료