from .modules.directory_maker import create_directory_from_tree, create_directory_if_not_exist


def autodir(DirStructure:list, RootFolder:str):
    """Creates The Structured Directory from BlockList

    Args:
        DirStructure (list): The BlockList to Create
        RootFolder (str): The Folder to Create It In
    """
    create_directory_if_not_exist(RootFolder)
    create_directory_from_tree(DirStructure, RootFolder)
