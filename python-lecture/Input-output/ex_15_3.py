# 파이썬은 읽고, 쓰기 위한 편리한 함수를 제공한다.
from typing import List

# 닫을 필요가 없음 with ~ as
with open('/Users/imchaeseong/Documents/python/python_study/python-lecture/Input-output/textFile.txt', 'r') as f:
    print('f.read() : {0}'.format(f.read()))

# 리스트 문자열 쓰기 f.writelines()
ts = ['hello python\n', 'hello c++\n', 'hello java\n']
with open('/Users/imchaeseong/Documents/python/python_study/python-lecture/Input-output/textLine.txt', 'w') as f:
    # for tl in ts:
    #     f.write(tl)
    f.writelines(ts)

# 모든 문자열 읽기 f.readlines()
# with open('/Users/imchaeseong/Documents/python/python_study/python-lecture/Input-output/textLine.txt', 'r') as f:
# ls = f.readlines()
# print('type(ls) : {0}'.format((type(ls))))
#
# l = ''
# for l in ls:
#     print(l, end='')

# 행단위로 문자열 읽기 f.readline()
# with open('/Users/imchaeseong/Documents/python/python_study/python-lecture/Input-output/textLine.txt', 'r') as f:
# r = f.readline()
# print('type(r) : {0}'.format((type(r))))
#
# while r != '':
#     print(r, end='')
#     r = f.readline()