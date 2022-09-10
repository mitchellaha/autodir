import os
from helpers.directory_maker import create_directory_if_not_exist


def create_URL_string(Link, IconPath):
    """
    Creates an Internet URL Shortcut File (.url)
    """
    returnString = f"[InternetShortcut]\nURL={Link}\nIconIndex=0\nIconFile={IconPath}\n"
    return returnString


def create_shortcut(Link, Filename, IconPath, Directory = None):
    fileName = f"{Filename}.url"
    filePath = os.path.join(Directory, fileName)

    create_directory_if_not_exist(os.path.dirname(filePath))

    with open(filePath, "w") as f:
        f.write(create_URL_string(Link, IconPath))
        f.close()
