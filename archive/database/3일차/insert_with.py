import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
db_password = os.getenv('DB_PASSWORD')
print(db_password)

# MySQL 연결 설정
with mysql.connector.connect(
    host="localhost",
    user="root",
    password=db_password,
    database="python_test"
) as connection:

    with connection.cursor()  as cursor:

        sql = "INSERT INTO users (name, email) VALUES (%s, %s)"  # 사용자 데이터를 삽입하는 SQL 쿼리
        values = ("Encore3", "encore3@example.com")  # 삽입할 데이터 값

        cursor.execute(sql, values)  # 쿼리 실행
        connection.commit()  # 변경 사항 커밋

        print(f"{cursor.rowcount}개의 행이 삽입되었습니다.")  # 삽입된 행 수 출력
