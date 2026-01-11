class Indent:
    def __init__(self, indent_str="  "):
        self.level = 0
        self.indent_str = indent_str

    def output(self, text):
        print(self.toStr() + text)
    
    def __enter__(self):
        self.level += 1
        return self
    
    def __exit__(self, *args):
        self.level -= 1

    def toStr(self):
        return self.indent_str * self.level


def printDir(
    obj,
    printValue=False,
    printDef=False,
    printPydoc=False,
    printFunctionArgs=False):
    for s in dir(obj):
        if s.startswith('__'):
            continue
        attr = getattr(obj, s)
        print(s + ' :')
        if printValue:
            print(f'  Val : {repr(attr)}')
        if printDef:
            print(f'  Def : {repr(type(attr))}')
        if printPydoc and attr.__doc__:
            print("  Doc: " + attr.__doc__.strip().replace('\n', '\n         '))
        if printFunctionArgs and callable(attr):
            import inspect
            sig = str(inspect.signature(attr))
            print("  Args: " + sig)
