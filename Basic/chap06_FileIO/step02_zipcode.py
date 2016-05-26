'''
Created on 2016. 5. 25.

우편번호 찾기
'''
import os #모듈추가 - 운영체제

try:
    files = open(os.getcwd()+'\\zipcode.txt',mode='r') 
    dong = input('검색할 동을 입력해:')
    #files에서 첫줄 만 읽기
    line = files.readline()
    #print(line)
    
    while line: #<-검색된 데이터가 있으면 반복
        lines = line.split('\t')
        if lines[3].startswith(dong): #4번째컬럼에 동이 있음,첫 문자랑 dong이랑 비교
            #[우편번호] 시 구 동 세부주소 일케 출력해보자
            print('['+ lines[0]+']'+''+lines[1]+' '+\
                  lines[2] +' ' +lines[3] + ' '+lines[4])
        line = files.readline() 
            
except FileNotFoundError as err:
    print('해당파일이 없어')
finally:
    files.close()