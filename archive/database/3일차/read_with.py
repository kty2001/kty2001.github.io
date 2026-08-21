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

        cursor.execute("SELECT * FROM users")

        rows = cursor.fetchall()  # 조회 결과를 모두 가져옴
        print(f'{cursor.rowcount}개 행 조회')
        print(rows)