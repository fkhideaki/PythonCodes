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
