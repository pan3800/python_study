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