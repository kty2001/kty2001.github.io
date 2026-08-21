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

        sql = "DELETE FROM users WHERE name = %s"
        values = ("Encore", )  # 업데이트할 데이터 값

        cursor.execute(sql, values)  # 쿼리 실행
        connection.commit()

        print(f"{cursor.rowcount}개의 행이 삭제되었습니다.")
