import os
import string

def create_directory_if_not_exist(Directory):
    CHECK_FOLDER = os.path.isdir(Directory)
    # If folder doesn't exist, then create it.
    if not CHECK_FOLDER:
        os.makedirs(Directory)


def create_lettered_folders(Directory = None):
    if Directory is not None:
        rootFolder = Directory
    else:
        rootFolder = os.getcwd()

    create_directory_if_not_exist(os.path.join(rootFolder, "#"))  # Create Directory For Numeric Customers
    for letter in string.ascii_uppercase:
        create_directory_if_not_exist(os.path.join(rootFolder, letter))  # Create Directories for Letters A-Z


def create_directory_list(DictTree, RootFolder, Path = str()):  # ! This Is a Really ugly way to do this but it works for now. Please Do Better Recursion Later
    folders = []

    def dict_to_dir(DictTree, RootFolder, Path = str()):
        currentRoot = os.path.join(RootFolder, Path)
        if isinstance(DictTree, dict):
            for key, value in DictTree.items():
                if isinstance(value, list):
                    for each in value:
                        dict_to_dir(each, currentRoot)
                if isinstance(value, str):
                    currentRoot = os.path.join(currentRoot, value)
                    folders.append(currentRoot)
        elif isinstance(DictTree, list):
            for i in DictTree:
                dict_to_dir(i, currentRoot)

    dict_to_dir(DictTree, RootFolder, Path)
    return folders

def create_subdir_list(DictTree, Path = str()):  # ! This Is a Really ugly way to do this but it works for now. Please Do Better Recursion Later
    folders = []

    def dict_to_dir(DictTree, Path = str()):
        currentRoot = os.path.join("\\", Path)
        if isinstance(DictTree, dict):
            for key, value in DictTree.items():
                if isinstance(value, list):
                    for each in value:
                        dict_to_dir(each, currentRoot)
                if isinstance(value, str):
                    currentRoot = os.path.join(currentRoot, value)
                    folders.append(currentRoot)
        elif isinstance(DictTree, list):
            for i in DictTree:
                dict_to_dir(i, currentRoot)

    dict_to_dir(DictTree, Path)
    return folders
