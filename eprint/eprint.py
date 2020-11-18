from colored import fg, attr
from enum import Enum, auto

RESET = attr('reset')


class MsgClass(Enum):
    PLAIN = auto()
    OK = auto()
    ERROR = auto()


COLOR_MAP = {
    MsgClass.PLAIN : fg("white"),
    MsgClass.OK : fg("green"),
    MsgClass.ERROR : fg("red")
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

    @staticmethod
    def ok(*args, **kwargs):
        eprint.raw(MsgClass.OK, *args, **kwargs)

    @staticmethod
    def error(*args, **kwargs):
        eprint.raw(MsgClass.ERROR, *args, **kwargs)
