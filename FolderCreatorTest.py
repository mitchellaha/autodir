import os
from pprint import pprint
from config import ROOT_CUSTOMERS_FOLDER

"""
:: Directory Structure ::
- Plans Drive
    -> CUSTOMERS
        -> A
            ...
        -> B
            ...
        -> C
            -> Customer Contractor
            -> Barricade
                TCR - Barricade.url
                -> 2022
                    -> PDF
                        CB S Lipan St.M1.01.PDF
                        CB S Lipan St.M2.01.PDF
                    -> TCP
                        CB S Lipan St.TCP
"""

def create_directory_list(DictTree, Path = str()):  # ! This Is a Really ugly way to do this but it works for now. Please Do Better Recursion Later
    folders = []

    def dict_to_dir(DictTree, Path = str()):
        currentRoot = os.path.join(ROOT_CUSTOMERS_FOLDER, Path)
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
