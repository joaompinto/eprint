from optparse import OptionParser
from .version import version


def arg_parser():
    parser = OptionParser(usage, version=version)
    (options, args) = parser.parse_args()
    if len(args) != 1:
        parser.error("incorrect number of arguments")
    return (options, args)
