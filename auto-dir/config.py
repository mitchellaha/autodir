import os
from dotenv import load_dotenv
load_dotenv()


MONGO_SRV = os.getenv("MONGO_SRV")
ROOT_FOLDER = r"C:\Users\mitch\Documents\Programming\Repositories\Plans-Directory-Structunator\TEST_ROOT_DRIVE\CUSTOMERS"

IGNORED_CUSTOMERS = ["Voided Customer", "Voided Customer TWO"]

standardTwoDirs = [
    {
        "Name": "PDF",
    },
    {
        "Name": "TCP"
    }
]

foldersToCreate = [
    {
        "Name": "2022",
        "Subfolders": standardTwoDirs
    },
    {
        "Name": "2021",
        "Subfolders": standardTwoDirs
    },
    {
        "Name": "Archive",
        "Subfolders": [
            {
                "Name": "2020",
                "Subfolders": standardTwoDirs
            },
            {
                "Name": "2019",
                "Subfolders": standardTwoDirs
            },
            {
                "Name": "2018",
                "Subfolders": standardTwoDirs
            },
            {
                "Name": "2017",
                "Subfolders": standardTwoDirs
            },
            {
                "Name": "2016",
                "Subfolders": standardTwoDirs
            },
            {
                "Name": "Other",
            },
        ]
    }
]