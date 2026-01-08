## 仮想環境
- 作成
  - python -m venv .venv
- 仮想環境への切り替え
  - .venv\Scripts\activate.bat

## パッケージ
- インストール済みパッケージ確認
  - pip freeze
- パッケージ一括復元
  - pip freeze > requirements.txt
  - pip install -r requirements.txt
- パッケージ一括アンインストール
  - pip freeze > requirements.txt
  - pip uninstall -y -r requirements.txt
- 依存パッケージをスキャンする
  - pipreqs --encoding UTF8 .
    - ※完全にはスキャンされない

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
