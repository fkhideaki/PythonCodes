import os
from pathlib import Path
import subprocess
import venv

class VenvManager:
    def __init__(self, venv_dir=".venv"):
        self.venv_dir = Path(venv_dir)
        self.venv_python = self.get_venv_python(venv_dir)

    def get_venv_python(self, venv_dir):
        if os.name == "nt":  # Windows
            return Path(venv_dir) / "Scripts/python.exe"
        else:  # macOS/Linux
            return Path(venv_dir) / "bin/python"

    def ensure_venv(self):
        if not self.venv_python.exists():
            venv.create(self.venv_dir, with_pip=True)

    def exec_pip(self, args):
        subprocess.run(
            [self.venv_python, "-m", "pip"] + args,
            check=True
        )

    def install_package(self, package_name):
        self.exec_pip(["install", package_name])

    def install_requirements(self, requirements_file="requirements.txt"):
        self.exec_pip(["install", "-r", requirements_file])
    
    def upgrade_pip(self):
        self.exec_pip(["install", "--upgrade", "pip"])
