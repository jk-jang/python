'''
문1) word counter
   - 여러줄의 문장을 단어로 분류하고, 단어 수 출력하기
'''

multiline="""안녕하세오. Python 세계로 오신걸
환영합니다.
파이션은 비단뱀 처럼 매력적인 언어입니다."""

# 공백 문자를 기준으로 단어수 카운터 
cnt = 0
word_result = [] # 빈 list : 줄 단위 저장
word  = [] # 빈 list : 줄 단위에서 단어 저장   
for line in multiline.split("\n"):   
    word_result.append(line) # 줄 단위 문장을 빈 list에 추가    
    for w in line.split(" "): # 공백으로 분리
        word.append(w) 
        print(w)
        cnt += 1  
print('단어수 :',cnt) # 단어수 출력 
print(word_result) # 줄 단위 문장 출력
print(word) # 줄 단위 단어 출력


'''
안녕하세오.
Python
세계로
오신걸
환영합니다.
파이션은
비단뱀
처럼
매력적인
언어입니다.
단어수 : 10
'''