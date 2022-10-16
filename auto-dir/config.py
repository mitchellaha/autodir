
ROOT_FOLDER = r"Z:\Repositories\auto-dir\TEST_ROOT_DRIVE"

IGNORED_DIRECTORIES = ["Voided Directory Name"]

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

foldersToCreate = [
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
        "Name": "TCR",
        "Type": "Shortcut",
        "IconPath": "Z:\\Repositories\\auto-dir\\assets\\github.ico"
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