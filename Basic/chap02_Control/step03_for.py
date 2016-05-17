'''
Created on 2016. 5. 13.
반복문(for)
    형식)
    for 변수 in python자료구조:
        실행문
'''
#list 이용
lidata=[3,2,3]
for i in lidata:
    print(i)
     
strdata=['d','c','a']
for s in strdata:
    print(s)

#tuple
data_tu = (1,2,3,4)
for i in data_tu: 
    print(i)

#set
datas ={'a','b','c'}
for i in datas:
    print(i)

#dict
soft={'java': '객제치향언어','python' : '만능언어','sql':'DB처리'}
print(soft.items())
#.items -> 리스트 타입으로 저장됨

for i in soft.items():
    print(i[0],'-->',i[1])

print(soft.keys())

for k in soft.keys():
    print(k,end=' ')

print()

print(soft.values())
for v in soft.values():
    print(v, end=' ')

#다중 for문 이용 구구단
print('\n구구단 출력2,3단')
for i in [2,3]:
    print('---{}단---'.format(i))
    for j in range(1,10): #range(시작:종료전)의 정수값 생성
    #for j in [1,2,3,4,5,6,7,8,9]:
        print('{0}*{1}={2}'.format(i,j,i*j))

#continue, break 사용
for i in range(1,7):
    if i == 2 : continue
    if i == 6 : break
    print(i, end = ' ')

#정규표현식
import re
# 형식 re.match('정규표현식', 문자열) -> True/False

for s in ['02-1234','전화번호','222-8541']:
    if re.match('\\d{2,}-\\d{4}$',s):
        print('전화번호입니다')
    else:
        print('전화번호 아냐')

#list 내포!
#[for 변수 in 자료구조]
price = {'사과': 1000, '배':2000, '바나나': 500}
buy = {'사과':5, '바나나':1}

bill = [price[i] * buy[i] for i in buy] #뒤에 먼저 해석, for 문 앞을 해석
#buy의 키값을 i로 넘겨준 후, price, buy i 
#--> 리스트 객체로 넘겨줌
#[1000*5, 500*1]
print('내가 구매한 상품 총 금액',sum(bill))

print('\nlist 내포 형식2')
li1=[3.5,4.5]
li2=[1,2,3]

for i in li1:
    for j in li2:
        re=i+j
        print(re,end=' ')

print('\n내포 형식2다른 방법')
re= [ i+j for i in li1 for j in li2]
print(re)

'''
range(n)함수
    - n 범위 내의 정수를 생성하는 함수
range(n1 ~ n2)
range(n1 ~ n2,n)2씩 증가
'''
print('range(5):',list(range(5)))
print('range(1,5):',list(range(1,5)))
print('range(-5,5):',list(range(-5,5)))
print('range(-5,5):',list(range(-5,5,2)))#2씩 증가

l=[2,1,8,4,5]
l.sort() #오름차순
print(l)
l.sort(reverse = True) #내림차순
print(l)
































