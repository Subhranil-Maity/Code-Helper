import os
import sys

__version__ = "0.0.1"


def helpCom() -> None:
    """
    Shows help Message
    """
    print(f"Code-Helper {__version__}")
    print()
    print("Commands: ")
    for command in commands:
        print(command['name'] + "\t" + command['dec'])


# Contains data o all the commands and its working
commands = [
    {
        "name": "help",
        "dec": "Shows all the usable commands",
        "com": helpCom
    }
]

def showError(eCode: int, args: list = None) -> None:
    """
    Simple function to show error message and exit if necessary
    :param eCode: Error Code
    :param args: the args to show proper exit message
    """
    if args is None: args = []
    # eCode Check
    if eCode == 1: print("No Arguments passed")
    if eCode == 2: print(f"The Command Does not exists: {args[1]}")
    # Terminates if necessary
    exit(eCode)


def runCom(com) -> dict:
    for command in commands:
        if com[1] == command['name']: return command
    return {
        "com": lambda: showError(2, com)
    }


def app():
    argc = len(sys.argv)
    argv = sys.argv
    # print(argc, argv)
    if not argc >= 2: showError(1)
    runCom(argv)['com']()
