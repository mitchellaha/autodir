import os
import re
from config import IGNORED_DIRECTORIES


def normaize_directory(DirPath, ReplaceWith = "-"):
    return os.path.normpath(re.sub(r'[\\/:"*?<>|]+', ReplaceWith, DirPath))


def create_directory_if_not_exist(Directory):
    CHECK_FOLDER = os.path.isdir(Directory)
    # If folder doesn't exist, then create it.
    if not CHECK_FOLDER:
        os.makedirs(Directory)


def folder_or_file(Value:str, Type:str):
    if Type == "Folder":
        currentRoot = os.path.join(currentRoot, Value)
        return currentRoot
    if Type == "Shortcut":
        ...
        # create_shortcut()


def create_directory_list(DictTree, RootFolder, Path = str()):
    folders = []

    def dict_to_dir(DictTree, RootFolder, Path = str()):
        currentRoot = os.path.join(RootFolder, Path)

        if isinstance(DictTree, dict):
            if DictTree["Type"] == "Folder":
                currentRoot = os.path.join(currentRoot, DictTree["Name"])
                create_directory_if_not_exist(currentRoot)
                if isinstance(DictTree["Subfolders"], list):
                        for each in DictTree["Subfolders"]:
                            dict_to_dir(each, RootFolder, Path=currentRoot)

            # TODO: PUT OTHER CHECKS HERE ... if DictTree["Type"] == "Shortcut":


        elif isinstance(DictTree, list):
            for i in DictTree:
                dict_to_dir(i, RootFolder, Path=currentRoot)


    dict_to_dir(DictTree, RootFolder, Path)
    return folders


# ? THIS ISNT BEING USED FOR ANYTHING???
# # # # def create_subdir_list(DictTree, Path = str()):  # ! This Is a Really ugly way to do this but it works for now. Please Do Better Recursion Later
# # # #     folders = []

# # # #     def dict_to_dir(DictTree, Path = str()):
# # # #         currentRoot = os.path.join("\\", Path)
# # # #         if isinstance(DictTree, dict):
# # # #             for key, value in DictTree.items():
# # # #                 if isinstance(value, list):
# # # #                     for each in value:
# # # #                         dict_to_dir(each, currentRoot)
# # # #                 if isinstance(value, str):
# # # #                     currentRoot = os.path.join(currentRoot, value)
# # # #                     folders.append(currentRoot)
# # # #         elif isinstance(DictTree, list):
# # # #             for i in DictTree:
# # # #                 dict_to_dir(i, currentRoot)

# # # #     dict_to_dir(DictTree, Path)
# # # #     return folders


def create_directory_from_tree(Root, Tree):
    dirList = create_directory_list(Tree, Root)
    for directory in dirList:
        if directory not in IGNORED_DIRECTORIES:
            create_directory_if_not_exist(directory)