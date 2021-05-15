from colored import fg, attr
from enum import Enum, auto
from functools import partialmethod

RESET = attr('reset')


class MsgClass(Enum):
    PLAIN = auto()
    OK = auto()
    ERROR = auto()
    INFO = auto()


COLOR_MAP = {
    MsgClass.PLAIN : fg("white"),
    MsgClass.OK : fg("green"),
    MsgClass.ERROR : fg("red"),
    MsgClass.INFO : fg("cyan")
}


class eprint:

    def __init__(self, *args, **kwargs):
        eprint.raw(MsgClass.PLAIN, *args, **kwargs)

    @staticmethod
    def raw(msg_class: MsgClass, *args, **kwargs):
        color = COLOR_MAP[msg_class]
        if len(args) == 1:
            msg = color + args[0] + RESET
        else:
            colored_args = [color + str(x) + RESET for x in args[1:]]
            msg = args[0].format(*colored_args)
        print(msg)

    error = partialmethod(raw, MsgClass.ERROR)
    info = partialmethod(raw, MsgClass.INFO)
    ok = partialmethod(raw, MsgClass.OK)
