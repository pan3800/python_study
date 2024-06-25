# 파일 모드란? 파일을 다루는 방식 이다.
# open(파일 이름, 파일 열기 모드)
# r -> 읽기 전용
# w -> 쓰기 전용(이미 존재하면 덮어씌움)
# a -> 쓰기 전용(이미 존재하면 덧붙임)
f = open('/Users/imchaeseong/Documents/python/python_study/python-lecture/Input-output/textFile.txt', 'a')
f.write('hello test#n')
f.close()

# x -> 이미 존재하면 예외(IOError) 발생


