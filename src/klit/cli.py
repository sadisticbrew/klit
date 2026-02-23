import argparse  # for passing the commands directly through cli
import sys


def handle_ignite(args: argparse.Namespace):  # Equivalent to git init
    print("Igniting the den...")


def handle_touch(args: argparse.Namespace):  # Equivalent to git add
    print("Touching files...")


def handle_climax(args: argparse.Namespace):  # Equivalent to git commit
    print("Reaching the climax...")


def build_parser() -> argparse.ArgumentParser:
    """Creates and returns the CLI parser."""
    parser = argparse.ArgumentParser(description="A wild git clone.")
    subparsers = parser.add_subparsers(title="Commands", dest="command", required=True)

    # Ignite
    p_ignite = subparsers.add_parser("ignite", help="The initialization of a den")
    p_ignite.set_defaults(func=handle_ignite)  # Map command to function

    # Touch
    p_touch = subparsers.add_parser("touch", help="Stage changes")
    p_touch.set_defaults(func=handle_touch)

    # Climax
    p_climax = subparsers.add_parser("climax", help="Save the state")
    p_climax.set_defaults(func=handle_climax)

    # Add the rest (tease, shove, yank) here

    return parser


def main(argv: list[str] | None = None):
    if argv is None:
        argv = sys.argv[1:]

    parser = build_parser()
    args = parser.parse_args(argv)

    # This is the use of the function we mapped earlier to the command. If the command/argument does not have the 'func' attribute then it will just print error message and exit. This uses the hasattr safety check already built into python.
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
