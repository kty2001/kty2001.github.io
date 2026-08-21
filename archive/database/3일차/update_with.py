import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
db_password = os.getenv('DB_PASSWORD')

# MySQL 연결 설정
with mysql.connector.connect(
    host="localhost",
    user="root",
    password=db_password,
    database="python_test"
) as connection:

    with connection.cursor()  as cursor:  # 삽입할 데이터 값
    # with connection.cursor(dictionary=True)  as cursor:  # 삽입할 데이터 값

        sql = "UPDATE users SET email = %s WHERE name = %s"  # 특정 사용자의 이메일을 업데이트하는 SQL 쿼리
        values = ("new_encore@example.com", "Encore")  # 업데이트할 데이터 값

        cursor.execute(sql, values)  # 쿼리 실행
        connection.commit()

        print(f"{cursor.rowcount}개의 행이 업데이트되었습니다.")
