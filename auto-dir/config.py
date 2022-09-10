import os
from dotenv import load_dotenv
load_dotenv()


MONGO_SRV = os.getenv("MONGO_SRV")
ROOT_FOLDER = r"C:\Users\mitch\Documents\Programming\Repositories\auto-dir\TEST_ROOT_DRIVE"

IGNORED_DIRECTORIES = ["Voided Directory"]

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