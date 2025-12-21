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
