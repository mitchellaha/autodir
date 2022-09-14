import os

from helpers.directory_maker import create_directory_from_tree, create_directory_if_not_exist
from config import foldersToCreate, ROOT_FOLDER


os.chdir(ROOT_FOLDER)
CWD = os.getcwd()

customerList = ["CustomerOne", "CustomerTwo", "CustomerThree"]

def main():
    for customer in customerList:
        customerDirectory = os.path.join(ROOT_FOLDER, customer)
        create_directory_if_not_exist(customerDirectory)
        create_directory_from_tree(customerDirectory, foldersToCreate)


if __name__ == "__main__":
    import time
    start_time = time.time()
    
    main()

    print("--- %s seconds ---" % (time.time() - start_time))



