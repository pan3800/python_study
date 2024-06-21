# overriding
class ParentCls:
    def __init__(self):
        pass
    def cooking(self):
        print('make pizza')

class ChildCls(ParentCls):
    def __init__(self):
        pass

    def cooking(self):
        print('make pasta')

childCls = ChildCls()
childCls.cooking()