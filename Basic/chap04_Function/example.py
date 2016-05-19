'''
문) 중첩함수를 적용하여 은행계좌 함수를 정의하시오.
 <조건1> outer 함수 : bank_account() -> balance(잔액) 초기화, Inner함수 포함
 <조건2> inner 함수 : getBalance() -> 잔액보기 : balance 리턴
                    deposit() -> 입금하기 : balance += money
                    withdraw() -> 출금하기 : balance -= money
 <조건3> 예외처리 : 출금액이 잔액보다 많은 경우 '잔액이 부족합니다.' 메시지 출력
 <조건4> 기타 나머지는 출력 예시 참조
'''

def bank_account(initial_balance) :
    balance = initial_balance
    def getBalance():     # 잔액보기 
        return balance
    def deposit(money) :  # 입금하기 
        nonlocal balance  # Outer 함수 변수 사용 
        balance = balance + money
        return balance
    def withdraw(money) : # 출금하기 
        nonlocal balance
        if(balance < money) : # 예외처리 
            print('잔액이 부족합니다.')
        else :
            balance = balance - money
        return balance
    return getBalance, deposit, withdraw # Inner 함수 리턴 

# getBalance, deposit, withdraw 함수 객체를 g, d, w로 받음
b = int(input('최초 계좌의 잔액을 입력하세요 : '))

g, d, w = bank_account(b) # 100- 잔액 초기값
print('현재 계좌 잔액은 {}원 입니다.'.format(g())) 
i = int(input('입금액을 입력하세요 : '))
print('{0}원 입금후 잔액은 {1}원 입니다.'.format(i, d(i))) 
o = int(input('출금액을 입력하세요 : ')) 
print('%d원 출금후 잔액은 %d원 입니다.'%(o, w(o))) 
