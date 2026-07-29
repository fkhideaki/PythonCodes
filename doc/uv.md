# macOS/Linuxへのインストール
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windowsへのインストール
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# キャッシュフォルダ指定
環境変数 UV_CACHE_DIR にフォルダを指定する
uv cache dir
で確認

# スタンドアロンスクリプトの実行
uv run example.py

# プロジェクトの作成と初期化
uv init my-project

# 依存関係を追加
uv add requests

# VSCodeでのテスト
- Python インタープリタの選択
  - Ctrl+Shift+P 
  - Python: Select Interpreter
  - .venv\Scripts\python.exe 

# チェックアウト操作
- git clone <URL>
- cd <プロジェクトフォルダ>
- uv sync

# 実行
uv run main.py
