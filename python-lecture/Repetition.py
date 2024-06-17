# for 문 List
list = ['a', 'hello', 123, 3.14]

for i in list:
    print(i)
print('end')

# for 문 tuple
tuple = ('A', 'HELLO', 456, 0.333)
for i in tuple:
    print(i)

# 딕셔너리
dic = {'홍길동': 20, '홍길자': 30, '홍길순': 40}
for i in dic:
    print('{0}의 나이{1}'.format(i, dic[i]))

# range 이용한 반복문 처리
for i in range(1, 10, 2):
    print(i)

# range 이용한 구구단 처리
for i in range(1, 10, 1):
    print('{0} * {1} = {2}'.format(6, i, (6 * i)))

# while 문 이용한 정수합
count = 0
target = 100
sum = 0
while count <= 100:
    sum = sum + count
    count = count + 1

print('0부터 {}까지의 합: {}'.format(target, sum))

# continue
for i in range(10):
    if (i % 2) == 0:
        continue
    print(i)

# break
for i in range(10):
    if i > 5:
        break
    print(i)




