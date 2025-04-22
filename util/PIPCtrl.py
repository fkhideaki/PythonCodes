import subprocess
import sys

class PIPCtrl:
    @classmethod
    def install(cls, package: str):
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

    @classmethod
    def installList(cls, packages: list[str]):
        for package in packages:
            cls.install(package)
