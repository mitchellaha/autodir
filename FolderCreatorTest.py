import os
from pprint import pprint

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
                        "Name": "TCP"  #! SHOULD BE ABLE TO GO AS DEEP AS NEEDED
                    }
                ]
            },
            {
                "Name": "Other",
            },
        ]
    }
]

ROOT_CUSTOMERS_FOLDER = r"C:\Users\MitchAndrews\NotOnedrive\AutoDump\TEST_ROOT_DRIVE\CUSTOMERS"
os.chdir(ROOT_CUSTOMERS_FOLDER)
CWD = os.getcwd()


allDirectoriesCreated = []

for folder in foldersToCreate:
    folderPath = os.path.join(ROOT_CUSTOMERS_FOLDER, folder["Name"])
    allDirectoriesCreated.append(folderPath)

    if folder["Subfolders"]:
        for subFolder in folder["Subfolders"]:
            subFolderPath = os.path.join(folderPath, subFolder["Name"])
            allDirectoriesCreated.append(subFolderPath)

pprint(allDirectoriesCreated)

"""
:: NEEDED OUTCOME ::

[
    'C:\\Users\\MitchAndrews\\NotOnedrive\\AutoDump\\TEST_ROOT_DRIVE\\CUSTOMERS\\2022',
    'C:\\Users\\MitchAndrews\\NotOnedrive\\AutoDump\\TEST_ROOT_DRIVE\\CUSTOMERS\\2022\\PDF',
    'C:\\Users\\MitchAndrews\\NotOnedrive\\AutoDump\\TEST_ROOT_DRIVE\\CUSTOMERS\\2022\\TCP',
    'C:\\Users\\MitchAndrews\\NotOnedrive\\AutoDump\\TEST_ROOT_DRIVE\\CUSTOMERS\\2021',
    'C:\\Users\\MitchAndrews\\NotOnedrive\\AutoDump\\TEST_ROOT_DRIVE\\CUSTOMERS\\2021\\PDF',
    'C:\\Users\\MitchAndrews\\NotOnedrive\\AutoDump\\TEST_ROOT_DRIVE\\CUSTOMERS\\2021\\TCP',
    'C:\\Users\\MitchAndrews\\NotOnedrive\\AutoDump\\TEST_ROOT_DRIVE\\CUSTOMERS\\Archive',
    'C:\\Users\\MitchAndrews\\NotOnedrive\\AutoDump\\TEST_ROOT_DRIVE\\CUSTOMERS\\Archive\\2020',
    'C:\\Users\\MitchAndrews\\NotOnedrive\\AutoDump\\TEST_ROOT_DRIVE\\CUSTOMERS\\Archive\\2020\\PDF',
    'C:\\Users\\MitchAndrews\\NotOnedrive\\AutoDump\\TEST_ROOT_DRIVE\\CUSTOMERS\\Archive\\2020\\TCP',
    'C:\\Users\\MitchAndrews\\NotOnedrive\\AutoDump\\TEST_ROOT_DRIVE\\CUSTOMERS\\Archive\\2019',
    'C:\\Users\\MitchAndrews\\NotOnedrive\\AutoDump\\TEST_ROOT_DRIVE\\CUSTOMERS\\Archive\\2019\\PDF',
    'C:\\Users\\MitchAndrews\\NotOnedrive\\AutoDump\\TEST_ROOT_DRIVE\\CUSTOMERS\\Archive\\2019\\TCP',
    'C:\\Users\\MitchAndrews\\NotOnedrive\\AutoDump\\TEST_ROOT_DRIVE\\CUSTOMERS\\Archive\\Other'
]
"""
