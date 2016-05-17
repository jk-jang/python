'''
Created on 2016. 5. 16.

Tuple 자료구조
    - 1차원 배열 구조
    형식) 변수 = (값1, 값2,...)
    - index 이용가능
    - 값 수정이 불가--> 읽기 전용!!--> list보다 속도 빠름!!
'''

#Tuple 생성
t= 1,2,3,4 #or t = (1,2,3,4) 
print(t)
print(t[0])
print('t길이:',len(t))

#Tuple 수정
#t[2]=300 #오류 발생
#--> list로 형변환 --> 수정 --> tuple로 형변환

tt= t *2
print(tt)

ltt=list(tt) #리스트형 변환
print(ltt)
ltt[3]=400 #수정
print(ltt)
ltt2=tuple(ltt)
print(ltt2)

#tuple과 변수
tt3 = 10, 20
print(tt3)
a,b=tt3
print(a,b)
a,b = b, a 
print(a,b)

print('\nurl을 tuple로 처리')
#from + 패키지명.모듈명 import+함수, 함수
from urllib.parse import urlparse,urlunparse
#모든 함수를 다 쓰겠다: * ,메모리에 올라가기 때문에 비권장
#from urllib.parse import *

url='www.naver.com/index.html?id=hong'
print(url)
url_info=urlparse(url) #url -> tuple형 리턴
print(url_info)

#파싱 결과를 사용
print(url_info.query) #id=hong

#파싱 이전 상태로 리턴
url_info2 = urlunparse(url_info)
print(url_info2)




























