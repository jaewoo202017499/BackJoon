import mysql.connector
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}

number = input("문제 번호를 입력하세요 : ")
url = "https://www.acmicpc.net/problem/{0}".format(number)
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

rate = soup.find("table", attrs ={"class" : "table"}).find_all("td")[5].get_text()
name = soup.find("span", attrs={"id" : "problem_title"}).get_text()
#level_url= soup.find("ul", attrs="nav nav-pills no-print problem-menu").img["src"]

try :
    conn = mysql.connector.connect(
        host ='localhost',
        user ='root',
        passwd ='jaewoo',
        db ='backjoon',
        charset='utf8'
    )

    #커서 생성
    cursor = conn.cursor()

    #쿼리 실행
    sql_query1 = "insert into backJoon values ('{0}','{1}','{2}','{3}');".format(name,number,rate,url)
    cursor.execute(sql_query1)
    sql_query2 = "select * from backjoon;"
    cursor.execute(sql_query2)

    #쿼리 결과 가져오기
    result = cursor.fetchall()

    #결과 출력
    for row in result:
        print(row)

    #데이터 저장
    conn.commit()

    #연결과 커서 닫기
    cursor.close()
    conn.close()
except :
    print("중복")