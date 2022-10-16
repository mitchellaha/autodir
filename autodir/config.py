## Sample Block
# {
#     "Name": "File/Folder Name",
#     "Type": "Folder/Shortcut",
#     "Config": {  # Required For Shortcuts
#         "IconPath": "Z:\\assets\\github.ico",
#         "Link": "https://google.com"
#     },
#     "Subfolders": list,  # Required For Folders
# }
## Sample Block

ROOT_FOLDER = r"Z:\Repositories\auto-dir\TEST_ROOT_DRIVE"


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