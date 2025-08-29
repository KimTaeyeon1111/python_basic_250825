# mod1.py
def add(a, b):
    return a+b
def sub(a,b):
    return a-b

if __name__ == "__main__":
    print(add(1, 4))
    print(sub(4, 2))














# terminal 입력
# module 폴더로 이동 - cd module
# 파이썬 실헹 - python (파이썬 환경으로 들어감)
# mod1 함수 불러오기 - import mod1
# import sys - 시스템 관련 정보 불러오기
# sys.path - 시스템 패스 경로에 있는 파일 불러오기/ 확인하기
# sys.path.append('파일 경로') - 패스에 파일 입력하기 (경로 중 \에 하나를 더 붙여 \ 하나 문자로 인식하도록 하기)