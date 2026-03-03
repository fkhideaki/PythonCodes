'''
コンソールとファイルの両方に出力するためのサンプルコード
'''

import sys
from contextlib import contextmanager, redirect_stdout

class PrinterTee:
    def __init__(self, *files):
        self.files = files
    def write(self, data):
        for f in self.files:
            f.write(data)
    def flush(self):
        for f in self.files:
            f.flush()

@contextmanager
def begin_log_print(filepath, encoding="utf-8"):
    with open(filepath, "w", encoding=encoding) as f:
        with redirect_stdout(PrinterTee(sys.stdout, f)):
            yield

def main():
    with begin_log_print('logfile.txt'):
        print('test')
    input()

if __name__ == '__main__':
    main()
