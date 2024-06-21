class ParantCls:
    def __init__(self):
        pass
    def printMethod(self):
        print('Hello Python')

class ChildCls(ParantCls):
    def __init__(self):
        pass

chilcls = ChildCls()
chilcls.printMethod()

# 다중 상속
class ParentCls1:
    def __init__(self):
        pass
    def clsMethod1(self):
        print('clsMethod')

class ParentCls2:
    def __init__(self):
        pass
    def clsMethod2(self):
        print('clsMethod2')

class ParentCls3:
    def __init__(self):
        pass
    def clsMethod3(self):
        print('clsMethod3')

class ChildCls(ParentCls1, ParentCls2, ParentCls3):
    def __init__(self):
        pass

chilcls = ChildCls()
chilcls.clsMethod1()
chilcls.clsMethod2()
chilcls.clsMethod3()