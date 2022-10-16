from modules.directory_maker import create_directory_from_tree, create_directory_if_not_exist


def autodir(DirStructure:list, RootFolder:str):
    """Creates The Structured Directory from BlockList

    Args:
        DirStructure (list): The BlockList to Create
        RootFolder (str): The Folder to Create It In
    """
    create_directory_if_not_exist(RootFolder)
    create_directory_from_tree(DirStructure, RootFolder)


if __name__ == "__main__":
    import time
    import os
    from config import dirStructure, ROOT_FOLDER

    start_time = time.time()

    MAIN_FOLDERS = ["FolderOne", "FolderTwo", "FolderThree"]

    def main():
        for folderName in MAIN_FOLDERS:
            mainDirPath = os.path.join(ROOT_FOLDER, folderName)  # Z:\Repositories\auto-dir\TEST_ROOT_DRIVE\FolderOne
            autodir(dirStructure, mainDirPath)
    
    main()

    print("--- %s seconds ---" % (time.time() - start_time))



