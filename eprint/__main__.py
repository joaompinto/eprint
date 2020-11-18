from .project import Project
from .argparser import arg_parser


def main():
    options, args = arg_parser()
    project_dir = args[0]
    proj = Project(options.name, project_dir)
    proj.create(options.force)


if __name__ == "__main__":
    main()
