'''
서울시를 대상으로 전체 동의 개수 파악하기

'''
'''
우편번호 찾기
'''
import os
try:
    files = open(os.getcwd()+r'\zipcode.txt', mode='r')        
    # files에서 첫줄만 읽기
    line = files.readline()     
    dong = [] # 서울 지역인 동 저장 
    while line : # 검색된 data가 있으면 반복 
        lines = line.split('\t')
        if lines[1] == '서울' :
            dong.append(lines[3]) # 서울 지역 동 저장 
            line = files.readline() # '서울' 있으면 다음줄 읽기
        else :
            break # 서울 지역이 없으면 반복 탈출    

    # 중복 데이터 제거 
    # list -> set 변경(중복 data 제거) -> list 변경 
    sdong = set(dong)
    ldong = list(sdong)
    cnt = len(ldong) # list 길이 -> 동 개수
    print('서울 지역 전체 동 개수 = %d'%cnt)

    # 10개 단위로 출력 - for문
    i = 1
    for d in ldong :
        if i%10 == 0 :
            print(d) # 줄 변경 후 출력
        else :
            print(d, end=' ') # 동일 줄 출력 
        i += 1
                   
except FileNotFoundError as err:
    print('해당 파일이 없습니다.')
finally: 
    files.close() 



