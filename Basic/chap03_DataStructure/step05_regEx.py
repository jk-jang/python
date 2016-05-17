'''
Created on 2016. 5. 17.

정규 표현식
메타문자 : . ^ $ * + ? { } [ ] \ | ( )
^x : 문자열이 x로 시작
x$ : 문자열이 x로 끝남
x. : x가 마지막으로 끝남
x* : x가 0번 이상 반복
x+ : x가 1개 이상 반복
x? : x가 0 또는 1개 존재
{m,n} : m~n 사이 매치 
{m,} : m 이상 매치
{,n} : n 이하 매치
[] : 한개 문자와 매치  
'''
import re
#정규표현식 모듈
ss = '1234 abc가나다ABC_553_6'
#re.findall-> list 타입으로 리턴
print(re.findall('[0-9]{1,}', ss))

print(re.findall('\d{3,}', ss)) #['1234', '553']
print(re.findall('\w{5,}', ss)) #['abc가나다ABC_553_6']
print(re.findall('[0-9]+', ss))
print(re.findall('[0-9]{2,4}', ss)) #2~4자리 숫자 출력

ss2 = 'test 1abcABC 123mbc 45tset'
print(re.findall('.bc', ss2))#끝이 bc로 끝나는 문자 출력
print(re.findall('[^t]+', ss2))#t 제외 시키고 뽑아 줘

#주민번호 양식
sid = '900721-2899251'
print(re.findall('\d{6}-[2]\d{6}', sid))

#이메일 양식
email = 'honggildont@naver.com'
print(re.findall('\w{2,}@\w{3,}.\w{2,}', email))
#잘못된 이메일 양식 - 숫자가 젤 앞에 있는 경우
email2 = '123honggildont@naver.com'
print(re.findall('[a-z]+@\w{3,}.\w{2,}', email2))

if re.findall('[a-z]+@\w{3,}.\w{2,}', email2) != email2:
    print('이메일양식 이상함')
else:
    print('이메일양식 올바름')