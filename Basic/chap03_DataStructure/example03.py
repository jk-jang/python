'''
문3) 다음과 같은 여러 줄의 문자열을 대상으로 정규표현식을
적용하여 email 양식이 올바른 것만 출력되도록 하시오.
'''
email = """hong@12.com
you@naver.com
12kang@hanmail.net
kimjs@gmail.com
"""
import re
result_email = [] # 정상 email 저장 list
for e1 in email.split('\n') : 
    print(e1)
    e2 = re.findall('[a-z]{2,}@\w{3,}.\w{2,}', e1) 
    # e2 길이가 1이상 이고, 원본과 동일한 경우 
    if len(e2) >= 1 and e1 == e2[0]: 
        result_email.append(e1) # list에 원본 추가 

print('='*25)                 
for r in result_email :
    print(r)



    