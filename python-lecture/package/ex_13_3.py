# module 탐색 경로
import sys

for path in sys.path:
    print(path)

# module
from userPackage import calculator

result = calculator.add(3, 10)
print('result : {0}'.format(result))

result = calculator.sub(3, 10)
print('result : {0}'.format(result))
