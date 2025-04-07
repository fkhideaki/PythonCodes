import os

def indexToStr(idx, len):
    return ('0' * len + str(idx))[-len:]

def dirp(obj):
    """非公開をメンバ一覧"""
    a = []
    for s in dir(obj):
        if s.startswith('__'): continue
        if s.endswith('__'): continue
        a.append(s)
    return a
