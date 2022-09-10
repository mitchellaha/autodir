import os

from helpers.directory_maker import create_directory_from_tree
from config import foldersToCreate, ROOT_FOLDER


os.chdir(ROOT_FOLDER)
CWD = os.getcwd()


def main():
    create_directory_from_tree(ROOT_FOLDER, foldersToCreate)


if __name__ == "__main__":
    import time
    start_time = time.time()
    
    main()

    print("--- %s seconds ---" % (time.time() - start_time))



