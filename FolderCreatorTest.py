import os
from pprint import pprint

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

foldersToCreate = [
    {
        "Name": "2022",
        "Subfolders": [
            {
                "Name": "PDF"
            },
            {
                "Name": "TCP"
            }
        ]
    },
    {
        "Name": "2021",
        "Subfolders": [
            {
                "Name": "PDF"
            },
            {
                "Name": "TCP"
            }
        ]
    },
    {
        "Name": "Archive",
        "Subfolders": [
            {
                "Name": "2020",
                "Subfolders": [
                    {
                        "Name": "PDF",
                    },
                    {
                        "Name": "TCP"
                    }
                ]
            },
            {
                "Name": "2019",
                "Subfolders": [
                    {
                        "Name": "PDF",
                    },
                    {
                        "Name": "TCP"  # ! SHOULD BE ABLE TO GO AS DEEP AS NEEDED
                    }
                ]
            },
            {
                "Name": "Other",
            },
        ]
    }
]

ROOT_CUSTOMERS_FOLDER = r"C:\Users\mitch\Documents\Programming\Repositories\Plans-Directory-Structunator\TEST_ROOT_DRIVE\CUSTOMERS\TestCustomer"
os.chdir(ROOT_CUSTOMERS_FOLDER)
CWD = os.getcwd()


def create_folders(DictTree, Path = str()):  # ! This Is a Realll ugly way to do this but it works for now. Please Do Better Recursion Later
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

pprint(create_folders(foldersToCreate))

