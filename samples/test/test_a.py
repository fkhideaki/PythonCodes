'''
# python unittestのサンプル

## 準備
- VSCodeのコマンドで  
  Python: Configure Test  
  と実行。
- ガイドに従ってテストに使うファイルの条件を指定する

## テストの記述
- このサンプルの通り

## テストの実行
- テストビューの実行ボタンを押す
'''

import unittest

def add(a: int, b: int) -> int:
    '''
    テスト用関数
    値が10以上になると間違える
    '''
    return (a + b) % 10

class TestGroup1(unittest.TestCase):
    def test_1(self):
        self.assertEqual(add(2, 3), 5)
    def test_2(self):
        self.assertEqual(add(12, 4), 16)
    def test_3(self):
        self.assertEqual(add(2, 4), 6)
    def test_4(self):
        self.assertEqual(add(12, 3), 15)
