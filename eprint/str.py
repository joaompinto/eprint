from .eprint import COLOR_MAP, MsgClass, RESET
from functools import partial


def raw(msg_class: MsgClass, *args, **kwargs):
    color = COLOR_MAP[msg_class]
    if len(args) == 1:
        msg = color + args[0] + RESET
    else:
        colored_args = [color + str(x) + RESET for x in args[1:]]
        msg = args[0].format(*colored_args)
    return msg


error = partial(raw, MsgClass.ERROR)
info = partial(raw, MsgClass.INFO)
ok = partial(raw, MsgClass.OK)
