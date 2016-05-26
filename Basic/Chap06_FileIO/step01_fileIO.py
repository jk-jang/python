'''
Created on 2016. 5. 25.

파일 입출력
    - 파일 데이터 or DB 데이터 입출력 시 예외처리 필요
    형식)
    try:
        코드 작성
    except + 예외처리 클래스 as 변수: 
        예외처리 코드 작성
    finally:
        open 객체 닫기 - 무조건 실행되는 코드 
    형식) open('경로/파일명', mode=r/w/a, encoding='utf-8')
        mode = a: write + append
'''
import os #모듈추가 - 운영체제

print(os.getcwd())

try:
    ####object open
    f = open(os.getcwd()+r'\ftest1.txt',mode='r') 
    #<-escape문자 \ 로 인식못하게 앞에 r을 붙임
    print(f)
    #<- <_io.TextIOWrapper name='C:\\Pywork\\workspace(python)\\Chap06_FileIO\\exe\\ftest1.txt' mode='r' encoding='cp949'>
    #<-file object 정보만 출력됨
    print(f.read()) #참조변수.메서드()
    ####object close
    f.close()
    
    ####파일 출력 - 파일 자동 생성
    letter = open(os.getcwd()+r'\ftest2.txt',mode='w')
    letter.write('I am happy')#참조변수.write('데이터')
    letter.close() #open object오픈 객체 닫기
    
    ####파일 출력(내용 추가)
    letter2 = open(os.getcwd()+r'\ftest2.txt',mode='a')
    letter2.write('\nmy friend')#참조변수.write('데이터')
    letter2.close() #open object오픈 객체 닫기
    
    #ftest2.txt파일 읽어서 결과의 첫줄을 콘솔에 출력 
    f2 = open(os.getcwd()+r'\ftest2.txt',mode='r') 
    print('--'*10)
    print(f2.readline()) #첫 줄만 읽기
    f2.close()
    
    #readlines(): 줄 단위로 여러줄 읽기
    f4 = open(os.getcwd()+'\\ftest1.txt',mode='r')
    lines = f4.readlines() # ->리스트 타입으로 출력
    print(type(lines))
    print(lines)
    f4.close()
    '''
    문제)
    programming is fun
    ...
    computer
    요렇게 만들어봐
    '''
    lines_doc =[]
    for l in lines:
        for line in l.split('\n'): #\n기준으로 나눔
            if line !='':
                lines_doc.append(line)#줄 단위 문자 저장
    
    for line in lines_doc:
        print(line)
    
    #유니코드 데이터 입출력
    f5 = open(os.getcwd()+r'\ftest3.txt',mode='w',encoding='utf-8')
    f5.write('파이썬 데이터 입출력')
    f5.write('\n유니코드 데이터 입출력')
    f5.write('\n파일 입출력 끝')
    f5.close()
    
    #import sys
    #sys.stdout.writelines(lines)
    
    
    
except FileNotFoundError as err: #err:예외 정보 저장 변수
    print('해당 파일이 없습니다.',err)
finally: #바로 윗줄 예외랑 상관없이 무조건 실행됨
    print('무조건 실행 ~~')
    

























