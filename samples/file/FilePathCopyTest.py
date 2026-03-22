'''
クリップボードからファイルパスを取得するサンプル。
エクスプローラでファイルを直接コピーしている場合はそのパス
テキストでパスをコピーしている場合はそれらをリストにしたものを返す
'''

import pyperclip
# pip install pywin32
import win32clipboard
import win32con

def getClipboardFilesExplorer():
    win32clipboard.OpenClipboard()
    try:
        if win32clipboard.IsClipboardFormatAvailable(win32con.CF_HDROP):
            data = win32clipboard.GetClipboardData(win32con.CF_HDROP)
            return list(data)
        else:
            return []
    finally:
        win32clipboard.CloseClipboard()

def getClipboardFiles():
    files = getClipboardFilesExplorer()
    if files:
        return files
    c = pyperclip.paste()
    files = c.splitlines()
    if files:
        v = []
        for s in files:
            if len(s) > 2 and s[0] == '"' and s[-1] == '"':
                s = s[1:-1]
            v.append(s)
        return v
    return None

def main():
    files = getClipboardFiles()
    for f in files:
        print(f)

if __name__ == "__main__":
    main()
