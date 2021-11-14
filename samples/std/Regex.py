
import re

def test1():
    m = re.search('(....)/(..)/(..)', '2021/11/22')
    print(m.group(1))
    print(m.group(2))
    print(m.group(3))

test1()
