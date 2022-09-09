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

    uppercaseLetterList = string.ascii_uppercase

    create_directory_if_not_exist(os.path.join(rootFolder, "#"))  # Create Directory For Numeric Customers
    for letter in uppercaseLetterList:
        create_directory_if_not_exist(os.path.join(rootFolder, letter))  # Create Directories for Letters A-Z