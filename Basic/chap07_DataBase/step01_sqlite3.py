'''
Created on 2016. 5. 25.

sqlite3 - python 내장 DBMS, 온라인상에서는 실행 안됨...ㅠ
'''
import sqlite3

print(sqlite3.sqlite_version_info) #(3, 8, 11)

#DB 연동 객체 생성 + DB 생성
conn = sqlite3.connect('nice.db') #nice.db란 DB를 만듬
cursor = conn.cursor() #cursor 객체 생성 - sql문 실행하게 해 줌 

#테이블 삭제
cursor.execute('drop table if exists sat') #sql문 실행
conn.commit() #sql문 실행 결과를 DB에 반영
#테이블 컬럼 작성, sat이란 테이블 생성
cursor.execute('create table sat(name text(15),phone text(20),addr text)')
#테이블 레코드 추가
cursor.execute("insert into sat(name,phone,addr) values('홍길동','010-111-222','서울시')")
cursor.execute("insert into sat(name,phone,addr) values('유관숨','010-111-222','강릉시')")
conn.commit()
#테이블 조회
cursor.execute('select *from sat')
for data in cursor.fetchall():
    print(data)

#object close
cursor.close() ;conn.close() #conn이 마지막이어야함, 인터넷 선 끊는 느낌?ㅋㅋ















