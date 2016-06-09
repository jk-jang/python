'''
파일 입출력 
'''

import pandas as pd # 별칭 

# 1. read.csv() 
emp_df = pd.read_csv('emp.csv') # 경로 생략
print(emp_df.info()) # 파일 정보 - str() 비슷한 역할 
print(emp_df)

# 구분자 지정 파일 가져오기 
emp_df = pd.read_csv('emp.csv', sep=',')
print(emp_df)

# 칼럼명이 없는 파일 가져오기
student_df = pd.read_csv('student.csv', header=None)
print(student_df) #  default : 0     1    2   3

# 칼럼명을 지정하여 파일 가져오기
student_df = pd.read_csv('student.csv', names=['sid','name','height','weight'] )
print(student_df)

name=['sid','name','height','weight']
student_df = pd.read_csv('student.csv', names=name )
print(student_df)

# 특정 행만 읽어오기 
line_skip_df = pd.read_csv('line_skip.csv', skiprows=[0,2,3])
print(line_skip_df)


# 2. read_table() 
# 공백이나 특수문자로 구분 칼럼의 파일을 가져올 때 사용하는 함수
student_txt = pd.read_table('student.txt', sep='\s+', header=None)
print(student_txt) #  0     1    2   3
# sep='\s+' : 2개 이상의 공백으로 구분된 칼럼 의미

# 칼럼명이 있는 텍스트 파일 가져오기
student2_txt = pd.read_table('student2.txt', sep='\s+') 
print(student2_txt)
    
# 특수문자를 NaN -> NA
conv = {'키':['-','$'],'몸무게':'-'} # dict 형식 
# 키 or 몸무게 칼럼에 '-' -> NaN
data = pd.read_table('student2.txt', sep='\s+', na_values=conv)
print(data)

# 데이터를 조금씩 가져오기
data = pd.read_table('data.csv', sep=',')
print(data.info()) # 파일 정보 
print(data)

data2 = pd.read_table('data.csv', nrows=100, sep=',')
print(data2)

# 3. 데이터를 파일에 저장하기 
data2.to_csv('data2_test.csv') # 행 번호 저장
data2.to_csv('data2_out.csv', index= False) # 행 번호 저장 안함 

# 파일 저장 전에 콘솔 출력 
import sys # 모듈 추가 
data2.to_csv(sys.stdout, index=False) 
data2.to_csv(sys.stdout, index=False, na_rep='NaN') # NA
data2.to_csv('data2_out2.csv', index=False, na_rep='NaN') # NA

# 특정 칼럼명 대상으로 저장 -> 순서 변경 
data2.to_csv('data2_out3.csv', index=False, na_rep='NaN',columns=['E','C','A'])

data2_out3 = pd.read_csv('data2_out3.csv')
print(data2_out3)














