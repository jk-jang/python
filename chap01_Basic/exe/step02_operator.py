'''
    - 산술, 논리, 관리 연산자
    - print 출력양식
    - escape 문자 처리
'''
v1 = v2 = v3 = 10
print(v1,v2,v3)
print('출력1',end=',') #줄 중복, 콤마로 구분
print(v1)

v1,v2=100,200
print(v1,v2)
v2,v1=v1,v2 #변수 교체(swap)
print(v1,v2)

print('변수 값을 할당(packing)')
v1,*v2=[1,2,3,4,5] #1차 배열 할당 *: v1를 제외 나머지 원소 할당
print(v1,v2) #1 [2, 3, 4, 5]
*v1,v2=[1,2,3,4,5] 
print(v1,v2) #[1, 2, 3, 4] 5

print('\nprint 출력양식') #or ""
'''
%s: 문자열 출력
%c: 문자 한개 출력
%d: 숫자 출력(정수)
%f: 숫자 출력(실수)
%o: 8진수 출력
%x: 16진수 출력
%%: %문자 출력
실수출력 


print('%1.4f' %123.1111)

'''

num1=10; num2=20
tot=num1+ num2

#형식1) '%출력양식문자'%(값1 or 변수, 값,..)
print('10 + 20 = %d'%tot) # 값1
print('%d+%d=%d'%(10,num2,tot))
print('실수 출력 : %5.2f'%1245.417) # %전체자리.소숫점f

#형식2) {index}.format(값)
print('나이는 {1}이고, 이름은 {0}이고, 나머지는{1}이다.'.format('홍길동',34)) 

print('\n\n연산자')
#산술연산자
print('산술연산자:',10+3,10-3,10*3,10/3,10//3,10%3, 10**3)#13 7 30 3.3333333333333335 3 1 1000

print(divmod(10, 3)) #몫3 나머지1 
#(3, 1) -> 파이썬에서 괄호()인 변수를 tuple type이라 함

print('\관계연산자')
print(5>2,5==3,5!=3,5<=3)

print('\논리연산자')
print(5>3 and 4<3, 5>3 or 4<3, not(5>=3))

#문자열 더하기(결합연산자)
print('대한민구'+'우리나라'+"만'홑따옴표'세")
print('만세'*10)

#카운터 변수: 변수에 일정값이 증가 또는 감소
var1=10
var1 = var1 +1
print(var1)
var1 += 1 #단축배정연산자
print(var1)

print('\nescape 문자')
#escape: 특수문자, 특수기능 문자들(ex:\n)
print('aa \nbb')
print('aa \tbb')#tab 키 
#escape 기능 차단
print(r'aa \nbb')
print('aa \\tbb')

#python에서 파일 경로
print(r'c:\aa\abc.txt')
print('c:\\aa\\abc.txt')
print('c:/aa/abc.txt')

print('\n여러 줄의 문자열 표현')
multilines='''안녕하세요
파이썬
쉑터풔큉
'''
print(multilines)

#DB에 쿼리문 작성 시 
query = '''create table test(
a varchar(20) primary key,
b varchar(20) not null,
c int
)'''

print(query)