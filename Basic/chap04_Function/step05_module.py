'''
Created on 2016. 5. 18.
기존에 생성된 모듈 부착하기
방법1)import 패키지명.모듈명
방법2)from 패키지명.모듈명 import 함수명, 함수명,...
'''
#형식1)
from exe.step05_mymodule1 import ListAll
from exe import step05_mymodule2

list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
print(list1,list2)
#->[1, 2, 3, 4, 5] ['a', 'b', 'c', 'd', 'e']
ListAll(list1,list2)
#->([1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e'])

#형식2)
from exe.step05_mymodule2 import *
x= 10
y= 20
print('덧셈=', ADD(10 , 20))

#형식3)
import exe.step05_mymodule2
print(step05_mymodule2.DIV(10, 5))



























































