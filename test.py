import time
import os
from autodir import autodir

CWD = os.getcwd()

EXEC_START_TIME = time.time()
ROOT_FOLDER = os.path.join(CWD, "TEST_ROOT_DRIVE")
MAIN_FOLDERS = ["FolderOne", "FolderTwo", "FolderThree"]


standardTwoDirs = [
    {
        "Name": "PDF",
        "Type": "Folder",
        "Subfolders": None
    },
    {
        "Name": "TCP",
        "Type": "Folder",
        "Subfolders": None
    }
]

dirStructure = [
    {
        "Name": "2022",
        "Type": "Folder",
        "Subfolders": standardTwoDirs
    },
    {
        "Name": "2021",
        "Type": "Folder",
        "Subfolders": standardTwoDirs
    },
    {
        "Name": "Other",
        "Type": "Folder",
        "Subfolders": None
    },
    {
        "Name": "Github",
        "Type": "Shortcut",
        "Config": {
            "IconPath": "Z:\\Repositories\\auto-dir\\assets\\github.ico",
            "Link": "https://github.com"
        }
        
    },
    {
        "Name": "Archive",
        "Type": "Folder",
        "Subfolders": [
            {
                "Name": "2020",
                "Type": "Folder",
                "Subfolders": standardTwoDirs
            },
            {
                "Name": "2019",
                "Type": "Folder",
                "Subfolders": standardTwoDirs
            },
            {
                "Name": "2018",
                "Type": "Folder",
                "Subfolders": standardTwoDirs
            },
            {
                "Name": "2017",
                "Type": "Folder",
                "Subfolders": standardTwoDirs
            },
            {
                "Name": "2016",
                "Type": "Folder",
                "Subfolders": standardTwoDirs
            },
            {
                "Name": "Other",
                "Type": "Folder",
                "Subfolders": None
            },
        ]
    }
]



def test_main():
    for folderName in MAIN_FOLDERS:
        mainDirPath = os.path.join(ROOT_FOLDER, folderName)  # Z:\Repositories\auto-dir\TEST_ROOT_DRIVE\FolderOne
        autodir(dirStructure, mainDirPath)



test_main()
print("--- %s seconds ---" % (time.time() - EXEC_START_TIME))
