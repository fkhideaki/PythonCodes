from dataclasses import dataclass
import sys

from .Utils import Indent

@dataclass
class ArgVal:
    cmd: str
    arg: str

class Args:
    def __init__(self):
        self.opt: list[ArgVal] = []
        self.std: list[str] = []

    @classmethod
    def getStd(cls):
        a = Args()
        a.parse(sys.argv[1:])
        return a

    def parse(self, argv: list[str]):
        opt = []
        std = []
        for a in argv:
            if a.startswith('--'):
                aa = a[2:]
                c = aa.split(':')[0]
                a = aa[len(c) + 1:]
                opt.append(ArgVal(c, a))
            else:
                std.append(a)
        self.opt = opt
        self.std = std

    def getOpt(self, opt) -> ArgVal:
        for a in self.opt:
            if a.cmd == opt:
                return a
        return None

    def hasOpt(self, opt):
        return self.getOpt(opt) is not None

    def printArgs(self):
        indent = Indent()

        indent.output('Options:')
        with indent:
            if not self.opt:
                print('Empty')
            for s in self.opt:
                a = s.arg if s.arg else '#NO_PARAM#'
                indent.output(f'{s.cmd} : {a}')

        indent.output('Args:')
        with indent:
            if not self.std:
                print('Empty')
            for s in self.std:
                indent.output(s)
