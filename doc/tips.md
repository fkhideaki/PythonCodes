## 仮想環境
- 作成
  - python -m venv .venv
- 仮想環境への切り替え
  - .venv\Scripts\activate.bat

## パッケージ
- インストール済みパッケージ確認
  - pip freeze
- パッケージ一括復元
  - pip freeze > libs.txt
  - pip install -r libs.txt
- パッケージ一括アンインストール
  - pip freeze > libs.txt
  - pip uninstall -y -r libs.txt

## Python Launcher
- インストールされているpython一覧を確認する
  - py --list
- 規定バージョンでpythonを実行
  - py t.py
- 特定のバージョンでpythonを実行
  - py -3.9 t.py
- デフォルトバージョンを指定する
  - set PY_PYTHON=3.9
- pipを使用する
  - py -m pip install xxxx
- 使用されたpythonを確認するコード
  ```
  import sys
  print(sys.executable)
  ```
