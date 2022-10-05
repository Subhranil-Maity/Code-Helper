import json
import os.path
import sys

__version__ = "0.0.1"

storagePath = "C:\\Code-Helper"
defaultConfig = {

}


def doesStorgeExists() -> bool:
    """
    check if storge exists
    :return: existence of storage directory
    """
    return os.path.isdir(storagePath)


def TemplatesPath() -> str:
    """
    returns path to Templates
    """
    return storagePath + "\\templates"


def helpCom() -> None:
    """
    Shows help Message
    """
    print(f"Code-Helper {__version__}")
    print()
    print("Commands: ")
    for command in commands:
        print(command['name'] + "\t" + command['dec'])


def gotoCom() -> None: pass


# Contains data o all the commands and its working
commands = [
    {
        "name": "help",
        "dec": "Shows all the usable commands",
        "com": helpCom
    },
    {
        "name": "version",
        "dec": "Shows Version",
        "com": lambda: print(__version__)
    },
    {
        "name": "goto",
        "dec": "Brings you to a predefined workspace",
        "com": gotoCom
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
    """
    returns the command info or just error
    :param com: command
    :return: command's info
    """
    for command in commands:
        if com == command['name']: return command
    return {
        "com": lambda: showError(2, com)
    }


def genStorage() -> None:
    """
    generates Storage
    """
    os.mkdir(storagePath)
    os.mkdir(TemplatesPath())
    with open(storagePath + "\\Config.json", "w") as config:
        config.write(json.dumps(defaultConfig))


def sCheck() -> None:
    """
    check the storage
    """
    if not doesStorgeExists(): genStorage()


def app():
    sCheck()
    argc = len(sys.argv)
    argv = sys.argv
    # print(argc, argv)
    if not argc >= 2: showError(1)
    runCom(argv[1])['com']()
