import os
import re
from .shortcut_maker import create_shortcut


def normaize_directory(DirPath, ReplaceWith = "-"):
    """Removed Illegal Characters from the Pathstring/Filename"""
    # TODO: This Doesnt Work and will need to be accounted for.
    return os.path.normpath(re.sub(r'[\\/:"*?<>|]+', ReplaceWith, DirPath))


def create_directory_if_not_exist(Directory):
    """Creates a Directory if it Doesnt Exist"""
    CHECK_FOLDER = os.path.isdir(Directory)
    # If folder doesn't exist, then create it.
    if not CHECK_FOLDER:
        os.makedirs(Directory)


def create_directory_from_tree(DictTree, RootFolder, Path = str()):
    """Recursively Iterates over the Provided BlockTree Structure Creating Folders and Files Defined"""
    def dict_to_dir(DictTree, RootFolder, Path = str()):
        currentRoot = os.path.join(RootFolder, Path)

        if isinstance(DictTree, dict):
            if DictTree["Type"] == "Folder":
                currentRoot = os.path.join(currentRoot, DictTree["Name"])
                create_directory_if_not_exist(currentRoot)
                if isinstance(DictTree["Subfolders"], list):
                        for each in DictTree["Subfolders"]:
                            dict_to_dir(each, RootFolder, Path=currentRoot)

            if DictTree["Type"] == "Shortcut":
                create_directory_if_not_exist(currentRoot)
                create_shortcut(
                    Link=DictTree["Config"]["Link"],
                    Filename="Test",
                    IconPath=DictTree["Config"]["IconPath"],
                    Directory=currentRoot
                )

        elif isinstance(DictTree, list):
            for i in DictTree:
                dict_to_dir(i, RootFolder, Path=currentRoot)
    dict_to_dir(DictTree, RootFolder, Path)
